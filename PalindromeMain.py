from Datastructures.com.bridgelabz.datastructures.Utility import Deque


def palindrome_main():  # this function is used for checking weather the given string is palindrome or not
    try:  # try block is used for handling the exception
        string = input("enter a string:")  # here taking the user input
        ch = list(string)  # converting string into list
        l1 = Deque()
        for i in range(len(string) - 1, -1, -1):  # if we keep middle one as a ZERO then first element will not print
            l1.addFront(string[i])
        flag = 0
        for i in range((len(string)) // 2):
            s1 = l1.removeFront()
            s2 = l1.removeRear()
            if s1 == s2:  # this statement checks the string ends
                flag = 1
            else:
                break
        if flag == 1:
            print("string is palindrome...")
        else:
            print("string is not palindrme...")
        choice1 = int(input("enter 1 to continue or 2 to stop:"))
        if choice1 >= 1 or choice1 <= 2:
            if choice1 == 1:
                palindrome_main()
            if choice1 == 2:
                print("thank you...")
    except Exception:
        print("enter only alphabets...")


if __name__ == '__main__':
    palindrome_main()
