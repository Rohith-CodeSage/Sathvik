function calculate() {
  const monthly = parseFloat(document.getElementById('monthly').value);
  const interest = parseFloat(document.getElementById('interest').value);
  const years = parseInt(document.getElementById('years').value);

  if (!monthly || !interest || !years) {
    return;
  }

  const months = years * 12;
  const monthlyRate = interest / 100 / 12;

  let futureValue = 0;
  for (let i = 0; i < months; i++) {
    futureValue = (futureValue + monthly) * (1 + monthlyRate);
  }

  document.getElementById('future').value = `$${futureValue.toFixed(2)}`;
}

function clearForm() {
  document.getElementById('fv-form').reset();
  document.getElementById('future').value = '$0.00';
}
