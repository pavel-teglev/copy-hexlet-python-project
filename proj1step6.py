from random import randint, choice
import prompt

main_question = 'What is the result of the expression?'


def colculation():
  first_operand = randint(0, 100)
  second_operand = randint(0, 100)
  operator = choice(['*', '-', '+'])
  condtions = f'{first_operand} {operator} {second_operand}'
  if operator == '*':
    result = first_operand * second_operand
  elif operator == '-':
    result = first_operand - second_operand
  elif operator == '+':
    result = first_operand + second_operand
  return [condtions, result]
    

game_function = colculation()


def game_engine1(main_question, game_function):
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name? ')
  print(f'Hello, {name}')
  print(main_question)
  trys_count = 3
  while trys_count > 0:
    game = game_function
    question = game[0]
    correct_answer = game[1]
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if int(answer) == correct_answer:
      print('Correct!')
      trys_count -= 1
    elif int(answer) != correct_answer:
      print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}" \nLet\'s try again, {name}!')
  print(f'Congratulations, {name}!')

#game_engine1(main_question, game_function)

def game_engine2():
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name? ')
  print(f'Hello, {name}')
  print(main_question)
  trys_count = 3
  while trys_count > 0:
    game = colculation()
    question = game[0]
    correct_answer = game[1]
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if int(answer) == correct_answer:
      print('Correct!')
      trys_count -= 1
    elif int(answer) != correct_answer:
      print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}" \nLet\'s try again, {name}!')
  print(f'Congratulations, {name}!')

game_engine2()
