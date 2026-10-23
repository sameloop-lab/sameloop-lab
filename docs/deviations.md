# Known gaps against the functional target

| Requirement / assumption | Actual scope of available evidence |
|---|---|
| Identical plant across stacks | KUKSA uses RK4 sameloop-plant; AFB and UIs retain older models |
| Automatic recovery F07 | KUKSA services fail visibly on RPC error and need explicit restart |
| Role enforcement F08 | Not implemented in the trusted-loopback KUKSA profile |
| Connected graphical application | Flutter/LVGL adapters to backends remain unvalidated |
| One signal layout | Original VSpec and KUKSA 0.1.0 paths differ; mapping is explicit |
| Full AGL/redpesk deployment | Broker/binder Linux tests do not qualify an OS image |
| Production hardware safety | Demonstration watchdog/inhibit rules are not a safety analysis |

Do not infer a link's validation from successful tests of its two endpoints.
A source archive, a compiled component, an integration test and a target-board
validation are separate evidence levels. No middleware performance winner can
be inferred from these initial tests.
