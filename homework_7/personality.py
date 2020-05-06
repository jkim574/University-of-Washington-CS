# please skip the following the code, and jump to main method!!!!

# Introduction to Personality Test Software
def intro():
   print("""This program processes a file of answers to the
   Keirsey Temperament Personality Sorter. It converts
   the various A and B annswers for each person into
   a sequence of B-percentages and then into a
   four-letter personality type.""")

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


# Returns percentage of B answers in the Keirsey test to determine a personality type
def percent_of_B(A_list, B_list):
   result = []
   for i in range(len(B_list)):
      percentage = int(round(float(B_list[i] / (A_list[i] + B_list[i]) * 100)))
      result.append(percentage)
   return result



def main():

   #The test has 10 groups of 7 questions with a repeating pattern in each group of 7 questions.
   #The first question in each group is an Extrovert/Introvert question (questions 1, 8, 15, 22, etc).
   #The next two questions are for Sensing/iNtuition (questions 2, 3, 9, 10, 16, 17, 23, 24, etc).
   #The next two questions are for Thinking/Feeling (questions 4, 5, 11, 12, 18, 19, 25, 26, etc).
   #And the final two questions in each group are for Judging/Perceiving (questions 6, 7, 13, 14, 20, 21, 27, 28, etc).
   #Notice that there are half as many Extrovert/Introvert questions as there are for the other three dimensions.
   #The seventy letters in the input file appear in question order (first letter for question 1, second letter for question 2, third letter for question 3, etc).

   intro()
   input_file = input("input file name? ")
   output_file = input("output file name? ")
   fo = open(input_file, 'r')
   fw = open(output_file, 'w')
   content = fo.readlines()
   names = []
   personality_test = []
   for i in range(len(content)):
      if i % 2 == 0:
         names.append(content[i].rstrip('\n'))
      else:
         personality_test.append(content[i].rstrip('\n'))
   count = 0
   while count < len(names):
      A_response = sort_answers(personality_test[count], 'A')
      B_response = sort_answers(personality_test[count], 'B')
      B_percent = percent_of_B(A_response, B_response)
      personality_type = extract_personality(B_percent)
      data = names[count] + ": " + str(B_percent) + " = " + personality_type + "\n"
      fw.write(data)
      count += 1
   fo.close()




def sort_answers(answer, char):

   list_counts = [0, 0, 0, 0]
   for i in range(10):
      if answer[i * 7].upper() == char:
         list_counts[0] += 1
      for j in range(1, 3):
         if answer[i * 7 + j].upper() == char:
            list_counts[1] += 1
      for j in range(3, 5):
         if answer[i * 7 + j].upper() == char:
            list_counts[2] += 1
      for j in range(5, 7):
         if answer[i * 7 + j].upper() == char:
            list_counts[3] += 1

   return list_counts
   #   list_counts_by_person = {}

#   for i, name in enumerate(names):
      #print(personality_test[0][1])
      #first index indicates the number of answer "A" of every first question in each 7 questions.
      #second index indicates the number of answer "A" of every second and third questions in each 7 questions.
      #third index indicates the number of answer "A" of every fourth and fifth questions in each 7 questions.
      #fourth index indicates the number of answer "A" of every six and seventh questions in each 7 questions.

      # for j in range(10):
      #    print(personality_test[i][j * 7], end='')
      #    if personality_test[i][j * 7].upper() == char:
      #       list_counts[0] += 1
      #    for k in range(1, 3):
      #       if personality_test[i][j * 7 + k].upper() == char:
      #          list_counts[1] += 1
      #    for k in range(3, 5):
      #       if personality_test[i][j * 7 + k].upper() == char:
      #          list_counts[2] += 1
      #    for k in range(5, 7):
      #       if personality_test[i][j * 7 + k].upper() == char:
      #          list_counts[3] += 1

      #this list is the number of Betty's answer with "A"
#       print()
#       print(list_counts)

#     list_counts_by_person[name] = list_counts


#    print(list_counts_by_person)




   fo.close()


if __name__ == "__main__":
    main()
