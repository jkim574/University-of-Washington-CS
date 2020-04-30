#from drawingpanel import*


starting_year = 1880
num_decades = 14
width_dacades = 70


#if __name__ == "__main__":
 #   for names in files("")
#    panel = DrawingPanel(num_decades * width_dacades, 550)


def user_intro():
    print("This program alalows you to search through the")
    print("data from the Social Security Administration")
    print("to see how popular a particular name has been")
    print("since the", starting_year, "'s.")
    print()


# method to prompt the user to search for a name, and return the line matching
# the requested name in the names database
def search():
    textf = open("names.txt", 'r')

    name = []
    gender = []
    for line in textf:
        words = line.split()
        name.append(words[0])
        gender.append(words[1])
#    print(name)
#    print(gender)

    user_name_input = input("name? ")
    user_sex_input = input("sex (M or F)? ")
    search_string = user_name_input.upper() , " " , user_sex_input.upper()

    print(search_string)
    if user_name_input and user_sex_input in name or gender:
        print("true")
    else:
        print("your name is not in the list")

    textf.close()

#panel.mainloop()
search()
