# OpenHarmony

**Status: planned; no implementation or validated build is included.**

## Intended approach

Explore System Abilities registered with SAMgr and local IPC proxy/stub interfaces. Start with one device; distributed communication is a later, separately validated extension.

Select the OpenHarmony system profile, release, supported board and native build/package flow. Do not assume it can be deployed like an ordinary Linux daemon or that Flutter is supported on the selected target.

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

- [Official project documentation or source](https://github.com/openharmony/communication_ipc)

This reference informs the planned approach; it is not proof that SameLoop Lab
already runs on this platform.
