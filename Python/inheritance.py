##Single inheritance##
# class Emp:
#     def __init__(self,eid, ename):
#         self.eid = eid
#         self.ename = ename
    
#     def printEmpData(self):
#         print(f"Eid: {self.eid}\nName: {self.ename}")

# class Org(Emp):
#     def __init__(self, eid, ename,org):
#         super().__init__(eid, ename)
#         self.org = org
        
#     def printOrgName(self):
#         print(f"Organization: {self.org}")

# if __name__ == '__main__':
#    org = Org('101', 'Shreyash','Delaplex')
#    org.printEmpData()
#    org.printOrgName()



##Multiple Inheritance##
# class Parent1:
#     a = 10
#     def show1(self):
#         print(f'Parent1 variable (a):{self.a}')

# class Parent2:
#     b = 20
#     def show2(self):
#         print(f'parent2 variable (b):{self.b}')

# class Child(Parent1, Parent2):
#     def show3(self):
#         print(f'In child (a+b): {self.a + self.b}')

# if __name__ == '__main__':
#     child = Child()
#     child.show1()
#     child.show2()
#     child.show3()



##Multi-level Inheritance##
# class grandFather:
#     def grandFatherFeatures(self):
#         print("GrandFather's Features")

# class father(grandFather):
#     def fatherFeatures(self):
#         print("Father's Features")

# class son(father):
#     def sonFeatures(self):
#         print("Son's Features")

# if __name__ =='__main__':
#     s = son()
#     s.grandFatherFeatures()
#     s.fatherFeatures()
#     s.sonFeatures()



##Hierarchical Inheritance
class Parent:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Child1(Parent):
    def add(self):
        print(f"addition: {self.x + self.y}")

class Child2(Parent):
    def sub(self):
        print(f"subtraction: {self.x - self.y}")

class Child3(Parent):
    def mul(self):
        print(f"multiplication: {self.x * self.y}")

if __name__ == '__main__':
    c1 = Child1(10,20)
    c1.add()
    
    c2 = Child2(20,5)
    c2.sub()
    
    c3 = Child3(2,5)
    c3.mul()
    

##Hibrid##
#combination of multiple types of inheritance listed above