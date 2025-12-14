import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ Domino Falling Text ❤️", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
html, body {
    margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden;
    background: radial-gradient(circle at center, #0b132b, #1c2541, #3a506b);
    font-family: 'Segoe UI', sans-serif;
}
.scene {
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.grid {
    display: grid;
    grid-template-columns: repeat(40, 16px);
    grid-gap: 6px;
}
.domino {
    width: 16px;
    height: 50px;
    background: linear-gradient(180deg, #ffffff, #d9d9d9);
    border-radius: 5px;
    transform-origin: bottom center;
    transform: rotate(0deg);
    opacity: 0;
}
.domino.fall {
    animation: fall 0.5s ease forwards;
}

@keyframes fall {
    from { transform: rotate(0deg); opacity: 1; }
    to { transform: rotate(-85deg); opacity: 1; }
}
</style>
</head>
<body>
<div class="scene">
  <div class="grid" id="grid"></div>
</div>

<script>
// 1 = domino present, 0 = empty space
const patterns = [
  // SORRY
  [
    "111110111100111110111110",
    "100000100000100010100010",
    "111110111100111110111110",
  ],
  // I WANT TO SEE YOU IN EVERY TIME
  [
    "111111000111011101110111011101110",
    "001000000100010001000100010001000",
    "111111000111011101110111011101110",
  ],
  // I AM REALLY SORRY
  [
    "111111001110111110111110",
    "001000000100100010100010",
    "111111001110111110111110",
  ],
  // I LOVE YOU SONA
  [
    "11111101110111011101110111",
    "00100001000100010001000100",
    "11111101110111011101110111",
  ]
];

const grid = document.getElementById('grid');
let delay = 0;

patterns.flat().forEach(row => {
  [...row].forEach(cell => {
    const d = document.createElement('div');
    d.className = 'domino';
    if (cell === '1') {
      setTimeout(() => {
        d.style.opacity = 1;
        d.classList.add('fall');
      }, delay);
      delay += 80; // one by one falling
    } else {
      d.style.visibility = 'hidden';
    }
    grid.appendChild(d);
  });
});
</script>
</body>
</html>
"""

html(html_code, height=900)
