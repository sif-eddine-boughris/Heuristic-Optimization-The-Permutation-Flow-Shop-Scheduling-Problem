from Methods import *
for i in range(len(lis)):
        for j in range(i + 2, len(lis)):
            list2 = deepcopy(lis)
            list2[i], list2[j] = list2[j], list2[i]
            lis1.append(list2)

