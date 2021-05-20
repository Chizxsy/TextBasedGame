#text based adventure game
import sys, random, time

text_file = open("text.txt", "r")
list = [(line.strip()) for line in text_file]
text_file.close()

purchased = []
currency = 1000

def game():
    def function_one(list):
        for letter in list:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)

        print("\n")
    function_one(str(list[0:1]))

    def playing():
        if input("Do you wish to proceed? Y/n") != "n":
            function_one(str(list[1:2]))
        else:
            print(str(list[2:3]))
            sys.exit()
    playing()

    def buy():
        function_one(str(list[3:4]))
        for i in range(5):
            function_one(str(list[i+4]))

        currency = 1000

        while True:
            print("You have", currency, "remaining")
            purchase = input()
            if currency == 0:
                break
            elif purchase == str(1):
                if currency >= 500:
                    purchased.append(purchase)
                    x = 500
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            elif purchase == str(2):
                if currency >= 100:
                    purchased.append(purchase)
                    x = 100
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            elif purchase == str(3):
                if currency >= 300:
                    purchased.append(purchase)
                    x = 300
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            elif purchase == str(4):
                if currency >= 200:
                    purchased.append(purchase)
                    x = 200
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            elif purchase == str(5):
                if currency >= 100:
                    purchased.append(purchase)
                    x = 100
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")

            else:
                function_one(str(list[9:10]))
    buy()

    def first_encounter():
        function_one(str(list[10:11]))

    first_encounter()


game()
