


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
   intro()
   input_file = input("input file name? ")
 #  output_file = input("output file name? ")
   fo = open(input_file, 'r')
 #  fw = open(output_file, 'w')
   content = fo.readlines()
   names = []
   personality_test = []
   for i in range(len(content)):
        if i % 2 == 0:
            names.append(content[i].rstrip('\n'))
        else:
            personality_test.append(content[i].rstrip('\n'))
   print(names)
   print(personality_test)
   print(personality_test[0])
   print(personality_test[0][1])
   list_counts = [0, 0, 0, 0]
   for j in range(10):
 #     print(personality_test[0][j * 7])
      if personality_test[0][j * 7].upper() == 'A':
         list_counts[0] += 1
      for k in range(1, 3):
         if personality_test[0][j * 7 + k].upper() == 'A':
            list_counts[1] += 1
      for k in range(3, 5):
         if personality_test[0][j * 7 + k].upper() == 'A':
            list_counts[2] += 1
      for k in range(5, 7):
         if personality_test[0][j * 7 + k].upper() == 'A':
            list_counts[3] += 1
   print(list_counts)

   fo.close()





if __name__ == "__main__":
    main()
