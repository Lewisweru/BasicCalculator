# CODE CRAFTERS PRESENTATION

inpt= input("Welcome to a basic calculator Program. Choose the type of calculation you want to perform.\nSELECT \n1 for Multiplacation \n2 for Division. \n3 for Addition.\n4 for Subtraction :\n")
if inpt == "2" :
  num1=int(input("Enter the numerator :"))
  num2=int(input("Enter the denominator :"))
  def division():
    quot= num1/num2
    print(f"When you divide {num1} by {num2} you get {quot}")
  division()

