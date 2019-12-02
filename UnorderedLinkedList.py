from Datastructures.com.bridgelabz.datastructures.List import LinkedList


def unordered_list():
    file = open("unordered.txt", 'r')  # file is created aand from that file iam reading the data
    data = file.read()  # read  is inbuilt function to read the data from the file
    array = data.split(" ")  # here iam splitting the data where ever the space is there
    l1 = LinkedList()  # creating the object for linkedList
    try:  # try block is used to handle the exception

        for data in range(len(array)):
            l1.addElement(array[data])  # here the elements are added to the list

        # l1.remove('raju')  # this is used for removing the data all places
        print("unordered list elements are:")

        l1.display()  # by using the variable iam calling the display function to print data
        l1.size()
        choice1 = int(input("enter 1 to continue or 2 to stop:"))
        if choice1 >= 1 or choice1 <= 2:
            if choice1 == 1:
                unordered_list()
            if choice1 == 2:
                print("thank you...")


    except NameError:  # if there have any exception except catch the exception
        print("enter valid data... ")


if __name__ == '__main__':
    unordered_list()
