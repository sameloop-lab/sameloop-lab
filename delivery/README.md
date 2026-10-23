# Delivery inventory

This 0.2.0 tarball is the public documentation hub, with static HTML, SVG diagrams,
source Markdown/JSON/DOT, signal metadata, branding and imported evidence.
It does not embed the implementation packages or external dependencies.

[archives.json](archives.json) records SHA-256 identities of earlier component
archives. A null URL means the public artifact address has not been registered.
[data/projects.json](../data/projects.json) records component status; repository
fields remain null until their actual locations are confirmed. Only the umbrella
repository and organization URLs supplied by the maintainer are asserted.

![Delivery paths](../assets/diagrammes/13-livraison.svg)

AFB uses Meson; Python components have wheels/sdists and draft RPM specs.
RPM/mock/OBS and Yocto image integration need their own validation. Future
releases should pin repository commits, third-party dependencies and image digests.
Do not equate a rebuildable workflow with proven bit-for-bit reproducibility.
