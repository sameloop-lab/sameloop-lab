# Signal model

[sameloop.vspec](sameloop.vspec) is the existing custom SameLoop catalog. Its
`Vehicle.SameLoop` paths are project extensions, not standard vehicle signals.
The model contains metadata only. It does not implement regulation or provide values.

The [functional specification](../docs/functional-spec.md) is the common behavioral
reference. Update both documents when signal semantics change. Freshness, quality,
command outcomes and service availability need adapter metadata beyond this file.

The VSpec comments contain a candidate vss-tools 6.x export command. Exporter,
unit/quantity catalogs and KUKSA API versions must be pinned and verified together.
The original catalog has not been validated with vss-tools or a running
Databroker. The separate [KUKSA 0.1.0 catalog](kuksa-0.1.0/vss.json) was used in
the reported real-broker tests; its paths differ. See [the mapping](kuksa-mapping.md).

Future DBC and mapping files belong here with provenance, compatible tool revisions
and an end-to-end validation procedure. No hypothetical mapping is presented as an
existing working integration.

References:
- [COVESA VSS](https://github.com/COVESA/vehicle_signal_specification)
- [VSS tools](https://github.com/COVESA/vss-tools)
- [KUKSA CAN Provider](https://github.com/eclipse-kuksa/kuksa-can-provider)
