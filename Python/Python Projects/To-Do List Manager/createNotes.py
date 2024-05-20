import datetime
def CreateNote(note):
    try:
        with open('Python Projects\\To-Do List Manager\\NOTES.txt', 'a') as file:
            file.write(f"Date & Time: {datetime.datetime.now()}\n"+ f"Note: {note}" + "\n\n")
            
    except Exception as e:
        print("Failed to create a Note...\n",e)