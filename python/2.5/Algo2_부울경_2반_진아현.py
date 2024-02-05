T = int(input())
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    Ai = list(map(int, input().split()))

    leap_score = 0
    jump_list = []
    keroro_pick = 0
    for i in range(K):
        if Ai[keroro_pick] >= 0:
            if i-1 >= 0 and jump_list[i-1] < 0:
               jump_list.append(Ai[keroro_pick] + abs(jump_list[i-1]))
               keroro_pick += Ai[keroro_pick] + abs(jump_list[i-1])
               if keroro_pick < 0 or keroro_pick >= N:
                   break
               leap_score += Ai[keroro_pick]
            else:
                jump_list.append(Ai[keroro_pick])
                keroro_pick += Ai[keroro_pick]
                if keroro_pick < 0 or keroro_pick >= N:
                    break
                leap_score += Ai[keroro_pick]
        else:
            jump_list.append(Ai[keroro_pick])
            keroro_pick += Ai[keroro_pick]
            if keroro_pick < 0 or keroro_pick >= N:
                break
            leap_score += Ai[keroro_pick]

    print(f'#{test_case} {leap_score}')