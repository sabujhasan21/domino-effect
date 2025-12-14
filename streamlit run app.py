import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ 3D Domino Letters (FIXED) ❤️", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
html, body {
  margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden;
  background: radial-gradient(circle at top, #050505, #1a1a1a, #000000);
  perspective: 1400px;
}
.scene {
  width: 100vw; height: 100vh;
  display: flex; align-items: center; justify-content: center;
  flex-wrap: wrap;
}
.letter {
  display: grid;
  grid-template-columns: repeat(5, 28px);
  gap: 8px;
  margin: 18px;
}
.domino {
  width: 28px; height: 90px;
  background: linear-gradient(135deg, #ffffff, #cfcfcf, #9e9e9e);
  border-radius: 6px;
  box-shadow: 0 15px 25px rgba(0,0,0,0.7);
  transform-origin: bottom center;
  transform-style: preserve-3d;
  opacity: 0;
}
.domino.fall {
  animation: fall3d 0.7s ease forwards;
}
@keyframes fall3d {
  from { transform: rotateX(0deg); opacity: 1; }
  to { transform: rotateX(-90deg) translateZ(10px); opacity: 1; }
}
</style>
</head>
<body>
<div class="scene" id="scene"></div>

<script>
// ===== LETTER DEFINITIONS (5x5) =====
const L = {
'S':['11111','10000','11111','00001','11111'],
'O':['11111','10001','10001','10001','11111'],
'R':['11110','10001','11110','10010','10001'],
'Y':['10001','01010','00100','00100','00100'],
'I':['11111','00100','00100','00100','11111'],
'L':['10000','10000','10000','10000','11111'],
'V':['10001','10001','01010','01010','00100'],
'E':['11111','10000','11110','10000','11111'],
'U':['10001','10001','10001','10001','11111'],
'N':['10001','11001','10101','10011','10001'],
'A':['01110','10001','11111','10001','10001']
};

const text = 'SORRY I LOVE YOU SONA';
const scene = document.getElementById('scene');
let delay = 0;

for (const ch of text) {
  if (ch === ' ') {
    const spacer = document.createElement('div');
    spacer.style.width = '60px';
    scene.appendChild(spacer);
    continue;
  }
  const letter = document.createElement('div');
  letter.className = 'letter';

  L[ch].forEach(row => {
    row.split('').forEach(bit => {
      if (bit === '1') {
        const d = document.createElement('div');
        d.className = 'domino';
        setTimeout(() => {
          d.style.opacity = 1;
          d.classList.add('fall');
        }, delay);
        delay += 120; // domino one by one
        letter.appendChild(d);
      } else {
        const empty = document.createElement('div');
        empty.style.width = '28px';
        empty.style.height = '90px';
        letter.appendChild(empty);
      }
    });
  });
  scene.appendChild(letter);
}
</script>
</body>
</html>
"""

html(html_code, height=900)
