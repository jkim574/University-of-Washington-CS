def top():
    print("    _____")
    print("   /     \\")
    print("  /       \\")

def bottom():
    print("  \\       /")
    print("   \\_____/")

def line():
    print("+--------+")

def egg():
    top()
    bottom()
    print("")

def cup():
    bottom()
    line()
    print("")

def stop():
    top()
    print("  |  Stop  |")
    bottom()
    print("")

def hat():
    top()
    line()


#main
egg()
cup()
stop()
hat()
