def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s



mystr = "chaman,zingurr,Bc"
print("Given String: ", mystr)


print("Reversed String: ", reverse(mystr))
