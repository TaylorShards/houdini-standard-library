# Architecture & Design Decisions

## 1. The Core Philosophy: "Engine vs. Component"
Most CSS frameworks (Bootstrap, Tailwind) provide **Components** (classes that look like buttons).
HSL provides an **Engine** (typed variables that behave like physics).

**Decision:** We do not provide `.btn` classes. We provide `--scale` and `--hue`.
**Reasoning:** This allows the library to be agnostic to the design system. It is infrastructure, not UI.

## 2. Type Strictness and The "Square Sun" Principle
Standard CSS is loosely typed. HSL is strictly typed using `@property`.

**Constraint:** A variable defined as `<length>` (e.g., `--radius`) generally rejects `<percentage>` values in strict environments.
**Example:** Passing `50%` to a `<length>` property will result in an invalid state (falling back to 0), causing rendering artifacts (e.g., a square instead of a circle).
**Implication:** Developers must respect the schema. Mathematical operations (`calc`) must resolve to the correct type.

## 3. Inheritance Model (The "Nervous System" vs "Physics")
We separate variables into two categories based on inheritance:

*   **Inheriting (Theme Data):** Color (`--hue`), Typography (`--font-size`), and State (`--progress`) must flow down the DOM tree so children match their parents.
*   **Non-Inheriting (Physics Data):** Transform vectors (`--x`, `--rotate`, `--scale`) must **NOT** inherit.
    *   *Why?* If `--scale: 1.1` inherited, a button inside a card would scale *twice* (1.1 * 1.1 = 1.21).
    *   *Correction:* By setting `inherits: false`, we ensure physics applied to a parent does not distort the child.

## 4. The Pipeline Model
The library is designed to function as a unidirectional data pipeline:
1.  **Input:** Javascript/User sets scalar values (`--progress`, `--scalar`).
2.  **Logic:** CSS `calc()` derives visual values (Input * Multiplier).
3.  **Output:** The browser renders the pixel.

This moves state management from the JavaScript thread to the CSS Compositor thread.