# Diagram gallery

Editable DOT sources and generated SVGs, adapted from sameloop-dev-project. All diagram labels are in English. Future project names are red; architecture dashed links indicate work to qualify. Functional arrows describe relationships, not test results.

## 01 · A box, a thermometer and a fan

Functional view · no technical background required

![01 · A box, a thermometer and a fan](../assets/diagrammes/01-fonctionnel.svg)

[Editable DOT](../assets/sources/01-fonctionnel.dot)

## 02 · Demo states

OFF/AUTO = user choice · availability and alarm are separate dimensions

![02 · Demo states](../assets/diagrammes/02-etats.svg)

[Editable DOT](../assets/sources/02-etats.dot)

## 03 · Same function, different implementations

Target architecture · choose one stack · red names = future projects

![03 · Same function, different implementations](../assets/diagrammes/03-panorama.svg)

[Editable DOT](../assets/sources/03-panorama.dot)

## 04 · redpesk / AFB: four bindings delivered

Solid = reported lab integration · dashed = future connection

![04 · redpesk / AFB: four bindings delivered](../assets/diagrammes/04-afb.svg)

[Editable DOT](../assets/sources/04-afb.dot)

## 05 · KUKSA on Linux: profile 0.1.0 delivered

Imported evidence · not a complete AGL image

![05 · KUKSA on Linux: profile 0.1.0 delivered](../assets/diagrammes/05-agl.svg)

[Editable DOT](../assets/sources/05-agl.dot)

## 06 · OpenHarmony: IPC services and external UI

Proposed architecture · same device for the first prototype

![06 · OpenHarmony: IPC services and external UI](../assets/diagrammes/06-openharmony.svg)

[Editable DOT](../assets/sources/06-openharmony.dot)

## 07 · webOS OSE: services on Luna Bus

Proposed architecture · OSE target; commercial TV support not assumed

![07 · webOS OSE: services on Luna Bus](../assets/diagrammes/07-webos.svg)

[Editable DOT](../assets/sources/07-webos.dot)

## 08 · Zephyr: software zbus and explicit external link

Shown variant: local MCU control · all connections remain to be developed

![08 · Zephyr: software zbus and explicit external link](../assets/diagrammes/08-zephyr.svg)

[Editable DOT](../assets/sources/08-zephyr.dot)

## 09 · From messages to wires: three alternative links

Conceptual diagram · pinout, transceivers, power and drivers require validation

![09 · From messages to wires: three alternative links](../assets/diagrammes/09-materiel.svg)

[Editable DOT](../assets/sources/09-materiel.dot)

## 10 · Plaintext, server-authenticated TLS and mTLS

Security concepts · no SameLoop TLS profile tested yet

![10 · Plaintext, server-authenticated TLS and mTLS](../assets/diagrammes/10-tls.svg)

[Editable DOT](../assets/sources/10-tls.dot)

## 11 · CommonAPI / SOME/IP: comparison extension

Proposed architecture · optional stack beyond the MVP

![11 · CommonAPI / SOME/IP: comparison extension](../assets/diagrammes/11-commonapi.svg)

[Editable DOT](../assets/sources/11-commonapi.dot)

## 12 · Every test level has a scope

Passing unit tests does not validate the network, UI or hardware

![12 · Every test level has a scope](../assets/diagrammes/12-tests.svg)

[Editable DOT](../assets/sources/12-tests.dot)

## 13 · From repositories to reproducible demos

Proposed workflow · build systems remain specific to each target

![13 · From repositories to reproducible demos](../assets/diagrammes/13-livraison.svg)

[Editable DOT](../assets/sources/13-livraison.dot)

## 14 · Connect two stacks with a single controller

Proposed first step: AFB → KUKSA telemetry only

![14 · Connect two stacks with a single controller](../assets/diagrammes/14-interop.svg)

[Editable DOT](../assets/sources/14-interop.dot)
