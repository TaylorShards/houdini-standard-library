# 📘 HOUDINI STANDARD LIBRARY — v0.4.0 REFERENCE

**Official Documentation Sheet**
*Organized by Layer, Purpose, and Recommended Usage.*

---

## LAYER 1 — SYSTEM INPUTS
**("The Nervous System")**
*These variables feed raw data into the system from JavaScript. They do not style elements directly; they drive the other layers.*

| Variable | Type | Inherits | Purpose | Typical Use |
| :--- | :--- | :--- | :--- | :--- |
| `--scalar` | `<number>` | ✔︎ | Main universal input | Scroll progress, multipliers |
| `--scalar-x` | `<number>` | ✔︎ | Horizontal input | Pointer X ratio |
| `--scalar-y` | `<number>` | ✔︎ | Vertical input | Pointer Y ratio |
| `--scalar-z` | `<number>` | ✔︎ | Depth input | 3D effects |
| `--state` | `<integer>` | ✔︎ | State machine value | Tabs, modes, steps |
| `--progress` | `<number>` | ✔︎ | Animation progress | Timelines, loaders |
| `--seed` | `<integer>` | ✔︎ | Randomization | Noise, procedural variation |

---

## LAYER 2 — COLOR SYSTEM
**("The Paint Layer")**
*Inherits by design. These determine the visual palette and flow downward through the DOM.*

| Variable | Type | Inherits | Purpose |
| :--- | :--- | :--- | :--- |
| `--hue` | `<number>` | ✔︎ | Base color hue |
| `--sat` | `<percentage>` | ✔︎ | Saturation |
| `--lit` | `<percentage>` | ✔︎ | Lightness |
| `--alpha` | `<number>` | ✔︎ | Opacity / global alpha |
| `--warmth` | `<number>` | ✔︎ | Shift hue toward warm/cool |
| `--contrast` | `<number>` | ✔︎ | Global tone mapping |
| `--vibrance` | `<number>` | ✔︎ | Selective saturation boost |

**Usage Note:** Combine with `color-mix()`, HSL functions, and gradients for dynamic skinning.

---

## LAYER 3 — TRANSFORM / MOTION
**("The Physics Layer")**
*Non-Inheriting. These are raw movement primitives suitable for animation and physics.*

### Translation
| Variable | Type | Inherits | Purpose |
| :--- | :--- | :--- | :--- |
| `--x` | `<length-percentage>` | ✘ | Horizontal movement |
| `--y` | `<length-percentage>` | ✘ | Vertical movement |
| `--z` | `<length>` | ✘ | Depth push/pull |

### Rotation & Scale
| Variable | Purpose |
| :--- | :--- |
| `--rotate` | Global rotation |
| `--rotate-x` / `y` / `z` | 3D axis rotation |
| `--scale` | Uniform scale |
| `--scale-x` / `y` | Axis scale |

### Kinetics (Velocity & Acceleration)
| Variable | Purpose |
| :--- | :--- |
| `--vx`, `--vy`, `--vz` | Velocity vectors |
| `--ax`, `--ay` | Acceleration vectors |

**Usage Note:** Use the full stack to build unified transforms without conflicts:
`transform: translate3d(var(--x), var(--y), var(--z)) rotateX(var(--rotate-x))...`

---

## LAYER 4 — FILTERS / EFFECTS
**("The FX Layer")**
*Local, Non-Inheriting. Post-processing style effects.*

| Variable | Purpose |
| :--- | :--- |
| `--opacity` | Element fade |
| `--blur` | Gaussian blur |
| `--brightness` | Brightness multiplication |
| `--contrast-fx` | Micro contrast |
| `--saturate` | Saturation multiplier |
| `--grayscale` | Monochrome |
| `--hue-rotate` | Color spin |
| `--invert` | Light/dark inversion |
| `--shadow-x/y` | Shadow offset |
| `--shadow-blur` | Shadow blur radius |
| `--glow` | Global glow intensity (Inherits) |

---

## LAYER 5 — TYPOGRAPHY
**("The Voice Layer")**
*Inheriting for consistency.*

| Variable | Type | Purpose |
| :--- | :--- | :--- |
| `--font-size` | `<length>` | Scale text responsively |
| `--font-weight` | `<number>` | Dynamic emphasis |
| `--letter-space` | `<length>` | Tracking |
| `--line-height` | `<number>` | Rhythm control |
| `--int` | `<integer>` | Counter animation |
| `--float` | `<number>` | Decimal counter animation |

---

## LAYER 6 — LAYOUT / GEOMETRY
**("The Shape Layer")**
*Controls box geometry. Inherited unless unsafe.*

| Variable | Purpose |
| :--- | :--- |
| `--radius` | Border radius |
| `--padding` | Internal spacing |
| `--gap` | Child spacing |
| `--columns` | Grid column count |
| `--perspective` | 3D depth |
| `--width` / `--height` | Explicit dimensions (Non-inheriting) |

---

## THE ENGINE MODEL (How Layers Combine)

1.  **Input Layer** drives **Motion, Color, and FX**.
    *   *Example:* `--y: calc(var(--progress) * 100vh);`
2.  **Motion Layer** builds the **Transform**.
3.  **Color + FX Layers** produce the **Visual State**.
4.  **Geometry Layer** defines the **Container**.

Together, these layers behave like a **CSS shader pipeline**, enabling procedural UI without JavaScript overhead.