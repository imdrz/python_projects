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


calc()