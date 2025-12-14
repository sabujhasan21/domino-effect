import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Life Support Love Intro", layout="wide")

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
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
  background: radial-gradient(circle at center, #02040a, #000);
}
canvas {
  position: absolute;
  inset: 0;
}
#ecg {
  position: absolute;
  inset: 0;
}
#text {
  position: absolute;
  bottom: 12%;
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
  font-size: 30px;
  font-weight: 700;
  color: #ff8fb1;
  opacity: 0;
}
.glow {
  filter: drop-shadow(0 0 12px #ff8fb1);
}
</style>
</head>
<body>
<div id="scene">
  <canvas id="stars"></canvas>
  <svg id="ecg" viewBox="0 0 1200 400" preserveAspectRatio="none">
    <path id="pulse" fill="none" stroke="#ffb3c7" stroke-width="2" />
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
/* STAR BACKGROUND */
const c = document.getElementById('stars');
const ctx = c.getContext('2d');
let w,h,stars=[];
function resize(){w=c.width=innerWidth;h=c.height=innerHeight}
window.onresize=resize;resize();
for(let i=0;i<120;i++) stars.push({x:Math.random()*w,y:Math.random()*h,r:Math.random()*1.5});
function drawStars(){ctx.clearRect(0,0,w,h);ctx.fillStyle='#fff';stars.forEach(s=>{ctx.globalAlpha=Math.random();ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,6.28);ctx.fill()});requestAnimationFrame(drawStars)}
drawStars();

/* ECG PATH */
const path = document.getElementById('pulse');
const beep = document.getElementById('beep');
let t = 0;
function ecg(){
  t++;
  let d = 'M0 200 ';
  if(t<180){ d+='L1200 200'; }
  else{
    d+='L300 200 L340 200 L360 120 L380 300 L400 200 ';
    d+='C450 160 520 160 580 200 C640 240 700 240 760 200 L1200 200';
    document.body.style.background='#050014';
    beep.volume=0.15;beep.play();
    showText();
    t=0;
  }
  path.setAttribute('d',d);
  path.classList.add('glow');
  requestAnimationFrame(ecg);
}
ecqgStart = setTimeout(()=>requestAnimationFrame(ecg),3000);

/* TEXT EFFECT */
function showText(){
  const l1=document.getElementById('line1');
  const l2=document.getElementById('line2');
  l1.style.opacity=1;l2.style.opacity=1;
  type(l1);setTimeout(()=>type(l2),2000);
}
function type(el){
  const txt=el.innerText;el.innerText='';let i=0;
  const iv=setInterval(()=>{el.innerText+=txt[i++];if(i>=txt.length)clearInterval(iv)},60);
}
</script>
</body>
</html>
"""

html(html_content, height=800)
