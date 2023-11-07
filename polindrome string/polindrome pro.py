def polindrome(x:str):
    symbols = ["-", "~","!","%","^","*"]
    x = x.lower()
    for i in symbols:
        x = x.replace(i,"")
    
    return x == x[::-1]

print(polindrome("ka-yak!"))