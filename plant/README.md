# Shared plant model

`sameloop-plant` 0.1.0 provides a deterministic Python model and a JSON-lines CLI.
It has no runtime dependency, network transport, controller or wall clock.
Temperature starts at 32.4 °C, ambient is 20 °C, normal heat input is 0.18 °C/s.

```text
dT/dt   = H - (0.015 + 0.12 × applied / 100) × (T - 20)
dApplied/dt = (demand - applied) / 0.6
dRPM/dt = (40 × applied - RPM) / 0.8
```

The coupled model uses RK4 with internal steps no larger than 10 ms.
[Six unit tests](../results/imported/plant/VALIDATION.md) include analytic thermal
and fan responses. This is a proposed reference, already used by the KUKSA
provider. AFB and the standalone UIs still use their older simulators.
No cross-stack numerical equivalence or real-equipment calibration is claimed.
