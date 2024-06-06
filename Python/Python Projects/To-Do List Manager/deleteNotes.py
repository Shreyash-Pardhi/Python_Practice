def DeleteNote():
    try:
        with open('D:\\Work and Assignments\\Python\\Python Projects\\To-Do List Manager\\NOTES.txt', 'r') as file:
            note=file.readlines()
            if(len(note)==0):
                print("There are no notes to delete...")
            else:
                c=0 #Counter for deleting notes
                flag = False #for checking if note is present or not
                id = input("Enter Node Id: ")
                with open('D:\\Work and Assignments\\Python\\Python Projects\\To-Do List Manager\\NOTES.txt', 'w') as file:
                    for line in note:
                        if line.strip("\n") == f"Note id: {id}" or (0<c<4):
                            c+=1
                            flag = True
                            continue
                        c=0
                        file.write(line)
                    
                print(f"Succefully deleted note {id}" if flag==True else "No note found to delete, Check again...")
    except Exception as e:
        print("Failed to delete Note,\n",e)