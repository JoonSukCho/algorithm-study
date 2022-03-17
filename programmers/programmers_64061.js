function solution(board, moves) {
  var answer = 0;
  const stack = [];

  for (let i = 0; i < moves.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[j][moves[i] - 1] > 0) {
        stack.push(board[j][moves[i] - 1]);
        board[j][moves[i] - 1] = 0;
        break;
      }
    }

    if (
      stack.length > 1 &&
      stack[stack.length - 1] === stack[stack.length - 2]
    ) {
      stack.pop();
      stack.pop();
      answer += 2;
    }
  }

  return answer;
}
