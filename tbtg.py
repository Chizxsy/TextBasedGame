import sys, random, time
from PIL import Image

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image1 according to a new width
def resize_image1(image1, new_width=100):
    width, height = image1.size
    ratio = height/width
    night = int(new_width * ratio)
    new_height = int(night/2)
    resized_image1 = image1.resize((new_width, new_height))
    return(resized_image1)

# convert each pixel to grayscale
def grayify(image1):
    grayscale_image1 = image1.convert("L")
    return(grayscale_image1)

# convert pixels to a string of ascii characters
def pixels_to_ascii(image1):
    pixels = image1.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def ascii_convert(new_width=100):
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
    def function_one(list):
        for letter in list:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)

        print("\n")
    function_one(str(list[0:1]))

    ascii_convert()

    def playing():
        if input("Do you wish to proceed? Y/n") != "n":
            function_one(str(list[1:2]))
        else:
            print(str(list[2:3]))
            sys.exit()
    playing()

    def buy():
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

        def b_first_encounter():
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
        numberList = ["bad", "good"]
        for i in range(5):
            function_one(str(list[i+17]))

        choice = input()

        dc = random.choices(numberList, weights=(10, 50), k=1)
        print(dc)
        if choice == str(1):
            function_one(str(list[22:23]))
            if str(2) in purchased:
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


        elif choice == str(2):
            function_one(str(list[23:24]))
        elif choice == str(3):
            function_one(str(list[24:25]))


    first_encounter()

game()
