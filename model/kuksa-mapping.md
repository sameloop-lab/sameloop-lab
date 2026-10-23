# Original catalog ↔ KUKSA 0.1.0

The supplied original `sameloop.vspec` is preserved unchanged. KUKSA 0.1.0 uses
a separate private catalog; do not load the original and assume the runtime
paths match. Neither catalog is a standard COVESA SameLoop model.

| Original relative path | KUKSA 0.1.0 relative path / semantics |
|---|---|
| Temperature.Value | Temperature (double); also Frame.temperature |
| Temperature.IsValid | SensorValid; Frame.valid plus consumer freshness |
| Fan.DutyCycle | FanDemand (request), FanApplied (feedback), internal Command envelope |
| Fan.Speed | FanRpm (double) |
| Controller.Setpoint | Settings target/current JSON, Setpoint accepted value |
| Controller.Mode | Settings target/current JSON, Mode accepted value |
| Alarm.Overtemperature | Overheat, with State.alarm_quality |
| Alarm.SensorUnavailable | Inverse of Available, including freshness |
| Model | No dedicated equivalent in runtime 0.1.0; identify via delivery versions |

All paths are relative to Vehicle.SameLoop. Integer/float representation differs
for fan duty/speed; consumers must account for it. Settings is a single JSON
string actuator containing id/mode/setpoint, so the request is treated atomically
by the controller. Frame and State carry coherent JSON snapshots with sequences.
The VSPEC/JSON under kuksa-0.1.0 is copied from the implementation delivery.
No DBC, CAN mapping or general VSPEC compiler is supplied here.
