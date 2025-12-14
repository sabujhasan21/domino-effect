import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Glowing Love Spike", layout="wide")

st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0b1020, #060814);
}
.main-title {
    font-size: 2.6rem;
    font-weight: 800;
    text-align: center;
    color: #ffd1dc;
    margin-bottom: 0.3rem;
}
.sub {
    text-align: center;
    color: #a5b4fc;
    margin-bottom: 2rem;
}
.wrap {
    display: flex;
    justify-content: center;
}
.card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(14px);
    border-radius: 28px;
    padding: 40px 60px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.45);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💗 For You</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Soft glowing spike → love shape → emotion</div>', unsafe_allow_html=True)

svg_html = """
<div class="wrap">
  <div class="card">
    <svg width="700" height="360" viewBox="0 0 700 360">

      <!-- Glowing ECG line -->
      <path id="pulse"
        d="M50 180 L150 180 L180 130 L210 240 L240 180 L300 180
           C320 140 360 140 380 180
           C400 220 440 220 460 180
           L560 180"
        fill="none"
        stroke="#ff5c8a"
        stroke-width="4"
        filter="url(#glow)"
        stroke-dasharray="6 10">
        <animate attributeName="stroke-dashoffset"
          from="0" to="-200" dur="2s" repeatCount="indefinite" />
      </path>

      <!-- Glow effect -->
      <defs>
        <filter id="glow">
          <feGaussianBlur stdDeviation="4" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      <!-- Love text -->
      <text x="350" y="290" text-anchor="middle"
            font-size="26" font-weight="600" fill="#ffe4e6">
        I am Sorry, Please I want you in every time.
      </text>
      <text x="350" y="325" text-anchor="middle"
            font-size="28" font-weight="800" fill="#ff8fab">
        I love you sona
      </text>

    </svg>
  </div>
</div>
"""

html(svg_html, height=420)

st.markdown("""
---
### Animation Meaning
- 💫 Soft glowing moving spike
- 💓 Middle e spike naturally **love curve** banay
- ❤️ Emotion-focused minimal design

Chaile ami aro add korte pari:
- Pulse speed emotion wise
- Typing text animation
- Background floating particles
- Auto full-screen love intro
""")
