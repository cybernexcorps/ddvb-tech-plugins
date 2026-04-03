# Proposal JavaScript Template

Copy and adapt this JS block for every interactive proposal. Place at the end of the HTML body.

## IntersectionObserver — Scroll Reveal

```javascript
// Animate elements as they enter viewport
document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll('[data-animate]').forEach(el => {
    observer.observe(el);
  });
});
```

### CSS for animated elements

```css
[data-animate] {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
[data-animate].visible {
  opacity: 1;
  transform: translateY(0);
}

/* Staggered grid items */
[data-animate-delay="1"] { transition-delay: 0.1s; }
[data-animate-delay="2"] { transition-delay: 0.2s; }
[data-animate-delay="3"] { transition-delay: 0.3s; }
[data-animate-delay="4"] { transition-delay: 0.4s; }
```

### Usage in HTML

```html
<div class="card" data-animate data-animate-delay="1">
  <h3>Card Title</h3>
  <p>Card content</p>
</div>
```

## Number Counter Animation

```javascript
function animateCounter(el) {
  const target = parseInt(el.dataset.target);
  const suffix = el.dataset.suffix || '';
  const prefix = el.dataset.prefix || '';
  const duration = 1500;
  const start = performance.now();

  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease-out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(target * eased);
    el.textContent = prefix + current.toLocaleString('ru-RU') + suffix;
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

// Trigger on scroll
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      animateCounter(entry.target);
      counterObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('[data-counter]').forEach(el => {
  counterObserver.observe(el);
});
```

### Usage

```html
<span data-counter data-target="350" data-suffix=" ч/мес">0</span>
```

## Active Section Navigation

```javascript
// Highlight current section in sidebar nav
const sections = document.querySelectorAll('.section-page, .cover');
const navLinks = document.querySelectorAll('.nav-link');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.id;
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === '#' + id);
      });
    }
  });
}, { threshold: 0.3 });

sections.forEach(section => {
  if (section.id) sectionObserver.observe(section);
});
```

## Smooth Scroll

```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
```

## Scroll Progress Bar

```javascript
const progressBar = document.querySelector('.progress-bar');
window.addEventListener('scroll', () => {
  const scrolled = window.scrollY;
  const total = document.documentElement.scrollHeight - window.innerHeight;
  const pct = (scrolled / total) * 100;
  progressBar.style.width = pct + '%';
});
```

### CSS

```css
.progress-bar {
  position: fixed;
  top: 0; left: 0;
  height: 3px;
  background: var(--ddvb-gold);
  z-index: 1000;
  transition: width 0.1s;
}
```

## Expandable Cards

```javascript
document.querySelectorAll('[data-expandable]').forEach(card => {
  const toggle = card.querySelector('.card-toggle');
  const content = card.querySelector('.card-details');
  toggle.addEventListener('click', () => {
    const isOpen = content.style.maxHeight;
    content.style.maxHeight = isOpen ? null : content.scrollHeight + 'px';
    toggle.classList.toggle('open');
  });
});
```

### CSS

```css
.card-details {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
}
.card-toggle {
  cursor: pointer;
  user-select: none;
}
.card-toggle::after {
  content: '+';
  float: right;
  font-size: 18px;
  font-weight: 700;
  color: var(--ddvb-gold);
  transition: transform 0.3s;
}
.card-toggle.open::after {
  transform: rotate(45deg);
}
```

## Tab Switcher

```javascript
document.querySelectorAll('.tabs').forEach(tabGroup => {
  const buttons = tabGroup.querySelectorAll('.tab-btn');
  const panels = tabGroup.querySelectorAll('.tab-panel');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      document.getElementById(btn.dataset.tab).classList.add('active');
    });
  });
});
```

### CSS

```css
.tab-btn {
  padding: 8px 20px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  border: none;
  background: var(--ddvb-gray-100);
  color: var(--ddvb-muted);
  cursor: pointer;
  transition: all 0.2s;
}
.tab-btn.active {
  background: var(--ddvb-black);
  color: var(--ddvb-gold);
}
.tab-panel { display: none; }
.tab-panel.active { display: block; }
```

## Sticky Navigation Sidebar

```css
.nav {
  position: fixed;
  left: 0; top: 50%;
  transform: translateY(-50%);
  z-index: 100;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 12px 8px;
  background: rgba(13, 13, 13, 0.9);
  backdrop-filter: blur(8px);
}

.nav-link {
  display: block;
  width: 32px; height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 700;
  color: var(--ddvb-gray-400);
  text-decoration: none;
  transition: color 0.2s;
}
.nav-link.active {
  color: var(--ddvb-gold);
}
.nav-link:hover {
  color: var(--ddvb-white);
}
```
