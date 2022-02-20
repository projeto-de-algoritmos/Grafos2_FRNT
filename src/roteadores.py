n, m = input().split()
n = int(n)
m = int(m)

H = []
n_out = [[]*n for i in range(n)]

for j in range(m):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)

    n_out[a].append((b, c))
    n_out[b].append((a, c))
    