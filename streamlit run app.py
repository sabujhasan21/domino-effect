import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ Heart with ECG Spike & Text ❤️", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<title>Heart ECG Spike</title>
<style>
html,body{
  margin:0; padding:0; width:100%; height:100%; background:black; overflow:hidden;
  font-family: Arial, sans-serif;
}
#container{
  position:relative; width:80vw; height:80vh; margin:auto; top:10%;
}
svg{
  width:100%; height:100%;
}
#text-display{
  position:absolute; width:100%; text-align:center; top:65%;
  color:#ff4d6d; font-size:3vw; font-weight:bold; text-shadow:0 0 15px #ff4d6d;
}
@keyframes spikeAnim{
  0% { stroke-dashoffset: 1000; }
  100% { stroke-dashoffset: 0; }
}
</style>
</head>
<body>
<div id="container">
<svg viewBox="0 0 800 600">
  <!-- Heart Shape -->
  <path id="heart" fill="none" stroke="#ff4d6d" stroke-width="4"
        d="M400,300 C400,200 600,200 600,300 C600,400 400,500 400,600 C400,500 200,400 200,300 C200,200 400,200 400,300"
        stroke-dasharray="1000" stroke-dashoffset="1000"></path>

  <!-- ECG Spike Wave -->
  <path id="wave" fill="none" stroke="#ff4d6d" stroke-width="3"
        d="M0,300 L50,300 L60,250 L70,350 L80,300 L150,300 L160,280 L170,320 L180,300 L250,300
           L260,250 L270,350 L280,300 L350,300 L360,270 L370,330 L380,300 L450,300 L460,260 L470,340 L480,300 L550,300
           L560,240 L570,360 L580,300 L650,300 L660,250 L670,350 L680,300 L750,300 L760,270 L770,330 L780,300"
        stroke-dasharray="1000" stroke-dashoffset="1000"></path>
</svg>
<div id="text-display"></div>
</div>
<script>
const heart = document.getElementById('heart');
const wave = document.getElementById('wave');
const textDisplay = document.getElementById('text-display');

// Heart draw
heart.style.transition = "stroke-dashoffset 3s ease-in-out";
heart.style.strokeDashoffset = 0;

// ECG Spike wave animation
setTimeout(()=>{
    wave.style.transition = "stroke-dashoffset 4s linear";
    wave.style.strokeDashoffset = 0;
}, 3000);

// Sequential text messages
const messages = ["SORRY","I WANT TO SEE YOU","I AM REALLY SORRY","I LOVE YOU SONA ❤️"];
let idx=0;
function showText(){
    if(idx<messages.length){
        textDisplay.textContent = messages[idx];
        idx++;
        setTimeout(showText,3000);
    }
}
setTimeout(showText,3500);
</script>
</body>
</html>
"""

html(html_code, height=900)
