import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Heartbeat Text", layout="wide")

st.markdown("""
<style>
body {
    background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
}
.main-title {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    color: #ffffff;
    margin-bottom: 0.5rem;
}
.sub {
    text-align: center;
    color: #c7d2fe;
    margin-bottom: 2rem;
}
.container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 60px;
}
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">❤️ Heartbeat Text Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Heart theke ber hobe ECG spike → oi spike diye text border draw hobe</div>', unsafe_allow_html=True)

text = st.text_input("Text dao", "LOVE")

svg_html = f"""
<div class="container">
  <div class="card">
    <svg width="600" height="300" viewBox="0 0 600 300">
      <!-- Heart -->
      <image href="https://upload.wikimedia.org/wikipedia/commons/8/88/Heart_anatomy_icon.svg"
             x="10" y="60" width="140" height="140" />

      <!-- ECG path -->
      <path id="ecg"
        d="M150 150 L200 150 L220 120 L240 190 L260 150 L300 150"
        fill="none" stroke="#ff4d6d" stroke-width="4">
        <animate attributeName="stroke-dasharray"
          from="0,500" to="500,0" dur="1.5s" repeatCount="indefinite" />
      </path>

      <!-- Text path -->
      <defs>
        <path id="textBorder"
          d="M320 80 Q420 20 520 80 Q580 150 520 220 Q420 280 320 220 Q260 150 320 80 Z" />
      </defs>

      <text font-size="32" fill="#ffffff" font-weight="700">
        <textPath href="#textBorder" startOffset="0%">
          {text} • {text} • {text} • {text} •
          <animate attributeName="startOffset" from="0%" to="100%" dur="6s" repeatCount="indefinite" />
        </textPath>
      </text>
    </svg>
  </div>
</div>
"""

html(svg_html, height=360)

st.markdown("""
---
### Features
- ❤️ Heart left side e
- 📈 Heartbeat (ECG) spike animation
- ✍️ ECG flow theke text border create
- ✨ Glassmorphism modern UI

Next step e ami chaile:
- Real audio-synced heartbeat
- Custom font & color picker
- SVG export / video export
- Mobile responsive version
""")
