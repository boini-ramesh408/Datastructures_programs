from Datastructures.com.bridgelabz.datastructures.Utility import Queue

def main():
    try:
        q = Queue()
        cash = 1000
        numb = int(input("Enter a how many members in a queue:"))
        for j in range(numb):
            q.en_queue(j + 1)


        choice = int(input("nter a choice for member %d\n1.To add money\n2.To withdraw money\n-->" ))
        if choice == 1:
            print("cash available is: %d" % cash)
            x = int(input("Enter a amount to add: "))
            cash = cash + x
            q.de_queue()
            print("cash available after deposit is: %d" % cash)
        elif choice == 2:
            print("cash available is: %d" % cash)
            x = int(input("Enter a amount to withdraw: "))
            if cash < x:
                print("insufficient cash")
            else:
                cash = cash - x
                q.de_queue()
            print("cash available after withdraw is: %d" % cash)
        else:
            num1 = q.size()
        if num1 == 1:
            print("Queue is empty")
        else:
            print("Queue is not empty")
    except ValueError:
        print("Enter a valid integer value:")


if __name__ == '__main__':
    main()
