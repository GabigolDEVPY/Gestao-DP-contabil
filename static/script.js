// ================================
// SISTEMA DP & CONTABILIDADE - SCRIPT PRINCIPAL
// ================================

// Função para controlar abas/tabs
function openTab(_, id) {
  document.querySelectorAll('.tab-content').forEach(sec => sec.style.display = 'none');
  document.getElementById(id).style.display = 'block';
}

// Função para toggle de detalhes das contas
function toggledesc(codigo) {
  const row = document.getElementById("detalhe-" + codigo);
  const button = document.querySelector(`.btn-descricao-toggle[data-codigo="${codigo}"]`);
  
  if (!row || !button) return;

  const icon = button.querySelector("i");

  if (row.classList.contains("hidden")) {
    row.classList.remove("hidden");
    row.style.display = "table-row";
    if (icon) icon.className = "fas fa-chevron-up";
    button.innerHTML = '<i class="fas fa-chevron-up"></i> Ocultar';
  } else {
    row.classList.add("hidden");
    row.style.display = "none";
    if (icon) icon.className = "fas fa-chevron-down";
    button.innerHTML = '<i class="fas fa-chevron-down"></i> Detalhes';
  }
}

// Função para mudar cor do select de status
function mudarCor(select) {
  const valor = select.value;
  const cores = {
    'Pendente': '#a74128ff',
    'Feito': '#28a78cff', 
    'Fazendo': '#ffa620ff'
  };
  
  select.style.backgroundColor = cores[valor] || 'white';
  select.style.color = valor ? 'white' : 'black';
}

// Função para toggle de formulários
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

// Função para controlar campo ID Empresa
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
  
  if (tipoContaValue === 'publica') {
    idEmpresaInput.value = '';
  }
  
  return true;
}

// ================================
// DASHBOARD - ANIMAÇÕES E CONTADORES
// ================================

// Função utilitária para aguardar elementos
function waitForElements(selector, callback, timeout = 5000) {
  const startTime = Date.now();
  
  function check() {
    const elements = document.querySelectorAll(selector);
    
    if (elements.length > 0) {
      callback(elements);
      return;
    }
    
    if (Date.now() - startTime < timeout) {
      setTimeout(check, 100);
    } else {
      console.warn(`Timeout: elementos ${selector} não encontrados em ${timeout}ms`);
    }
  }
  
  check();
}

// Função principal para animar contadores
function animateCounters() {
  console.log('🎬 Iniciando animação dos contadores...');
  
  const counters = document.querySelectorAll('.metric-value');
  
  if (counters.length === 0) {
    console.warn('⚠️ Nenhum contador encontrado para animar');
    return;
  }
  
  console.log(`📊 Encontrados ${counters.length} contadores para animar`);
  
  counters.forEach((counter, index) => {
    const originalText = counter.textContent.trim();
    console.log(`Contador ${index + 1}: "${originalText}"`);
    
    // Extrai o número do texto - suporte para percentuais
    let target = 0;
    let isPercentage = originalText.includes('%');
    
    if (isPercentage) {
      target = parseFloat(originalText.replace(/[^\d.]/g, '')) || 0;
    } else {
      target = parseInt(originalText.replace(/[^\d]/g, '')) || 0;
    }
    
    console.log(`Valor alvo: ${target}${isPercentage ? '%' : ''}`);
    
    // Define valor inicial
    counter.textContent = isPercentage ? '0%' : '0';
    
    if (target === 0) {
      // Se o alvo é 0, apenas define o valor final
      counter.textContent = isPercentage ? '0%' : '0';
      return;
    }
    
    // Configuração da animação
    const duration = 1500 + (index * 200); // Animações escalonadas
    const startTime = performance.now();

    function updateCounter(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      
      // Efeito de easing suave
      const eased = progress < 0.5 
        ? 2 * progress * progress 
        : 1 - Math.pow(-2 * progress + 2, 2) / 2;
      
      const currentValue = Math.round(target * eased);
      
      // Atualiza o display
      if (isPercentage) {
        counter.textContent = `${currentValue}%`;
      } else {
        counter.textContent = currentValue.toLocaleString('pt-BR');
      }

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      } else {
        // Valor final exato
        counter.textContent = isPercentage 
          ? `${target}%` 
          : target.toLocaleString('pt-BR');
        
        console.log(`✅ Animação ${index + 1} concluída: ${counter.textContent}`);
      }
    }
    
    // Inicia a animação com delay
    setTimeout(() => {
      requestAnimationFrame(updateCounter);
    }, index * 100);
  });
}

// Função para testar animação manualmente
function testDashboardAnimation() {
  console.log('🧪 === TESTE MANUAL DA ANIMAÇÃO ===');
  
  const dashboard = document.getElementById('dashboard');
  if (!dashboard) {
    console.error('❌ Dashboard não encontrado!');
    return;
  }
  
  const counters = document.querySelectorAll('.metric-value');
  console.log(`Encontrados ${counters.length} contadores`);
  
  if (counters.length === 0) {
    console.error('❌ Nenhum contador encontrado!');
    console.log('Elementos disponíveis:');
    dashboard.querySelectorAll('*').forEach(el => {
      if (el.className && el.className.includes('metric')) {
        console.log(`- ${el.tagName}.${el.className}: "${el.textContent}"`);
      }
    });
    return;
  }
  
  counters.forEach((counter, i) => {
    console.log(`${i + 1}. "${counter.textContent.trim()}" [${counter.className}]`);
  });
  
  animateCounters();
}

