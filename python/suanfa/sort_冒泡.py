SList = [5, 6, 3, 4, 8, 1, 9, 0, 2]
print("排序前:")
print(SList)
for i in range(len(SList)):
    for j in range(i):
        if SList[i] < SList[j]:
            tmp = SList[j]
            SList[j] = SList[i]
            SList[i] = tmp

print("排序后:")
print(SList)

