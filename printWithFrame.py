def printWithFrame(s):
    topBottom = (len(s) + 9) * "|"
    print(topBottom)
    print("|||", s + "! |||")
    print(topBottom)


printWithFrame("Hello")
