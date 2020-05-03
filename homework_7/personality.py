# please skip the following the code, and jump to main method!!!!

# Introduction to Personality Test Software
def intro():
   print("""This program processes a file of answers to the
 Keirsey Temperament Personality Sorter. It converts
the various A and B answers for each person into
a sequence of B-percentages and then into a
four-letter personality type.""");

# # Returns a person's personality type based on their responses
# # 'X' signifies that a specific personality type for that dimension cannot be determined.
# def extract_personality(B_list):
#     result = ""
#     #E vs I
#     if B_list[0] > 50:
#         result += "I"
#     elif B_list[0] < 50:
#         result += "E"
#     else:
#         result += "X"
#     # S vs N
#     if B_list[1] > 50:
#         result += "N"
#     elif B_list[1] < 50:
#         result += "S"
#     else:
#         result += "X"
#     # T vs F
#     if B_list[2] > 50:
#         result += "F"
#     elif B_list[2] < 50:
#         result += "T"
#     else:
#         result += "X"
#     # J vs P
#     if B_list[3] > 50:
#         result += "P"
#     elif B_list[3] < 50:
#         result += "J"
#     else:
#         result += "X"

#     return result


# # Returns percentage of B answers in the Keirsey test to determine a personality type
# def percent_of_B(A_list, B_list):
#     result = []
#     for i in range(len(B_list)):
#         percentage = int(round(float(B_list[i] / (A_list[i] + B_list[i]) * 100)))
#         result.append(percentage)
#     return result


def main():

   #The test has 10 groups of 7 questions with a repeating pattern in each group of 7 questions.
   #The first question in each group is an Extrovert/Introvert question (questions 1, 8, 15, 22, etc).
   #The next two questions are for Sensing/iNtuition (questions 2, 3, 9, 10, 16, 17, 23, 24, etc).
   #The next two questions are for Thinking/Feeling (questions 4, 5, 11, 12, 18, 19, 25, 26, etc).
   #And the final two questions in each group are for Judging/Perceiving (questions 6, 7, 13, 14, 20, 21, 27, 28, etc).
   # Notice that there are half as many Extrovert/Introvert questions as there are for the other three dimensions.
   #The seventy letters in the input file appear in question order (first letter for question 1, second letter for question 2, third letter for question 3, etc).

   intro()
   input_file = input("input file name? ")
 #  output_file = input("output file name? ")
   fo = open(input_file, 'r')
 #  fw = open(output_file, 'w')
   content = fo.readlines()
   names = []
   personality_test = []
   print(range(len(content)))
   for i in range(len(content)):
        if i % 2 == 0:
            names.append(content[i].rstrip('\n'))
        else:
            personality_test.append(content[i].rstrip('\n'))
   print(names)
   print(personality_test)
   print(personality_test[0])

   list_counts_by_person = {}

   # for example, below code indicates the number of Betty's answers with "A" in each groups of 7 questions.
   # As you count the number of "A", you add the number to the list.

   #Betty Boop's answer:
   #BABAAAA / BAAAAAA / ABAAAAB / BAAAAAA / BAAAABA / BAABAAA / BABABAA / BAAAAAA / BAAAAAA / BAAAAAA

   #1234567 (number)
   #BABAAAA
   #BAAAAAA
   #ABAAAAB
   #BAAAAAA
   #BAAAABA
   #BAABAAA
   #BABABAA
   #BAAAAAA
   #BAAAAAA
   #BAAAAAA

   for i, name in enumerate(names):
      #print(personality_test[0][1])
      #first index indicates the number of answer "A" of every first question in each 7 questions.
      #second index indicates the number of answer "A" of every second and third questions in each 7 questions.
      #third index indicates the number of answer "A" of every fourth and fifth questions in each 7 questions.
      #fourth index indicates the number of answer "A" of every six and seventh questions in each 7 questions.
      list_counts = [0, 0, 0, 0]

      for j in range(10):
         print(personality_test[i][j * 7], end='')
         if personality_test[i][j * 7].upper() == 'A':
            list_counts[0] += 1
         for k in range(1, 3):
            if personality_test[i][j * 7 + k].upper() == 'A':
               list_counts[1] += 1
         for k in range(3, 5):
            if personality_test[i][j * 7 + k].upper() == 'A':
               list_counts[2] += 1
         for k in range(5, 7):
            if personality_test[i][j * 7 + k].upper() == 'A':
               list_counts[3] += 1

      #this list is the number of Betty's answer with "A"
      print()
      print(list_counts)

      list_counts_by_person[name] = list_counts

   #In conclusion, even though I managed to write code of Betty's, but how am I supposed to find other's record?
   #I could just write down code like above for each person, but don't know how to write that in short?

   print(list_counts_by_person)

   fo.close()


if __name__ == "__main__":
    main()
