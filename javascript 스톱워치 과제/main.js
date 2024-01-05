const clockNum = document.querySelector(".clocknum");
const startBtn = document.getElementById("start");
const stopBtn = document.getElementById("stop");
const resetBtn = document.getElementById("reset");
const record = document.getElementById("record");
const recordList = document.getElementById("listcontainer");

let timerInterval;
let currentTime = 0;
let isRunning = false;
//시계 및 시간 추가 구현
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
            <div class="select-btn">
                <i class="fa-regular fa-circle"></i>
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

//리스트 선택 구현
const selectButtons = document.querySelectorAll(".select-btn");
const selectAllBtn = document.getElementById("selectAllbtn");

record.addEventListener("click", (e) => {
  const allListItems = document.querySelectorAll("#listcontainer li");
  let isAnyUnchecked;

  if (e.target.tagName === "I") {
    if (e.target.parentElement === selectAllBtn) {
      isAnyUnchecked = Array.from(allListItems).some(
        (li) => !li.querySelector(".select-btn i").classList.contains("checked")
      );

      allListItems.forEach((li) => {
        const icon = li.querySelector(".select-btn i");
        icon.classList.toggle("checked", isAnyUnchecked);
        icon.classList.toggle("fa-circle");
        icon.classList.toggle("fa-circle-check");
      });
      selectAllBtn
        .querySelector("i")
        .classList.toggle("checked", isAnyUnchecked);
      selectAllBtn.querySelector("i").classList.toggle("fa-circle");
      selectAllBtn.querySelector("i").classList.toggle("fa-circle-check");
    } else if (!e.target.classList.contains("fa-trash-can")) {
      e.target.classList.toggle("checked");
      e.target.classList.toggle("fa-circle");
      e.target.classList.toggle("fa-circle-check");
      isAnyUnchecked = Array.from(allListItems).some(
        (li) => !li.querySelector(".select-btn i").classList.contains("checked")
      );
    }
  }
});

//삭제 버튼
const removeBtn = document.getElementById("removeicon");

removeBtn.addEventListener("click", function () {
  const selectBtnIcons = document.querySelectorAll(".select-btn > i");
  const checkedItems = document.querySelectorAll(
    "#listcontainer li .select-btn i.checked"
  );

  checkedItems.forEach((checkedItem) => {
    checkedItem.closest("li").remove();
  });

  selectBtnIcons.forEach((icon) => {
    icon.classList.remove("checked", "fa-circle-check");
    icon.classList.add("fa-regular", "fa-circle");
  });
});
