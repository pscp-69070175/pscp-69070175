"""8"""
def main():
    """flower"""
    L, N = map(int, input().split())
    planted = 0
    strip = 0

    while planted < N:
        strip += 1
        cells = L * (2 * L * strip - L + 1) // 2
        planted += cells

    print(strip)
main()
