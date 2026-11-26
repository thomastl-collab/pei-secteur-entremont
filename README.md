# PEI – secteur de Saint-Pierre-d'Entremont

Carte et outil de suivi des points d'eau incendie (DECI) de Saint-Pierre-d'Entremont et de ses communes limitrophes :

- **Orne (SDIS 61)** : Saint-Pierre-d'Entremont, Caligny, Cerisy-Belle-Étoile, Moncy, Montsecret-Clairefougère — 91 PEI
- **Calvados (SDIS 14)** : Condé-en-Normandie — 146 PEI

👉 **Application en ligne : https://thomastl-collab.github.io/pei-secteur-entremont/**

## Fonctions

- Carte du secteur : statut de chaque PEI (disponible, non conforme, indisponible), rayons de 200 m et 400 m, PEI les plus proches d'un point d'intervention
- Fiche détaillée de chaque PEI, avec liens Google Maps et Waze
- Correction d'un PEI existant, création d'un nouveau PEI, demande de suppression
- Export CSV des modifications (séparateur `;`, s'ouvre dans Excel) pour envoi au SDIS

Les modifications saisies sur le site sont enregistrées **dans le navigateur de l'appareil utilisé**. Elles ne sont ni partagées ni envoyées : il faut exporter le CSV et le transmettre au SDIS.

## Sources

| Données | Source | Licence |
|---|---|---|
| PEI de l'Orne | Carte publique REMOcRA du SDIS 61 (remocra.sdis61.fr) | Aucune licence de réutilisation affichée |
| PEI du Calvados | [DECI – Calvados – SDIS14](https://www.data.gouv.fr/datasets/deci-calvados-sdis14) | Licence Ouverte |
| Contours des communes | [geo.api.gouv.fr](https://geo.api.gouv.fr) | Licence Ouverte |

Extraction du 26/11/2026. Ces données sont une copie figée, **non opérationnelle** : seuls les outils du SDIS font foi.

## Dossier `donnees/`

- `pei_orne_secteur.json`, `pei_calvados_conde.json` : données brutes extraites, coordonnées en Lambert 93
- `construire_donnees.py` : script qui assemble ces données avec les contours des communes pour la page
