def polindrome(x:str) -> str:
    x = x.lower()
    return x == x[::-1]


print(polindrome("Kayak"))