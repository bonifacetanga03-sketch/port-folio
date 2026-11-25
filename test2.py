from pathlib import Path
import zipfile, textwrap

out = Path("/mnt/data/cv_tanga_boniface")
out.mkdir(exist_ok=True)

html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="CV de Tanga Boniface Andy, apprenant développeur web et mobile.">
  <title>CV - Tanga Boniface Andy</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="toolbar">
    <label class="photo-button" for="photoInput">Ajouter ma photo</label>
    <input id="photoInput" type="file" accept="image/*" hidden>
    <button id="themeButton" type="button">Mode sombre</button>
    <button id="printButton" type="button">Télécharger / Imprimer en PDF</button>
  </div>

  <main class="cv">
    <aside class="sidebar">
      <header class="identity">
        <div class="portrait-wrap">
          <div class="portrait-placeholder" id="portraitPlaceholder">TB</div>
          <img id="portrait" class="portrait" alt="Photo de Tanga Boniface Andy">
        </div>
        <h1>TANGA BONIFACE<br>ANDY</h1>
        <p class="job-title">DÉVELOPPEUR WEB / MOBILE</p>
      </header>

      <section class="side-section">
        <h2>Mes contacts</h2>
        <ul class="contact-list">
          <li><span class="icon">☎</span><a href="tel:+237697159402">+237 697 15 94 02</a></li>
          <li><span class="icon">✉</span><a href="mailto:bonifacetanga03@gmail.com">bonifacetanga03@gmail.com</a></li>
          <li><span class="icon">◎</span><a href="#" class="editable-link" contenteditable="true" aria-label="Lien du portfolio">Mon Portfolio</a></li>
          <li><span class="icon">⌖</span><span>Bépanda Trois Baham<br>Douala, Cameroun</span></li>
        </ul>
      </section>

      <section class="side-section">
        <h2>Formations</h2>
        <div class="education">
          <strong>2025 – 2026</strong>
          <p>1ère année en Génie logiciel</p>
          <span>Université des Grandes Écoles des Tropiques (IUGET)</span>
        </div>
        <div class="education">
          <strong>2024 – 2025</strong>
          <p>Baccalauréat</p>
          <span>Lycée de Deido</span>
        </div>
        <div class="education">
          <strong>2023 – 2024</strong>
          <p>Probatoire</p>
          <span>Lycée de Deido</span>
        </div>
        <div class="education">
          <strong>2021 – 2022</strong>
          <p>BEPC</p>
          <span>Lycée de Deido</span>
        </div>
      </section>

      <section class="side-section">
        <h2>Langues</h2>
        <div class="language"><div><span>Français</span><b>Très bon</b></div><div class="meter"><i style="width:100%"></i></div></div>
        <div class="language"><div><span>Anglais</span><b>Intermédiaire</b></div><div class="meter"><i style="width:35%"></i></div></div>
        <div class="language"><div><span>Espagnol</span><b>Débutant</b></div><div class="meter"><i style="width:55%"></i></div></div>
      </section>
    </aside>

    <section class="content">
      <section class="main-section profile">
        <h2>Profil</h2>
        <p>
          Je me nomme <strong>Tanga Boniface Andy</strong>, apprenant développeur et étudiant
          en Génie logiciel à l’Université des Grandes Écoles des Tropiques (IUGET).
          Je m’intéresse au développement web et mobile et je renforce progressivement
          mes compétences en HTML, CSS et JavaScript. J’ai déjà travaillé sur quelques
          projets pratiques, notamment la création d’un site animé et d’un site de restaurant.
          Je suis motivé à apprendre, à progresser et à concevoir des solutions numériques utiles.
        </p>
      </section>

      <section class="main-section">
        <h2>Expériences et parcours</h2>
        <article class="timeline-item">
          <div class="date">2025 – 2026<br><small>EN FORMATION</small></div>
          <div class="details">
            <h3>Étudiant en Génie logiciel</h3>
            <p>Durant ma première année de formation, j’ai acquis des bases en programmation
              et découvert différentes méthodes de conception d’applications web et mobiles.</p>
          </div>
        </article>
        <article class="timeline-item">
          <div class="date">2024 – 2025<br><small>FORMATION EN LIGNE</small></div>
          <div class="details">
            <h3>Apprentissage en informatique</h3>
            <p>J’ai suivi des formations en ligne sur les langages HTML, CSS et JavaScript,
              ainsi que des initiations au langage PHP.</p>
          </div>
        </article>
        <article class="timeline-item">
          <div class="date">2022 – 2023<br><small>PARCOURS SCOLAIRE</small></div>
          <div class="details">
            <h3>Élève passionné de technologie</h3>
            <p>C’est durant cette période que j’ai développé un intérêt marqué pour
              l’informatique et décidé de m’orienter vers le domaine du numérique.</p>
          </div>
        </article>
      </section>

      <section class="main-section skills-section">
        <h2>Compétences</h2>
        <div class="skill"><span>HTML, CSS et JavaScript</span><div class="skill-track"><i style="width:70%"></i></div></div>
        <div class="skill"><span>Java et PHP</span><div class="skill-track"><i style="width:42%"></i></div></div>
        <div class="skill"><span>Word, Excel et PowerPoint</span><div class="skill-track"><i style="width:80%"></i></div></div>
        <p class="hint">Les niveaux sont modifiables directement dans le fichier <code>style.css</code>.</p>
      </section>

      <section class="main-section projects">
        <h2>Projets</h2>
        <ul>
          <li>Création d’un site web animé.</li>
          <li>Réalisation d’un site web de restaurant.</li>
          <li>Développement d’une calculatrice avec Visual Studio.</li>
        </ul>
      </section>
    </section>
  </main>
  <script src="script.js"></script>
