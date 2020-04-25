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
    file = open("names.txt", 'r')

    name = []
    gender = []
    for line in file:
        words = line.split()
        name.append(words[0])
        gender.append(words[1])


    user_name_input = input("name? ")
    user_sex_input = input("sex (M or F)? ")
    search_string = user_name_input.upper() , " " , user_sex_input.upper()

    print(search_string)
    # if user_name_input and user_sex_input in name or gender:
    #     print("true")
    # else:
    #     print("your name is not in the list")



#panel.mainloop()
search()










# def search_string_in_file(file_name, string_to_search):
#     """Search for the given string in file and return lines containing that string,
#     along with line numbers"""
#     line_number = 0
#     list_of_results = []
#     # Open the file in read only mode
#     with open(file_name, 'r') as read_obj:
#         # Read all lines in the file one by one
#         for line in read_obj:
#             # For each line, check if line contains the string
#             line_number = line_number + words
#             line_number += 1
#             if string_to_search in line:
#                 # If yes, then add the line number & line as a tuple in the list
#                 list_of_results.append((line_number, line.rstrip()))

#     # Return list of tuples containing line numbers and lines where string is found
#     return list_of_results

# def SearchStudent(ID):
#     with open("Students.txt", 'r') as file:
#         for i in file:
#             data = i.rstrip().split(",")
#             if data[0] == ID:
#                 return "The student you require is: {} {}".format(data[2], data[1])

#     return "No matches found"
# search = input("Please enter a student ID: ")
# print(SearchStudent(search))

# def extract_data(filename):
#     infile = open(filename, 'r')
#     infile.readline() # skip the first line
#     months = []
#     rainfall = []
#     for line in infile:
#         words = line.split()
#         # words[0]: month, words[1]: rainfall
#         months.append(words[0])
#         rainfall.append(float(words[1]))
#     infile.close()
#     months = months[:-1]      # Drop the "Year" entry
#     annual_avg = rainfall[-1] # Store the annual average
#     rainfall = rainfall[:-1]  # Redefine to contain monthly data
#     return months, rainfall, annual_avg

# months, values, avg = extract_data('rainfall.dat')
# print 'The average rainfall for the months:'
# for month, value in zip(months, values):
#     print month, value
# print 'The average rainfall for the year:', avg
