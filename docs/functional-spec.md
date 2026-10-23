# Functional specification

Status: draft baseline for implementation. Numerical data ranges and alarm
thresholds below follow the existing custom VSpec. Startup and recovery behavior
are proposed project decisions, not inherited platform behavior. Change this
contract explicitly when a decision changes; do not silently diverge by stack.

## Components and responsibilities

The plant simulator produces temperature, sensor validity, applied fan duty cycle
and measured speed. The controller owns regulation, accepted settings and alarms.
The UI observes state and requests changes to mode and setpoint. A scenario runner
will inject faults and disturbances through a separate test interface.

The initial plant is cooling-only, with a simulated heat source and ambient
exchange. The proposed reference model now lives in sameloop-plant; older AFB/UI models
are not yet aligned. Cross-stack quantitative comparisons require alignment. No physical plant implementation is included.

## Data contract

Paths are relative to `Vehicle.SameLoop` in the VSS representation. Read/write
below describes application roles, not a middleware permission syntax.

| Signal | Type and range | Producer / command owner | Operator access |
| --- | --- | --- | --- |
| Model | string | Simulator | Read |
| Temperature.Value | float, -40 to 150 °C | Simulator | Read/subscribe |
| Temperature.IsValid | boolean | Simulator | Read/subscribe |
| Fan.DutyCycle | integer, 0 to 100 % | Controller requests; simulator reports applied value | Read/subscribe |
| Fan.Speed | integer, 0 to 10000 rpm | Simulator | Read/subscribe |
| Controller.Setpoint | float, 15 to 40 °C | Operator requests; controller accepts | Read/request change |
| Controller.Mode | OFF or AUTO | Operator requests; controller applies | Read/request change |
| Alarm.Overtemperature | boolean | Controller | Read/subscribe |
| Alarm.SensorUnavailable | boolean | Controller | Read/subscribe |

Fan speed is feedback, not a conversion guaranteed by the duty-cycle command.
Actuator requests and actual values must remain distinct even where the native API
exposes them through different methods or fields. An acknowledgement alone does
not prove actuation. Missing values must not be presented as zero or false.

## Required behavior

- **F01 — Startup:** proposed baseline is OFF with accepted setpoint 25 °C and
  requested fan duty 0 %. Report actual state only after the provider publishes it.
  Do not restore an earlier AUTO request silently after a controller restart.
- **F02 — Measurements:** the simulator publishes temperature at 10 Hz. Validity
  and freshness are separate. Invalid, non-finite or out-of-range measurements
  must not feed regulation. The timeout is one second since the last valid fresh
  measurement, measured with a monotonic clock at the consumer. Startup without
  a valid sample is unavailable immediately. Transport buffering must not make
  old data look fresh; record timestamps/sequence information in the adapter.
- **F03 — Settings:** accept only OFF/AUTO and finite setpoints in [15, 40] °C.
  Reject invalid requests without modifying accepted state. Report a useful error.
  Duplicate requests must not create additional side effects.
- **F04 — Regulation:** AUTO uses `clamp(20 × (temperature − setpoint), 0, 100)` to cool toward the
  setpoint and clamps requests to [0, 100] %. OFF requests 0 %. The UI cannot
  command fan duty directly in the baseline. Unreachable setpoints are not a
  communications failure.
- **F05 — Sensor loss:** publish SensorUnavailable on invalid data or timeout.
  Proposed simulation policy: suspend regulation and request 0 % duty; remain
  visibly degraded. Resume AUTO only with fresh valid data if AUTO is still the
  accepted mode. This is a demonstration policy, not a physical safety design.
- **F06 — Overtemperature:** with valid fresh data, the alarm is true above
  50 °C and false at or below 50 °C. There is no latching or hysteresis initially.
  On sensor loss preserve the last known alarm value with unavailable quality;
  never present a stale false as an all-clear. This alarm does not override F04/F05.
- **F07 — Connectivity:** show unavailable/disconnected services and stale data.
  Reconnect, resubscribe and refresh state after recovery. Discard pending commands
  across a disconnect; do not replay them silently. Recovery timing is measured,
  not prescribed before the implementations exist.
- **F08 — Roles:** a viewer reads state; an operator may request setpoint/mode;
  a controller commands the fan; providers publish their own state. Each adapter
  documents and tests enforcement. UI visibility alone is not authorization.
- **F09 — Observability:** log command requests/outcomes, state transitions and
  faults with timestamps and correlation where available. Distinguish unknown,
  invalid, stale and available state in the UI; quality is adapter metadata and
  is not fully represented by the VSpec alone.

## Interface and simulation controls

The first UI provides a temperature view, setpoint input, OFF/AUTO selector, fan
request/feedback display, alarms and active-stack indicator. Invalid input must
produce feedback without changing accepted state.

Test-only controls will set a reproducible heat disturbance, mark a sensor invalid,
pause measurements and restart services. They are separate from the operator API.
A strict write-only reset command is not part of the baseline contract.

## Acceptance

Use the scenario IDs in [scenarios](../scenarios/README.md). Initial tests check
functional equivalence; quantitative settling, latency and recovery targets remain
open until a simulator/control law and measurement method are pinned. All four
implementations must report deviations, including unsupported features.

## Implementation status

This remains the target contract. Read [known deviations](deviations.md): F07
automatic recovery and F08 permissions are not implemented in the KUKSA 0.1.0
trusted-loopback profile. Current source packages are separate from this hub.
