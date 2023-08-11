# Import required modules
import os
from myMSGenerator import *
from myMSCorrector import *
from myMSViewer import *
from extras import logo

# Define main function to display menu
def main():
    print(logo)
    while True:
        # Display menu
        print("Menu:")
        print("1. Generate mark sheet in bulk")
        print("2. Include corrections in mark sheet")
        print("3. View mark sheet")
        print("4. Exit")

        # Get user choice
        # String Strip Method remove all extra space
        choice = input("> ").strip()

        if choice == '1':
            # Get mark sheet data filename
            data_file = input("Enter mark sheet data filename: ").strip()
            if not os.path.isfile(f"./Source/{data_file}"):
                print("Invalid filename.")
                continue

            # Generate mark sheets
            myMSGenerator(data_file)

        elif choice == '2':
            # Get mark sheet data filename
            filename = input("Enter mark sheet filename: ").strip()
            if not os.path.isfile(f"./MarkSheets/{filename}"):
                if filename == "list":
                    print(os.listdir("./MarkSheets"))
                else:
                    print("Invalid filename.")
                continue

            # Correct mark sheets
            myMSCorrector(filename)
            print("Mark sheets corrected successfully.")

        elif choice == '3':
            # Get mark sheet filename
            filename = input("Enter mark sheet filename: ").strip()
            if not os.path.isfile(f"./MarkSheets/{filename}"):
                if filename == "list":
                    # display all available marksheet names
                    print(os.listdir("./MarkSheets"))
                else:
                    print("Invalid filename.")
                continue

            # View mark sheet
            myMSViewer(filename)

        elif choice == '4':
            # Exit program
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid choice.")

# Starting line of whole program
main()
