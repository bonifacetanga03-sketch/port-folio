const photoInput = document.getElementById('photoInput');
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
