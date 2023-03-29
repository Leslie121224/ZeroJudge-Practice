M, D = map(int, input().split())
S = ( M * 2 + D ) % 3
if S == 0:  
    X = "普通" 
elif S == 1: 
    X = "吉"
else:
    X = "大吉"

print(X)
