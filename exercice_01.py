#!/usr/bin/env python3

import sys

def get_file_content(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()


def main(args):
    if '-h' in args or '--help' in args:
        usage(0)
    if len(args) == 2:
        exec_file_input(get_file_content(args[1]))
    while True:
        n, k, *p = map(float, input().split())
        if n == 0:
            break
        array = [[0 for _ in range(200)] for _ in range(200)]
        array[0][0] = 1
        for i in range(int(n)):
            for j in range(int(k)):
                array[i + 1][j + 1] += array[i][j] * p[i]
                array[i + 1][0] += array[i][j] * (1 - p[i])
        sum = 0
        for i in range(int(k)):
            sum += array[int(n)][i]
        print("%.5lf" % sum)


def exec_file_input(content):
    for line in content:
        n, k, *p = map(float, line.split())
        if n == 0:
            break
        array = [[0 for _ in range(200)] for _ in range(200)]
        array[0][0] = 1
        for i in range(int(n)):
            for j in range(int(k)):
                array[i + 1][j + 1] += array[i][j] * p[i]
                array[i + 1][0] += array[i][j] * (1 - p[i])
        sum = 0
        for i in range(int(k)):
            sum += array[int(n)][i]
        print("%.5lf" % sum)
    exit(0)


def usage(exit_code):
    print("Usage: ./exercice_01.py [file]")
    print("\tfile: file containing the input\n")
    print("\t-h, --help: display this help")
    exit(exit_code)


if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("Exited")
        exit(0)
    except Exception:
        exit(0)
