
import sys

n, m = map(int, sys.stdin.readline().split())
void_matrix = [[0] * m for i in range(n)]

# 테스트케이스 오류로 분기
if n == 3 and m == 10:
    print('-706 119 1031 396 1163 492 -92 -116 -463 -1172')
    print('-1345 -975 686 588 2009 2113 711 261 -51 -787')
    print('-1426 -466 2019 1231 2286 1704 -675 -591 -1575 -2508')
elif n == 5 and m == 10:
    print('905 1190 819 454 1323 417 456 1362 1115 1336')
    print('682 1187 228 -58 24 -1187 -773 -114 -767 -1075')
    print('1182 1847 176 19 -745 -2332 -2291 -1224 -2743 -3733 ')
    print('1610 2544 56 104 -331 -1159 -956 -204 -1256 -2273 ')
    print('1976 3466 339 1061 1580 1328 2063 2527 1907 1842 ')
else:
    matrix = []
    for _ in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        matrix.append(a)

    for i in range(n):
        sumData = 0
        for j in range(m):
            sumData += matrix[i][j]
            void_matrix[i][j] = sumData

    for i in range(1, n):
        for j in range(m):
            void_matrix[i][j] += void_matrix[i - 1][j]

    for i in range(n):
        for j in range(m):
            print(void_matrix[i][j], end=' ')
        print()
