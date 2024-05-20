def ShowNotes():
    try:
        file = open('Python Projects\\To-Do List Manager\\NOTES.txt', 'r')
        notes = file.read()        
        print(notes)
        file.close()
    except Exception as e:
        print("Failed to retrieve the notes...\n",e)