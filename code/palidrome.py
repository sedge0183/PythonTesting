
def ispalindrome(string):
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - 1- i]:
            return False
    return True

def main():
    lst = ["hello", "world", "racecar", "test", "w", "civic", "redder"]
    for word in lst:
        print("{}: {}".format(word, ispalindrome(word)))

if __name__ == "__main__":
    main()