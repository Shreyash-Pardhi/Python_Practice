allProd=[]
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def addProd(self):
        allProd.append({"Name": self.name, "Quantity": self.quantity, "Price":self.price})
    
    def showProd(self):
        for i in allProd:
            print("---------------")
            for k,v in i.items():
                print(f"{k} = {v}")
    
    def updateProdQuantity(self,prodName:str,quan:int):
        for i in allProd:
            for _,v in i.items():
                if v==prodName:
                    i.update(Quantity = quan)
                    return
        print(f"No Product named '{prodName}' found in database...")
        
    def inventoryInfo(self):
        print(f"Total items in Inventory: {len(allProd)}")
        items = []
        Total = 0
        for i in allProd:
            items.append(list(i.values())[0])
            Total += (list(i.values())[1]) *  (list(i.values())[2])
        print(f"Items: {items}")
        print(f"Total Inventory Value: {Total}")

if __name__ == "__main__":
    while(True):
        opt = int(input("\nPress 1.Add Product  2.Update Quantity  3.Show Products  4.Inventory Analysis  0.Exit:\n"))
        match(opt):
            case 0:
                break
            case 1:
                name = input("Product name: ")
                quan = int(input("Product Quantity: "))
                price = float(input("Product Price: "))
                p = Product(name, quan, price)
                p.addProd()
                print("Product added succesfully...")
            
            case 2:
                prodName = input("Product name: ")
                q = int(input("Quantity: "))
                p.updateProdQuantity(prodName, q)
            
            case 3:
                p.showProd()
            
            case 4:
                p.inventoryInfo()