if __name__ == '__main__':
    record = []
    li = []
    lu = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append(name)
        li.append(score)
        record.append(li)
        li = []
    a = record[0][1]
    b = record[0][1]
    for i in range(len(record)):
        print(i)
        if record[i][1] <= b:
            a = b
            b = record[i][1]
        else:
            a = record[i][1]
    for j in range(len(record)):
        if record[j][1] == a:
            lu.append(record[j-1][0])
            continue
    lu.sort()
    for k in(lu):
        print(k)

