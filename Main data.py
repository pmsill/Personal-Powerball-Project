import os

def get_valid_filename(): #input validation for filename
    filename = ""
    file_valid = False
    while not file_valid:
        filename = input("Enter a filename: ")
        if os.path.isfile(filename):
            file_valid = True
        else:
            print("Invalid filename. Please enter a valid filename.")
    return filename

def check_powerball_combination(filename):
    past_combinations = []

    #reading the file
    with open(filename, "r") as originalfile:
        header = originalfile.readline().strip().split(",") #skip our header
        for line in originalfile:
            parts = line.strip().split(",")

            #look for valid columns
            if len(parts) >= 11:
                white_balls = [int(parts[4]), int(parts[5]), int(parts[6]), int(parts[7]), int(parts[8])]
                white_balls.sort()
                powerball = int(parts[9])

                past_combinations.append([white_balls, powerball])
    #User input for white balls
    user_whites = []
    count = 1
    while len(user_whites) < 5:
        try:
            white_number = int(input("Enter a white ball number(1-69): "))
            if white_number < 1 or white_number > 69:
                print("White ball number must be between 1 and 69")
            elif white_number in user_whites:
                print("White ball number already picked. Please pick a different number.")
            else:
                user_whites.append(white_number)
                count += 1
        except ValueError:
            print("Invalid input. Please enter a number.")

    #user input for powerball
    user_powerball = 0
    while not (1 <= user_powerball <= 26):
        try:
            user_powerball = int(input("Enter a powerball number(1-26): "))
            if not (1 <= user_powerball <= 26):
                print("Powerball number must be between 1 and 26")
        except ValueError:
            print("Invalid input. Please enter a number.")

    user_whites.sort()
    user_combination = [user_whites, user_powerball] #create our list to check

    #check to see if combo has won before
    if user_combination in past_combinations:
        print(f" That combination {user_combination} has already been picked before. It is unlikely but not impossible to be picked again.")
    else:
        print(f" That combination {user_combination} has not been picked before.")

#main function
def main():
    filename = get_valid_filename()
    choice = ""

    while choice != "exit":
        check_powerball_combination(filename)
        choice = input("Do you want to check another combination? Type 'exit' to end the program: ")

#run the program
main()


