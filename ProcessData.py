#ProcessData.py
#Name: Grant Schaeffer
#Date: 10/2/25
#Assignment: Lab8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  line = inFile.readline()
  for line in inFile:
    data = line.split()
    First = data[0]
    Last = data[1]
    IDNumber = data[3]
    MajorYear = get_majoryear(data)
    student_id = make_ID(First, Last, IDNumber)
    output = Last + "," + First + "," + student_id + "," + MajorYear + "\n"
    outFile.write(output)
    #print(student_id)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def make_ID(First, Last, IDNumber):
  #print(First, Last, IDNumber)
  id_len = len(IDNumber)
  id = First[0] + Last + IDNumber[id_len - 3: ]

  while len(Last) < 5:
    Last = Last + "X"

  #print(id)
  return(id)

def get_majoryear(data):
  class_options = ["Freshman", "Sophmore", "Junior", "Senior"]
  class_index = -1
  for i in range(len(data)):
    if data[i] in class_options:
      class_index = i
      break
  Major = ""
  if class_index != -1:
    Major_words = data[class_index + 1:]
    Major = " ".join(Major_words)
  Major_short = Major[:3]
  class_name = data[class_index]
  if class_name == "Freshman":
       Year = "FR"
  elif class_name == "Sophomore":
    Year = "SO"
  elif class_name == "Junior":
    Year = "JR"
  elif class_name == "Senior":
      Year = "SR"
  else:
      Year = ""
  MajorYear = Major_short + "-" + Year
  return MajorYear

if __name__ == '__main__':
  main()
