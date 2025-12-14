import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Glowing Love Spike", layout="wide")

st.markdown("""
<style>
body {
    background: radial-gradient(circle at center, #02040a, #000000);
    animation: breathe 6s infinite alternate;
}
@keyframes breathe {
    from { background-color: #000000; }
    to { background-color: #040414; }
}
.main-title {
    display:none;
}
.sub {
    display:none;
}
.wrap {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.card {
    background: transparent;
    border-radius: 0;
    padding: 0;
    box-shadow: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💗 For You</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Soft glowing spike → love shape → emotion</div>', unsafe_allow_html=True)

svg_html = """
<div class="wrap">
  <div class="card">
    <svg width="1200" height="420" viewBox="0 0 1200 420">

      <!-- Life support ECG flatline + spike -->
      <path id="pulse"
        d="M20 210 
           L500 210 
           L520 210 
           L540 140 
           L560 300 
           L580 210 
           L700 210
           C740 170 800 170 840 210
           C880 250 940 250 980 210
           L1180 210"
        fill="none"
        stroke="#ffb3c7"
        stroke-width="2"
        filter="url(#glow)">
        <animate attributeName="stroke-dasharray"
          from="0,1600" to="1600,0" dur="6s" repeatCount="indefinite" />
      </path>

      <!-- Glow effect -->
      <defs>
        <filter id="glow">
          <feGaussianBlur stdDeviation="10" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      <!-- Emotional text -->
      <text x="600" y="330" text-anchor="middle"
            font-size="26" font-weight="400" fill="#ffdbe7" opacity="0">
        I am Sorry, Please I want you in every time.
        <animate attributeName="opacity" from="0" to="1" begin="3s" dur="3s" fill="freeze" />
      </text>
      <text x="600" y="370" text-anchor="middle"
            font-size="32" font-weight="700" fill="#ff8fb1" opacity="0">
        I love you sona
        <animate attributeName="opacity" from="0" to="1" begin="4s" dur="3s" fill="freeze" />
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
