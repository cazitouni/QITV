# Plugin QGIS - Import Inspection Télévisée (NF EN 13508-2)

Ce plugin QGIS permet l'import et l'export de fichiers d'inspection télévisée des réseaux d'assainissement, conformément à la norme **NF EN 13508-2**. Il facilite la visualisation et l'analyse des données d'inspection directement dans QGIS.

## Fonctionnalités

- 📥 **Import de fichiers d'inspection**
-    **Export de fichiers d'inspection**
- 📌 **Conformité à la norme NF EN 13508-2**
- 🗂️ **Création automatique de couches attributaires à partir des données importées**
- 🗺️ **Affichage géographique des observations**

## Formats supportés

- **XML**
- **TXT**

## Installation

1. Télécharger le zip disponible en release.
2. Installer le fichier ZIP à l'aide du menu `Extensions` de Qgis.
3. Activer le plugin via le menu `Extensions > Installer/Gérer les extensions`.

## Utilisation

Il est possible de personaliser les couches contentenant les branchements et les canalisations depuis le menu `Extensions` -> `QITV`

Pour l'import des troncon cliquer sur le boutons `Import`, sélectionner le fichier `xml` ou `txt` et cliquer sur traiter. 

Pour l'export, cliquer sur le bouton `Export` une interface va s'ouvrir. il est ensuite possible dans cette interface d'ajouter des tronçons, le boutton de selection permetant de choisir un troncon défini dans la couche configurée en amont. une fois tous les tronçons selectionés, il faut shoisir ou suvegarder les fichiers et enfin cliquer sur le bouton exporter. Deux fichier vont se créer un fichier `xml` ainsi qu'un fichier `txt`.


## Note concernant les branchements

Selon la norme, il est possible de déterminer les inspections latérales (branchements) de plusieurs manières. Dans le cadre de ce plugin, le code AAV a été choisi pour déterminer quels tubes sont à lier aux branchements. Assurez-vous de la présence de ce code dans les fichiers d’import.

## Contribuer

Les contributions sont les bienvenues ! N’hésitez pas à ouvrir des issues ou à proposer des pull requests pour corriger des bugs ou ajouter de nouvelles fonctionnalités.

## Licence

Ce plugin est distribué sous la licence AGPLv3. Voir le fichier `LICENSE` pour plus d'informations.

---

🔧 **Statut du développement** : Expérimental pour l'import et l'export
