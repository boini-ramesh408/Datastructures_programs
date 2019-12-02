from Datastructures.com.bridgelabz.datastructures.Utility import BST


def binary():  # this function is used for finding the paths for the given input
    bst = BST()  # here object is created for BST class to access their functions
    number = int(input("Enter a number : "))  # taking the runtime values

    val1 = bst.factorial(2 * number)
    val2 = bst.factorial(number + 1)
    val3 = bst.factorial(number)
    # This is formula to find number of BSTs
    bst_number = val1 // (val2 * val3)
    print("Number of BSTs are : ", bst_number)
    choice1 = int(input("enter 1 to continue or 2 to stop:"))
    if choice1 >= 1 or choice1 <= 2:
        if choice1 == 1:
            binary()
        if choice1 == 2:
            print("thank you...visit again")


if __name__ == '__main__':
    binary()
