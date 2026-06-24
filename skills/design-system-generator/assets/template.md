# Frontend Design System & Guidelines for AI

This document defines the strict design and styling rules for this project.

## 1. Overview and Design Concept
* **Application Type:** [APPLICATION_TYPE - e.g., Corporate internal administrative dashboard (B2B SaaS), E-commerce storefront, Marketing landing page, Mobile-first social app, etc.]
* **Visual Style (Vibe):** [VISUAL_STYLE - e.g., Minimalist, clean, and focused on text readability / Bold and vibrant with high visual impact / Dark and immersive with glassmorphism / Warm and organic with soft gradients, etc.]
* **Target Audience and Tone:** [TARGET_AUDIENCE - e.g., Directed at project managers and analysts. The tone must be professional, reliable, and free of unnecessary visual distractions / Young users aged 18-30. The tone must be playful, energetic, and visually stimulating, etc.]

## 2. Tech Stack and CSS Architecture
* **Styling Framework/Methodology:** [STYLING_FRAMEWORK - e.g., Tailwind CSS v3 / Vanilla CSS with BEM / Styled Components / CSS Modules, etc.]
* **Component Library:** [COMPONENT_LIBRARY - e.g., Shadcn UI / MUI (Material UI) / Ant Design / Chakra UI / None (custom components), etc.]
* **Icon Library:** [ICON_LIBRARY - e.g., Lucide React / Heroicons / Font Awesome / Phosphor Icons, etc.]
* **Animation Library:** [ANIMATION_LIBRARY - e.g., Only native CSS/Tailwind transitions and Framer Motion / GSAP / Lottie / None, etc.]

## 3. Design Tokens (Base Variables)

### 3.1. Color Palette
* **Main Background:** [MAIN_BG - e.g., `#FAFAFA` (bg-zinc-50)]
* **Secondary Background (Surfaces/Cards):** [SECONDARY_BG - e.g., `#FFFFFF` (bg-white)]
* **Primary Text:** [PRIMARY_TEXT - e.g., `#09090B` (text-zinc-950)]
* **Secondary Text (Muted):** [SECONDARY_TEXT - e.g., `#71717A` (text-zinc-500)]
* **Primary Color (Accents/Buttons):** [PRIMARY_COLOR - e.g., `#18181B` (bg-zinc-900)]
* **Primary Hover/Active:** [PRIMARY_HOVER - e.g., `#27272A` (bg-zinc-800)]
* **Borders and Dividers:** [BORDER_COLOR - e.g., `#E4E4E7` (border-zinc-200)]
* **System States:**
    * Error/Destructive: [ERROR_COLOR - e.g., `#EF4444` (text/bg-red-500)]
    * Success: [SUCCESS_COLOR - e.g., `#10B981` (text/bg-emerald-500)]
    * Warning: [WARNING_COLOR - e.g., `#F59E0B` (text/bg-amber-500)]
    * Information: [INFO_COLOR - e.g., `#3B82F6` (text/bg-blue-500)]

### 3.2. Typography
* **Primary Font (Reading and Interface):** [PRIMARY_FONT - e.g., `Inter`, fallback to `ui-sans-serif, system-ui`.]
* **Monospace Font (Code/Numerical Data):** [MONO_FONT - e.g., `JetBrains Mono`, fallback to `ui-monospace`.]
* **Strict Hierarchy:**
    * `h1`: [H1_STYLE - e.g., `text-3xl font-bold tracking-tight text-zinc-950`]
    * `h2`: [H2_STYLE - e.g., `text-2xl font-semibold tracking-tight text-zinc-950`]
    * `h3`: [H3_STYLE - e.g., `text-xl font-semibold text-zinc-900`]
    * `body`: [BODY_STYLE - e.g., `text-base font-normal text-zinc-950 leading-relaxed`]
    * `small/caption`: [SMALL_STYLE - e.g., `text-sm font-medium text-zinc-500`]

### 3.3. Spacing, Layout, and Geometry
* **Base Spacing System:** [SPACING_SYSTEM - e.g., Multiples of 4px (Tailwind base: `p-2` = 8px, `gap-4` = 16px, `mt-8` = 32px).]
* **Maximum Container Width:** [MAX_WIDTH - e.g., `1280px` (`max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`).]
* **Border Radius (Rounding):**
    * Interactive elements (Buttons, Inputs): [INTERACTIVE_RADIUS - e.g., `0.375rem` (`rounded-md`).]
    * Container elements (Cards, Modals): [CONTAINER_RADIUS - e.g., `0.5rem` (`rounded-lg`).]
* **Shadows (Elevation):** 
    * Base cards: [CARD_SHADOW - e.g., `shadow-sm`]
    * Dropdowns/Modals: [MODAL_SHADOW - e.g., `shadow-lg`]

