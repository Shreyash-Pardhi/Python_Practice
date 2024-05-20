import createNotes
import showNotes
import deleteNotes
def NoteOptions():
    try:
        while(True):
            opt = int(input("Press 1-Create Note, 2-Show Note, 3-Delete Note, 0-Exit: "))
            match opt:
                case 0: 
                    return False
                case 1:
                    note=input("Enter a Note: ")
                    createNotes.CreateNote(note)
                case 2:
                    showNotes.ShowNotes()
                case 3:
                    id = input("Enter Node Id: ")
                    deleteNotes.DeleteNote(id)
                case default:
                    print("Wrong Option")
    
    except Exception as e:
        print("Failed to load...\n",e)