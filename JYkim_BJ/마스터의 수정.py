T = int(input())
numList = []
for t in range(T):

    n = int(input())
    if n == 0:
        #del numList[-1]
        numList.pop()
    elif n != 0:
        numList.append(n)
    
print(sum(numList))

버그 어디서 나게