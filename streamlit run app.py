import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="🎥 Domino Chain – Clear Text View", layout="wide")n
html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<style>
html,body{
  margin:0; padding:0; width:100%; height:100%; overflow:hidden;
  background:#000;
}
.scene{
  width:100vw; height:100vh;
  perspective:1600px;
}
.camera{
  width:100%; height:100%;
  transform-style: preserve-3d;
  animation: cameraMove 18s ease-in-out forwards;
}
.board{
  display:grid;
  grid-template-columns: repeat(60, 22px);
  gap:10px;
  transform: rotateX(65deg) translateY(260px);
}
.domino{
  width:22px; height:70px;
  background: linear-gradient(135deg,#ffffff,#d9d9d9,#bfbfbf);
  border-radius:6px;
  box-shadow:0 14px 26px rgba(0,0,0,.8);
  transform-origin: bottom center;
}
.domino.fall{ animation: fall .7s ease forwards; }
@keyframes fall{ to{ transform: rotateX(-90deg); } }
.empty{ visibility:hidden; }

@keyframes cameraMove{
  0%{ transform: translateZ(0px); }
  55%{ transform: translateZ(380px); }
  100%{ transform: rotateX(90deg) translateZ(520px); }
}
</style>
</head>
<body>
<div class='scene'>
  <div class='camera'>
    <div class='board' id='board'></div>
  </div>
</div>
<script>
// CLEAN BIG LETTER PATTERN
const pattern = [
// SORRY
"1111100000111110000011111",
"1000000000100010000010000",
"1111100000111110000011111",
"0000100000000010000000001",
"1111100000111110000011111",
// SPACE
"0000000000000000000000000",
// I LOVE YOU SONA
"111110001000111110001011111000100011111",
"001000001000100000001010000001000100000",
"001000001000111100001011110001000111100",
"001000001000100000001010000001000100000",
"111110001000111110001011111001000111110"
];

const board = document.getElementById('board');
let delay = 0;

pattern.forEach(row=>{
  [...row].forEach(cell=>{
    const d = document.createElement('div');
    if(cell==='1'){
      d.className='domino';
      setTimeout(()=>d.classList.add('fall'),delay);
      delay+=80;
    } else {
      d.className='domino empty';
    }
    board.appendChild(d);
  });
});
</script>
</body>
</html>
"""

html(html_code, height=900)
