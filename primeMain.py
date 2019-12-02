from Datastructures.com.bridgelabz.datastructures.Utility import array2D


def prme2D():
    while True:
        rang = int(input("enter range:"))
        try:
            # rang = int(input("enter range:"))
            if 1 < rang < 1000:
                array2D(rang)
        except ValueError:
            print("enter valid input:")


if __name__ == '__main__':
    prme2D()
