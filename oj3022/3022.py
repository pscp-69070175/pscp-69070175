"""8"""
def main():
    """8"""
    temp = float(input())
    unit1 = input().strip()
    unit2 = input().strip()
    if unit1 == "C":
        c = temp
    elif unit1 == "F":
        c = (temp - 32)*5/9
    elif unit1 == "K":
        c = temp - 273.15
    else:
        c = temp *5/9 - 273.15
    if unit2 == "C":
        temp = c
    elif unit2 == "F":
        temp = c * 9 / 5 + 32
    elif unit2 == "K":
        temp = c +273.15
    else:
        temp = (c + 273.15)*9/5
    print(f"{temp:.2f}")
main()
