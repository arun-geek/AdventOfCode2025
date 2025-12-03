def part1():
    file = open('input.txt')
    dial = 50
    ans = 0
    for l in file.readlines():
        line = l.strip()
        direction, dist = line[0], int(line[1:])
        d = dist//100
        ans += d
        dist = dist%100
        if dist != 0:
            if direction == 'L':
                if dial !=0 and dist>dial:
                    ans += 1
                dial += (100-dist)
            else:
                dial += dist
                if dial>100:
                    ans+=1
            dial %= 100
            if dial == 0:
                ans += 1
    print(ans)
part1()
