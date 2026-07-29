"""8"""
def main():
    """8"""
    total = float(input())
    high = float(input())
    low = (total - high) - high
    if low < 0:
        low = 0
    diff = high - low
    if diff > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
