# webOS Open Source Edition / LS2

**Status: planned; no implementation or validated build is included.**

## Intended approach

Implement native services using Luna Service 2 with methods and subscriptions for the common contract. Document service discovery, permissions and reconnect behavior.

Select a webOS OSE release and target, then document native service/application packaging and image integration. Do not infer compatibility with commercial webOS TV products.

## Common contract

Implement the [functional specification](../docs/functional-spec.md) and run the
[common scenarios](../scenarios/README.md). The [signal model](../model/README.md)
provides a vocabulary; native APIs may use a different representation.

## Implementation record to complete

- Supported release, board/host, prerequisites and immutable source revisions.
- Process/service layout and signal-to-native-API mapping.
- Command acknowledgement versus applied state; error and quality propagation.
- Authentication/authorization, lifecycle, subscriptions and recovery.
- Reproducible build, install, start, stop and uninstall commands.
- UI adapter and any additional bridge or remote process.
- Component repositories, licenses and package/image references.
- Scenario outcomes, limitations and links to result reports.

No setup commands are provided until they have been exercised on the selected
release. Use the [delivery index](../delivery/README.md) for external components and
release artifacts. Pin dependencies rather than relying on a moving branch.

## Upstream reference

- [Official project documentation or source](https://www.webosose.org/docs/reference/)

This reference informs the planned approach; it is not proof that SameLoop Lab
already runs on this platform.
