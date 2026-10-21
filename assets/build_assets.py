#!/usr/bin/env python3
"""Generates the SVG artwork used in README.md.

Run from anywhere:  python3 assets/build_assets.py

Change the copy or colours below and re-run. The SVGs it writes are plain
text, so small edits can also be made by hand.
"""
from __future__ import annotations

import random
from pathlib import Path
from string import Template

OUT = Path(__file__).resolve().parent

# SVGs shown through <img> cannot load web fonts, so every stack ends in fonts
# that ship with macOS, Windows and Linux.
FONTS = {
    "SANS": "'Helvetica Neue', 'Segoe UI', Inter, Roboto, Arial, sans-serif",
    "SERIF": "Georgia, 'Times New Roman', serif",
    "MONO": "'JetBrains Mono', SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace",
}
PALETTE = {
    "STARLIGHT": "#f5f3ff",  # primary text
    "LAVENDER": "#c4b5fd",   # taglines, request packet
    "LILAC": "#a78bfa",      # borders, prompt
    "MUTED": "#a5a1c2",      # secondary text
    "RED": "#f87171",        # failed calls
    "GREEN": "#4ade80",      # successful calls
}


def render(template: str, **values: object) -> str:
    return Template(template).substitute(**FONTS, **PALETTE, **values)


def starfield(seed: int, count: int, width: int, height: int,
              brightness: tuple[float, float], twinkle_every: int | None) -> str:
    rng = random.Random(seed)
    stars = []
    for i in range(count):
        x, y = rng.uniform(0, width), rng.uniform(0, height)
        r = rng.choice((0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.4))
        if twinkle_every and i % twinkle_every == 0:
            stars.append(
                f'<circle class="tw" cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" '
                f'style="animation-delay:-{rng.uniform(0, 6):.1f}s;'
                f'animation-duration:{rng.uniform(4, 8):.1f}s"/>'
            )
        else:
            opacity = rng.uniform(*brightness)
            stars.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" opacity="{opacity:.2f}"/>')
    return "\n    ".join(stars)


