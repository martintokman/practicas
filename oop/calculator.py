#Create a calculator with basic functionalities such as addition, 
#subtraction, multiplication and division, using classes to represent operations.

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        self.result = 0
        self.equation = ""
        self.pending_operations_list = []    
        
    def current_result(self):
        print(f"Current result {self.result}")
    
    def current_equation(self):
        print(f"Current equation {self.equation}")



class sum(Calculator):
    def __init__(self, number1, number2):
        super().__init__(number1, number2)
        self.result = f"{number1}+{number2}= {number1 + number2}"
        

class subtract(Calculator):
    def __init__(self, number1, number2):
        super().__init__(number1, number2)
        self.result = f"{number1} - {number2} = {number1 - number2}"


class multiply(Calculator):
    def __init__(self, number1, number2):
        super().__init__(number1, number2)
        self.result = f"{number1} * {number2} = {number1 * number2}"
        

class divide(Calculator):
    def __init__(self, number1, number2):
        super().__init__(number1, number2)
        self.result = f"{number1} / {number2} = {number1 / number2}"
        


print("Welcome to the calculator")

while True:
    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))
    operation = input("Operation: ")

    if operation == "+":
        sum_var = sum(number1, number2)
        sum_var.current_result()
        #sum.current_equation()
        

    elif operation == "-":
        subtract_var = subtract(number1, number2)
        subtract_var.current_result()
        #subtract.current_equation()
        

    elif operation == "*":
        multiply_var = multiply(number1, number2)
        multiply_var.current_result()
        #multiply.current_equation()
        

    elif operation == "/":
        divide_var = divide(number1, number2)
        divide_var.current_result()
        #divide.current_equation()
        

    else:
        print("Invalid operation")

























"""
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")

nombre = input("Nombre: ")
edad = input("Edad: ")
grado = input("Grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"Name: {estudiante.nombre}")"""