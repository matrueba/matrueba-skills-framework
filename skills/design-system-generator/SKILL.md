---
name: design-system-generator
description: Generates a comprehensive frontend Design System & Guidelines document (DESIGN.md) for AI-assisted development. Use this skill when the user asks to define the visual style, design system, design tokens, CSS architecture, or frontend guidelines for a project. It asks discovery questions and produces a structured DESIGN.md file.
---

# design-system-generator

This skill generates a standardized `DESIGN.md` document that defines the visual style, design tokens, component patterns, and strict AI behavior rules for a frontend project. The generated document acts as a single source of truth for any AI agent building the frontend.

## Interaction Flow

Before generating the design system document, you MUST gather context from the user through a structured discovery phase. Ask the following **5 questions** in a single message, clearly numbered. Do not proceed until the user has answered:

### Discovery Questions

1. **¿Qué tipo de aplicación estás construyendo y quién la va a usar?**
   - Describe the application type (e.g., internal dashboard, e-commerce, social app, landing page, SaaS platform, portfolio, blog...) and the target audience (e.g., project managers, end consumers, developers, designers...). This determines the overall tone and visual density.

2. **¿Qué estilo visual o "vibe" quieres para tu interfaz?**
   - Choose or describe the desired aesthetic direction. Examples: minimalist and clean, bold and colorful, dark and immersive, warm and organic, brutalist, retro-futuristic, glassmorphism, corporate/professional, playful/fun. You can also reference specific websites or apps as inspiration.

3. **¿Qué stack de tecnologías CSS y componentes vas a utilizar?**
   - Specify the styling framework (Tailwind CSS, Vanilla CSS, Styled Components, CSS Modules...), component library (Shadcn UI, MUI, Ant Design, Chakra UI, custom...), icon library (Lucide, Heroicons, Font Awesome, Phosphor...), and animation library if any (Framer Motion, GSAP, CSS only...).

4. **¿Tienes colores de marca o preferencias de paleta de colores definidos?**
   - Provide any existing brand colors, preferred color scales (e.g., zinc, slate, indigo, emerald...), or describe the mood you want the colors to convey (e.g., "professional grays", "vibrant blues and oranges", "earthy tones", "dark mode with neon accents"). If you have no preference, the AI will propose a coherent palette based on the application type and visual style.

5. **¿Hay alguna regla o restricción especial que deba seguir la IA al generar el frontend?**
   - Mention any special constraints: dark mode support (yes/no), mobile-first requirement, specific accessibility standards (WCAG AA), brand fonts to use, forbidden patterns, whether to use inline styles, any specific responsive breakpoints, or any other design rule the team enforces.

### Handling Partial Answers

- If the user answers only some questions, **do not assume values for the missing ones**. Re-ask the specific missing questions before proceeding.
- If the user explicitly says "you decide" or "use your best judgment" for any question, you may infer reasonable defaults based on the other answers and clearly state what you chose and why.

## How to use this skill

1. **Ask the discovery questions** listed above in a single, clear message.
2. **Wait for the user's answers** to all 5 questions.
3. **Draft the design system document**:
   - Read the template located at `assets/template.md` and use it as the base structure.
   - Fill in ALL sections with concrete, specific values based on the user's answers. Replace every `[PLACEHOLDER]` with real values.
   - **Be opinionated and specific**: Do not leave vague descriptions. Every color must have a hex code, every typography rule must have concrete classes/values, every component pattern must have implementable styles.
   - Adapt the template to the user's chosen tech stack (e.g., if using Vanilla CSS instead of Tailwind, provide CSS custom properties instead of Tailwind classes; if using MUI instead of Shadcn, reference MUI component conventions).
   - Ensure internal consistency: colors in component patterns must match the design tokens, typography in components must follow the hierarchy, etc.
4. **Save the design system document**:
   - Save the generated file as `DESIGN.md` in the root of the user's project directory.
   - If a `DESIGN.md` already exists, ask the user whether to overwrite it or save with a different name.
5. **Notify the user**:
   - Inform the user that the `DESIGN.md` has been created.
   - Remind them that this file should be referenced by any AI agent building the frontend to ensure visual consistency.
   - Suggest they review it and tweak any values that don't match their exact vision — the document is meant to be a starting point that they refine.
