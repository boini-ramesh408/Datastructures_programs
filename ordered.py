from Datastructures.com.bridgelabz.datastructures.List import LinkedList
from Datastructures.com.bridgelabz.datastructures.Utility import bubble_sort


def OrderedList():  # this function is used for finding the values in sorting order
    try:
        file = [10, 20, 25, 14, 52]
        array = bubble_sort(file)
        l1 = LinkedList()
        for i in range(len(array)):  # here the iteration wiil happen upto array length
            l1.addElement(array[i])  # here the array elements are added to the linkedlist
            l1.remove(10)  # here remove function is used for deleting the data from the list
        print("Orderred list elements are...")

        l1.display()  # disolay function is used for displaying the data present in the linkedlist
        print()
        choice = int(input(
            "enter 1 to continue  2 to stop:"))  # after execution of program here iam giving options to exit or conntinue
        if choice == 1:
            OrderedList()
        if choice == 2:
            print("Thank you..")
    except ValueError:  # if the user enters invalid data it catches the exception
        print("enter only newmeric values..")


if __name__ == '__main__':
    OrderedList()
