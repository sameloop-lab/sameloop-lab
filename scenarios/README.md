# Common acceptance scenarios

Status: specification only; no automated runner exists yet.

| ID | Action | Expected observation |
| --- | --- | --- |
| S01 | Start all components | F01 defaults; actual values absent until published |
| S02 | Observe valid measurements | 10 Hz producer; fresh temperature and fan feedback |
| S03 | Request a valid setpoint and AUTO | Accepted settings visible; fan follows common control law |
| S04 | Request OFF | Requested duty becomes zero; applied duty and speed remain distinct feedback |
| S05 | Request invalid mode, NaN or out-of-range setpoint | Explicit rejection; accepted state unchanged |
| S06 | Mark sensor invalid, then separately pause updates | Unavailable alarm; timeout behavior and F05 policy |
| S07 | Restore valid fresh samples | Unavailable clears; regulation resumes if still AUTO |
| S08 | Inject 51 °C, then 50 °C, with valid data | Overtemperature true, then false |
| S09 | Stop/restart provider, controller and broker separately | Missing services visible; resubscription; controller restart returns OFF |
| S10 | Disconnect UI with a pending request, then reconnect | No silent replay; refresh applied state |
| S11 | Attempt operator writes as a viewer | Backend rejects unauthorized requests |
| S12 | Repeat the same deterministic input scenario | Equivalent logical outcomes within declared tolerances |

Record prerequisites, stimuli, timestamps, observations and pass/fail/unsupported
for each platform. Reset to documented initial conditions between tests. Precise
settling and timing tolerances remain to be chosen; do not claim S03/S12 numerical
conformance before the simulator and control law are fixed.
