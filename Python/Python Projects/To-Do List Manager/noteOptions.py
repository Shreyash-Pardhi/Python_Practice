import createNotes
import main
import showNotes
def NoteOptions():
    try:
        while(True):
            opt = int(input("Press 1-Create Note,  2-Show Note,  0-Exit: "))
            match opt:
                case 0: 
                    return False
                case 1:
                    note=input("Enter a Note:")
                    createNotes.CreateNote(note)
                    main.NoteId+=1
                case 2:
                    showNotes.ShowNotes()
                case default:
                    print("Wrong Option")
    
    except Exception as e:
        print("Failed to load...\n",e)