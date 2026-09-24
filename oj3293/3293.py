"""8"""
def main():
    """frame"""
    longest = ""
    allword = []
    for _ in range (5):
        word = input().strip()
        if len(word) > len(longest):
            longest = word
        allword.append(word)

    max_len = len(longest)
    width = max_len + 4
    print("*" * width)
    for i in allword:
        space = " " * (max_len - len(i))
        print("*" + " " + i + space + " " + "*")
    print("*" * width)
main()
