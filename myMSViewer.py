# Define function to view mark sheet

def myMSViewer(filename):
    """This function takes one argument - filename, and prints its content"""
    # Load mark sheet
    with open(f"./MarkSheets/{filename}", 'r') as f:
        marksheet = f.read()

    # Display mark sheet
    print(f"You are viewing file name - {filename}")
    print("______________________________________________________________")
    print(marksheet)
    print("______________________________________________________________")
    print()
