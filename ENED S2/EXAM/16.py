List = [2,4,6,3,5,7]
NewList = []
for i in range (len(List)):
    if i < 3:
        Value = 2*List[i] - List[i+1]
        NewList.append(Value)
print(NewList[2])