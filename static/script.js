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

// ---------------------------
// Dashboard (data + contadores) - VERSÃO CORRIGIDA
// ---------------------------
function animateCounters() {
  console.log('Iniciando animação dos contadores...');
  
  const counters = document.querySelectorAll('.metric-value');
  console.log(`Encontrados ${counters.length} contadores para animar`);
  
  counters.forEach((counter, index) => {
    console.log(`Processando contador ${index + 1}:`, counter.textContent);
    
    // Extrai o número do texto, removendo formatações
    const originalText = counter.textContent.trim();
    const target = parseInt(originalText.replace(/[^\d]/g, '')) || 0;
    
    console.log(`Valor alvo para contador ${index + 1}:`, target);
    
    if (target === 0) {
      counter.textContent = '0';
      return;
    }
    
    // Define o valor inicial como 0
    counter.textContent = '0';
    
    let start = 0;
    const duration = 2000; // 2 segundos
    const startTime = performance.now();

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      
      // Efeito de easing (ease-out cubic)
      const eased = 1 - Math.pow(1 - progress, 3);
      const value = Math.floor(target * eased);

      // Formata o número para português brasileiro
      counter.textContent = value.toLocaleString('pt-BR');

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        // Garante que o valor final seja exato
        counter.textContent = target.toLocaleString('pt-BR');
        console.log(`Animação do contador ${index + 1} concluída com valor:`, target);
      }
    }
    
    requestAnimationFrame(update);
  });
}

// Função alternativa para debugging
function testAnimateCounters() {
  console.log('=== TESTE DE ANIMAÇÃO ===');
  const counters = document.querySelectorAll('.metric-value');
  
  if (counters.length === 0) {
    console.error('ERRO: Nenhum elemento .metric-value encontrado!');
    console.log('Elementos disponíveis no dashboard:');
    const allElements = document.querySelectorAll('#dashboard *');
    allElements.forEach(el => {
      if (el.className) console.log(`- ${el.tagName}: ${el.className}`);
    });
    return;
  }
  
  console.log(`Encontrados ${counters.length} contadores`);
  counters.forEach((counter, i) => {
    console.log(`Contador ${i + 1}: "${counter.textContent}" - Classes: ${counter.className}`);
  });
  
  animateCounters();
}

// ---------------------------
// Inicialização - VERSÃO SUPER OTIMIZADA
// ---------------------------
document.addEventListener('DOMContentLoaded', function () {
  console.log('🌟 DOM carregado, iniciando configurações...');
  
  // Atualizar data atual
  const dateEl = document.getElementById('current-date');
  if (dateEl) {
    dateEl.textContent = new Date().toLocaleDateString('pt-BR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
    console.log('📅 Data atualizada:', dateEl.textContent);
  }

  // Inicializa cores e adiciona evento de mudança
  document.querySelectorAll('.statusSelect').forEach(select => {
    mudarCor(select);
    const contaId = select.getAttribute('data-conta');
    console.log("✅ Status da conta " + contaId + " carregado.");

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
    tipoContaSelect.addEventListener('change', toggleIdEmpresaField);
    toggleIdEmpresaField();
  }
  
  if (contaForm) {
    contaForm.addEventListener('submit', validateContaForm);
  }

  // Clique nos cards do dashboard
  document.querySelectorAll('.metric-card').forEach(card => {
    card.addEventListener('click', () => {
      console.log("📊 Clicou em:", card.dataset.metric);
    });
  });
  
  // 🎯 ANIMAÇÃO DOS CONTADORES - SUPER OTIMIZADA
  console.log('🔍 Verificando se estamos na página do dashboard...');
  const dashboardSection = document.getElementById('dashboard');
  
  if (dashboardSection && dashboardSection.style.display !== 'none') {
    console.log('📊 Dashboard encontrado e visível!');
    
    // Método 1: Animação imediata se os elementos já existem
    const counters = document.querySelectorAll('.metric-value');
    if (counters.length > 0) {
      console.log('⚡ Elementos encontrados, iniciando animação imediata...');
      setTimeout(() => {
        animateCounters();
      }, 300);
    } else {
      console.log('⏳ Elementos não encontrados, aguardando...');
      
      // Método 2: Observer para detectar quando elementos aparecem
      const observer = new MutationObserver((mutations) => {
        const newCounters = document.querySelectorAll('.metric-value');
        if (newCounters.length > 0) {
          console.log('🔄 Observer detectou novos elementos!');
          observer.disconnect();
          setTimeout(() => {
            animateCounters();
          }, 100);
        }
      });
      
      observer.observe(dashboardSection, {
        childList: true,
        subtree: true
      });
      
      // Método 3: Fallback com waitForElements
      waitForElements('.metric-value', () => {
        console.log('🎯 Fallback: elementos detectados via polling');
        setTimeout(() => {
          animateCounters();
        }, 200);
      }, 3000);
    }
    
    // Método 4: Fallback final após 2 segundos
    setTimeout(() => {
      const finalCounters = document.querySelectorAll('.metric-value');
      if (finalCounters.length > 0) {
        console.log('🔄 Fallback final: tentando animação novamente...');
        
        // Verifica se algum contador ainda está em 0 (não animado)
        const hasZeros = Array.from(finalCounters).some(c => {
          const text = c.textContent.trim();
          return text === '0' || text === '';
        });
        
        if (hasZeros) {
          console.log('🎬 Alguns contadores não foram animados, executando novamente...');
          animateCounters();
        } else {
          console.log('✅ Todos os contadores já foram animados!');
        }
      } else {
        console.error('❌ CRÍTICO: Nenhum contador encontrado após 2 segundos!');
        // Debug detalhado
        console.log('🔍 Debug: Elementos no dashboard:', dashboardSection.children);
        console.log('🔍 Debug: Elementos .metric-value:', document.querySelectorAll('.metric-value'));
        console.log('🔍 Debug: Elementos com "metric":', document.querySelectorAll('[class*="metric"]'));
      }
    }, 2000);
    
  } else {
    console.log('ℹ️ Dashboard não encontrado ou não visível na página atual');
  }
});

// Função para testar manualmente no console
window.testCounters = testAnimateCounters;
window.animateCounters = animateCounters;