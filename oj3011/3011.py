"""8"""
def main():
    """8"""
    co1 = input()
    co2 = input()
    colour = ("Red" , "Yellow" , "Blue")
    if (co1 in colour) and (co2 in colour) :
        if co1 == "Red" and co2 == "Blue":
            print("Violet")
        elif co1 == "Red" and co2 == "Yellow":
            print("Orange")
        elif co1 == "Yellow" and co2 == "Blue":
            print("Green")
        elif co1 == "Yellow" and co2 == "Red":
            print("Orange")
        elif co1 == "Blue" and co2 == "Yellow":
            print("Green")
        elif co1 == "Blue" and co2 == "Red":
            print("Violet")
        elif co1 == co2 :
            print(co1)
        else:
            print("Error")
    else:
        print("Error")
main()