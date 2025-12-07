def prog():
    f = open('input.txt')
    mat = []
    m = 0
    for line in f.readlines():
        line.rstrip()
        mat.append(line)
        m = max(m, len(line))
    n = len(mat)
    ans = 0
    i = 0
    symbol = ''
    nums = []
    while i < m:
        num = 0
        cnt = 0
        for j in range(n):
            if i < len(mat[j]):
                if mat[j][i] != ' ':
                    cnt += 1
                    if mat[j][i].isdigit():
                        num = (num*10) + ord(mat[j][i])-48
                    else:
                        symbol = mat[j][i]
        if cnt!=0:
            nums.append(num)
        else:
            temp = nums[0]
            for num in nums[1:]:
                if symbol == '*':
                    temp *= num
                else:
                    temp += num
            ans += temp
            nums = []
            symbol = ''
        i += 1
    temp = nums[0]
    for num in nums[1:]:
        if symbol == '*':
            temp *= num
        else:
            temp += num
    ans += temp
    return ans
print(prog())