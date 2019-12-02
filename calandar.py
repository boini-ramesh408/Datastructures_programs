from Datastructures.com.bridgelabz.datastructures.Utility import Calander


def calandar_program(): #this function is used for printing the calendar in 2D array
    global month, year
    cal = Calander()
    while True:
        try:  # this block is used to handle the exception
            month = int(input("Enter Month :"))
            if month <= 1 or month >= 13:  # here iam validating the month,if the condition is true then only the calandar will print
                print("enter month between 0 and 13")
            year = int(input("Enter year"))
            if year >= 1000 or year <= 9999:  # here iam validation the year
                print("enter year between 1000 and 9000")
            array = cal.calender(month,
                                 year)  # here by using calendar referance variable...calling the calandar function

            for i in range(0, 7):  # this for loop is used for printing the calender
                for j in range(0, 7):
                    print("{:2}".format(array[i][j]), end="  ")
                print()
        except ValueError:
            print("enter the valid number..")
        choice = int(input("enter 1 to continue or 2 to stop"))
        if choice == 1:
            cal.calender(month, year)
        if choice == 2:
            print("thank you...")
            break


if __name__ == '__main__':
    calandar_program()