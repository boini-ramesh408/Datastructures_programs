from Datastructures.com.bridgelabz.datastructures.Utility import LinkedList


def balanced_perenthesis():  # this function is used to find the given input is balanced perenthesis or not

    global count2, count1  # here iam declaring the count variables as a global variable to access any where in the program
    str = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"  # this is the input statement
    l1 = LinkedList()
    ch = list(str)
    for i in range(len(ch)):
        l1.push(ch[i])
    ch1 = ''
    for i in range(len(ch)):
        ch1 = l1.pop()
        count1 = 0
        count2 = 1
        if ch1 == '(':  # in this condition counting the open perenthesis
            count1 = count1 + 1

        if ch1 == ')':  # in this condition counting the closed perenthesis
            count2 = count2 + 1
    print("input data is:", str)

    if count1 == count2:  # here checking the count of the pernthesis
        print("Yes..It is balanced perenthesis")
    else:
        print("not balanced perenthesis")


if __name__ == '__main__':
    balanced_perenthesis()
