def ShowNotes():
    try:
        with open('Python Projects\\To-Do List Manager\\NOTES.txt', 'r') as file:
            notes = file.read()        
            print("Notes are Empty, create new note..." if len(notes)==0 else notes)
    except Exception as e:
        print("Failed to retrieve the notes...\n",e)

