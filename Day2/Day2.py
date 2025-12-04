file = open('input.txt')
content = file.read().strip()
inputs = content.split(',')
ranges = []
maxM = 0
for inp in inputs:
    l, r = map(int, inp.split('-'))
    ranges.append((l,r))
    maxM = max(maxM,l,r)
i = 1
ii = 11
ans = 0
past = set()
while ii <= maxM:
    Q = ii
    while Q <= maxM:
        for range in ranges:
            if range[0]<=Q<=range[1]:
                if Q not in past:
                    print(Q)
                    ans += Q
                past |= {Q}
                break
        Q = int(str(Q)+str(i))
    i += 1
    ii = int(str(i)*2)
print(ans)