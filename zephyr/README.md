# Zephyr / zbus — planned

Proposed projects: `sameloop-zephyr` and `sameloop-gateway`. No firmware or
hardware integration is delivered here.

![Zephyr boundary](../assets/diagrammes/08-zephyr.svg)

**zbus is a software message bus in the Zephyr firmware, not a physical bus.**
A driver reads an I²C/SPI sensor; a task publishes the measurement on zbus.
A gateway serializes messages over UART, CAN or an IP link to Linux.
Choose one controller owner: Linux OR the MCU. The diagram shows the MCU option.

![Physical alternatives](../assets/diagrammes/09-materiel.svg)

Candidates include STM32 boards, ESP32 variants and Nordic devices, subject to
actual drivers/peripherals. CAN needs a suitable controller and transceiver;
PWM/GPIO does not power a motor directly. Start with native_sim and one physical
link, then qualify the board, framing, watchdog and loss-of-link policy.

Reference: https://docs.zephyrproject.org/latest/services/zbus/index.html
