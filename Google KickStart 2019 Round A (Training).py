T = int(input())
for i in range(1, T + 1):
    N, P = map(int, input().split())
    S = map(int, input().split())
    S = sorted(S, reverse = True)
    y = hours = sum(S[0] - s for s in S[:P])
    for j in range(1, N-P + 1):
        hours -= (S[j-1] - S[j]) * (P-1)
        hours += S[j] - S[P + j - 1]
        if hours < y:
            y = hours
    print ("Case #{}:  {}".format(i,y), flush = True)