</body>
</html>
"""

css = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --red: #a9282c;
  --red-light: #ff8589;
  --ink: #242424;
  --muted: #666;
  --paper: #fff;
  --side-text: #fff;
  --line: #ead5d3;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  padding: 28px 16px;
  background: #555;
  color: var(--ink);
  font-family: Inter, Arial, sans-serif;
}
.toolbar {
  max-width: 1000px;
  margin: 0 auto 14px;
  display: flex;
  justify-content: flex-end;
  gap: 9px;
  flex-wrap: wrap;
}
.toolbar button, .photo-button {
  border: 0;
  border-radius: 7px;
  padding: 10px 14px;
  background: #fff;
  color: #333;
  font: 600 13px Inter, sans-serif;
  cursor: pointer;
  text-decoration: none;
}
.toolbar button:hover, .photo-button:hover { background: #f3dede; }
.cv {
  max-width: 1000px;
  min-height: 1120px;
  margin: auto;
  display: grid;
  grid-template-columns: 32% 68%;
  background: var(--paper);
  box-shadow: 0 12px 35px #0003;
}
.sidebar {
  background: var(--red);
  color: var(--side-text);
  padding: 38px 30px;
}
.identity { text-align: center; padding-bottom: 28px; border-bottom: 1px solid #ffffff55; }
.portrait-wrap {
  width: 176px; height: 176px; margin: 0 auto 18px;
  border-radius: 50%; overflow: hidden; background: #f7e9e5;
  display: grid; place-items: center; border: 5px solid #ffffff22;
}
.portrait-placeholder { color: var(--red); font-size: 48px; font-weight: 800; }
.portrait { width: 100%; height: 100%; object-fit: cover; display: none; }
.identity h1 { margin: 0; font-size: 23px; line-height: 1.2; letter-spacing: .3px; }
.job-title { margin: 8px 0 0; font-size: 12px; font-weight: 600; letter-spacing: .7px; }
.side-section { margin-top: 32px; }
.side-section h2 {
  margin: 0 0 20px; font-size: 17px; text-transform: uppercase; letter-spacing: 1.4px;
}
.contact-list { list-style: none; padding: 0; margin: 0; }
.contact-list li { display: flex; align-items: flex-start; gap: 10px; margin: 0 0 16px; font-size: 13px; line-height: 1.5; overflow-wrap: anywhere; }
.contact-list a { color: white; text-decoration: none; }
.contact-list a:hover { text-decoration: underline; }
.icon { width: 18px; flex: 0 0 18px; font-size: 17px; text-align: center; }
.education { margin-bottom: 18px; font-size: 13px; line-height: 1.35; }
.education strong { display: block; font-size: 12px; color: #ffe1df; }
.education p { margin: 2px 0; font-weight: 600; }
.education span { opacity: .9; }
.language { margin: 0 0 14px; font-size: 13px; }
.language > div:first-child { display: flex; justify-content: space-between; gap: 8px; }
.language b { font-size: 10px; font-weight: 500; opacity: .8; }
.meter, .skill-track { height: 7px; margin-top: 7px; background: #f6a0a2; }
.meter i { display: block; height: 100%; background: #333; }
.content { padding: 42px 40px 48px; }
.main-section { margin-bottom: 35px; }
.main-section h2 {
  margin: 0 0 13px; color: #f04d55; font-size: 22px;
  text-transform: uppercase; letter-spacing: 1.1px;
}
.profile p, .details p { margin: 0; font-size: 13.5px; line-height: 1.55; }
.timeline-item { display: grid; grid-template-columns: 125px 1fr; gap: 18px; margin: 22px 0; }
.date { color: #f0646a; font-size: 12px; font-weight: 600; line-height: 1.4; }
.date small { font-size: 11px; }
.details h3 { margin: 0 0 5px; font-size: 14px; }
.details p { color: #333; }
.skill { display: grid; grid-template-columns: 135px 1fr; align-items: center; gap: 16px; margin: 18px 0; }
.skill > span { color: #f04d55; font-size: 13px; text-transform: uppercase; line-height: 1.3; }
.skill-track { margin: 0; background: #f4a0a3; height: 9px; }
.skill-track i { display: block; height: 100%; background: #333; }
.hint { color: #888; font-size: 10px; margin-top: 12px; }
.projects ul { margin: 0; padding-left: 18px; font-size: 13px; line-height: 1.8; }
body.dark { --paper: #242424; --ink: #f4f4f4; --muted: #bbb; }
body.dark .content { color: #eee; }
body.dark .details p { color: #ddd; }
body.dark .hint { color: #aaa; }
@media (max-width: 720px) {
  body { padding: 10px; }
  .cv { grid-template-columns: 1fr; }
  .sidebar { padding: 30px 25px; }
  .content { padding: 30px 25px; }
  .timeline-item { grid-template-columns: 1fr; gap: 5px; }
  .skill { grid-template-columns: 1fr; gap: 7px; }
  .toolbar { justify-content: center; }
}
@media print {
  @page { size: A4; margin: 0; }
  body { padding: 0; background: white; print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .toolbar { display: none !important; }
  .cv { width: 210mm; min-height: 297mm; max-width: none; margin: 0; box-shadow: none; }
  .sidebar { padding: 30px 24px; }
  .content { padding: 34px 30px; }
}
"""

