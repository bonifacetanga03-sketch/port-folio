const EXCHANGE_RATE = 655;
const dishes = [
  {
    id: 1,
    name: 'Filet de bœuf grillé',
    category: 'Signature',
    price: 38,
    time: '25 min',
    calories: '640 kcal',
    ingredients: ['Bœuf', 'Truffe', 'Purée'],
    image: 'https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=900&q=80',
    popular: true,
    available: true
  },
  {
    id: 2,
    name: 'Risotto aux champignons',
    category: 'Végétarien',
    price: 24,
    time: '20 min',
    calories: '510 kcal',
    ingredients: ['Risotto', 'Champignons', 'Parmesan'],
    image: 'https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=900&q=80',
    popular: false,
    available: true
  },
  {
    id: 3,
    name: 'Tarte chocolat noir',
    category: 'Desserts',
    price: 14,
    time: '10 min',
    calories: '430 kcal',
    ingredients: ['Chocolat', 'Crème', 'Fruits rouges'],
    image: 'https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=900&q=80',
    popular: true,
    available: true
  },
  {
    id: 4,
    name: 'Salade d’été',
    category: 'Entrées',
    price: 16,
    time: '12 min',
    calories: '310 kcal',
    ingredients: ['Avocat', 'Tomates', 'Herbes'],
    image: 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?auto=format&fit=crop&w=900&q=80',
    popular: false,
    available: false
  }
];

const cart = [];
let currentFilter = 'Tous';

const menuGrid = document.getElementById('menuGrid');
const filters = document.getElementById('filters');
const searchInput = document.getElementById('searchInput');
const cartItems = document.getElementById('cartItems');
const subtotalEl = document.getElementById('subtotal');
const totalEl = document.getElementById('total');
const cartCount = document.getElementById('cartCount');
const toast = document.getElementById('toast');
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');
const themeToggle = document.getElementById('themeToggle');
const reservationForm = document.getElementById('reservationForm');
const availabilityText = document.getElementById('availabilityText');
const trackToggle = document.getElementById('trackToggle');
const timelineSteps = Array.from(document.querySelectorAll('.timeline-step'));
const checkoutBtn = document.getElementById('checkoutBtn');

function formatFcfa(value) {
  return `${Math.round(value).toLocaleString('fr-FR')} FCFA`;
}

function renderFilters() {
  const categories = ['Tous', ...new Set(dishes.map((dish) => dish.category))];
  filters.innerHTML = categories.map((category) => `
    <button class="filter-chip ${currentFilter === category ? 'active' : ''}" data-category="${category}">${category}</button>
  `).join('');

  filters.querySelectorAll('.filter-chip').forEach((btn) => {
    btn.addEventListener('click', () => {
      currentFilter = btn.dataset.category;
      renderFilters();
      renderMenu();
    });
  });
}

function renderMenu() {
  const query = searchInput.value.trim().toLowerCase();
  const visible = dishes.filter((dish) => {
    const matchesCategory = currentFilter === 'Tous' || dish.category === currentFilter;
    const matchesSearch = dish.name.toLowerCase().includes(query) || dish.ingredients.join(' ').toLowerCase().includes(query);
    return matchesCategory && matchesSearch;
  });

  menuGrid.innerHTML = visible.map((dish) => `
    <article class="menu-card">
      <div class="menu-image" style="background-image:url('${dish.image}')"></div>
      <div class="menu-content">
        <div class="menu-meta">
          <span>${dish.category}</span>
          <span>${dish.time}</span>
        </div>
        <h3>${dish.name}</h3>
        <p>${dish.ingredients.join(' • ')}</p>
        <div class="menu-meta">
          <span>${dish.calories}</span>
          <strong>${formatFcfa(dish.price * EXCHANGE_RATE)}</strong>
        </div>
        <div class="card-actions">
          <button class="primary" data-add="${dish.id}">Ajouter</button>
          <button data-fav="${dish.id}">☆</button>
        </div>
      </div>
    </article>
  `).join('');

  menuGrid.querySelectorAll('[data-add]').forEach((btn) => {
    btn.addEventListener('click', () => addToCart(Number(btn.dataset.add)));
  });
}

function addToCart(id) {
  const dish = dishes.find((item) => item.id === id);
  if (!dish) return;

  const existing = cart.find((item) => item.id === id);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ ...dish, quantity: 1 });
  }

  renderCart();
  showToast(`${dish.name} ajouté au panier`);
}

function updateQuantity(id, delta) {
  const item = cart.find((entry) => entry.id === id);
  if (!item) return;
  item.quantity += delta;
  if (item.quantity <= 0) {
    const index = cart.findIndex((entry) => entry.id === id);
    cart.splice(index, 1);
  }
  renderCart();
}

function renderCart() {
  cartCount.textContent = cart.reduce((sum, item) => sum + item.quantity, 0);

  if (!cart.length) {
    cartItems.innerHTML = '<p>Aucun plat dans le panier pour le moment.</p>';
    subtotalEl.textContent = '0 FCFA';
    totalEl.textContent = '3 275 FCFA';
    return;
  }

  cartItems.innerHTML = cart.map((item) => `
    <div class="cart-item">
      <div>
        <strong>${item.name}</strong>
        <p>${formatFcfa(item.price * EXCHANGE_RATE)}</p>
      </div>
      <div class="qty-control">
        <button data-change="-${item.id}">−</button>
        <span>${item.quantity}</span>
        <button data-change="+${item.id}">+</button>
      </div>
    </div>
  `).join('');

  const subtotal = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  subtotalEl.textContent = formatFcfa(subtotal * EXCHANGE_RATE);
  totalEl.textContent = formatFcfa((subtotal * EXCHANGE_RATE) + 3275);

  cartItems.querySelectorAll('[data-change]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const sign = btn.dataset.change.startsWith('+') ? 1 : -1;
      const id = Number(btn.dataset.change.slice(1));
      updateQuantity(id, sign);
    });
  });
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add('show');
  clearTimeout(showToast.timeout);
  showToast.timeout = setTimeout(() => toast.classList.remove('show'), 1800);
}

menuToggle.addEventListener('click', () => navLinks.classList.toggle('open'));
searchInput.addEventListener('input', renderMenu);

reservationForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const date = document.getElementById('resDate').value;
  const guests = document.getElementById('resGuests').value;
  availabilityText.textContent = `Réservation prête pour ${guests} personnes le ${date || 'ce soir'}.`;
  showToast('Réservation vérifiée');
});

trackToggle.addEventListener('click', () => {
  timelineSteps.forEach((step, index) => {
    step.classList.toggle('active', index <= 2);
  });
  showToast('Statut mis à jour');
});

checkoutBtn.addEventListener('click', () => {
  showToast('Paiement sécurisé prêt à être finalisé');
});

themeToggle.addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', next);
  themeToggle.textContent = next === 'light' ? '☀︎' : '☾';
});

renderFilters();
renderMenu();
renderCart();
