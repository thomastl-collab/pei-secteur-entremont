# PEI – secteur de Saint-Pierre-d'Entremont

Carte et outil de suivi des points d'eau incendie (DECI) de Saint-Pierre-d'Entremont et de ses communes limitrophes :

- **Orne (SDIS 61)** : Saint-Pierre-d'Entremont, Caligny, Cerisy-Belle-Étoile, Moncy, Montsecret-Clairefougère — 91 PEI
- **Calvados (SDIS 14)** : Condé-en-Normandie — 146 PEI

👉 **Application en ligne : https://thomastl-collab.github.io/pei-secteur-entremont/**

## Fonctions

- Carte du secteur : statut de chaque PEI (disponible, non conforme, indisponible), rayons de 200 m et 400 m, PEI les plus proches d'un point d'intervention
- Fond de carte au choix : Plan IGN, photos aériennes IGN ou OpenStreetMap
- Fiche détaillée de chaque PEI, avec liens Google Maps et Waze
- Correction d'un PEI existant, création d'un nouveau PEI, demande de suppression
- Export CSV des modifications (séparateur `;`, s'ouvre dans Excel) pour envoi au SDIS

Les modifications saisies sur le site sont enregistrées **dans le navigateur de l'appareil utilisé**. Elles ne sont ni partagées ni envoyées : il faut exporter le CSV et le transmettre au SDIS.

## Sur iPhone

- Ouvrir le lien dans **Safari**, puis Partager → **Sur l'écran d'accueil** : l'app s'ouvre alors en plein écran comme une application.
- Bouton **◎** : affiche votre position GPS et les PEI les plus proches (autoriser la localisation pour Safari).
- Toucher un PEI : fiche résumée en bas de la carte avec **Modifier**, **Plans** et **Waze**.
- « + Nouveau PEI » puis **Ma position** : crée un PEI à l'endroit où vous vous trouvez.
- Les exports CSV ouvrent la feuille de partage (Mail, AirDrop, Fichiers…) pour l'envoyer directement au SDIS.

⚠️ Les corrections sont stockées dans le navigateur. L'app ajoutée à l'écran d'accueil et Safari ont chacune leur propre stockage : utiliser toujours le même accès, et exporter le CSV avant d'effacer les données de Safari.

## Sources

| Données | Source | Licence |
|---|---|---|
| PEI de l'Orne | Carte publique REMOcRA du SDIS 61 (remocra.sdis61.fr) | Aucune licence de réutilisation affichée |
| PEI du Calvados | [DECI – Calvados – SDIS14](https://www.data.gouv.fr/datasets/deci-calvados-sdis14) | Licence Ouverte |
| Fonds de carte | IGN Géoplateforme (Plan IGN, photos aériennes), © contributeurs OpenStreetMap | Licence Ouverte / ODbL |
| Contours des communes | [geo.api.gouv.fr](https://geo.api.gouv.fr) | Licence Ouverte |

Extraction du 26/11/2026. Ces données sont une copie figée, **non opérationnelle** : seuls les outils du SDIS font foi.

## Dossier `donnees/`

- `pei_orne_secteur.json`, `pei_calvados_conde.json` : données brutes extraites, coordonnées en Lambert 93
- `construire_donnees.py` : script qui assemble ces données avec les contours des communes pour la page
