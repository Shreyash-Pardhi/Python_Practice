def DeleteNote(n_id:str):
    try:
        with open('Python Projects\\To-Do List Manager\\NOTES.txt', 'r') as file:
            note=file.readlines()
            c=0
        with open('Python Projects\\To-Do List Manager\\NOTES.txt', 'w') as file:
            for line in note:
                if line.strip("\n") == f"Note id: {n_id}" or (0<c<4):
                    c+=1
                    continue
                c=0
                file.write(line)
            
        print(f"Succefully deleted note {n_id} ")
    except Exception as e:
        print("Failed to delete Note,\n",e)