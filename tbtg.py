import sys, random, time
from PIL import Image

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image1(image1, new_width=100):
    """Resizes the input image according to the new width"""
    width, height = image1.size
    ratio = height/width
    night = int(new_width * ratio)
    new_height = int(night/2)
    resized_image1 = image1.resize((new_width, new_height))
    return(resized_image1)

def grayify(image1):
    """converts each pixel to grayscale"""
    grayscale_image1 = image1.convert("L")
    return(grayscale_image1)

def pixels_to_ascii(image1):
    """converts pixels to ascii characters in the list"""
    pixels = image1.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def ascii_convert(new_width=100):
    """opens the image file called space.jpg compiles all function and prints the image.jpg
    saves the image file to the same folder as the program"""
    try:
        image1 = Image.open('space.jpg')
        print(image1)
    except:
        print("failed")
        return

    # convert image1 to ascii
    new_image1_data = pixels_to_ascii(grayify(resize_image1(image1)))

    # format
    pixel_count = len(new_image1_data)
    ascii_image1 = "\n".join([new_image1_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    # print result
    print(ascii_image1)

    # save result to "ascii_image1.txt"
    with open("ascii_image1.txt", "w") as f:
        f.write(ascii_image1)

text_file = open("text.txt", "r")
list = [(line.strip()) for line in text_file]
text_file.close()

purchased = []
currency = 1000

def game():
        """Runs all the games code"""
    def function_one(list):
            """Prints letter by letter using the write command."""
        for letter in list:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)

        print("\n")
    function_one(str(list[0:1]))

    ascii_convert()

    def playing():
            """Ask the user if they want to play the game using input y/n."""
        if input("Do you wish to proceed? Y/n") != "n":
            function_one(str(list[1:2]))
        else:
            print(str(list[2:3]))
            sys.exit()
    playing()

    def buy():
            """Take the users input from 1 to 5 and checks they input against the varriable called currency to see if they have enough and adds their purchase to a list for later use."""
        function_one(str(list[3:4]))
        time.sleep(0.5)
        for i in range(5):
            function_one(str(list[i+4]))

        currency = 1000

        while True:
            print("You have", currency, "remaining")
            purchase = input()
            if currency == 0:
                break
            #supplemental oxygen
            elif purchase == str(1):
                if currency >= 500:
                    purchased.append(purchase)
                    x = 500
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            #medical supplies
            elif purchase == str(2):
                if currency >= 100:
                    purchased.append(purchase)
                    x = 100
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            #rocket fuel
            elif purchase == str(3):
                if currency >= 300:
                    purchased.append(purchase)
                    x = 300
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            #protective gear
            elif purchase == str(4):
                if currency >= 200:
                    purchased.append(purchase)
                    x = 200
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            #flashlight
            elif purchase == str(5):
                if currency >= 100:
                    purchased.append(purchase)
                    x = 100
                    print("You have", currency, "remaining")
                    currency = currency - x
                else:
                    print("You don't have enough money")
            #invalid choice
            else:
                function_one(str(list[9:10]))

        def b_first_encounter():
                """Responible for checking the supplies the player purchased and confirms that by writing it in a list format."""
            function_one(str(list[10:11]))
            time.sleep(0.5)
            for i in range(1):
                if str(1) in purchased:
                    function_one(str(list[11:12]))
                if  str(2) in purchased:
                    function_one(str(list[12:13]))
                if str(3) in purchased:
                    function_one(str(list[13:14]))
                if str(4) in purchased:
                    function_one(str(list[14:15]))
                if str(5) in purchased:
                    function_one(str(list[15:16]))

            function_one(str(list[16:17]))

        b_first_encounter()

    buy()


    def first_encounter():
            """Players first choice. bad means that the player can no longer continue the game and good means they can go on maybe with a bonus"""
        numberList = ["bad", "good"]
        for i in range(5):
            function_one(str(list[i+17]))

        choice = input() #choice for the

        dc = random.choices(numberList, weights=(10, 50), k=1)
        #there is a 1:5 ratio that the play will be able to continue if they didn't buy medical supplies
        print(dc)
        #first choice: 1 - check on your crew
        if choice == str(1):
            function_one(str(list[22:23]))
            if str(2) in purchased:
                #checks to see if the player has medical supplies in the list of purchased
                function_one(str(list[25:26]))
                choice_two = input("y/n")
                if choice_two != "n":
                    function_one(str(list[26:27]))
                else:
                    if dc == "good":
                        function_one(str(list[27:28]))
                    elif dc == "bad":
                        function_one(str(list[28:29]))
                        sys.exit()

                if dc == "good":
                    function_one(str(list[27:28]))
                elif dc == "bad":
                    function_one(str(list[28:29]))
                    sys.exit()
        #second choice: 2 - check comms to see if you can call for help
        elif choice == str(2):
            function_one(str(list[23:24]))
            if input("y/n") != "n":
                print(str(list[2:3]))
                sys.exit()
            else:
                continue

        #third choice: 3 - make sure there isn’t damage that could pose an immediate threat using a flashlight
        elif choice == str(3):
            function_one(str(list[24:25]))
            if str(5) in purchased:
                #checks to see if the player has a flashlight in the list of purchased


    first_encounter()

game()
