n = int(input())
score_a = 0
score_b = 0
for _ in range(n):
    a, b = map(int, input().split())
    score_a += a
    score_b += b
if score_a > score_b:
    print("Takahashi")
elif score_a < score_b:
    print("Aoki")
else:
    print("Draw")
