print("kalkulator perbandingan")

number1 = int(input("masukkan angka pertama"))
number2 = int(input("masukkan angka kedua"))

Equal = number1 == number2
notEqual = number1 != number2
greaterThan = number1 > number2
lessThan = number1 < number2
greaterEqual = number1 >= number2
lessEqual = number1 <= number2

print(f"{number1} == {number2} : {Equal}")
print(f"{number1} != {number2} : {notEqual}")
print(f"{number1} > {number2} : {greaterThan}")
print(f"{number1} < {number2} : {lessThan}")
print(f"{number1} >= {number2} : {greaterEqual}")
print(f"{number1} <= {number2} : {lessEqual}")
