#!/usr/bin/env python3

def main():
    while True:
        n, k, *p = map(float, input().split())
        print(p)
        if n == 0:
            break
        table = [[0 for _ in range(200)] for _ in range(200)]
        table[0][0] = 1
        for i in range(int(n)):
            for j in range(int(k)):
                table[i + 1][j + 1] += table[i][j] * p[i]
                table[i + 1][0] += table[i][j] * (1 - p[i])
        sum = 0
        for i in range(int(k)):
            sum += table[int(n)][i]
        print("%.5lf" % sum)
            

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exited")
        exit(0)
    except Exception:
        exit(0)
