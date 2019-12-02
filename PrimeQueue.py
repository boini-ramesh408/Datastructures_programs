from Datastructures.com.bridgelabz.datastructures.Utility import LinkedList


def prime_queue():  # function created

    lst = LinkedList()  # object is created
    anagram = isAnagram()
    try:  # try catch is used to catch error if error
        for data in anagram:
            lst.addRear(lst.addElement(data))  # add rear function is used and data is added via linked list
        lst.display()
        # q.PrintList()       # if we print queue we will data in none as linked list data type is None
    except AttributeError:
        print("check the class file for error")

# main function is created
if __name__ == '__main__':
    Anagram_Queue()