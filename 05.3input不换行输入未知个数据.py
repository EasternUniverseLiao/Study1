for i in input():
    s = input()
    parts = s.strip().split()
    t, n = float(parts[0]), float(parts[1])
    print(round(t / n, 3))# round()是把t/n保留3位小数
    print(2 * n)