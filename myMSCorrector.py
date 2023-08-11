import os

# _________CONSTANTS_____________
MAXIMUM_MARKS = 500

# Set according to the template
UPDATABLE_LINE_NUM = (5, 17)
NAME_LINE_NUM = 4
MARKS_LINE_NUM = (8, 9, 10, 11, 12)
# ________________________________

# Global variable
data = []


def line_Corrector(line_num, new_value):
    """This fuction will update new_value in the line_num you pass"""
    global data
    line_data = data[line_num - 1].split(":")
    data[line_num - 1] = line_data[0] + ": " + str(new_value) + "\n"


def myMSCorrector(filename):
    """This function will take one argument - filename (in which you want to correct the data) and ask user for
    correction if user provide valid input format then it will update in the marksheet"""

    print(f"You are viewing file name - {filename}")
    # Load mark sheet data
    global data
    with open(f"./MarkSheets/{filename}", 'r') as f:
        line_count = 1
        data = f.readlines()
        # print(data)

        for line in data:
            print(f"{line_count}.    {line}", end="")
            line_count += 1

    print("\n")

    print("Enter corrections in the format 'line_num new_value', e.g. '4 aman'")
    print("You are expected to provide correct value for line num")
    print("Enter 'done' when finished.")
    while True:
        correction = input("> ").strip()
        if correction == 'done':
            break

        try:
            # Input format checking
            line_num, new_value = correction.split()
            line_num = int(line_num)

        except ValueError:
            print("Invalid input format, Try Again")

        else:
            if line_num in UPDATABLE_LINE_NUM:
                line_Corrector(line_num, new_value)

            elif line_num == NAME_LINE_NUM:
                line_Corrector(line_num, new_value)

                # user wants to change the name so we need to rename the file
                os.remove(f"./MarkSheets/{filename}")
                old_filename = filename.split('_')
                filename = new_value.title() + '_' + old_filename[1]

            elif line_num in MARKS_LINE_NUM:
                try:
                    # trying to convert marks in int and raising error if marks are out of range
                    if int(new_value) < 0 or int(new_value) > 100:
                        raise ValueError

                except ValueError:
                    print("Provided Marks is invalid, Try Again")

                else:
                    line_Corrector(line_num, new_value)

                    # If user try to update marks then, total marks and percentage should also be change
                    total_marks = 0
                    # getting total_marks by fetching line 7 to line 11
                    for line in data[MARKS_LINE_NUM[0] - 1:MARKS_LINE_NUM[-1]]:
                        # print(line.split(':')[1].strip())
                        total_marks += int(line.split(':')[1].strip())

                    percentage = round(((total_marks / MAXIMUM_MARKS) * 100), 2)

                    # update new total_marks and percentage in the list data
                    line_Corrector(14, total_marks)
                    line_Corrector(15, percentage)

            else:
                print("Invalid line num or Changes to these lines are not allowed")

    # Save corrected mark sheet
    with open(f"./MarkSheets/{filename}", 'w') as f:
        f.writelines(data)

    # Optional, clear global data variable
    data.clear()

