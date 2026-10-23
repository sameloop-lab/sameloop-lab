# E01 — Bindings AFB 0.1.0

Origine : rapport `docs/VALIDATION.md` et sortie de la suite joints à la livraison
AFB du 24 octobre 2026. Environnement rapporté : Linux x86_64 isolé, GCC 13.3.0,
Meson 1.12.1, JSON-C 0.17, Python 3.12, websockets 16.0.

Compilation des quatre projets, trois exécutables de tests de modèle et installation
DESTDIR rapportées réussies. Un binder construit depuis les sources a chargé les
quatre modules. Les 11 scénarios couvrent notamment les API privées, réglages
invalides, AUTO, perte et retour de mesure, fraîcheur, qualité d'alarme et clients
abonnés indépendants. Le profil normal refuse les injections et le redémarrage
réinitialise OFF/25.

[Sortie brute importée](brut/afb-integration.txt) ;
[révisions amont](brut/afb-revisions.json).

Limites : pas de validation utilisateur Fedora/redpesk encore fournie, pas de GUI,
pas de TLS/mTLS, pas de SMACK/Cynagora, pas de CAN/MCU, pas de RPM/Yocto.
La simulation AFB n'utilise pas exactement l'intégrateur des UI 0.1.0.
Cette preuve n'est pas un benchmark, un test de longue durée ou une certification.
