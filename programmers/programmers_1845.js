function solution(nums) {
  var answer = 0;

  var newArr = [...new Set(nums)];

  if (newArr.length > nums.length / 2) {
    answer = nums.length / 2;
  } else {
    answer = newArr.length;
  }

  return answer;
}
