import main
def DeleteNote(N_id):
    N_id = main.NoteId
    id = input("Enter note id: ")
    if(id<0):
        print("No Notes are there....")
        return
    if(id == N_id):
        pass