# HSL Examples (v0.5.0)

This directory contains reference implementations of the **Houdini Standard Library**. 
Each example targets specific layers of the engine to verify browser support and syntax strictness.

### 01. Interpolated Gradient (`01-interpolated-gradient.html`)
**Target:** Layer 2 (Color)
**Concept:** Type Mixing
Demonstrates the engine's ability to interpolate two different variable types simultaneously inside a gradient:
*   `--hue-rotate` (`<angle>`) for direction.
*   `--hue` (`<number>`) for color palette shifting.

### 02. Integer Counter (`02-integer-counter.html`)
**Target:** Layer 5 (Typography/Voice)
**Concept:** Integer Interpolation
Uses `transition` on a strictly typed `<integer>` variable.
*   Bridges CSS variables to CSS Counters (`content: counter(num)`).
*   Proves that the browser rounds values automatically during animation.

### 03. Physics Button (`03-physics-button.html`)
**Target:** Layer 3 (Physics)
**Concept:** Reactive UI & Composition
A "Physics Rig" that separates inputs from outputs.
*   Button interactions do not touch `transform`.
*   They update `--scale`, `--y`, and `--rotate-z` independently.
*   The engine composites these into a single 3D matrix.

### 04. Cinematic Card (`04-cinematic-card.html`)
**Target:** Layer 1 (Inputs)
**Concept:** Logic & Calculus
A logic-heavy demo with zero JavaScript logic.
*   JS only provides raw mouse coordinates (0.0 - 1.0).
*   CSS handles all `calc()` math for 3D tilt and glare positioning.
*   *Refactored in v0.5.0 to use standard `--scalar-x` inputs.*

### 05. Reactive Timeline (`05-reactive-timeline.html`)
**Target:** Layer 6 (Shape)
**Concept:** Timeline Mapping
Maps a single variable (`--progress`) to an entire scene.
*   Demonstrates how to drive geometry, color, and position from one slider.
*   *Verified v0.5.0 patch:* `--radius` now supports percentages (e.g., sun geometry).

### 06. Metronome (`06-time-and-origin.html`)
**Target:** Layer 7 (Time) & Layer 8 (Anchor)
**Concept:** The v0.5.0 Feature Set
Specifically designed to test the newest primitives.
*   **Time:** Uses `<time>` typed variables (`--duration`) to control animation speed dynamically.
*   **Anchor:** Uses `<length-percentage>` (`--origin-y`) to move the pivot point for pendulum physics.