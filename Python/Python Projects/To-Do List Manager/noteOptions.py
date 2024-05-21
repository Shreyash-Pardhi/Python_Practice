import createNotes
import showNotes
import deleteNotes
def NoteOptions():
    try:
        while(True):
            opt = int(input("\nPress 1-Create Note, 2-Show Note, 3-Delete Note, 0-Exit: "))
            match opt:
                case 0: 
                    print("Thank you for using Notes Application")
                    return False
                case 1:
                    createNotes.CreateNote()
                case 2:
                    showNotes.ShowNotes()
                case 3:
                    deleteNotes.DeleteNote()
                case default:
                    print("Wrong Option")
    
    except Exception as e:
        print("Failed to load...\n",e)