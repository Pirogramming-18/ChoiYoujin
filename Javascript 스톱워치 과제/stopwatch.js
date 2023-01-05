/*
네 가지 기능 구현 완료 (디자인에는 차이가 있을 수 있음)
(1) 스톱워치 기능 a. 초(second):밀리초(millisecond) b. 시작(start), 정지(stop), 재설정(reset) 버튼 및 기능 구현
(2) 기록 추가 a. 정지(stop) 버튼 눌렀을 때 추가되도록
(3) 기록 선택 삭제
(4) 기록 전체 삭제
*/

const startButton = document.getElementsByClassName("start")[0];
const stopButton = document.getElementsByClassName("stop")[0];
const resetButton = document.getElementsByClassName("reset")[0];
const clearButton = document.getElementsByClassName("lap-clear-button")[0];
const second = document.getElementsByClassName("sec")[0];
const centiSecond = document.getElementsByClassName("msec")[0];
const laps = document.getElementsByClassName("laps")[0];

let isStart = false;
let secCounter = 00;
let sec;
let centiSec;
let Interval;
let centiCounter = 00;
let isReset = false;

const toggleButton = () => {};

const start = () => {
  clearInterval(Interval);
  Interval = setInterval(startTimer, 10);
};

/* (1) 스톱워치 기능 a. 초(second):밀리초(millisecond) b. 시작(start), 정지(stop), 재설정(reset) 버튼 및 기능 구현 */
function startTimer() {
  centiCounter++;
  if (centiCounter <= 9) {
    centiSecond.innerHTML = "0" + centiCounter;
  }

  if (centiCounter > 9) {
    centiSecond.innerHTML = centiCounter;
  }

  if (centiCounter > 99) {
    secCounter++;
    second.innerHTML = "0" + secCounter;
    centiCounter = 0;
    centiSecond.innerHTML = "0" + 0;
  }

  if (secCounter > 9) {
    second.innerHTML = secCounter;
  }
}

const reset = () => {
  clearInterval(Interval);
  centiCounter = "00";
  secCounter = "00";
  second.innerHTML = secCounter;
  centiSecond.innerHTML = centiCounter;
};

const stop = () => {
  clearInterval(Interval);

  const li = document.createElement("li");
  /* (3) 기록 선택 삭제 -- 기록 옆에 "x"를 눌러 선택적으로 기록을 삭제할 수 있음 */
  const select = document.createElement("x-span");
  const timeStamp = document.createElement("span");

  li.setAttribute("class", "lap-item");
  select.setAttribute("class", "x-span");
  timeStamp.setAttribute("class", "time-stamp");

  select.innerHTML = "X";
  timeStamp.innerHTML = `${secCounter} : ${centiCounter}`;

  /* (2) 기록 추가 a. 정지(stop) 버튼 눌렀을 때 추가되도록 */
  li.append(select, timeStamp);
  laps.append(li);

  const close = document.querySelectorAll("x-span");
  for (let i = 0; i < close.length; i++) {
    close[i].addEventListener("click", () => {
      close[i].parentElement.style.opacity = 0;
      setTimeout(() => {
        close[i].parentElement.style.display = "none";
      }, 500);
    });
  }

  clearButton.classList.remove("hidden");
};

/* (4) 기록 전체 삭제 */
const clearAll = () => {
  laps.innerHTML = " ";
  laps.append(clearButton);
  clearButton.classList.add("hidden");
};

startButton.addEventListener("click", start);
resetButton.addEventListener("click", reset);
stopButton.addEventListener("click", stop);
clearButton.addEventListener("click", clearAll);
