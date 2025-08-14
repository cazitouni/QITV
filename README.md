# Plugin QGIS - Import Inspection Télévisée (NF EN 13508-2)

Ce plugin QGIS permet l'importation de fichiers d'inspection télévisée des réseaux d'assainissement, conformément à la norme **NF EN 13508-2**. Il facilite la visualisation et l'analyse des données d'inspection directement dans QGIS.

## Fonctionnalités

- 📥 **Importation de fichiers d'inspection**
- 📌 **Conformité à la norme NF EN 13508-2**
- 🗂️ **Création automatique de couches attributaires à partir des données importées**
- 🗺️ **Affichage géographique des observations**

## Formats supportés

- **XML**
- **TXT**

## Export

🚧 Les fonctionnalités d'**exportation vers les formats normalisés** NF EN 13508-2 sont **en cours de développement**. Elles seront disponibles dans une prochaine version du plugin.

## Installation

1. Télécharger le zip disponible en release.
2. Installer le fichier ZIP à l'aide du menu `Extensions` de Qgis.
3. Activer le plugin via le menu `Extensions > Installer/Gérer les extensions`.

## Utilisation

1. Ouvrir QGIS.
2. Lancer le plugin depuis la barre d’outils`.
3. Sélectionner le fichier XML ou TXT à importer.
4. Sélectionner les couches de canalisation et de branchement, ainsi que les identifiant commun entre la couche et le fichier.
5. Lancer le traitement.

## Note concernant les branchements

Selon la norme, il est possible de déterminer les inspections latérales (branchements) de plusieurs manières. Dans le cadre de ce plugin, le code AAV a été choisi pour déterminer quels tubes sont à lier aux branchements. Assurez-vous de la présence de ce code dans les fichiers d’import.

## Contribuer

Les contributions sont les bienvenues ! N’hésitez pas à ouvrir des issues ou à proposer des pull requests pour corriger des bugs ou ajouter de nouvelles fonctionnalités.

## Licence

Ce plugin est distribué sous la licence AGPLv3. Voir le fichier `LICENSE` pour plus d'informations.

---

🔧 **Statut du développement** : Expérimental pour l'import, export en développement.
