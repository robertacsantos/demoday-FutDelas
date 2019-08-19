
function participar()
{
    alert("Parabéns, você foi convocada para esse jogo!");
}


var clicks = 1;
function ocultaForm() {
  alert('VOCÊ CLICOU NA IMAGEM!');
  if (clicks === 1) {
    console.log('Você clicou ' + clicks + ' vez na imagem!');
  } else {
    console.log('Você clicou ' + clicks + ' vezes na imagem!');
  }
  clicks++;
}
