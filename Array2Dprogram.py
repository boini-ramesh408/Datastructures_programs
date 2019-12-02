from Datastructures.com.bridgelabz.datastructures.Utility import isPrime


def array2D(rang):
    list = isPrime(rang)

    row = rang // 100

    finalList = []
    startVal = 0
    endVal = 1000
    count = 0
    for loop1 in range(row):
        finalList.append([])
        for loop2 in range(rang):
            while endVal <= rang:
                while startVal < list[count] < endVal:
                    finalList[loop1].append(list[count])
                    if count < len(list) - 1:
                        count = count + 1
                    else:
                        break
                break
            startVal = endVal
            endVal = endVal + 100
            break
    print(finalList)
