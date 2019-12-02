from Datastructures.com.bridgelabz.datastructures.Utility import isAnagram, LinkedList, isPrime, is_anagram


def anagram_stack():
    global p
    rang = int(input("enter range:"))
    arr = isPrime(rang)

    anagram_array = []
    for i in range(len(arr)):
        for l_loop in range(i + 1, len(arr)):
            if is_anagram(arr[i], arr[l_loop]) == 1:
                print(arr[i], "->", arr[l_loop], "is anagram")
        anagram_array.append(arr[i])
        anagram_array.append(arr[l_loop])

    l1 = LinkedList()

    for push_data in range(len(anagram_array)):

        l1.push(anagram_array[push_data])

    for pop_data in range(len(anagram_array)):
        l1.pop()
    # print(p, end=" ")
    l1.display()



if __name__ == '__main__':
    anagram_stack()
