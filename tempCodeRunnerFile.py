import random
import time

first_num = 3
second_num = 12
OPERATOR = ["+", "-","*"]
problems = 5
def generate():
  left = random.randint(first_num, second_num)
  right = random.randint(first_num,second_num)
  operator = random.choice(OPERATOR)

  expresion = str(left) + " " + operator + " " + str(right)
  answer = eval(expresion)
  return expresion, answer
start_time = time.time()
wrong = 0
input("Press enter to begin")
print("-------------")
for i in range(problems):
    expr, answer = generate()
    while True:
     guess = input("Problem #" + str(i+1)+ ": " + expr + " = " )
     if guess == str(answer):
         break
     wrong += 1
     

end_time = time.time()
finish_time = round(end_time - start_time, 2)
print("-------------") 
print("You got " + str(wrong) + " questions wrongly!")
print("Nice work! You took " + str(finish_time) + " seconds!")    
     