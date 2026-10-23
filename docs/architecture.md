# Architecture

The functional contract is shared; native middleware mechanisms remain visible.
AFB subcalls, KUKSA signal operations, OpenHarmony IPC and webOS LS2 are not a
single interchangeable protocol. Read [known deviations](deviations.md) before comparing.

![Architecture overview](../assets/diagrammes/03-panorama.svg)

The current implementations have different packaging and simulation boundaries.
The [plant](../plant/README.md) is used by KUKSA today, not yet by all stacks.
The [diagram gallery](diagrams.md) distinguishes delivered lab profiles from
proposals. Red project names identify proposed components; dashed links indicate
future work in architecture diagrams. Solid lines in functional diagrams express
relationships, not executed tests. French diagram text is retained from the development dossier.