### 3.4. Z-Index Management (Layers)
Forbidden to use arbitrary values (e.g., `9999`). Strictly use the following stacking scale:
* **Base (Normal content):** `z-0`
* **Dropdowns / Floating menus:** `z-10`
* **Sticky / Scroll-fixed elements:** `z-20` (e.g., Top Header).
* **Overlays (Dark background for modals):** `z-40` (`bg-black/50 backdrop-blur-sm`).
* **Modals / Dialogs:** `z-50`
* **Notifications / Toasts / Tooltips:** `z-50` (Rendered in a Portal).

## 4. Component Patterns

### Buttons
* **Primary:** [PRIMARY_BUTTON - e.g., `bg-zinc-900 text-white hover:bg-zinc-800 rounded-md px-4 py-2 text-sm font-medium transition-colors`.]
* **Secondary/Outline:** [SECONDARY_BUTTON - e.g., `bg-transparent border border-zinc-200 text-zinc-900 hover:bg-zinc-100 rounded-md px-4 py-2 text-sm font-medium transition-colors`.]
* **Ghost/Text:** [GHOST_BUTTON - e.g., `bg-transparent text-zinc-700 hover:bg-zinc-100 hover:text-zinc-900 rounded-md px-4 py-2 text-sm font-medium`.]

### Cards
* **Visual Appearance:** [CARD_APPEARANCE - e.g., `bg-white border border-zinc-200 rounded-lg shadow-sm`.]
* **Internal Structure:** [CARD_STRUCTURE - e.g., General padding of `p-6`. The Card Header must have an `h3` and separate the main content with `gap-4`.]

### Forms and Inputs
* **Input Style:** [INPUT_STYLE - e.g., `bg-white border border-zinc-200 rounded-md px-3 py-2 text-sm placeholder:text-zinc-500`.]
* **Focus State:** [FOCUS_STATE - e.g., `focus:outline-none focus:ring-2 focus:ring-zinc-900 focus:ring-offset-2 focus:border-transparent`.]
* **Labels:** [LABEL_STYLE - e.g., `text-sm font-medium text-zinc-950 mb-1.5 block`.]

## 5. Interface States (Loading and Empty)

### Loading States
* **Global Strategy:** [LOADING_STRATEGY - e.g., Use animated Skeletons instead of spinners for page content. Small `16px` spinners for buttons in a processing state.]
* **Skeleton Style:** [SKELETON_STYLE - e.g., `animate-pulse bg-zinc-200 rounded-md`.]
* **Interaction Blocking:** [INTERACTION_BLOCKING - e.g., Loading buttons must have `opacity-50 cursor-not-allowed` and show the spinner to the left of the text.]

### Empty States
* **Layout:** [EMPTY_LAYOUT - e.g., Container with `flex flex-col items-center justify-center py-12 text-center`.]
* **Visual Components:** [EMPTY_VISUAL - e.g., Lucide React icon of `w-12 h-12 text-zinc-400 mb-4`.]
* **Typography:** [EMPTY_TYPOGRAPHY - e.g., Title in `h3` and an explanatory subtitle using `text-zinc-500 max-w-sm`.]
* **Call to Action (CTA):** [EMPTY_CTA - e.g., Always include a Primary Button below the text to initiate resource creation.]

## 6. Animations and Transitions (Motion)
* **Global Rule:** [MOTION_RULE - e.g., All state interactions (hover, focus, active) must be transitioned. Zero abrupt changes. Use Tailwind's `transition-all` class.]
* **Standard Duration:** [MOTION_DURATION - e.g., `duration-200`.]
* **Acceleration Curve (Easing):** [MOTION_EASING - e.g., `ease-in-out`.]
* **Page/Route Transitions:** [PAGE_TRANSITIONS - e.g., Smooth entrance opacity with Framer Motion (`initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.3 }}`).]
* **Micro-interactions:** [MICRO_INTERACTIONS - e.g., Modals should scale slightly upon entering (`scale-95` to `scale-100`).]

## 7. Strict AI Behavior Rules
1. **Token Consistency:** [TOKEN_RULE - e.g., Apply only the Tailwind variables declared in section 3. Do not use colors outside the `zinc` scale unless it is a system state (error, success, etc.).]
2. **Inline Styles Usage:** [INLINE_RULE - e.g., The use of `style="..."` attributes is strictly prohibited except for values calculated by JS (e.g., `transform` or progress bar widths).]
3. **Responsiveness:** [RESPONSIVE_RULE - e.g., Mobile-first development is mandatory. Use the `base` format for mobile and `md:` modifiers for tablets/desktop.]
4. **Accessibility (a11y):** [A11Y_RULE - e.g., Mandatory use of semantic tags (`<nav>`, `<main>`, `<section>`). Every button or link must be keyboard navigable and have the `focus:ring` state defined.]
5. **Dark Mode:** [DARK_MODE_RULE - e.g., Completely ignore dark mode in this phase. Do not generate `dark:` classes / Implement full dark mode support using `dark:` variant classes.]
6. **Iconography:** [ICON_RULE - e.g., Lucide icons must always have `className="w-5 h-5"` and `strokeWidth={2}` by default, except in Empty States.]
