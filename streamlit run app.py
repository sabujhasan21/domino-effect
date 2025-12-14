import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ 3D Domino Letter Fall ❤️", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
html, body {
    margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden;
    background: radial-gradient(circle at top, #050505, #1a1a1a, #000000);
    perspective: 1200px;
    font-family: Arial, sans-serif;
}
.scene {
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.letter-group {
    display: grid;
    grid-template-columns: repeat(5, 26px);
    grid-gap: 8px;
    margin: 0 25px;
}
.domino {
    width: 26px;
    height: 90px;
    background: linear-gradient(135deg, #ffffff, #cfcfcf, #9e9e9e);
    border-radius: 6px;
    box-shadow: 0 12px 20px rgba(0,0,0,0.6);
    transform-style: preserve-3d;
    transform-origin: bottom center;
    opacity: 0;
}
.domino.fall {
    animation: fall3d 0.7s ease forwards;
}

@keyframes fall3d {
    0% { transform: rotateX(0deg); opacity: 1; }
    60% { transform: rotateX(-60deg); }
    100% { transform: rotateX(-90deg) translateZ(10px); opacity: 1; }
}
</style>
</head>
<body>
<div class="scene" id="scene"></div>

<script>
// 5x5 LETTER MAPS (1 = domino, 0 = space)
const letters = {
  'S': [
    '11111',
    '10000',
    '11111',
    '00001',
    '11111'
  ],
  'O': [
    '11111',
    '10001',
    '10001',
    '10001',
    '11111'
  ],
  'R': [
    '11110',
    '10001',
    '11110',
    '10010',
    '10001'
  ],
  'Y': [
    '10001',
    '01010',
    '00100',
    '00100',
    '00100'
  ],
  'I': [
    '11111',
    '00100',
    '00100',
    '00100',
    '11111'
  ],
  'L': [
    '10000',
    '10000',
    '10000',
    '10000',
    '11111'
  ],
  'V': [
    '10001',
    '10001',
    '01010',
    '01010',
    '00100'
  ],
  'E': [
    '11111',
    '10000',
    '11110',
    '10000',
    '11111'
  ],
  'U': [
    '10001',
    '10001',
    '10001',
    '10001',
    '11111'
  ],
  'N': [
    '10001',
    '11001',
    '10101',
    '10011',
    '10001'
  ],
  'A': [
    '01110',
    '10001',
    '11111',
    '10001',
    '10001'
  ]
};

const text = 'SORRY I LOVE YOU SONA';
const scene = document.getElementById('scene');
let delay = 0;

text.split('').forEach(char => {
  if (char === ' ') {
    const space = document.createElement('div');
    space.style.width = '40px';
    scene.appendChild(space);
    return;
  }
  const group = document.createElement('div');
  group.className = 'letter-group';

  letters[char].forEach(row => {
    row.split('').forEach(cell => {
      const d = document.createElement('div');
      if (cell === '1') {
        d.className = 'domino';
        setTimeout(() => {
          d.style.opacity = 1;
          d.classList.add('fall');
        }, delay);
        delay += 90; // one by one
      } else {
        d.style.visibility = 'hidden';
      }
      group.appendChild(d);
    });
  });
  scene.appendChild(group);
});
</script>
</body>
</html>
"""

html(html_code, height=900)
