# direct loop solution for fizzbuzz
# re: python 'boot camp'

for x in range(1, 101):
  if x % 15 == 0:
    message = "fizzbuzz"
  else:
    if x % 3 == 0:
      message = "fizz"
    elif x % 5 == 0:
      message = "buzz"
    else:
      message = ""
  print(x, message)
