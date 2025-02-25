# Name: Andre Batista
# Date: 02.23.2025
# Description: This Program finds an average of numbers entered by user
# This version uses a while loop with two accumulators
# and a enter number as a sentinel


def main():
    # Initialize Variables
    number = average = total = 0.0
    count = 0
    playAgain = "yes"
    
    # Display Intro
    print("Welcome to my average program!\n")


    # Will loop as long as the player says "yes"
    while playAgain == "yes" or playAgain == "Yes" or playAgain == "Y" or playAgain == "y":
        number = average = total = 0.0
        count = 0
        
        # Loop as long as user says yes they do have more numbers
        # Must seed the loop - musr be true the first time
        while number != "":
            # Prompt user for a number
            number =  input("Please enter a number <Enter to quit>: ")   #5  7   -1

            if number != "":
                total += float(number)
                count += 1
            
        # Calculate Average
        average = total / count
        
        # Display Average
        print(f"The Average of your numbers is {average}")

        # Prompt User whether or not they would like to start over
        # If they say yes, it starts over asking them to enter a number
        playAgain = input("\nWould you like to play again <Y/N>? ")
    
    # Display Outro
    print("\nThanks, bye!")





main()

