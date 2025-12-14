import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Still Beating", layout="wide")

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
  display: flex;
  align-items: center;
  justify-content: center;
}
svg {
  width: 100%;
  height: 100%;
}
#pulse {
  fill: none;
  stroke: #ff8fa3;
  stroke-width: 2;
  filter: drop-shadow(0 0 12px rgba(255,143,163,0.6));
}
#text {
  position: absolute;
  bottom: 14%;
  width: 100%;
  text-align: center;
  font-family: 'Segoe UI', sans-serif;
  color: #ffdbe7;
}
#line1 {
  font-size: 22px;
  opacity: 0;
}
#line2 {
  font-size: 32px;
  font-weight: 700;
  opacity: 0;
  margin-top: 6px;
}
.fade-in {
  animation: fade 3s forwards;
}
@keyframes fade {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>
</head>
<body>
<div id="scene">
  <svg viewBox="0 0 1200 400" preserveAspectRatio="none">
    <path id="pulse" />
  </svg>
  <div id="text">
    <div id="line1">I am Sorry, Please I want you in every time.</div>
    <div id="line2">I love you sona</div>
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

let start = null;
function animate(ts){
  if(!start) start = ts;
  const t = ts - start;

  // 4s flatline
  if(t < 4000){
    path.setAttribute('d', 'M0 200 L1200 200');
  }
  // spike + love curve
  else if(t < 9000){
    path.setAttribute('d',
      'M0 200 L420 200 ' +
      'L450 200 L470 120 L490 280 L510 200 ' +
      'C550 150 620 150 680 200 ' +
      'C740 250 810 250 870 200 ' +
      'L1200 200'
    );
    document.body.style.background = '#050014';
    if(beep.paused){ beep.volume = 0.12; beep.play(); }
    l1.classList.add('fade-in');
    setTimeout(()=>l2.classList.add('fade-in'),1200);
  }
  // hold
  else {
    path.setAttribute('d', path.getAttribute('d'));
  }

  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);
</script>
</body>
</html>
"""

html(html_content, height=800)
