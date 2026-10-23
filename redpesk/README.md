# redpesk / AFB

Four separate 0.1.0 C binding projects were delivered: `sameloop-api-binding`,
`sameloop-sensor-binding`, `sameloop-controller-binding`, `sameloop-fan-binding`.
They use Meson and run in one afb-binder process. Internal subcalls are not
WebSocket messages. The facade exposes the client API; the three other APIs
are private in the demonstrated configuration.

![AFB architecture](../assets/diagrammes/04-afb.svg)

[Imported validation](../results/imported/AFB.md): builds, model tests and
11 integration scenarios with a real binder were reported successful on Linux.
This does not establish a complete redpesk image, SMACK isolation between
modules, role enforcement, TLS, hardware or connected GUI support.

Implementation archives remain separate from this documentation tarball.
Register their published URLs in [the delivery inventory](../delivery/README.md).
The simulation currently differs numerically from the new RK4 plant model.

Upstream: https://github.com/redpesk-core/afb-binder
