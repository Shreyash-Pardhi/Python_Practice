class open_file:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(exc_type)
        self.file.close()

with open_file('file.txt','r') as f:
    print(f.read())
    print("File closing status inside context manager: ",f.closed)

print("File closing status after context manager: ",f.closed)