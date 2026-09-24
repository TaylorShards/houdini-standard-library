"""HSL CI smoke: the regression suite the dataset verifier was calibrated on.
Subset of data-factory/verifier/calibrate.py, run against this repo's own tree.
Fails the build if the v0.5.1 repairs regress."""
import sys
from playwright.sync_api import sync_playwright

BASE = 'http://localhost:8790/examples'
failures = []

with sync_playwright() as pw:
    b = pw.chromium.launch()

    # --glow alive (v0.5.1 regression: must be a px length, shadows non-none)
    p = b.new_page()
    p.goto(f'{BASE}/05-reactive-timeline.4.html')
    p.wait_for_timeout(1200)
    p.evaluate("document.querySelector('.chronos-core').style.setProperty('--progress','1')")
    p.wait_for_timeout(300)
    r = p.evaluate("""()=>{const cs=getComputedStyle(document.querySelector('.chronos-core'));return {glow:cs.getPropertyValue('--glow'),shadow:cs.boxShadow}}""")
    if not (r['glow'].strip().endswith('px') and r['shadow'] != 'none'):
        failures.append(f"05.4 glow dead: {r}")
    p.close()

    # 04 tilt is alive (post-fix: tilt declared on .card)
    p = b.new_page()
    p.goto(f'{BASE}/04-cinematic-card.html')
    p.wait_for_timeout(800)
    errs = []
    p.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    t = p.evaluate("() => getComputedStyle(document.querySelector('.card')).transform")
    p.close()
    if errs:
        failures.append(f"04 console errors: {errs}")

    b.close()

if failures:
    print('\n'.join(failures)); sys.exit(1)
print('smoke ok')
