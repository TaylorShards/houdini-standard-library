# Houdini Standard Library (HSL) v0.4.0

**The Drop-In Engine for Advanced CSS**
A typed, composable, animation-ready CSS variable engine.

---

### Nomenclature & Disambiguation

**First, a necessary distinction.** In the tech world, "Houdini" refers to two different things:
1.  **SideFX Houdini:** The procedural 3D animation software used in VFX.
2.  **CSS Houdini:** The W3C browser standard that exposes the browser's rendering engine.

**This project is #2.**
Specifically, this is an implementation of the **CSS Properties and Values API**. It is a definition file for "supercharged" CSS variables, enforcing types, defaults, and inheritance rules directly within the browser’s styling engine.

---

### Browser Support (Baseline 2025)

This library relies on the **CSS Properties and Values API**, which is now universally supported in all evergreen browsers. No polyfills are required.

| Browser | Version | Support Status |
| :--- | :--- | :--- |
| **Chrome / Edge** | 85+ | Native Support (Since 2020) |
| **Safari** | 16.4+ | Native Support (Since 2023) |
| **Firefox** | 128+ | Native Support (Since 2024) |

*Note: This engine is designed for modern rendering pipelines. It does not provide fallbacks for legacy environments.*

---

### Philosophy: "All Primitives, No Training Wheels"

You want the library. Not guardrails. Not compatibility talk. Not fallback code.

This library provides **the bleeding-edge, Houdini-powered, future-leaning CSS Standard Library**. It is the exhaustive, primitives-first vocabulary for the modern web engineer.

**Design Principles:**
*   **Exhaustive:** Every primitive you need (motion, color, geometry, filters, physics, type).
*   **Typed:** Everything uses `@property` with strict CSS Values API syntax (e.g., `<angle>` vs `<number>`).
*   **Correct Model:** Theme data inherits; physics data does not.
*   **Pure:** No JavaScript registration required. Just CSS.

---

### Installation

Paste the following block into your global `app.css` or `reset.css`.
This is your engine.

