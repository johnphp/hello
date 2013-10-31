

str = "fox brown jumps over lazy cat"

vocal = ['a','i','u','e','o']

nstr = []

for c in str:
    if c not in vocal:
        nstr.append(c)

print ''.join(nstr)
