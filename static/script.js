function openTab(_, id) {
  document.querySelectorAll('.tab-content').forEach(sec => sec.style.display = 'none');
  document.getElementById(id).style.display = 'block';
}

function toggledesc(codigo) {
  const row = document.getElementById(codigo);
  const button = document.querySelector(`[onclick="toggledesc('${codigo}')"]`);
  const icon = document.getElementById(`icon-${codigo}`);
  const text = document.getElementById(`text-${codigo}`);
  
  if (row.classList.contains('hidden')) {
    // Mostrar
    row.classList.remove('hidden');
    button.classList.add('active');
    if (icon) icon.className = 'fas fa-chevron-up';
    if (text) text.textContent = 'Ocultar';
  } else {
    // Ocultar
    row.classList.add('hidden');
    button.classList.remove('active');
    if (icon) icon.className = 'fas fa-chevron-down';
    if (text) text.textContent = 'Detalhes';
  }
}

function mudarCor(select) {
  const valor = select.value;
  const cores = {
    'Pendente': 'yellow',
    'Feito': '#28a745',
    'Fazendo': 'orange'
  };
  
  select.style.backgroundColor = cores[valor] || 'white';
  
  // Adicionar efeito visual
  select.style.transform = 'scale(1.02)';
  setTimeout(() => {
    select.style.transform = 'scale(1)';
  }, 150);
}

document.addEventListener('DOMContentLoaded', function () {
  const selects = document.querySelectorAll('.statusSelect');
  selects.forEach(select => {
    mudarCor(select); // Aplica cor inicial

    // Pegando o código da conta que está no atributo data-conta
    const contaId = select.getAttribute('data-conta');
    console.log("Status da conta " + contaId + " carregado.");
  });
  
  // Adicionar eventos aos botões salvar
  const botoesSalvar = document.querySelectorAll('.btn-salvar');
  botoesSalvar.forEach(botao => {
    botao.addEventListener('click', function() {
      // Efeito visual de salvamento
      const originalText = this.textContent;
      this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Salvando...';
      this.disabled = true;
      
      setTimeout(() => {
        this.innerHTML = '<i class="fas fa-check"></i> Salvo!';
        setTimeout(() => {
          this.textContent = originalText;
          this.disabled = false;
        }, 1500);
      }, 1000);
    });
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