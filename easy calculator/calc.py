#creating easiest calc 
def calc(num1, num2, act):
    return eval(f"{num1} {act} {num2}")

num1 = float(input("num1: "))
num2 = float(input("num2: "))
action = input("action(* , / , + , - , **): ")

result = calc(num1, num2, action)
print("Result:",round(result))
