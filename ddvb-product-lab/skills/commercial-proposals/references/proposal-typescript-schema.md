# Proposal TypeScript Schema

All interfaces are defined in `src/data/proposals.ts`. When creating a new proposal, add a new entry to the `proposals` array in that file.

## Interfaces

```typescript
export interface ProposalMeta {
  label: string;    // dt — small gold uppercase label
  value: string;    // dd — regular text
}

export interface ProposalHero {
  kicker: string;           // Small uppercase text above title (e.g., "Commercial Proposal")
  title: string;            // Main title — use **bold** for gold-highlighted words
  subtitle: string;         // 1-2 sentence description
  meta: ProposalMeta[];     // 3-4 metadata items (client, contact, date, format/referral)
}

export interface ProposalStat {
  value: string;    // The number or short text (e.g., "8", "CZ", "B2C")
  label: string;    // Label below the value (e.g., "Интервью", "Рынка")
  note?: string;    // Optional footnote
}

export interface ProposalPainPoint {
  icon: string;     // Single emoji character
  heading: string;  // Pain point name
  quote: string;    // Verbatim client quote (Russian)
  detail: string;   // Expanded description of the pain
  hours: string;    // Impact/outcome statement
}

export interface ProposalSolution {
  number: string;       // "01", "02", etc.
  name: string;         // Solution name
  description: string;  // 1-2 sentence summary
  painSolved: string;   // Which pain point this addresses
  features: string[];   // List of capabilities/deliverables
}

export interface ProposalPricingTier {
  name: string;          // Tier/component name
  price: string;         // Price with currency (e.g., "40 000 ₽", "$3,000")
  period?: string;       // Payment type (e.g., "Разовый платёж", "Ежемесячно")
  features: string[];    // What's included
  highlighted?: boolean; // Golden highlight for recommended/total tiers
}

export interface ProposalPhase {
  name: string;      // Phase name
  duration: string;  // "Неделя 01", "Шаг 03", etc.
  items: string[];   // What happens in this phase
}

export interface ProposalCta {
  title: string;             // Use **bold** for gold-highlighted words
  subtitle: string;          // 1-2 sentences describing next step
  acceptLabel: string;       // Primary button text (e.g., "Принять предложение")
  discussLabel: string;      // Secondary button text (e.g., "Обсудить детали")
  contactGrid: ProposalMeta[];  // 4 contact items (Telegram, Email, Web, next step)
}

export interface Proposal {
  slug: string;              // URL slug, kebab-case (e.g., "adapter")
  locale: "ru" | "en";      // Usually "ru"
  client: string;            // Client company name
  date: string;              // Month + year in Russian (e.g., "Апрель 2026")
  validUntil?: string;       // Optional expiry date
  referral?: string;         // Who referred the client
  hero: ProposalHero;
  stats?: ProposalStat[];           // Exactly 4 items
  painPoints?: {
    title: string;
    items: ProposalPainPoint[];
  };
  solutions?: {
    title: string;
    subtitle?: string;
    items: ProposalSolution[];
  };
  pricing?: {
    title: string;
    tiers: ProposalPricingTier[];
  };
  timeline?: {
    title: string;
    phases: ProposalPhase[];
  };
  bodyHtml: string;          // Loaded from {slug}-body.html via loadProposalHtml()
  cta: ProposalCta;
}
```

## Loading HTML Bodies

HTML body files live in `src/data/proposals/{slug}-body.html` and are loaded at build time:

```typescript
function loadProposalHtml(filename: string): string {
  return readFileSync(
    join(process.cwd(), "src/data/proposals", filename),
    "utf-8"
  );
}
```

Reference in the data entry: `bodyHtml: loadProposalHtml("{slug}-body.html")`

## Complete Example — Adapter Proposal

