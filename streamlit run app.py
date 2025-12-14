import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Still Beating – Clean", layout="wide")

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
html, body {
  margin: 0;
  padding: 0;
  background: #000000;
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
  stroke-width: 2;
  filter: drop-shadow(0 0 10px rgba(255,155,181,0.55));
}
#text {
  position: absolute;
  bottom: 14%;
  width: 100%;
  text-align: center;
  font-family: 'Segoe UI', sans-serif;
}
.line {
  font-size: 24px;
  color: #ffdbe7;
  opacity: 0;
  transition: opacity 2.5s ease;
}
#line2 {
  font-size: 32px;
  font-weight: 700;
  color: #ff8fa8;
  margin-top: 8px;
}
.show {
  opacity: 1;
}
</style>
</head>
<body>
<div id="scene">
  <svg viewBox="0 0 1200 400" preserveAspectRatio="none">
    <path id="pulse" />
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
let flatTime = 0;
let phase = 'flat';

function draw(){
  let d = 'M0 200 ';

  if(phase === 'flat'){
    d += `L${x} 200`;
    flatTime++;
    if(flatTime > 240){ // ~4s
      phase = 'spike';
      beep.volume = 0.12;
      beep.play();
      setTimeout(()=>l1.classList.add('show'),1000);
      setTimeout(()=>l2.classList.add('show'),3000);
    }
  }

  if(phase === 'spike'){
    d += `L${x-40} 200 ` +
         `L${x-30} 140 ` +
         `L${x-20} 260 ` +
         `L${x-10} 200 `;
  }

  path.setAttribute('d', d);
  x += 6;

  if(x > 1200){ x = 0; flatTime = 0; phase = 'flat'; l1.classList.remove('show'); l2.classList.remove('show'); }

  requestAnimationFrame(draw);
}
requestAnimationFrame(draw);
</script>
</body>
</html>
"""

html(html_content, height=800)
