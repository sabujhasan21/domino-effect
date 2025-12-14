import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ Heart + ECG Spike Text ❤️", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<title>Heart ECG Text on Spike</title>
<style>
html,body{
  margin:0; padding:0; width:100%; height:100%; background:black; overflow:hidden;
  font-family: Arial, sans-serif;
}
#container{
  display:flex; justify-content: space-between; align-items:center;
  width:90vw; height:80vh; margin:auto; top:10%;
}
#heart-svg{
  width:40%; height:100%;
}
#heart{
  fill:#ff4d6d;
  transform-origin: center center;
  animation: heartbeat 1s infinite;
}
@keyframes heartbeat{
  0% { transform: scale(1); }
  25% { transform: scale(1.1); }
  50% { transform: scale(1); }
  75% { transform: scale(1.1); }
  100% { transform: scale(1); }
}
#ecg-svg{
  width:55%; height:100%;
}
#text {
  fill:#ff4d6d;
  font-size:24px;
  font-weight:bold;
  text-shadow:0 0 5px #ff4d6d;
}
</style>
</head>
<body>
<div id="container">
  <!-- Left Heart -->
  <svg id="heart-svg" viewBox="0 0 200 200">
    <path id="heart" d="M100 180 C20 120, 40 40, 100 70 C160 40, 180 120, 100 180"/>
  </svg>

  <!-- Right ECG Spike -->
  <svg id="ecg-svg" viewBox="0 0 800 200">
    <path id="wave" fill="none" stroke="#ff4d6d" stroke-width="3"
          d="M0,100 L50,100 L60,60 L70,140 L80,100 L150,100 L160,80 L170,120 L180,100
             L250,100 L260,60 L270,140 L280,100 L350,100 L360,70 L370,130 L380,100 L450,100
             L460,50 L470,150 L480,100 L550,100 L560,60 L570,140 L580,100 L650,100 L660,60
             L670,140 L680,100 L750,100 L760,70 L770,130 L780,100"
          stroke-dasharray="1000" stroke-dashoffset="1000"/>
    <text id="text"><textPath href="#wave" startOffset="0%">SORRY</textPath></text>
  </svg>
</div>

<script>
const wave = document.getElementById('wave');
const textPath = document.querySelector('textPath');
const messages = ["SORRY","I WANT TO SEE YOU","I AM REALLY SORRY","I LOVE YOU SONA ❤️"];
let idx = 0;

// Animate wave draw
setTimeout(()=>{
    wave.style.transition = "stroke-dashoffset 4s linear";
    wave.style.strokeDashoffset = 0;
}, 500);

// Animate text along spike
function animateText(){
    if(idx < messages.length){
        textPath.textContent = messages[idx];
        let offset = 0;
        const interval = setInterval(()=>{
            offset += 2; // move text along path
            textPath.setAttribute('startOffset', offset+'%');
            if(offset>=100){ clearInterval(interval); idx++; setTimeout(animateText, 500); }
        },30);
    }
}
setTimeout(animateText, 600);
</script>
</body>
</html>
"""

html(html_code, height=700)
