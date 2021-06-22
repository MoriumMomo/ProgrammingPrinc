import random 

# Function to ask question and check if answer is correct or not

def ask_question(minimum,maximum):
  
 #Get 2 random integers in given range
  
  first = random.randint(minimum,maximum) 
  second = random.randint(minimum,maximum)

  # Get the sign 1 for + and 2 for -
  
  sign = random.randint(1,2)

  # + sign condition
  
  if(sign == 1):
    print("What is %d+%d? "%(first,second))
    answer=int(input())
    if(answer == (first+second)):
      print("Correct!")
      return True
    else: 
      print("Incorrect! Correct answer is %d"%((first+second)))
      return False
  else: 
    # - sign condition
    print("What is %d-%d? "%(first,second))
    answer=int(input())
    if(answer == (first-second)):
      print("Correct!")
      return True
    else: 
      print("Incorrect! Correct answer is %d"%((first-second)))
      return False  

## Welcome message for the quiz

print("Welcome to Maths Tester Pro.\n")
print("Select  a difficulty:\n")
print("1) Easy\n2) Medium\n3) Hard\n")

score=0

# Keep on asking for correct choice until its incorrect

while True:
  choice=input()
  if(choice == '1' or choice == '2' or choice =='3'):
    break
  print("Invalid choice! Enter 1,2 or 3.\n")

if(int(choice) == 1):
  lives = 3
  max_mum = 10
  question = 5
  print("Easy mode selected\n")
elif(int(choice) ==2):
  lives = 2
  max_mum = 25
  question = 10
  print("Medium mode selected\n")
elif(int(choice) ==3): 
  lives = 1
  max_mum = 50
  question = 15
  print("Hard mode selected\n")

# Ask given number of questions

for i in range(1,question+1):
  print("\nQuestion %d of %d. %d lives remaining\n"%(i,question,lives))

  if(i!=question):
    return_value = ask_question(1,max_mum)
  else:
    print("Challenge question!\n")
    return_value = ask_question(max_mum,max_mum*2)
  
  if(return_value):
    score = score+1
  else:
    lives = lives-1

#when no more lives left

  if(lives==0):
    print("Out of lives, game over!\n")
    break

print("Test complete\n")
percentage_score =(score/question)*100

#Show final result

print("You scored %d/%d (%.2f%%).\n"%(score,question,percentage_score))
if(percentage_score>=50):
  print("You passed!")
else:
  print("You failed!")
