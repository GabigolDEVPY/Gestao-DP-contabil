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