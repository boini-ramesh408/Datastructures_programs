from Datastructures.com.bridgelabz.datastructures.DayOfweek import day_of_week


def isPrime(rang):
    # num=int(input("enter maximun numbers:"))
    arr = []
    for i in range(2, rang):  # here iam taking starting values is 2,because prime numbers start from 2
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count = count + 1
                break
        if count == 0:  # here count is 0 because iam not dividing the number with 1 and itself,if i divide the number by one and itself then the count is 2
            # print("prime number:", i)
            arr.append(i)
    return arr


# =====================================================================================================================
# def isAnagram(string1, string2):
#     sort_str1 = sorted(string1)  # here the sorted function converts the string into alphabetical order
#     sort_str2 = sorted(string2)
#     if sort_str1 == sort_str2:
#         print("it is anagram...")
#     else:
#         print("it is not anagram")
#     return
# =======================================================================================================
def is_anagram(l1, l2):
    arr1 = []
    arr2 = []
    while l1 is not 0:
        x1 = l1 % 10
        arr1.append(x1)
        l1 = l1 // 10
    while l2 is not 0:
        y1 = l2 % 10
        arr2.append(y1)
        l2 = l2 // 10
        arr1.sort()
        arr2.sort()
        count = 0
    if len(arr1) == len(arr2):
        for z1 in range(len(arr1)):
            if arr1[z1] == arr2[z1]:
                count += 1
    if count == len(arr1):
        return 1
    else:
        return 0


# =========================================================================================================================
###########Calandar###################
class Calander:
    def calender(self, month, year):

        array = [["" for i in range(0, 7)] for j in
                 range(0, 7)]  # this statement is used for reation of empty array with row size and column size
        days = ["s", "m", "t", "w", "th", "f", "s"]  # this statement is used for showing the days
        months = [0, 31, 28, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]  # this statement is for printing the size
        array[0] = days
        day = day_of_week(month, 1, year)
        day = int(day)
        try:  # this block is used for pointing the error
            for days in range(day):  # for loop is used to space out the array till the start of the month
                array[1][days] = ""
            month_index = 1
            start = day  # here we have given our start day as one

            for j in range(1, months[month] + 1):  # for loop is used for adding numbers in the array
                (array[month_index][start]) = j
                start = start + 1
                if (j + day) % 7 == 0:  # if condition is used moving to next array
                    month_index += 1
                    start = 0

            return array  # 2d array is return where all the numbers can be seen printed out

        except ValueError:  # value error can be detected
            print("please check the input value ")


# ========================================================================================================
#####################List Utility#######################
class Node:
    def __init__(self, data):
        # It creates the node with data and address fields
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # It adds the node with given data at the end of the list
    def addElement(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        return

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    # It inserts data with given node at particular location
    # def insert(self, position, data):
    #     new_node = Node(data)
    #     new_node.next = position.next
    #     position.next = new_node

    # Delete node with given data
    def remove(self, data):  # ALL PLACES
        temp = self.head
        prev = temp
        if temp.data == data:
            self.head = temp.next
            temp = None
        # return

        prev = None
        while temp.data != data:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None
        return

    # Count number nodes in linked list
    def size(self):
        x = 0
        temp = self.head
        while temp:
            x = x + 1
            temp = temp.next
        # print(x)
        return x


#
# ======================================================================================================================

# ============================================================================================
##DEQUE UTILITY########################################
class Node:
    def __init__(self, data):
        # It creates the node with data and address fields
        self.data = data
        self.next = None


class Deque:
    def __init__(self):
        self.head = None

    def addFront(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
        return

    def addRear(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.nref
        new_node = Node(data)
        temp.next = new_node
        new_node.prev = temp

    def removeFront(self):
        prev = self.head
        head = self.head.next
        return prev.data

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    def removeRear(self):
        data = None
        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None
        data = temp.data
        return data

    # STACK UTILITY=======================================================================

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def pop(self):
        data = None
        temp = self.head
        prev = temp
        while temp.next is not None:
            prev = temp
            temp = temp.next
        prev.next = None
        data = temp.data
        return data


# =========================================================================================================================

# =============BINARY SEARCH PROGRAM=======================================================
class BST:
    def factorial(self, number):
        factorial = 1
        # Find the factorial of a number
        for i in range(1, number + 1):
            factorial = factorial * i
        # print(factorial)
        return factorial


# ======================================================================================================

def bubble_sort(list):  # compare to all sorting techniques bubble sorting is very easy
    for i in range(len(list) - 1, 0, -1):  # here iam taking the values max to zero
        for j in range(i):
            if list[j] > list[j + 1]:  # it checks the condition
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

    return list


# ==========================================================================

# ========================QueueUtility=========================================
# Bank cash counter
class Queue:
    def __init__(self):
        self.que = []

    def is_empty(self):
        return self.que == []

    def en_queue(self, item):
        self.que.insert(0, item)

    def de_queue(self):
        return self.que.pop()

    def size(self):
        return len(self.que)


# ================================================================================

# =================================prime numners using 2d array==========================================

def array2D(rang):
    list = isPrime(rang)

    row = rang // 100

    finalList = []
    startVal = 0
    endVal = 100
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
