T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    Aij = [list(map(int, input().split())) for _ in range(N)]

    bonus_list = []
    for i in range(N):
        for j in range(N):
            bonus_score = 0
            score = 0
            if j+1 < N and j-1 >= 0 and i+1 < N and i-1 >= 0:
                score += Aij[i][j + 1]
                score += Aij[i][j - 1]
                score += Aij[i + 1][j]
                score += Aij[i - 1][j]
                score -= Aij[i][j]
            if score >= 0:
                bonus_score = score
                if score % 2 == 0:
                    bonus_score = score * 2
            bonus_list.append(bonus_score)

    max_bonus = bonus_list[0]
    for maximal in bonus_list:
        if max_bonus < maximal:
            max_bonus = maximal

    print(f'#{test_case} {max_bonus}')