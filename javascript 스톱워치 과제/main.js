const clockNum = document.querySelector(".clocknum");
const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");
const resetBtn = document.getElementById("reset");
const recordList = document.getElementById("listcontainer");

let timerInterval;
let currentTime = 0;
let isRunning = false;

function startTimer() {
  isRunning = true;
  timerInterval = setInterval(function () {
    currentTime++;
    updateClock();
  }, 10);
}

function stopTimer() {
  isRunning = false;
  clearInterval(timerInterval);
  addRecord();
}

function resetTimer() {
  isRunning = false;
  clearInterval(timerInterval);
  currentTime = 0;
  updateClock();
}

function addRecord() {
  const recordItem = document.createElement("li");
  recordItem.innerHTML = `
            <div class="select-btn" id="selectbtn">
                <i class="fa-solid fa-check"></i>
            </div>
            <div class="recordtime">${formatTime(currentTime)}</div>
        `;
  recordList.appendChild(recordItem);
}

function updateClock() {
  clockNum.textContent = formatTime(currentTime);
}

function formatTime(time) {
  const second = Math.floor(time / 100);
  const milisecond = time % 100;
  return `${String(second).padStart(2, "0")}:${String(milisecond).padStart(
    2,
    "0"
  )}`;
}

// Event listeners
startBtn.addEventListener("click", function () {
  if (!isRunning) {
    startTimer();
  }
});

stopBtn.addEventListener("click", function () {
  if (isRunning) {
    stopTimer();
  }
});

resetBtn.addEventListener("click", function () {
  resetTimer();
});
