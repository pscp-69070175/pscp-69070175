"""8"""
def main():
    """8"""
    season = ["winter","spring","summer","fall"]
    month = int(input())
    day = int(input())
    if month in (3,6,9,12) and day>=21:
        month += 1
        if month == 13:
            month = 1
    index = (month - 1)//3
    print(season[index])
main()
