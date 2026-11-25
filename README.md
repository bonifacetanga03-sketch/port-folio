# Portfolio – Tanga Boniface

Site 100 % statique (HTML / CSS / JS), sans étape de build.

```
index.html · index.css · main.js   le portfolio
img/                               images du portfolio
certificates/                      certificats Cisco (PDF)
projects/commerce/                 site e-commerce
projects/restaurant/               application de restaurant (page statique)
projects/etat-civil/               application état civil (mode démo hors connexion)
```

## Déployer sur GitHub Pages
1. Crée un dépôt GitHub et envoie-y le contenu de ce dossier (`index.html` doit être à la racine du dépôt).
2. Settings → Pages → Source : « Deploy from a branch » → branche `main`, dossier `/ (root)` → Save.

## Déployer sur Vercel
1. vercel.com → Add New → Project → importe le dépôt GitHub.
2. Framework Preset : **Other**. Laisse Build Command et Output Directory vides. Deploy.

## Ajouter un projet
Mets son dossier dans `projects/`, puis dans `index.html` donne à sa carte :
`<a href="projects/mon-projet/index.html" data-viewer="Nom du projet">` — il s'ouvrira dans la fenêtre du portfolio.
Utilise des chemins **relatifs** et des noms de fichiers sans espaces ni accents.
