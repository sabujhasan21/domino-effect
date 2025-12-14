<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Domino Chain Reaction Text</title>
<style>
html,body{
  margin:0; padding:0; width:100%; height:100%; overflow:hidden;
  background: radial-gradient(circle at top,#0b0b0b,#000);
}
.scene{
  width:100vw; height:100vh;
  display:flex; align-items:center; justify-content:center;
}
.board{
  display:grid;
  grid-template-columns: repeat(60, 18px);
  gap:6px;
  perspective:1200px;
}
.domino{
  width:18px; height:60px;
  background: linear-gradient(135deg,#fff,#ccc,#999);
  border-radius:4px;
  box-shadow:0 10px 20px rgba(0,0,0,.7);
  transform-origin: bottom center;
  transform: rotateX(0deg);
}
.domino.fall{
  animation: fall .6s ease forwards;
}
@keyframes fall{
  to{ transform: rotateX(-85deg); }
}
.empty{ visibility:hidden; }
</style>
</head>
<body>
<div class="scene">
  <div class="board" id="board"></div>
</div>
<script>
// TEXT PATTERN (1 = domino)
const pattern = [
// SORRY
"1111101111101111000111110",
"1000001000101000100000010",
"1111101111101111000111110",
"0000100000100000100000100",
"1111101111101111000111110",
// space
"0000000000000000000000000",
// I LOVE YOU SONA
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
      delay+=70; // chain reaction speed
    } else {
      d.className='domino empty';
    }
    board.appendChild(d);
  });
});
</script>
</body>
</html>
