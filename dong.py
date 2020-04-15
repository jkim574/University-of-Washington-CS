#University of Washington CS142 1st assignment

def lastLine():
    print("I don't know why she swallowed that fly,\nPerhaps she'll die.\n")
    # emptyPrintln()

# def emptyPrintln():
#     print()


def firstVerse():
    fly()
    lastLine()


def secondVerse():
    spider()
    swallowSpider()
    lastLine()


def thridVerse():
    bird()
    swallowBird()
    lastLine()


def fourthVerse():
    cat()
    swallowCat()
    lastLine()


def fifthVerse():
    dog()
    swallowDog()
    lastLine()


def sixthVerse():
    hedgehog()
    swallowHedgehog()
    lastLine()




def fly():
    print("There was an old woman who swallowed a fly.")

def spider():
    print("There was an old woman who swallowed a spider,")
    print("That wriggled and iggled and jiggled inside her.")

def swallowSpider():
    print("She swallowed the spider to catch the fly,")

def bird():
    print("There was an old woman who swallowed a bird,")
    print("How absured to swallow a bird.")

def swallowBird():
    print("She swallowed the bird to catch the spider,")
    swallowSpider()

def cat():
    print("There was an old woman who swallowed a cat,")
    print("Imagine that to swallow a cat.")

def swallowCat():
    print("She swallowed the cat to catch the bird,")
    swallowBird()

def dog():
    print("There was an old woman who swallowed a dog,")
    print("What a hog to swallow a dog.")

def swallowDog():
    print("She swallowed the dog to catch the cat,")
    swallowCat()

def hedgehog():
    print("There was an old woman who swallowed a hedgehog,")
    print("How cruel it is to swallow a hedgehog.")

def swallowHedgehog():
    print("She swallowed the hedgehog to catch the dog.")
    swallowDog()

def horse():
    print("There was an old woman who swallowed a horse,")
    print("She died of course.")

if __name__ == "__main__":
    firstVerse()
    secondVerse()
    thridVerse()
    fourthVerse()
    fifthVerse()
    sixthVerse()
    horse()
