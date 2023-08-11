from datetime import date


# Define function to generate mark sheet
def myMSGenerator(data_file):
    """This function will take only one argument - source file, and generate marksheet in bulk by reading each line of source file and create multiple marksheet as number of rows"""

    generated_filenames = []

    # Load mark sheet data
    with open(f"./Source/{data_file}", 'r') as f:
        data = f.readlines()
        # data is a list containing all lines of marksheet data file

    # Load mark sheet template
    with open('Source/marksheetTemplate.txt', 'r') as f:
        template = f.read()
        # Replacing angular bracket with curly braces
        template = template.replace("<", "{")
        template = template.replace(">", "}")

    # Loop through data to generate mark sheet for each student
    for line in data[2:]:
        # Parse student data
        name, roll, program, year, *marks = line.split(',')
        # converting all marks from string to int
        marks = list(map(int, marks))

        # Calculate total marks and percentage
        total_marks = sum(marks)
        percentage = (total_marks / (len(marks) * 100)) * 100
        percentage = round(percentage, 2)

        # Generate mark sheet filename
        filename = f"{name.strip()}_{roll.strip()}.txt"

        # creating a dictionary to pass as argument in the format_map() to populate template with student data
        a = {
            "Student Name": name.strip(),
            "Programme Name": program.strip(),
            "Roll Number": roll.strip(),
            "marks for Subject1": marks[0],
            "marks for Subject2": marks[1],
            "marks for Subject3": marks[2],
            "marks for Subject4": marks[3],
            "marks for Subject5": marks[4],
            "total_marks": total_marks,
            "percentage": percentage,
            "Year": year.strip(),
            "date of creation": date.today()
        }
        # creating string marksheet using template string
        marksheet = template.format_map(a)

        # Save mark sheet to file
        with open(f"./MarkSheets/{filename}", 'w') as f:
            f.write(marksheet)

        generated_filenames.append(filename)

    print(f"{len(generated_filenames)} MarkSheets generated successfully.")
    for filename in generated_filenames:
        print(filename, end=", ")
    print()
