import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="❤️ Domino Effect ❤️", layout="wide")

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
    position: relative;
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
}
.domino-container {
    position: absolute;
    bottom: 20%;
    display: flex;
    gap: 14px;
}
.domino {
    width: 18px;
    height: 90px;
    background: linear-gradient(180deg, #fff, #ddd);
    border-radius: 6px;
    transform-origin: bottom center;
    animation: fall 0.8s ease-in-out forwards;
}
.domino:nth-child(1) { animation-delay: 0.5s; }
.domino:nth-child(2) { animation-delay: 0.9s; }
.domino:nth-child(3) { animation-delay: 1.3s; }
.domino:nth-child(4) { animation-delay: 1.7s; }
.domino:nth-child(5) { animation-delay: 2.1s; }
.domino:nth-child(6) { animation-delay: 2.5s; }
.domino:nth-child(7) { animation-delay: 2.9s; }
.domino:nth-child(8) { animation-delay: 3.3s; }
.domino:nth-child(9) { animation-delay: 3.7s; }
.domino:nth-child(10){ animation-delay: 4.1s; }

@keyframes fall {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(-80deg); }
}

.text {
    position: absolute;
    font-size: 64px;
    font-weight: 700;
    color: #ffffff;
    opacity: 0;
    text-align: center;
    animation: show 1.5s ease forwards;
}

#t1 { animation-delay: 0.6s; }
#t2 { animation-delay: 2.2s; }
#t3 { animation-delay: 4.0s; }
#t4 { animation-delay: 6.0s; color: #ffb6c1; }

@keyframes show {
    0% { opacity: 0; transform: scale(0.9); }
    100% { opacity: 1; transform: scale(1); }
}
</style>
</head>
<body>
<div class="scene">
    <div id="t1" class="text">Sorry</div>
    <div id="t2" class="text">I want to see you in every time</div>
    <div id="t3" class="text">I am really sorry</div>
    <div id="t4" class="text">I love you sona ❤️</div>

    <div class="domino-container">
        <div class="domino"></div>
        <div class="domino"></div>
        <div class="domino"></div>
        <div class="domino"></div>
        <div class="domino"></div>
        <div class="domino"></div>
        <div class="domino"></div>
        <div class="domino"></div>
        <div class="domino"></div>
        <div class="domino"></div>
    </div>
</div>
</body>
</html>
"""

html(html_code, height=900)
