
# f = open("scores.txt", 'r')
# f1 = f.readlines()
# for i in f1:
#     print(i)



# scores = [0]*102

# #for each line in the file increment count of that score
# for line in file("scores.txt"):
#     scores[int(line)]+=1

# for i in range(len(scores)):
#     if scores[i] > 0:
#         print str(i) + ": " + "*" * scores[i]



# f = open("hours.txt")

# for line in f:
#     tokens = line.split()
#     id = tokens[0]
#     name = tokens[1]
# #    print("id is: ", id)
# #    print("name is: ", name)


# #    cumulative sum of employee's hours
#     hours = 0.0
#     days = 0
#     for token in tokens[2:]:
#         hours += float(token)
#         days += 1
#         print("hours :", hours)
#         print("days: ", days)

#     average = hours / days
#     above = 0
#     for token in tokens[2:]:
#         if float(token) > average:
#             above += 1

#     print(name, "worked for", hours, ", and the average is", average, "and", above, "days above the average")








# Introduction to Personality Test Software
def intro():
   print("""This program processes a file of answers to the
 Keirsey Temperament Personality Sorter. It converts
the various A and B answers for each person into
a sequence of B-percentages and then into a
four-letter personality type.""");



# Returns a person's personality type based on their responses
# 'X' signifies that a specific personality type for that dimension cannot be determined.
def extract_personality(B_list):
    result = ""
    #E vs I
    if B_list[0] > 50:
        result += "I"
    elif B_list[0] < 50:
        result += "E"
    else:
        result += "X"
    # S vs N
    if B_list[1] > 50:
        result += "N"
    elif B_list[1] < 50:
        result += "S"
    else:
        result += "X"
    # T vs F
    if B_list[2] > 50:
        result += "F"
    elif B_list[2] < 50:
        result += "T"
    else:
        result += "X"
    # J vs P
    if B_list[3] > 50:
        result += "P"
    elif B_list[3] < 50:
        result += "J"
    else:
        result += "X"

    return result


# Returns number of times a specific answer was recordedin each of the four categories.
def sort_answers(answers, char):
    my_list = [0, 0, 0, 0]
    for i in range(10):
        if answers[i * 7].upper() == char:
            my_list[0] += 1
        for j in range(3):
            for k in range(1, 3):
                if answers[i*7 + j*2 + k].upper() == char:
                    my_list[j+1] += 1
    return my_list


# Returns percentage of B answers in the Keirsey test to determine a personality type
def percent_of_B(A_list, B_list):
    result = []
    for i in range(len(B_list)):
        percentage = int(round(float(B_list[i] / (A_list[i] + B_list[i]) * 100)))
        result.append(percentage)
    return result





def main():
    intro()
    input_file = input("input file name? ")
    output_file = input("output file name? ")
    fo = open(input_file, 'r')
    fw = open(output_file, 'w')
    content = fo.readlines()
    names = []
    personality_test = []
    for i in range(len(content)):
        if i % 2 != 0:
            personality_test.append(content[i].rstrip('\n'))
        else:
            names.append(content[i].rstrip('\n'))
    ppl_count = 0
    while ppl_count < len(names):
        A_response = sort_answers(personality_test[ppl_count], 'A')
        B_response = sort_answers(personality_test[ppl_count], 'B')
        overall_B = percent_of_B(A_response, B_response)
        personality = extract_personality(overall_B);
        data = names[ppl_count] + ": " + str(overall_B) + " = " + personality  + "\n";
        fw.write(data);
        ppl_count+= 1;

    fo.close();





if __name__ == "__main__":
    main()
