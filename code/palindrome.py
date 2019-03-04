
def ispalindrome(string):
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - 1- i]:
            return False
    return True
