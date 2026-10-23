# Comparison method

Compare functional behavior first. Separate middleware observations under matched
conditions from full-platform observations on different operating systems or boards.
A whole-platform result cannot establish that its transport alone caused a difference.

For every run, record immutable source revisions, platform/kernel/toolchain versions,
hardware, CPU settings, process topology, UI placement, security settings, payload,
publication rate, warm-up, duration, repetitions and measurement overhead.

| Dimension | Evidence to retain |
| --- | --- |
| Functionality | Common scenario outcomes, errors and known deviations |
| Recovery | Failure injection time, detection time, usable service return time |
| Communication | Defined timing boundaries, timestamp source, distributions and losses |
| Resources | Per-process CPU/RSS plus attributable broker and adapter overhead |
| Integration | Native API mapping, lifecycle, access controls and diagnostic steps |
| Build/delivery | Clean build steps, pinned inputs, package/image sizes and installation |
| Engineering effort | Explicit counting method for handwritten/generated code and work scope |

For cross-host latency, synchronize clocks and report uncertainty, or use round-trip
measurements. Do not subtract unrelated clocks. Report median and tail values only
with raw samples, sample count and method. Never substitute missing results with zero.
No measurements or rankings have been produced yet.

Use [results](../results/README.md) for evidence and [delivery](../delivery/README.md)
for reproducible releases. UI framework comparisons are a separate experiment from
service-stack comparisons.
