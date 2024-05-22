import calculatorOperations as co
if __name__ == "__main__":
    def options():
        while(True):
            opt = int(input("\npress, 1.Addition, 2.Subtraction, 3.Multiplication, 4.Division, 5.Power, 0.Exit:\n"))
            match opt:
                case 0:
                    print("Total: ",co.ans)
                    return True
                case 1:
                    print(co.add())
                case 2:
                    print(co.sub())
                case 3:
                    print(co.mul())
                case 4:
                    print(co.div())
                case 5:
                    print(co.power())
                case default:
                    print("Please select Correct Option...")
    
    options()