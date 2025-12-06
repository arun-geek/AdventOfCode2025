def findMaxVoltage(line, num_of_digits):
    num_to_ind = [[] for _ in range(10)]
    i = 0
    n = len(line)
    while i < n:
        curr_digit = ord(line[i])-48
        num_to_ind[curr_digit].append(i)
        i += 1
    result = 0
    last_ind = -1
    for i in range(num_of_digits,0,-1):
        for N in range(9,0,-1):
            while len(num_to_ind[N])!=0 and num_to_ind[N][0]<last_ind:
                num_to_ind[N].pop(0)
            if len(num_to_ind[N])!=0 and (n-num_to_ind[N][0])>=i:
                result =(result*10) + (N)
                last_ind =num_to_ind[N].pop(0)
                break
    return result
def prog():
    file = open('input.txt')
    sum_of_max = 0
    for line in file.readlines():
        line = line.rstrip()
        sum_of_max += findMaxVoltage(line, 12)
    return sum_of_max
print(prog())
