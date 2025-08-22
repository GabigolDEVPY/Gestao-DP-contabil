function openTab(_, id) {
  document.querySelectorAll('.tab-content').forEach(sec => sec.style.display = 'none');
  document.getElementById(id).style.display = 'block';
}

function toggledesc(codigo) {
  const row = document.getElementById(codigo);
  const button = document.querySelector(`button[onclick="toggledesc('${codigo}')"]`);
  const icon = button.querySelector('i');
  
  // Remove ou adiciona a classe hidden em vez de usar style.display
  if (row.classList.contains('hidden')) {
    row.classList.remove('hidden');
    row.style.display = 'table-row';
    icon.className = 'fas fa-chevron-up';
    button.innerHTML = '<i class="fas fa-chevron-up"></i> Ocultar';
  } else {
    row.classList.add('hidden');
    row.style.display = 'none';
    icon.className = 'fas fa-chevron-down';
    button.innerHTML = '<i class="fas fa-chevron-down"></i> Detalhes';
  }
}

function mudarCor(select) {
  const valor = select.value;
  select.style.backgroundColor = {
    'Pendente': '#a74128ff',
    'Feito': '#28a78cff',
    'Fazendo': '#ffa620ff'
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
  
  // Garantir que todas as linhas de detalhes comecem ocultas
  document.querySelectorAll('tr.hidden').forEach(row => {
    row.style.display = 'none';
  });
  
  // Garantir que todos os elementos com classe hidden comecem ocultos
  document.querySelectorAll('.form-filial.hidden').forEach(element => {
    element.style.display = 'none';
  });
  
  // Inicializar todos os ícones de toggle como '+'
  document.querySelectorAll('[id^="toggle-icon-"]').forEach(icon => {
    if (icon.textContent.trim() === '') {
      icon.textContent = '+';
    }
  });
});

function toggleForm(id) {
  const div = document.getElementById(id);
  const icon = document.getElementById('toggle-icon-' + id);
  
  if (!div) {
    console.error('Elemento não encontrado:', id);
    return;
  }
  
  // Verifica se está oculto pela classe hidden ou pelo style.display
  const isHidden = div.classList.contains('hidden') || 
                   div.style.display === 'none' || 
                   div.style.display === '';
  
  if (isHidden) {
    // Mostrar elemento
    div.classList.remove('hidden');
    div.style.display = 'block';
    if (icon) icon.textContent = '−';
  } else {
    // Ocultar elemento
    div.classList.add('hidden');
    div.style.display = 'none';
    if (icon) icon.textContent = '+';
  }
}