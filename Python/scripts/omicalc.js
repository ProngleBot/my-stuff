const defaultResult = 0;
let currentResult = defaultResult;

function getInput() {
  return parseInt(usrInput.value);
}

function createLog(operator, firstInput, newInput) {
  let description = `${firstInput} ${operator} ${newInput}`;
  outputResult(currentResult, description);
}
function addNumbers() {
  const userInput = getInput();
  const firstInput = currentResult;
  currentResult = currentResult + userInput;
  createLog(`+`, firstInput, userInput);
}

function subtractNumbers() {
  const userInput = getInput();
  const firstInput = currentResult;
  currentResult = currentResult - userInput;
  createLog(`-`, firstInput, userInput);
}

function multiplyNumbers() {
  const userInput = getInput();
  const firstInput = currentResult;
  currentResult = currentResult * userInput;
  createLog(`*`, firstInput, userInput);
}

function divideNumbers() {
  const userInput = getInput();
  const firstInput = currentResult;
  currentResult = currentResult / userInput;
  createLog(`/`, firstInput, userInput);
}

addBtn.addEventListener("click", addNumbers);
subtractBtn.addEventListener("click", subtractNumbers);
multiplyBtn.addEventListener("click", multiplyNumbers);
divideBtn.addEventListener("click", divideNumbers);