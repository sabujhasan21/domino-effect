import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Life Support – Visible", layout="wide")

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body {
  margin: 0;
  padding: 0;
  background: #000;
  overflow: hidden;
}
#scene {
  position: fixed;
  inset: 0;
}
svg {
  width: 100%;
  height: 100%;
}
#pulse {
  fill: none;
  stroke: #ff9bb5;
  stroke-width: 3;
  filter: drop-shadow(0 0 12px rgba(255,155,181,0.8));
}
#text {
  position: absolute;
  bottom: 12%;
  width: 100%;
  text-align: center;
  font-family: 'Segoe UI', sans-serif;
}
.line {
  font-size: 26px;
  color: #ffdbe7;
  opacity: 0;
  transition: opacity 2s ease;
}
#line2 {
  font-size: 34px;
  font-weight: 700;
  color: #ff7fa3;
  margin-top: 10px;
}
.show { opacity: 1; }
</style>
</head>
<body>
<div id="scene">
  <svg viewBox="0 0 1200 400" preserveAspectRatio="none">
    <path id="pulse" d="M0 200 L1200 200" />
  </svg>
  <div id="text">
    <div id="line1" class="line">I am Sorry, Please I want you in every time.</div>
    <div id="line2" class="line">I love you sona</div>
  </div>
</div>

<audio id="beep" preload="auto">
  <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
</audio>

<script>
const path = document.getElementById('pulse');
const beep = document.getElementById('beep');
const l1 = document.getElementById('line1');
const l2 = document.getElementById('line2');

let x = 0;
let mode = 'flat';
let frame = 0;

function animate(){
  let d = `M0 200 `;

  if(mode === 'flat'){
    d += `L${x} 200`;
    frame++;
    if(frame > 180){ // ~3s flatline
      mode = 'spike';
      frame = 0;
      beep.volume = 0.15;
      beep.play();
      setTimeout(()=>l1.classList.add('show'),800);
      setTimeout(()=>l2.classList.add('show'),2400);
    }
  }

  if(mode === 'spike'){
    d += `L${x-60} 200 ` +
         `L${x-45} 140 ` +
         `L${x-30} 260 ` +
         `L${x-15} 200 `;
  }

  path.setAttribute('d', d);
  x += 10;

  if(x > 1200){
    x = 0;
    mode = 'flat';
    frame = 0;
    l1.classList.remove('show');
    l2.classList.remove('show');
  }

  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);
</script>
</body>
</html>
"""

html(html_content, height=800)
