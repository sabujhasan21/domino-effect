import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="🎥 Domino Chain + Camera Move", layout="wide")

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
  perspective:1400px;
  overflow:hidden;
}
.camera{
  width:100%; height:100%;
  transform-style: preserve-3d;
  animation: cameraMove 16s ease-in-out forwards;
}
.board{
  display:grid;
  grid-template-columns: repeat(60, 18px);
  gap:6px;
  transform: rotateX(70deg) translateY(200px);
}
.domino{
  width:18px; height:60px;
  background: linear-gradient(135deg,#fff,#ccc,#999);
  border-radius:4px;
  box-shadow:0 10px 20px rgba(0,0,0,.7);
  transform-origin: bottom center;
}
.domino.fall{ animation: fall .6s ease forwards; }
@keyframes fall{ to{ transform: rotateX(-85deg); } }
.empty{ visibility:hidden; }

@keyframes cameraMove{
  0%{ transform: translateZ(0px); }
  60%{ transform: translateZ(300px); }
  100%{ transform: rotateX(90deg) translateZ(400px); }
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
const pattern = [
"1111101111101111000111110",
"1000001000101000100000010",
"1111101111101111000111110",
"0000100000100000100000100",
"1111101111101111000111110",
"0000000000000000000000000",
"11111001001011110001011111001001011110",
"00100001001010000001010000001001010000",
"00100001001011100001011100001001011100",
"00100001001010000001010000001001010000",
"11111011111011110001011111011111011110"
];

const board = document.getElementById('board');
let delay = 0;

pattern.forEach(row=>{
  [...row].forEach(cell=>{
    const d = document.createElement('div');
    if(cell==='1'){
      d.className='domino';
      setTimeout(()=>d.classList.add('fall'),delay);
      delay+=60;
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
