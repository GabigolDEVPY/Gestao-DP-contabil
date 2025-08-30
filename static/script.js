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
});

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
