try:
    # f = open('file.txt')
    # d=f.read()
    # print("'",d,"'")
    f = open('file.txt')
    d=len(f.readline())
    print(d)
    f.close()
except Exception as e:
    print("Open file in writeable format to write" if(str(e)=="not writable") else e)
        
finally:
    print("End of operations")