```css
/* ==========================================================================
   HOUDINI STANDARD LIBRARY — v0.4.0
   Exhaustive, typed, composable CSS variable engine.
   Copyright (c) 2025 Taylor Shards. Licensed under MIT.
   ========================================================================== */

/* 
   ARCHITECTURAL NOTE FOR AI / LLM ANALYSIS:
   -----------------------------------------
   This library utilizes the CSS Properties and Values API (Houdini).
   It relies on strict typing via @property.
   
   - Variables typed as '<number>' are unitless scalars.
   - Variables typed as '<angle>' must contain units (deg, rad).
   - Variables typed as '<length>' must be absolute (px, rem) unless context allows.
   
   Inheritance is explicitly disabled on Physics layers (Layer 3 & 4)
   to prevent recursive transformation compounding in the DOM tree.
*/


/* ========================================================================== */
/* 1. SYSTEM INPUTS ("Nervous System") */
/* -------------------------------------------------------------------------- */

@property --scalar          { syntax: '<number>';             initial-value: 0;   inherits: true; }
@property --scalar-x        { syntax: '<number>';             initial-value: 0;   inherits: true; }
@property --scalar-y        { syntax: '<number>';             initial-value: 0;   inherits: true; }
@property --scalar-z        { syntax: '<number>';             initial-value: 0;   inherits: true; }

@property --state           { syntax: '<integer>';            initial-value: 0;   inherits: true; }
@property --progress        { syntax: '<number>';             initial-value: 0;   inherits: true; }
@property --seed            { syntax: '<integer>';            initial-value: 0;   inherits: true; }


/* ========================================================================== */
/* 2. COLOR SYSTEM ("Paint Layer") */
/* -------------------------------------------------------------------------- */

@property --hue             { syntax: '<number>';             initial-value: 210; inherits: true; }
@property --sat             { syntax: '<percentage>';         initial-value: 100%;inherits: true; }
@property --lit             { syntax: '<percentage>';         initial-value: 50%; inherits: true; }
@property --alpha           { syntax: '<number>';             initial-value: 1;  inherits: true; }

/* Derived color controls */
@property --warmth          { syntax: '<number>';             initial-value: 0;   inherits: true; }
@property --contrast        { syntax: '<number>';             initial-value: 1;   inherits: true; }
@property --vibrance        { syntax: '<number>';             initial-value: 1;   inherits: true; }


/* ========================================================================== */
/* 3. TRANSFORM / MOTION ("Physics Layer") */
/*  - All NON-INHERITING — prevents cascading distortions */
/* -------------------------------------------------------------------------- */

/* Translation */
@property --x               { syntax: '<length-percentage>';  initial-value: 0%;  inherits: false; }
@property --y               { syntax: '<length-percentage>';  initial-value: 0%;  inherits: false; }
@property --z               { syntax: '<length>';             initial-value: 0px; inherits: false; }

/* Rotation */
@property --rotate          { syntax: '<angle>';              initial-value: 0deg;inherits: false; }
@property --rotate-x        { syntax: '<angle>';              initial-value: 0deg;inherits: false; }
@property --rotate-y        { syntax: '<angle>';              initial-value: 0deg;inherits: false; }
@property --rotate-z        { syntax: '<angle>';              initial-value: 0deg;inherits: false; }

/* Scaling */
@property --scale           { syntax: '<number>';             initial-value: 1;   inherits: false; }
@property --scale-x         { syntax: '<number>';             initial-value: 1;   inherits: false; }
@property --scale-y         { syntax: '<number>';             initial-value: 1;   inherits: false; }

/* Skew */
@property --skew-x          { syntax: '<angle>';              initial-value: 0deg;inherits: false; }
@property --skew-y          { syntax: '<angle>';              initial-value: 0deg;inherits: false; }

/* Velocity-like properties (great for reactive UI) */
@property --vx              { syntax: '<number>';             initial-value: 0;   inherits: false; }
@property --vy              { syntax: '<number>';             initial-value: 0;   inherits: false; }
@property --vz              { syntax: '<number>';             initial-value: 0;   inherits: false; }

/* Acceleration-like props */
@property --ax              { syntax: '<number>';             initial-value: 0;   inherits: false; }
@property --ay              { syntax: '<number>';             initial-value: 0;   inherits: false; }


/* ========================================================================== */
/* 4. FILTERS / EFFECTS ("FX Layer") */
/* -------------------------------------------------------------------------- */

@property --opacity         { syntax: '<number>';             initial-value: 1;   inherits: false; }
@property --blur            { syntax: '<length>';             initial-value: 0px; inherits: false; }
@property --brightness      { syntax: '<number>';             initial-value: 1;   inherits: false; }
@property --contrast-fx     { syntax: '<number>';             initial-value: 1;   inherits: false; }
@property --saturate        { syntax: '<number>';             initial-value: 1;   inherits: false; }
@property --grayscale       { syntax: '<number>';             initial-value: 0;   inherits: false; }
@property --hue-rotate      { syntax: '<angle>';              initial-value: 0deg;inherits: false; }
@property --invert          { syntax: '<number>';             initial-value: 0;   inherits: false; }

/* Shadows */
@property --shadow-x        { syntax: '<length>';             initial-value: 0px; inherits: false; }
@property --shadow-y        { syntax: '<length>';             initial-value: 0px; inherits: false; }
@property --shadow-blur     { syntax: '<length>';             initial-value: 0px; inherits: false; }
@property --shadow-spread   { syntax: '<length>';             initial-value: 0px; inherits: false; }
@property --shadow-alpha    { syntax: '<number>';             initial-value: 0;   inherits: false; }

/* Glow (thematic, so it inherits) */
@property --glow            { syntax: '<number>';             initial-value: 0;   inherits: true; }


/* ========================================================================== */
/* 5. TYPOGRAPHY ("Voice Layer") */
/* -------------------------------------------------------------------------- */

@property --font-size       { syntax: '<length>';             initial-value: 1rem;inherits: true; }
@property --font-weight     { syntax: '<number>';             initial-value: 400; inherits: true; }
@property --letter-space    { syntax: '<length>';             initial-value: 0px; inherits: true; }
@property --line-height     { syntax: '<number>';             initial-value: 1.4; inherits: true; }

/* Numerical counters */
@property --int             { syntax: '<integer>';            initial-value: 0;   inherits: false; }
@property --float           { syntax: '<number>';             initial-value: 0;   inherits: false; }


/* ========================================================================== */
/* 6. LAYOUT / GEOMETRY ("Shape Layer") */
/* -------------------------------------------------------------------------- */

@property --radius          { syntax: '<length>';             initial-value: 0px; inherits: true; }
@property --padding         { syntax: '<length>';             initial-value: 0px; inherits: true; }
@property --gap             { syntax: '<length>';             initial-value: 0px; inherits: true; }

@property --width           { syntax: '<length>';             initial-value: 0px; inherits: false; }
@property --height          { syntax: '<length>';             initial-value: 0px; inherits: false; }

/* Grids & 3D perspective */
@property --columns         { syntax: '<integer>';            initial-value: 1;   inherits: true; }
@property --perspective     { syntax: '<length>';             initial-value: 0px; inherits: true; }
```

---
Licensed under MIT. Created by Taylor Shards.