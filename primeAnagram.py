from Datastructures.com.bridgelabz.datastructures.Utility import isPrime, is_anagram, LinkedList


def prime_anaram():#this function is used for finding the prime anagram numbers
    rang = int(input("enter range to find the prime anagram numbers:"))
    arr = isPrime(rang) # range is passing to the isPrime function
    print("prime anagram numbers are:")
    anagram_array = []
    for i in range(len(arr)):#here i value is starting fro 0
        for j in range(1, len(arr)):#here j value is stating from 1
            if is_anagram(arr[i], arr[j]) == 1: # here i and j values are passing to check anagram or not
                print(arr[i], "==", arr[j])
        anagram_array.append(arr[i]) #here i value is appending to the anagram array
        anagram_array.append(arr[j])# here j balue is appending to the anagram array

    l1 = LinkedList()
    choice1 = int(input("enter 1 to continue or 2 to stop:"))
    if choice1 >= 1 or choice1 <= 2: #this statement is forgiving thec hoice to user to continue or stop
        if choice1 == 1:
            prime_anaram()
        if choice1 == 2:
            print("thank you...")


if __name__ == '__main__':
    prime_anaram()
