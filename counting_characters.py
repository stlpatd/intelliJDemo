alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def letterLst(myList):
    #mylist = myList.lower()
    letTable = {}
    for let in (alphabet):
        if let in (myList):
            letOccur = 0
            letOccur = myList.count(let)
            letTable[let] = letOccur
    for x in sorted(letTable):
         print(x,letTable.get(x))
    return

(letterLst("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc"+
" accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Prae"+
"sent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus"+
", non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat"+
" eget massa. Donec nec velit non ligula efficitur luctus."))
