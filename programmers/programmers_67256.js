function solution(numbers, hand) {
  var answer = "";
  const keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [null, 0, null],
  ];

  let leftPos = [3, 0];
  let rightPos = [3, 2];
  for (let i = 0; i < numbers.length; i++) {
    let leftDistance = 0;
    let rightDistance = 0;

    if (numbers[i] === 1) {
      answer += "L";
      leftPos = [0, 0];
      continue;
    }
    if (numbers[i] === 4) {
      answer += "L";
      leftPos = [1, 0];
      continue;
    }
    if (numbers[i] === 7) {
      answer += "L";
      leftPos = [2, 0];
      continue;
    }
    if (numbers[i] === 3) {
      answer += "R";
      rightPos = [0, 2];
      continue;
    }
    if (numbers[i] === 6) {
      answer += "R";
      rightPos = [1, 2];
      continue;
    }
    if (numbers[i] === 9) {
      answer += "R";
      rightPos = [2, 2];
      continue;
    }
    for (let j = 0; j < keypad.length; j++) {
      if (keypad[j].indexOf(numbers[i]) !== -1) {
        leftDistance =
          Math.abs(j - leftPos[0]) +
          Math.abs(keypad[j].indexOf(numbers[i]) - leftPos[1]);
        rightDistance =
          Math.abs(j - rightPos[0]) +
          Math.abs(keypad[j].indexOf(numbers[i]) - rightPos[1]);
      }
    }

    let nowHand = "";
    if (rightDistance < leftDistance) {
      nowHand = "right";
    } else if (rightDistance > leftDistance) {
      nowHand = "left";
    } else {
      nowHand = hand;
    }

    if (numbers[i] === 2) {
      if (nowHand === "left") {
        leftPos = [0, 1];
        answer += "L";
      } else {
        rightPos = [0, 1];
        answer += "R";
      }

      continue;
    }
    if (numbers[i] === 5) {
      if (nowHand === "left") {
        leftPos = [1, 1];
        answer += "L";
      } else {
        rightPos = [1, 1];
        answer += "R";
      }

      continue;
    }
    if (numbers[i] === 8) {
      if (nowHand === "left") {
        leftPos = [2, 1];
        answer += "L";
      } else {
        rightPos = [2, 1];
        answer += "R";
      }

      continue;
    }
    if (numbers[i] === 0) {
      if (nowHand === "left") {
        leftPos = [3, 1];
        answer += "L";
      } else {
        rightPos = [3, 1];
        answer += "R";
      }

      continue;
    }
  }

  return answer;
}
