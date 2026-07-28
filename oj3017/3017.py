"""8"""
def main():
    """8"""
    price = int(input())
    service = price * 0.10
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    total = price + service
    vat = total * 0.07
    overall = total + vat
    print(f"{overall:.2f}")
main()
