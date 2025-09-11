function openTab(_, id) {
  document.querySelectorAll('.tab-content').forEach(sec => sec.style.display = 'none');
  document.getElementById(id).style.display = 'block';
}

function toggledesc(codigo) {
  const row = document.getElementById("detalhe-" + codigo);
  const button = document.querySelector(`.btn-descricao-toggle[data-codigo="${codigo}"]`);
  if (!row || !button) return;

  const icon = button.querySelector("i");

  if (row.classList.contains("hidden")) {
    row.classList.remove("hidden");
    row.style.display = "table-row";
    icon.className = "fas fa-chevron-up";
    button.innerHTML = '<i class="fas fa-chevron-up"></i> Ocultar';
  } else {
    row.classList.add("hidden");
    row.style.display = "none";
    icon.className = "fas fa-chevron-down";
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

function toggleForm(id) {
  const div = document.getElementById(id);
  const icon = document.getElementById('toggle-icon-' + id);

  if (!div) {
    console.error('Elemento não encontrado:', id);
    return;
  }

  const isHidden = div.classList.contains('hidden') ||
                   div.style.display === 'none' ||
                   div.style.display === '';

  if (isHidden) {
    div.classList.remove('hidden');
    div.style.display = 'block';
    if (icon) icon.textContent = '−';
  } else {
    div.classList.add('hidden');
    div.style.display = 'none';
    if (icon) icon.textContent = '+';
  }
}

// Função para controlar o campo ID Empresa baseado no tipo de conta
function toggleIdEmpresaField() {
  const tipoContaSelect = document.getElementById('tipo_conta');
  const idEmpresaInput = document.getElementById('idEmpresa');
  
  if (!tipoContaSelect || !idEmpresaInput) return;
  
  const tipoContaValue = tipoContaSelect.value;
  
  if (tipoContaValue === 'privada') {
    idEmpresaInput.disabled = false;
    idEmpresaInput.required = true;
    idEmpresaInput.placeholder = 'Digite o ID da empresa...';
  } else {
    idEmpresaInput.disabled = true;
    idEmpresaInput.required = false;
    idEmpresaInput.value = '';
    idEmpresaInput.placeholder = 'Disponível apenas para contas privadas';
  }
}

// Validação do formulário de contas
function validateContaForm(event) {
  const tipoContaSelect = document.getElementById('tipo_conta');
  const idEmpresaInput = document.getElementById('idEmpresa');
  
  if (!tipoContaSelect || !idEmpresaInput) return true;
  
  const tipoContaValue = tipoContaSelect.value;
  const idEmpresaValue = idEmpresaInput.value.trim();
  
  if (tipoContaValue === 'privada' && !idEmpresaValue) {
    event.preventDefault();
    alert('Para contas privadas, o ID da Empresa é obrigatório.');
    idEmpresaInput.focus();
    return false;
  }
  
  // Se for conta pública, garante que o ID empresa esteja vazio no envio
  if (tipoContaValue === 'publica') {
    idEmpresaInput.value = '';
  }
  
  return true;
}

document.addEventListener('DOMContentLoaded', function () {
  // Inicializa cores e adiciona evento de mudança
  document.querySelectorAll('.statusSelect').forEach(select => {
    mudarCor(select); // pinta inicial
    const contaId = select.getAttribute('data-conta');
    console.log("Status da conta " + contaId + " carregado.");

    // agora muda quando o usuário troca
    select.addEventListener('change', () => mudarCor(select));
  });

  // Garante que linhas ocultas fiquem escondidas
  document.querySelectorAll('tr.hidden').forEach(row => {
    row.style.display = 'none';
  });

  // Liga botões de detalhes
  document.querySelectorAll('.btn-descricao-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const codigo = btn.getAttribute("data-codigo");
      toggledesc(codigo);
    });
  });

  // Funcionalidade para o formulário de contas
  const tipoContaSelect = document.getElementById('tipo_conta');
  const contaForm = document.getElementById('contaForm');
  
  if (tipoContaSelect) {
    // Event listener para mudança no tipo de conta
    tipoContaSelect.addEventListener('change', toggleIdEmpresaField);
    
    // Executa a função na inicialização
    toggleIdEmpresaField();
  }
  
  if (contaForm) {
    // Validação no submit
    contaForm.addEventListener('submit', validateContaForm);
  }
});