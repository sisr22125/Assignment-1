#Python quiz game
# Get the username before the quiz starts
print("Hello welcome to my quiz! Would you like to start?")
start_quiz = input("Enter yes or no: ").lower()

if start_quiz == "yes":
  while True:
    username = input("Please enter your name: ")
    if any(char.isdigit() or char in "!@#$%^&*()_+-={}[]|:;'<>,.?/" for char in username):
      print("You cannot use that name. Please enter a valid name.")
    else:
      print(f"Welcome {username}!")
      break

  questions = ("First question:What was the purpose of the movie cousins?: ",
               "Your second question:What was the name of the main character in the movie cousins?: ",
               "Nearly there:Where was this movie mainly filmed in?: ",
               "2nd to last question:When was this movie made?: ",
               "Yay and last question:Who was this story made about?: ")

  options = [("A.To show how māori live their life ", "B. To tell the story of how children were brought up", "C.To show the world how some people's lives are",),
             ("A.Missy ", "B.Mata", "C.Keita",),
             ("A.Taupo,Wairarapa ", "B.Auckland,Dunedin", "C. Rotorua,Wellington",),
             ("A.2018-2020 ", "B.2020-2021 ", "C.2021-2022",),
             ("A.Rachel house ", "B.Tanea heke ", "C.Patricia grace",)]

  answers = ("B", "A", "C", "B", "C")
  guesses = []
  score = 0
  question_num = 0


  for question in questions:
      print("----------------------")
      print(question)
      for option in options[question_num]:
          print(option) 
      guess = input("Enter (A, B, C): ").upper()
      guesses.append(guess)
      if guess == answers[question_num]:
          score += 1
          print("Yes you are correct!")
      else:
          print("Sorry you are wrong!")
          print(f"{answers[question_num]} is the correct answer")
      question_num += 1


  print("----------------------")
  print("       RESULTS        ")
  print("----------------------")

  # Display the username in the results section
  print(f"Thank you, {username}!")

  print("answers: ", end="")
  for answer in answers:
      print(answer, end=" ")
  print()

  print("guesses: ", end="")
  for guess in guesses:
      print(guess, end=" ")
  print()

  score = int(score / len(questions) * 100)
  print(f"You got: {score}%!")

  print("Thanks for doing my quiz!")
elif start_quiz == "no":
  print("Ok, do you want to start now?")
  start_quiz = input("Enter yes or no: ").lower()
  if start_quiz == "yes":
    while True:
      username = input("Please enter your name: ")
      if any(char.isdigit() or char in "!@#$%^&*()_+-={}[]|:;'<>,.?/" for char in username):
        print("You cannot use that name. Please enter a valid name.")
      else:
        print(f"Hello {username}!")
        break

    questions = ("What was the purpose of the movie cousins?: ",
                 "What was the name of the main character in the movie cousins?: ",
                 "Where was this movie mainly filmed in?: ",
                 "When was this movie made?: ",
                 "Who was this story made about?: ")

    options = [("A.To show how māori live their life ", "B. To tell the story of how children were brought up", "C.To show the world how some people's lives are",),
               ("A.Missy ", "B.Mata", "C.Keita",),
               ("A.Taupo,Wairarapa ", "B.Auckland,Dunedin", "C. Rotorua,Wellington",),
               ("A.2018-2020 ", "B.2020-2021 ", "C.2021-2022",),
               ("A.Rachel house ", "B.Tanea heke ", "C.Patricia grace",)]

    answers = ("B", "A", "C", "B", "C")
    guesses = []
    score = 0
    question_num = 0


    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option) 
        guess = input("Enter (A, B, C): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1


    print("----------------------")
    print("       RESULTS        ")
    print("----------------------")

    # Display the username in the results section
    print(f"Thank you, {username}!")

    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"You got: {score}%!")

    print("Thanks for doing my quiz!")
  else:
    print("Ok, come back later!")
