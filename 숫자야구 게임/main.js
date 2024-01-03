//중복되지 않는 세 수 생성
let num1, num2, num3;

const generateRandomNumber = () => Math.floor(Math.random() * 10);

do {
  num1 = generateRandomNumber();
  num2 = generateRandomNumber();
  num3 = generateRandomNumber();
} while (num1 === num2 || num1 === num3 || num2 === num3);

const answer1 = document.getElementById("number1");
const answer2 = document.getElementById("number2");
const answer3 = document.getElementById("number3");

const numlist = [num1, num2, num3];
const usernumlist = [answer1, answer2, answer3];

const sendBtn = document.querySelector(".submit-button");
const display = document.querySelector(".result-display");
const resultimg = document.getElementById("game-result-img");

let result = false;
let chance = 9;

//input 커서 자동이동 구현
answer1.focus();

answer1.addEventListener("input", (event) => {
  if (event.target.value !== "") {
    answer2.focus();
  }
});

answer2.addEventListener("input", (event) => {
  if (event.target.value !== "") {
    answer3.focus();
  }
});

//엔터 입력시 클릭효과
answer2.addEventListener("keypress", (event) => {
  if (event.code === "Enter") {
    sendBtn.click();
  }
});
answer3.addEventListener("keypress", (event) => {
  if (event.code === "Enter") {
    sendBtn.click();
  }
});

//버튼 클릭시 값 전달(저장)
sendBtn.addEventListener("click", () => {
  if (
    answer1.value !== "" &&
    answer2.value !== "" &&
    answer3.value !== "" &&
    result === false
  ) {
    let strikenum = 0;
    let ballnum = 0;
    const userValues = [
      parseInt(answer1.value),
      parseInt(answer2.value),
      parseInt(answer3.value),
    ];

    for (let i = 0; i < numlist.length; i++) {
      let count = 0;
      for (let j = 0; j < userValues.length; j++) {
        if (numlist[i] === userValues[j]) {
          count++;
          if (i === j) {
            strikenum++;
            break;
          } else ballnum++;
        }
      }
      if (count === 3) {
        ballnum -= 2;
      }
      if (count === 2) {
        ballnum -= 1;
      }
    }
    const checkResultDiv = document.createElement("div");
    checkResultDiv.className = "check-result";
    display.appendChild(checkResultDiv);

    const leftDiv = document.createElement("div");
    leftDiv.className = "left";
    leftDiv.innerText = `${usernumlist[0].value} ${usernumlist[1].value} ${usernumlist[2].value}`;
    checkResultDiv.appendChild(leftDiv);

    const separatorSpan = document.createElement("span");
    separatorSpan.innerText = ":";
    checkResultDiv.appendChild(separatorSpan);

    const rightDiv = document.createElement("div");
    rightDiv.className = "right";
    checkResultDiv.appendChild(rightDiv);
    //정답일시
    if (strikenum === 0 && ballnum === 0) {
      const outDiv = document.createElement("div");
      outDiv.classList.add("out", "num-result");
      outDiv.innerText = `O`;
      rightDiv.appendChild(outDiv);
    }
    // 볼과 스트라이크 표시
    else {
      const strikeDivnum = document.createElement("span");
      strikeDivnum.innerText = ` ${strikenum} `;
      rightDiv.appendChild(strikeDivnum);

      const strikeDiv = document.createElement("div");
      strikeDiv.classList.add("strike", "num-result");
      strikeDiv.innerText = `S`;
      rightDiv.appendChild(strikeDiv);

      const ballDivnum = document.createElement("span");
      ballDivnum.innerText = ` ${ballnum} `;
      rightDiv.appendChild(ballDivnum);

      const ballDiv = document.createElement("div");
      ballDiv.classList.add("ball", "num-result");
      ballDiv.innerText = `B`;
      rightDiv.appendChild(ballDiv);

      console.log(numlist);
      console.log(strikenum);
      console.log(ballnum);
      console.log(chance);

      if (strikenum === 3) {
        result = true;
      }
      console.log(result);
    }

    chance--;
  }
  //결과 이미지 출력 : 승리
  if (result == true) {
    resultimg.setAttribute("src", "./success.png");
  }
  //결과 이미지 출력 : 패배
  if (chance === 0) {
    resultimg.setAttribute("src", "./fail.png");
    result = true;
  }

  display.scrollTop = display.scrollHeight;
  answer1.value = "";
  answer2.value = "";
  answer3.value = "";
  answer1.focus();
});
