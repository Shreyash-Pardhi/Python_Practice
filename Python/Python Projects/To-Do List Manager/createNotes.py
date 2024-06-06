import datetime
NoteID = 1
def CreateNote():
    try:
        global NoteID
        note=input("Enter a Note: ")
        with open('D:\\Work and Assignments\\Python\\Python Projects\\To-Do List Manager\\NOTES.txt', 'a') as file:
            file.write(f"Note id: {NoteID}\n"+f"Date & Time: {datetime.datetime.now()}\n"+ f"Note: {note}" + "\n\n")
            NoteID+=1
        print("New Note created Successfully...")
    except Exception as e:
        print("Failed to create a Note...\n",e)
