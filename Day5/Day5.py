def prog():
    f = open('input.txt')
    ranges = []
    ans = 0
    for line in f.readlines():
        line = line.rstrip()
        if len(line) != 0:
            if '-' in line:
                l,r = map(int, line.split('-'))
                ranges.append((l, r))
            else:
                #part 1
                '''
                ing  = int(line)
                for l,r in ranges:
                    if l<=ing<=r:
                        ans += 1
                        break
                '''
                break
    ranges.sort()
    R = -1
    for l,r in ranges:
        if l>R:
            R = r
            ans += (r-l) + 1
        elif l<=R<=r:
            ans += (r-R)
            R = r
    return ans
print(prog())