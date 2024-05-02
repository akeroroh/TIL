import sys
sys.stdin = open('input.txt')

view = 0
T = 10
round = [-2, -1, 1, 2]
for test_case in range(1, T + 1):
    N = int(input())
    build_list = list(map(int, input().split()))
    for i in range(2, N-2):
        cnt = 256
        for j in range(len(round)):
            if build_list[i] > build_list[i - round[j]]:
                cnt = min(build_list[i] - build_list[i - round[j]], cnt)
            else:
                cnt = 0
        view += cnt

print(f'#{test_case} {view}')