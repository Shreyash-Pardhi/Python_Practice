class My_Stack:
    stack = []
    def insert(self,ele):
        self.stack.append(ele)
        return self.stack
    
    def delete(self):
        self.stack.pop()
        return self.stack
    
    def show(self):
        i=0
        l=len(self.stack)
        for i in range(l,0,-1):
            if(i == l):
                print(self.stack[i-1],"----> top")
            else: print(self.stack[i-1])

if __name__ == '__main__':
    st = My_Stack()
    print("----Stack----")
    st.insert(10)
    st.insert(20)
    st.insert(30)
    st.insert(40)
    st.insert(50)
    st.insert(100)
    st.delete()
    st.delete()
    st.delete()
    st.show()