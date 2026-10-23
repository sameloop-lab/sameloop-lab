# Communication layers

| Layer | Examples | SameLoop status |
|---|---|---|
| Local service mechanism | AFB subcalls, OpenHarmony IPC, webOS LS2 | AFB demonstrated; other two planned |
| Firmware software bus | Zephyr zbus | Planned; messages in firmware memory |
| Network application protocol | AFB WSJ1, KUKSA VAL gRPC, HTTP APIs | AFB/KUKSA loopback reports available |
| Transport protection | HTTPS, WSS, gRPC with TLS | No SameLoop validation yet |
| Physical/peripheral link | CAN, UART, I²C, SPI, Ethernet, Wi-Fi | Candidate hardware paths, not implemented |

![Authentication modes](../assets/diagrammes/10-tls.svg)

TLS with server authentication and mutual TLS describe authentication modes;
TLS 1.2 and 1.3 are protocol versions. Authentication does not define application
permissions. TLS does not wrap local zbus channels or turn I²C/CAN into secure
network protocols. A gateway must explicitly define trust boundaries.

![Read-only interop proposal](../assets/diagrammes/14-interop.svg)

Cross-stack interop is planned, initially one-way telemetry. A single controller
must own an actuator. No AFB/KUKSA bridge is currently delivered.