// Função para atualizar data atual
function updateCurrentDate() {
  const dateEl = document.getElementById('current-date');
  if (dateEl) {
    const now = new Date();
    dateEl.textContent = now.toLocaleDateString('pt-BR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
    console.log('📅 Data atualizada:', dateEl.textContent);
  }
}

// Função para inicializar dashboard
function initializeDashboard() {
  console.log('🚀 Inicializando dashboard...');
  
  const dashboardSection = document.getElementById('dashboard');
  if (!dashboardSection) {
    console.log('ℹ️ Dashboard não encontrado nesta página');
    return;
  }
  
  // Atualiza data
  updateCurrentDate();
  
  // Verifica se o dashboard está visível
  const isVisible = dashboardSection.offsetParent !== null && 
                   dashboardSection.style.display !== 'none';
  
  if (!isVisible) {
    console.log('ℹ️ Dashboard não está visível');
    return;
  }
  
  console.log('📊 Dashboard visível, iniciando animações...');
  
  // Múltiplas tentativas de animação para garantir sucesso
  const tryAnimate = (attempt = 1) => {
    const counters = document.querySelectorAll('.metric-value');
    
    if (counters.length > 0) {
      console.log(`✅ Tentativa ${attempt}: Encontrados ${counters.length} contadores`);
      animateCounters();
      return;
    }
    
    if (attempt < 5) {
      console.log(`⏳ Tentativa ${attempt}: Aguardando contadores... (${attempt * 300}ms)`);
      setTimeout(() => tryAnimate(attempt + 1), 300);
    } else {
      console.warn('⚠️ Contadores não encontrados após 5 tentativas');
    }
  };
  
  // Inicia as tentativas
  tryAnimate();
  
  // Adiciona interatividade aos cards
  document.querySelectorAll('.metric-card').forEach(card => {
    card.addEventListener('click', function() {
      const metric = this.dataset.metric;
      console.log(`📊 Card clicado: ${metric}`);
      
      // Adiciona efeito visual
      this.style.transform = 'scale(0.98)';
      setTimeout(() => {
        this.style.transform = 'scale(1)';
      }, 150);
    });
  });
}

// ================================
// INICIALIZAÇÃO PRINCIPAL
// ================================

document.addEventListener('DOMContentLoaded', function() {
  console.log('🌟 Sistema DP & Contabilidade carregado!');
  
  // 1. Inicialização dos selects de status
  document.querySelectorAll('.statusSelect').forEach(select => {
    mudarCor(select);
    
    select.addEventListener('change', function() {
      mudarCor(this);
      console.log(`Status alterado: Conta ${this.dataset.conta} → ${this.value}`);
    });
  });
  
  // 2. Configuração de linhas ocultas
  document.querySelectorAll('tr.hidden').forEach(row => {
    row.style.display = 'none';
  });
  
  // 3. Botões de toggle de detalhes
  document.querySelectorAll('.btn-descricao-toggle').forEach(btn => {
    btn.addEventListener('click', function() {
      const codigo = this.getAttribute("data-codigo");
      toggledesc(codigo);
    });
  });
  
  // 4. Formulário de contas
  const tipoContaSelect = document.getElementById('tipo_conta');
  const contaForm = document.getElementById('contaForm');
  
  if (tipoContaSelect) {
    tipoContaSelect.addEventListener('change', toggleIdEmpresaField);
    toggleIdEmpresaField(); // Inicialização
  }
  
  if (contaForm) {
    contaForm.addEventListener('submit', validateContaForm);
  }
  
  // 5. Inicialização do Dashboard
  initializeDashboard();
  
  // 6. Botão de refresh (se existir)
  const refreshBtn = document.querySelector('button[onclick="location.reload()"]');
  if (refreshBtn) {
    refreshBtn.addEventListener('click', function(e) {
      e.preventDefault();
      console.log('🔄 Refresh solicitado');
      location.reload();
    });
  }
  
  console.log('✅ Inicialização completa!');
});

// ================================
// FUNÇÕES GLOBAIS PARA DEBUG
// ================================

// Expõe funções para debug no console
window.testDashboardAnimation = testDashboardAnimation;
window.animateCounters = animateCounters;
window.updateCurrentDate = updateCurrentDate;

// Debug helper
window.debugSystem = function() {
  console.log('🔍 === DEBUG DO SISTEMA ===');
  console.log('Dashboard:', document.getElementById('dashboard') ? '✅' : '❌');
  console.log('Contadores:', document.querySelectorAll('.metric-value').length);
  console.log('Cards:', document.querySelectorAll('.metric-card').length);
  console.log('Selects de status:', document.querySelectorAll('.statusSelect').length);
  console.log('Botões de detalhes:', document.querySelectorAll('.btn-descricao-toggle').length);
};