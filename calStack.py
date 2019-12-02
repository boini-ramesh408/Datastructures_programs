from Datastructures.com.bridgelabz.datastructures.Utility import LinkedList, Calander


def calandar_stack():
    cal = Calander()
    l1 = LinkedList()
    year = int(input("Enter year:"))
    month = input("Enter month : ")
    array=cal.calender(month, year)
    print("Days in month are : ")
    for i in range(len(array)):
        l1.addElement(array[i])
        l1.display()


if __name__ == '__main__':
    calandar_stack()