```typescript
{
  slug: "adapter",
  locale: "ru",
  client: "Adapter",
  date: "Апрель 2026",
  bodyHtml: loadProposalHtml("adapter-body.html"),
  hero: {
    kicker: "Commercial Proposal",
    title: "AI Transformation Discovery для **Adapter**",
    subtitle:
      "От болей клиентов — к продуктам автоматизации. Глубинное исследование, дорожная карта и приоритизация.",
    meta: [
      { label: "Подготовлено для", value: "Adapter" },
      { label: "Контакт", value: "Павел Полищук" },
      { label: "Дата", value: "Апрель 2026" },
      { label: "Формат", value: "Discovery Phase" },
    ],
  },
  stats: [
    { value: "8", label: "Интервью" },
    { value: "3", label: "Недели" },
    { value: "4", label: "Отдела" },
    { value: "5", label: "Deliverables" },
  ],
  painPoints: {
    title: "Мы понимаем ваши задачи",
    items: [
      {
        icon: "⚙",
        heading: "Ручные процессы",
        quote:
          "Так как это делается всё руками, мы всем продаём тарифы с ограниченным количеством SKU.",
        detail:
          "Мониторинг, биддинг, отчётность, аналитика — всё делается руками. Это создаёт жёсткий лимит по SKU на клиента и блокирует масштабирование.",
        hours:
          "Автоматизация снимает лимит по SKU и позволяет масштабироваться.",
      },
      {
        icon: "📊",
        heading: "Отчётность в Excel",
        quote:
          "Чтобы от менеджера ответить на вопрос, нужно пойти в личный кабинет, зайти, посмотреть в продажи...",
        detail:
          "Еженедельные отчёты клиентам собираются вручную из разных кабинетов. Ответ на вопрос «почему упали продажи?» требует 30+ минут.",
        hours:
          "Автоматизация отчётности освобождает 40-60% времени аналитиков.",
      },
    ],
  },
  solutions: {
    title: "От клиента внутрь",
    subtitle:
      "Боли клиентов · Внутренние процессы · Roadmap · Приоритизация",
    items: [
      {
        number: "01",
        name: "Интервью с клиентами",
        description:
          "4 глубинных интервью с текущими клиентами Adapter. Фокус: боли, ожидания, готовность платить за новые AI-сервисы.",
        painSolved: "Понимание клиентских потребностей",
        features: [
          "Подготовка индивидуальных гайдов",
          "60-минутные сессии с записью и транскрибированием",
          "Фокус: боли, ожидания, новые продукты",
          "Выявление точек роста через AI",
        ],
      },
      {
        number: "02",
        name: "Интервью с командой",
        description:
          "4 интервью с сотрудниками ключевых подразделений: продвижение, контент, торговля, продажи.",
        painSolved: "Понимание внутренних процессов",
        features: [
          "Shadow-сессии с наблюдением за реальной работой",
          "Карты процессов as-is с замерами времени",
          "Выявление узких мест и рутинных задач",
          "Аудит API-возможностей маркетплейсов",
        ],
      },
      {
        number: "03",
        name: "Синтез, Roadmap, Приоритизация",
        description:
          "Тематический анализ всех интервью. Структурированный отчёт, дорожная карта автоматизации и матрица приоритизации.",
        painSolved: "Принятие решений на основе данных",
        features: [
          "Тепловая карта болей (частота × влияние)",
          "Дорожная карта с фазами и зависимостями",
          "Impact vs. Effort матрица для каждого продукта",
          "Презентация результатов руководству",
        ],
      },
    ],
  },
  pricing: {
    title: "Инвестиции",
    tiers: [
      {
        name: "Интервью с клиентами",
        price: "40 000 ₽",
        period: "4 сессии × 10 000 ₽",
        features: [
          "Подготовка гайдов, проведение, запись, транскрипт",
          "60 минут на интервью",
        ],
      },
      {
        name: "Интервью с командой",
        price: "40 000 ₽",
        period: "4 сессии × 10 000 ₽",
        features: [
          "Shadow-сессии, карты процессов, замеры времени",
          "60 минут на интервью",
        ],
      },
      {
        name: "Отчёт + Roadmap + Приоритизация",
        price: "100 000 ₽",
        period: "Фиксированная стоимость",
        features: [
          "Тематический анализ, тепловая карта болей, аудит API",
          "Дорожная карта автоматизации",
          "Матрица приоритизации продуктов",
        ],
        highlighted: true,
      },
      {
        name: "Итого",
        price: "180 000 ₽",
        period: "Полный пакет Discovery",
        features: [
          "8 интервью + отчёт + roadmap + приоритизация",
          "3 недели от старта до финального отчёта",
        ],
        highlighted: true,
      },
    ],
  },
  timeline: {
    title: "План работ",
    phases: [
      {
        name: "Интервью с клиентами",
        duration: "Неделя 01",
        items: [
          "4 глубинных интервью с текущими клиентами Adapter.",
          "Фокус: боли, ожидания, какие сервисы хотят получать, за что готовы платить больше.",
        ],
      },
      {
        name: "Интервью с командой",
        duration: "Неделя 02",
        items: [
          "4 интервью с сотрудниками ключевых подразделений.",
          "Shadow-сессии с наблюдением за реальной работой.",
          "Карты процессов as-is с замерами времени.",
        ],
      },
      {
        name: "Синтез + Отчёт + Roadmap",
        duration: "Неделя 03",
        items: [
          "Тематический анализ всех интервью.",
          "Структурированный отчёт (PDF).",
          "Дорожная карта автоматизации.",
          "Матрица приоритизации.",
          "Презентация результатов руководству.",
        ],
      },
    ],
  },
  cta: {
    title: "Давайте **начнём**",
    subtitle:
      "Через 3 недели у вас будет полная картина: что автоматизировать, в каком порядке и почему — начиная с того, что важно вашим клиентам.",
    acceptLabel: "Принять предложение",
    discussLabel: "Обсудить детали",
    contactGrid: [
      { label: "Telegram", value: "@slavickk" },
      { label: "Email", value: "info@ddvb.tech" },
      { label: "Web", value: "ddvb.tech" },
      { label: "Следующий шаг", value: "NDA + расписание интервью" },
    ],
  },
},
```

## Checklist for New Proposals

1. Choose a slug (kebab-case, lowercase, no spaces)
2. Create `src/data/proposals/{slug}-body.html`
3. Add entry to `proposals` array in `src/data/proposals.ts`
4. Set `bodyHtml: loadProposalHtml("{slug}-body.html")`
5. Verify `npm run build` generates the page for both locales
