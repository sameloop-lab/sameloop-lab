# SameLoop Lab

**Bind & Seek — Une même boucle de contrôle, plusieurs piles embarquées.**

SameLoop compare des architectures de services à travers une démo commune :
une température, une consigne, un contrôleur et un ventilateur.

Ouvrir [index.html](index.html) après extraction pour consulter le tableau de bord
hors ligne, les états des projets et les 14 schémas. La documentation publique
principale est en anglais ; les schémas et les preuves importés du dossier de
développement conservent leur français d'origine.

Les bindings AFB, le profil KUKSA sur PC et le modèle physique disposent de preuves
de tests importées. LVGL a été testé en simulation sans écran. Flutter est livré
sans preuve de compilation établie dans ce dossier. OpenHarmony, webOS, Zephyr
et CommonAPI restent des propositions. Une GUI reliée à un backend n'est pas
encore validée. Voir [les limites](docs/deviations.md).

Le catalogue de signaux d'origine reste conservé. Le profil KUKSA livré utilise
un encodage différent, documenté dans [le mapping](model/kuksa-mapping.md).
Les frameworks de mocks restent une piste future : le simulateur physique,
les vrais brokers et les outils de perturbation ont des rôles distincts.

Pour reconstruire : `npm ci`, puis `npm run build`, puis `npm run check`.
Aucune installation n'est nécessaire pour consulter les HTML et SVG fournis.

Organisation : https://github.com/sameloop-lab

Dépôt : https://github.com/sameloop-lab/sameloop-lab
