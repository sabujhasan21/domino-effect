import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ Heart ECG Text Animation ❤️", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Heart ECG Text Animation</title>
<style>
html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    background: black;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    font-family: Arial, sans-serif;
}
#container {
    position: relative;
    width: 80vw;
    height: 80vh;
}
svg {
    width: 100%;
    height: 100%;
}
#text-display {
    position: absolute;
    width: 100%;
    text-align: center;
    top: 60%;
    color: #ff4d6d;
    font-size: 3vw;
    font-weight: bold;
    text-shadow: 0 0 10px #ff4d6d;
}
@keyframes wave {
    0% { stroke-dashoffset: 1000; }
    100% { stroke-dashoffset: 0; }
}
</style>
</head>
<body>
<div id="container">
<svg viewBox="0 0 800 600">
  <!-- Heart Shape Path -->
  <path id="heart" fill="none" stroke="#ff4d6d" stroke-width="4"
        d="M400,300
           C400,200 600,200 600,300
           C600,400 400,500 400,600
           C400,500 200,400 200,300
           C200,200 400,200 400,300"
        stroke-dasharray="1000" stroke-dashoffset="1000"></path>

  <!-- ECG-like Wave -->
  <path id="wave" fill="none" stroke="#ff4d6d" stroke-width="3"
        d="M0,300 Q50,250 100,300 T200,300 T300,300 T400,300 T500,300 T600,300 T700,300 T800,300"
        stroke-dasharray="1000" stroke-dashoffset="1000"></path>
</svg>
<div id="text-display"></div>
</div>
<script>
const heart = document.getElementById('heart');
const wave = document.getElementById('wave');
const textDisplay = document.getElementById('text-display');

// Animate heart draw
heart.style.transition = "stroke-dashoffset 3s ease-in-out";
heart.style.strokeDashoffset = 0;

// Animate wave after heart
setTimeout(()=>{
    wave.style.transition = "stroke-dashoffset 3s linear";
    wave.style.strokeDashoffset = 0;
}, 3000);

// Sequential text display
const messages = [
    "SORRY",
    "I WANT TO SEE YOU",
    "I AM REALLY SORRY",
    "I LOVE YOU SONA ❤️"
];
let idx = 0;

function showText(){
    if(idx < messages.length){
        textDisplay.textContent = messages[idx];
        idx++;
        setTimeout(showText, 3000);
    }
}
setTimeout(showText, 3500); // start after heart and wave begin
</script>
</body>
</html>
"""

html(html_code, height=900)
