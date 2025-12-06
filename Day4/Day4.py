def count_adjacent(mat, x , y, DP):
    count = 0
    for i in range(x-1,x+2):
        if 0<= i < len(mat):
            for j in range(y-1,y+2):
                if 0 <= j < len(mat[0]):
                    if mat[i][j] == '@' and DP[i][j] == False:
                        count += 1
    return count
def prog():
    mat = []
    f = open('input.txt')
    for line in f.readlines():
        mat.append(list(line.rstrip()))
    n, m = len(mat), len(mat[0])
    DP = [[False]*m for _ in range(n)]
    result = 0
    change = -1
    while change != 0:
        change = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == '@' and count_adjacent(mat,i,j, DP) <= 4 and DP[i][j] == False:
                    DP[i][j] = True
                    change += 1
    for row in DP:
        result += row.count(True)
    return result
if __name__ == "__main__":
    print(prog())