# --------------------------------------------------------------------------
# Hero: name on the left, a Gargantua-style black hole on the right
# (the same motif as the live renderer on aaryanbairagi.in).
# --------------------------------------------------------------------------
HERO = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-labelledby="title desc">
  <title id="title">Aaryan Bairagi</title>
  <desc id="desc">Software engineer in Pune, India. I build systems that work in production, not just on localhost. Open to backend, full-stack and AI/ML roles.</desc>
  <style>
    .name { font: 200 58px $SANS; letter-spacing: 10px; fill: $STARLIGHT; }
    .tag { font: italic 400 23px $SERIF; fill: $LAVENDER; }
    .sub { font: 400 17px $SANS; fill: $MUTED; }
    .chip { font: 500 14px $SANS; fill: #d1fae5; }
    .url { font: 400 13px $SANS; fill: $MUTED; opacity: .75; }
    .tw { opacity: .2; animation: twinkle 6s ease-in-out infinite; }
    .orbit { animation: orbit 3.2s linear infinite; }
    .halo { animation: breathe 9s ease-in-out infinite; }
    @keyframes twinkle { 0%, 100% { opacity: .12; } 50% { opacity: .95; } }
    @keyframes orbit { to { stroke-dashoffset: -$period; } }
    @keyframes breathe { 0%, 100% { opacity: .6; } 50% { opacity: .95; } }
    @media (prefers-reduced-motion: reduce) { .tw, .orbit, .halo { animation: none; } }
  </style>
  <defs>
    <clipPath id="frame"><rect width="1200" height="400" rx="24"/></clipPath>
    <radialGradient id="space" cx="$cx" cy="$cy" r="760" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#160d33"/>
      <stop offset=".45" stop-color="#05030d"/>
      <stop offset="1" stop-color="#000"/>
    </radialGradient>
    <linearGradient id="disk" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ff7a1a" stop-opacity="0"/>
      <stop offset=".14" stop-color="#ff7a1a" stop-opacity=".55"/>
      <stop offset=".34" stop-color="#ffc46b"/>
      <stop offset=".44" stop-color="#fff6e5"/>
      <stop offset=".58" stop-color="#ffd590"/>
      <stop offset=".8" stop-color="#ff8a2a" stop-opacity=".6"/>
      <stop offset="1" stop-color="#ff7a1a" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ring" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fff1d6"/>
      <stop offset=".5" stop-color="#ffb547" stop-opacity=".75"/>
      <stop offset="1" stop-color="#ff8a2a" stop-opacity=".45"/>
    </linearGradient>
    <radialGradient id="halo">
      <stop offset=".42" stop-color="#ffb547" stop-opacity="0"/>
      <stop offset=".5" stop-color="#ffb547" stop-opacity=".32"/>
      <stop offset=".75" stop-color="#a855f7" stop-opacity=".12"/>
      <stop offset="1" stop-color="#7c3aed" stop-opacity="0"/>
    </radialGradient>
    <filter id="nebula" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="70"/></filter>
    <filter id="soft" x="-20%" y="-300%" width="140%" height="700%"><feGaussianBlur stdDeviation="11"/></filter>
    <filter id="lens" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="4"/></filter>
    <filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="1200" height="400" fill="url(#space)"/>
    <circle cx="1010" cy="60" r="200" fill="#6d28d9" opacity=".28" filter="url(#nebula)"/>
    <circle cx="760" cy="390" r="180" fill="#2563eb" opacity=".16" filter="url(#nebula)"/>
    <circle cx="110" cy="10" r="170" fill="#7c3aed" opacity=".12" filter="url(#nebula)"/>
    <g>
    $stars
    </g>

    <g transform="rotate($tilt $cx $cy)">
      <circle class="halo" cx="$cx" cy="$cy" r="150" fill="url(#halo)"/>
      <!-- far side of the accretion disk, behind the shadow -->
      <ellipse cx="$cx" cy="$cy" rx="$rx" ry="$ry" fill="none" stroke="url(#disk)" stroke-width="30" opacity=".45" filter="url(#soft)"/>
      <path d="$upper" fill="none" stroke="url(#disk)" stroke-width="13"/>
      <path class="orbit" d="$upper" fill="none" stroke="#fff7e8" stroke-width="2" stroke-linecap="round" stroke-dasharray="$dash" opacity=".6"/>
      <!-- light from the far side, bent over and under the shadow -->
      <ellipse cx="$cx" cy="$cy" rx="88" ry="83" fill="none" stroke="url(#ring)" stroke-width="10" opacity=".85" filter="url(#lens)"/>
      <circle cx="$cx" cy="$cy" r="71" fill="none" stroke="#fff3dc" stroke-width="1.6" filter="url(#glow)"/>
      <circle cx="$cx" cy="$cy" r="66" fill="#000"/>
      <!-- near side of the disk, crossing in front of the shadow -->
      <path d="$lower" fill="none" stroke="url(#disk)" stroke-width="26" opacity=".35" filter="url(#soft)"/>
      <path d="$lower" fill="none" stroke="url(#disk)" stroke-width="15"/>
      <path class="orbit" d="$lower" fill="none" stroke="#fffaf0" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="$dash" opacity=".7"/>
    </g>

    <text class="name" x="64" y="168">AARYAN BAIRAGI</text>
    <text class="tag" x="64" y="218">I build systems that work in production, not just on localhost.</text>
    <text class="sub" x="64" y="256">Software engineer in Pune, India. Backend, full-stack and AI/ML systems.</text>
    <g transform="translate(64 290)">
      <rect width="372" height="34" rx="17" fill="$GREEN" fill-opacity=".08" stroke="$GREEN" stroke-opacity=".35"/>
      <circle cx="20" cy="17" r="4" fill="$GREEN"/>
      <text class="chip" x="34" y="22">Open to backend, full-stack and AI/ML roles</text>
    </g>
    <text class="url" x="1136" y="372" text-anchor="end">aaryanbairagi.in</text>
  </g>
  <rect x=".5" y=".5" width="1199" height="399" rx="23.5" fill="none" stroke="$LILAC" stroke-opacity=".18"/>
</svg>
"""


def hero() -> str:
    cx, cy, rx, ry = 950, 200, 270, 36
    dash = (1.5, 26, 5, 38, 2, 20, 9, 52)
    return render(
        HERO,
        cx=cx, cy=cy, rx=rx, ry=ry, tilt=-6,
        # Far side runs right-to-left over the top, near side left-to-right
        # underneath, so the moving flecks read as one rotating disk.
        upper=f"M{cx + rx} {cy}A{rx} {ry} 0 0 0 {cx - rx} {cy}",
        lower=f"M{cx - rx} {cy}A{rx} {ry} 0 0 0 {cx + rx} {cy}",
        dash=" ".join(str(d) for d in dash),
        period=sum(dash),
        stars=starfield(7, 120, 1200, 400, (0.18, 0.8), twinkle_every=7),
    )


# --------------------------------------------------------------------------
# llmfuse card: the package on the left, one request during an outage on
# the right. Timeline (10 s loop): request leaves the app, Groq answers 503
# three times with growing backoff, Groq's breaker records 1 of 5 failures,
# llmfuse fails over to Gemini, 200 OK returns to the app.
# --------------------------------------------------------------------------
CARD = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="480" viewBox="0 0 1200 480" role="img" aria-labelledby="title desc">
  <title id="title">llmfuse: production-grade reliability for LLM calls</title>
  <desc id="desc">Animated diagram of one request while Groq is down. The request goes from your app through llmfuse to Groq, which answers HTTP 503. llmfuse retries with backoff, records one failure on Groq's circuit breaker, then fails over to Gemini, which answers 200 OK, and the response returns to the app.</desc>
  <style>
    .pkg { font: 700 64px $MONO; fill: $STARLIGHT; }
    .tag { font: italic 400 23px $SERIF; fill: $LAVENDER; }
    .body { font: 400 16.5px $SANS; fill: $MUTED; }
    .cmd { font: 500 20px $MONO; fill: $STARLIGHT; }
    .prompt { fill: $LILAC; }
    .fact { font: 400 14.5px $SANS; fill: #8f8aad; }
    .h { font: 500 15px $SANS; fill: #e4e0f5; }
    .note { font: 400 12.5px $SANS; fill: #8f8aad; }
    .label { font: 500 15px $SANS; fill: #e4e0f5; }
    .mono { font: 500 15px $MONO; fill: $STARLIGHT; }
    .rank { font: 400 12px $SANS; fill: #6f6a8c; }
    .say { font: 500 12.5px $SANS; opacity: 0; }
    .bad { fill: $RED; }
    .good { fill: $GREEN; }
    .wire { stroke: rgba(255,255,255,.16); stroke-width: 1.5; fill: none; }
    .box { fill: #0b0916; stroke: rgba(255,255,255,.16); stroke-width: 1.4; }
    .fuse { stroke: $LILAC; }
    .dot { fill: rgba(255,255,255,.22); }
    .idle { opacity: .6; }

    .pk { fill: $LAVENDER; animation: pk 10s linear infinite; }
    .groq { animation: groq 10s linear infinite; }
    .gem { animation: gem 10s linear infinite; }
    .app { animation: app 10s linear infinite; }
    .strike { animation: strike 10s linear infinite; }
    .s1 { animation: s1 10s linear infinite; }
    .s2 { animation: s2 10s linear infinite; }
    .ok { animation: ok 10s linear infinite; }
    .done { animation: done 10s linear infinite; }

    @keyframes pk {
      0% { transform: translate(680px, 233px); opacity: 0; fill: $LAVENDER; }
      2% { transform: translate(680px, 233px); opacity: 1; }
      9% { transform: translate(832px, 233px); }
      12% { transform: translate(944px, 233px); }
      15% { transform: translate(944px, 145px); }
      18% { transform: translate(1063px, 145px); }
      44% { transform: translate(1063px, 145px); }
      47% { transform: translate(944px, 145px); }
      50% { transform: translate(944px, 233px); }
      54% { transform: translate(1063px, 233px); fill: $LAVENDER; }
      56% { transform: translate(1063px, 233px); fill: $GREEN; }
      60% { transform: translate(944px, 233px); }
      64% { transform: translate(832px, 233px); }
      70% { transform: translate(680px, 233px); opacity: 1; fill: $GREEN; }
      71% { transform: translate(680px, 233px); opacity: 0; }
      100% { transform: translate(680px, 233px); opacity: 0; fill: $GREEN; }
    }
    /* three attempts, each wait longer than the last: backoff */
    @keyframes groq {
      0%, 18% { stroke: rgba(255,255,255,.16); fill: #0b0916; }
      19% { stroke: $RED; fill: #2a0d12; }
      22%, 26% { stroke: rgba(248,113,113,.45); fill: #12080d; }
      27% { stroke: $RED; fill: #2a0d12; }
      30%, 38% { stroke: rgba(248,113,113,.45); fill: #12080d; }
      39% { stroke: $RED; fill: #2a0d12; }
      42%, 90% { stroke: rgba(248,113,113,.55); fill: #12080d; }
      96%, 100% { stroke: rgba(255,255,255,.16); fill: #0b0916; }
    }
    @keyframes gem {
      0%, 53% { stroke: rgba(255,255,255,.16); fill: #0b0916; }
      55%, 90% { stroke: $GREEN; fill: #0a1f14; }
      96%, 100% { stroke: rgba(255,255,255,.16); fill: #0b0916; }
    }
    @keyframes app {
      0%, 69% { stroke: rgba(255,255,255,.16); }
      71%, 90% { stroke: $GREEN; }
      96%, 100% { stroke: rgba(255,255,255,.16); }
    }
    @keyframes strike {
      0%, 43.5% { fill: rgba(255,255,255,.22); }
      44.5%, 90% { fill: $RED; }
      96%, 100% { fill: rgba(255,255,255,.22); }
    }
    @keyframes s1 { 0%, 18% { opacity: 0; } 19.5%, 43% { opacity: 1; } 44%, 100% { opacity: 0; } }
    @keyframes s2 { 0%, 43.5% { opacity: 0; } 44.5%, 90% { opacity: 1; } 95%, 100% { opacity: 0; } }
    @keyframes ok { 0%, 54.5% { opacity: 0; } 56%, 90% { opacity: 1; } 95%, 100% { opacity: 0; } }
    @keyframes done { 0%, 70% { opacity: 0; } 72%, 90% { opacity: 1; } 95%, 100% { opacity: 0; } }

    /* Reduced motion: hold the end state instead of animating */
    @media (prefers-reduced-motion: reduce) {
      .pk, .groq, .gem, .app, .strike, .s1, .s2, .ok, .done { animation: none; }
      .pk, .s1 { opacity: 0; }
      .s2, .ok, .done { opacity: 1; }
      .groq { stroke: rgba(248,113,113,.55); }
      .gem, .app { stroke: $GREEN; }
      .strike { fill: $RED; }
    }
  </style>
  <defs>
    <clipPath id="frame"><rect width="1200" height="480" rx="20"/></clipPath>
    <filter id="nebula" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="70"/></filter>
    <filter id="glow" x="-150%" y="-150%" width="400%" height="400%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="1200" height="480" fill="#000"/>
    <circle cx="1120" cy="-20" r="220" fill="#6d28d9" opacity=".22" filter="url(#nebula)"/>
    <circle cx="60" cy="520" r="200" fill="#2563eb" opacity=".10" filter="url(#nebula)"/>
    <g>
    $stars
    </g>
  </g>
  <rect x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="$LILAC" stroke-opacity=".22"/>

  <text class="pkg" x="56" y="118">llmfuse</text>
  <text class="tag" x="56" y="160">Production-grade reliability for LLM calls.</text>
  <text class="body" x="56" y="206">One client in front of many LLM providers. When one is</text>
  <text class="body" x="56" y="232">slow, rate-limited or down, llmfuse retries it sensibly</text>
  <text class="body" x="56" y="258">and answers from the next provider instead.</text>
  <rect x="56" y="288" width="440" height="58" rx="12" fill="#07050f" stroke="$LILAC" stroke-opacity=".4"/>
  <text class="cmd" x="80" y="324"><tspan class="prompt">$$</tspan> pip install llmfuse</text>
  <text class="fact" x="56" y="394">Zero runtime dependencies. Fully typed. Python 3.10+. MIT licensed.</text>
  <text class="fact" x="56" y="420">Verified live against Groq, Gemini, OpenAI and Anthropic.</text>

  <rect x="600" y="36" width="564" height="408" rx="16" fill="#fff" fill-opacity=".025" stroke="#fff" stroke-opacity=".07"/>
  <text class="h" x="628" y="74">One request while Groq is down</text>
  <text class="note" x="990" y="108">In priority order</text>
  <path class="wire" d="M732 233H772M892 233H944M944 145V321M944 145H990M944 233H990M944 321H990"/>

  <circle class="pk" r="6" filter="url(#glow)"/>

  <rect class="box app" x="628" y="210" width="104" height="46" rx="10"/>
  <text class="label" x="680" y="238" text-anchor="middle">your app</text>
  <rect class="box fuse" x="772" y="210" width="120" height="46" rx="10"/>
  <text class="mono" x="832" y="238" text-anchor="middle">llmfuse</text>

  <rect class="box groq" x="990" y="122" width="146" height="46" rx="10"/>
  <text class="label" x="1006" y="150">groq</text>
  <circle class="dot strike" cx="1086" cy="145" r="2.6"/>
  <circle class="dot" cx="1095" cy="145" r="2.6"/>
  <circle class="dot" cx="1104" cy="145" r="2.6"/>
  <circle class="dot" cx="1113" cy="145" r="2.6"/>
  <circle class="dot" cx="1122" cy="145" r="2.6"/>
  <text class="rank" x="1148" y="150">1</text>

  <rect class="box gem" x="990" y="210" width="146" height="46" rx="10"/>
  <text class="label" x="1006" y="238">gemini</text>
  <text class="rank" x="1148" y="238">2</text>

  <g class="idle">
    <rect class="box" x="990" y="298" width="146" height="46" rx="10"/>
    <text class="label" x="1006" y="326">anthropic</text>
  </g>
  <text class="rank" x="1148" y="326">3</text>

  <text class="say bad s1" x="1063" y="193" text-anchor="middle">503, retrying with backoff</text>
  <text class="say bad s2" x="1063" y="193" text-anchor="middle">retries exhausted, breaker 1/5</text>
  <text class="say good ok" x="1063" y="281" text-anchor="middle">200 OK</text>
  <text class="say good done" x="680" y="284" text-anchor="middle">answered by gemini</text>

  <text class="note" x="628" y="414">Each provider gets its own retries, circuit breaker and rate limit.</text>
</svg>
"""


def card() -> str:
    return render(CARD, stars=starfield(11, 45, 1200, 480, (0.08, 0.4), twinkle_every=None))


# --------------------------------------------------------------------------
# Buttons: one filled primary action, the rest outlined.
# --------------------------------------------------------------------------
BUTTON = """<svg xmlns="http://www.w3.org/2000/svg" width="$w" height="44" viewBox="0 0 $w 44" role="img" aria-label="$label">
  <title>$label</title>
  <rect x=".75" y=".75" width="$rw" height="42.5" rx="21.25" fill="$fill" $stroke/>
  <text x="$cx" y="27.5" text-anchor="middle" style="font: 500 15px $SANS; fill: $ink;">$label</text>
</svg>
"""

BUTTONS = {
    "portfolio": ("Portfolio", True),
    "resume": ("Resume", False),
    "linkedin": ("LinkedIn", False),
    "email": ("Email", False),
    "x": ("X (Twitter)", False),
}


def button(label: str, primary: bool) -> str:
    w = round(40 + len(label) * 8.4)
    return render(
        BUTTON, w=w, rw=w - 1.5, cx=w / 2, label=label,
        fill="#c4b5fd" if primary else "#000",
        ink="#0b0716" if primary else "#f5f3ff",
        stroke="" if primary else 'stroke="#a78bfa" stroke-opacity=".55" stroke-width="1.5"',
    )


def main() -> None:
    (OUT / "hero.svg").write_text(hero(), encoding="utf-8")
    (OUT / "llmfuse.svg").write_text(card(), encoding="utf-8")
    (OUT / "buttons").mkdir(exist_ok=True)
    for name, (label, primary) in BUTTONS.items():
        (OUT / "buttons" / f"{name}.svg").write_text(button(label, primary), encoding="utf-8")
    print("wrote hero.svg, llmfuse.svg and", len(BUTTONS), "buttons to", OUT)


if __name__ == "__main__":
    main()
