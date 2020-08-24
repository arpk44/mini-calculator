#calculator progression

while True:
  typ = {
      "Addition"
      "Multiplication"
      "Division"
      "Power"
      "Subtraction"
      }
  
  choice = input("What would you like to do Addition/Multiplication/Division/Subtraction/Power?")
  if choice == "Addition":
      um = int(input("Enter one number ").strip())
      num = int(input("Enter another number: ").strip())
      answer = um + num
      print(answer)
  elif choice == "Multiplication":
      mu = int(input("Enter one number ").strip())
      mul = int(input("What is your second number? ").strip())
      answer = mu * mul
      print(answer)
  elif choice == "Division":
      div = int(input("Enter your number ").strip())
      divi = int(input("Enter your 2nd Number ").strip())
      answer = div / divi
      print(answer)
  elif choice == "Power":
      div = int(input("Enter your number ").strip())
      divi = int(input("Enter your 2nd Number ").strip())
      answer = div ** divi
      print(answer)
  elif choice == "Subtraction":
      div = int(input("Enter your number ").strip())
      divi = int(input("Enter your 2nd Number ").strip())
      answer = div - divi
      print(answer)
  else:
      print("You entered wrong value")
