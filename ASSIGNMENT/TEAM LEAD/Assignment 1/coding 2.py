def add(N1, N2):
    return N1 + N2
def subtract(N1, N2):
    return N1 - N2
def multiply(N1, N2):
    return N1 * N2
def divide(N1, N2):
    return N1 / N2
print("please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")
select = int(input("select operations from 1, 2, 3, 4 :"))
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("Invalid input")
