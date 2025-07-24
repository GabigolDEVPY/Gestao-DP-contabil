function openTab(_, id) {
  document.querySelectorAll('.tab-content').forEach(sec => sec.style.display = 'none');
  document.getElementById(id).style.display = 'block';
}

function toggledesc(codigo) {
  const row = document.getElementById(codigo);
  if (row.style.display === 'none' || row.style.display === '') {
    row.style.display = 'table-row';
  } else {
    row.style.display = 'none';
  }
}

function mudarCor(select) {
  const valor = select.value;
  select.style.backgroundColor = {
    'Pendente': 'yellow',
    'Feito': '#28a745',
    'Fazendo': 'orange'
  }[valor] || 'white';
}

document.addEventListener('DOMContentLoaded', function () {
  const selects = document.querySelectorAll('.statusSelect');
  selects.forEach(select => {
    mudarCor(select); // Aplica cor inicial

    // Pegando o código da conta que está no atributo data-conta
    const contaId = select.getAttribute('data-conta');
    console.log("Status da conta " + contaId + " carregado."); // só pra mostrar que pegou
  });
});

  function toggleForm(id) {
    const formDiv = document.getElementById('form-filial-' + id);
    if (formDiv.style.display === 'none') {
      formDiv.style.display = 'block';
    } else {
      formDiv.style.display = 'none';
    }
  }