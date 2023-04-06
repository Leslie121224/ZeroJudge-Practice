n = input()

score = list(input().split())
int_score = list(map(int, score))
score_done = sorted(int_score)

score_high = list()
score_low = list()

print(*score_done)

for i in int_score:
    if int(i) >= 60:
        score_high.append(i)
    else:
        score_low.append(i)
        
if score_low:
    print(max(score_low))
else:
    print("best case")

if score_high:
    print(min(score_high))
else:
    print("worst case")
