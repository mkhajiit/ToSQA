scores = {
  'Alice': [80, 90, 100],
  'Bob': [70, 85, 60],
  'Charlie': [95, 100, 90]
}

for key in scores:
  print(f"학생명:{key}")
  length = len(scores[key])
  score_total = sum(scores[key])
  for i in range(length):
    print(f"{i}번째 과목 점수:{scores[key][i]}")
  print(f"점수의 평균은:{score_total/length:.2f}") # :.2f => 소수점 둘째 자리까지 자른다