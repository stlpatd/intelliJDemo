#import math

def analyze_text(text):
    position = 0
    numAlph = 0

    while position < len(text):
        newString = text.lower()
        stringChar = text[position]
        eOccur = newString.count("e")
        if stringChar.isalpha():
            numAlph = numAlph +1
        position = int(position) + 1
    percentE = str(eOccur/numAlph*100)
    print percentE
    return ("The text contains " + str(numAlph) + " alphabetic characters, " +
        "of which " +  str(eOccur) + " (" + str(percentE) + "%) are 'e'.")

print(analyze_text("Blueberries are tasteee!"))

# Don't copy these tests into Vocareum
# from test import testEqual
#
# text1 = "Eeeee"
# answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
# testEqual(analyze_text(text1), answer1)
#
# text2 = "Blueberries are tasteee!"
# answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
# testEqual(analyze_text(text2), answer2)
#
# text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
# answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
# testEqual(analyze_text(text3), answer3)
