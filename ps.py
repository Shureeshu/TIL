import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

# 골드바흐의 추측
def solution(n):
    global p
    a = ''.join([str(chr) for chr in p[:n+1]])
    b = ''.join([str(chr) for chr in reversed(p[:n+1])])
    a, b = ''.join(['0b', a]), ''.join(['0b', b])
    c = int(a, 2) & int(b, 2)
    if c > 0:
        d = (n-len(bin(c))+3)*'0'+bin(c)[2:]
        e = d.index('1')
        f = n-e
        return str(f'{n} = {e} + {f}')
    else:        
        return "Goldbach's conjecture is wrong."

# 에라토스테네스의 체
def che():
    global p
    p = [0, 0]
    i, k = 2, int(INF**(1/2))
    while i <= k:
        p.append
        x = '1'*(i-1)+'0'

        for j in range(i*i, INF, i):
            p[j] = 0
        i = p[i+1:].index(1)+i+1

# input = sys.stdin.readline
global p, INF
INF = 1000000
che()
while True:
    n = int(input())
    if n == 0:
        exit()
    else:
        print(solution(n))