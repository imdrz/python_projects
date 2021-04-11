def calc():
  amt = int(input("How Many Triangular Numbers To Calculate?\n-> "))
  n = 1
  numbers = []
  for x in range(0, amt):
    one = n*(n+1)
    two = one/2
    numbers.append(int(two))
    n+=1
  print(numbers)

  yesorno = input("Do You Want To Learn What A Triangular Number Is? [Y/N] ")

  if yesorno.lower() == "y":
    print()
    print("Triangular Numbers:")
    print("Generates a list of triangular numbers. Triangular numbers are any series of numbers by continued summation, or adding, of numbers. Example: 1, 3, 6, 10. The formula to find the triangular numbers is (n*(n+1))/2, where n is the last number. You would continuesly do that for how many triangular numbers you want. 😉 ")
  else:
    print()


calc()