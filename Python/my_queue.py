class My_queue:
    queue =[]
    def insert(self, ele):
        self.queue.append(ele)
    
    def delete(self):
        self.queue.pop(0)
    
    def show(self):    
        print(self.queue)
    
if __name__=='__main__':
    q = My_queue()
    q.insert(10)
    q.show()
    q.insert(20)
    q.show()
    q.insert(40)
    q.show()
    q.delete()
    q.show()
    q.insert(100)
    q.show()
    q.delete()
    q.show()