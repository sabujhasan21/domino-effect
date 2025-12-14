import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ Domino Text Effect ❤️", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
html, body {
    margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden;
    background: radial-gradient(circle at center, #0f2027, #203a43, #2c5364);
    font-family: 'Segoe UI', sans-serif;
}
.scene {
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.word {
    display: flex;
    gap: 10px;
    position: absolute;
    opacity: 0;
    animation: show 1s ease forwards;
}
.word:nth-child(1) { animation-delay: 0.5s; }
.word:nth-child(2) { animation-delay: 3s; }
.word:nth-child(3) { animation-delay: 6s; }
.word:nth-child(4) { animation-delay: 9s; }

.letter {
    display: grid;
    grid-template-columns: repeat(5, 14px);
    grid-gap: 4px;
}
.domino {
    width: 14px;
    height: 40px;
    background: linear-gradient(180deg, #ffffff, #dcdcdc);
    border-radius: 4px;
    transform-origin: bottom;
    animation: fall 0.6s ease forwards;
}
.domino.empty { visibility: hidden; }

@keyframes fall {
    from { transform: rotate(0deg); }
    to { transform: rotate(-85deg); }
}

@keyframes show {
    from { opacity: 0; }
    to { opacity: 1; }
}
</style>
</head>
<body>
<div class="scene">

<!-- SORRY -->
<div class="word">
  <div class="letter"> <!-- S -->
    <div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div>
    <div class="domino"></div><div class="domino empty"></div><div class="domino empty"></div><div class="domino empty"></div><div class="domino empty"></div>
    <div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div>
  </div>
</div>

<!-- I WANT TO SEE YOU IN EVERY TIME -->
<div class="word">
  <div class="letter">
    <div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div>
    <div class="domino"></div><div class="domino empty"></div><div class="domino empty"></div><div class="domino empty"></div><div class="domino"></div>
    <div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div>
  </div>
</div>

<!-- I AM REALLY SORRY -->
<div class="word">
  <div class="letter">
    <div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div>
    <div class="domino empty"></div><div class="domino"></div><div class="domino empty"></div><div class="domino"></div><div class="domino empty"></div>
    <div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div>
  </div>
</div>

<!-- I LOVE YOU SONA -->
<div class="word">
  <div class="letter">
    <div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div>
    <div class="domino"></div><div class="domino empty"></div><div class="domino empty"></div><div class="domino empty"></div><div class="domino"></div>
    <div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div><div class="domino"></div>
  </div>
</div>

</div>
</body>
</html>
"""

html(html_code, height=900)
