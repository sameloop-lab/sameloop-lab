# User interfaces

Priority remains Flutter, LVGL, then Qt. Flutter and LVGL 0.1.0 have been delivered
as standalone simulation interfaces. Qt is proposed.

- [Flutter evidence](../results/imported/FLUTTER.md): build/tests not established.
- [LVGL evidence](../results/imported/LVGL.md): build and headless SDL tests reported.
- No Flutter/LVGL ↔ AFB/KUKSA integration is validated in these reports.

Implement the [functional contract](../docs/functional-spec.md), including stale
values, accepted versus requested settings, active stack and disconnect state.
A future native Flutter Linux gRPC client is distinct from Flutter Web and any
gRPC-Web proxy. Keep the physical simulator out of the GUI once a provider is connected.