js = """const photoInput = document.getElementById('photoInput');
const portrait = document.getElementById('portrait');
const placeholder = document.getElementById('portraitPlaceholder');

photoInput.addEventListener('change', (event) => {
  const file = event.target.files && event.target.files[0];
  if (!file) return;
  if (!file.type.startsWith('image/')) {
    alert('Veuillez choisir un fichier image.');
    return;
  }
  const reader = new FileReader();
  reader.onload = () => {
    portrait.src = reader.result;
    portrait.style.display = 'block';
    placeholder.style.display = 'none';
  };
  reader.readAsDataURL(file);
});

document.getElementById('printButton').addEventListener('click', () => window.print());

document.getElementById('themeButton').addEventListener('click', (event) => {
  document.body.classList.toggle('dark');
  event.currentTarget.textContent = document.body.classList.contains('dark')
    ? 'Mode clair'
    : 'Mode sombre';
});
"""

readme = """CV HTML/CSS/JavaScript — Tanga Boniface Andy

1. Décompressez le dossier.
2. Ouvrez index.html avec Chrome, Edge ou Firefox.
3. Cliquez sur « Ajouter ma photo » pour choisir votre portrait.
4. Modifiez les textes directement dans index.html avec VS Code.
5. Cliquez sur « Télécharger / Imprimer en PDF », puis choisissez « Enregistrer au format PDF ».

Les fichiers sont séparés :
- index.html : contenu du CV
- style.css : mise en page et couleurs
- script.js : ajout de photo, thème sombre et impression

Pensez à vérifier le numéro, l'adresse e-mail, les dates et les niveaux de compétences avant d'envoyer le CV.
"""

(out/"index.html").write_text(html, encoding="utf-8")
(out/"style.css").write_text(css, encoding="utf-8")
(out/"script.js").write_text(js, encoding="utf-8")
(out/"README.txt").write_text(readme, encoding="utf-8")

zip_path = Path("/mnt/data/CV_Tanga_Boniface_HTML_CSS_JS.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for f in out.iterdir():
        z.write(f, arcname=f.name)

print("Fichiers créés :", ", ".join(p.name for p in out.iterdir()))
print("Archive :", zip_path)
