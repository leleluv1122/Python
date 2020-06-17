def main():
    try:
        number1, number2 = eval(
            input("Enter two numbers, separated by a comma: "))
        result = number1 / number2
        print("Result is " + str(result))

    except ZeroDivisionError:
        print("Dicision by zero!") # 2,0
    except SyntaxError:
        print("A comma may be missing in the input") # 3 2
    except:
        print("Something wrong in the input")
    else:
        print("No exceptions")
    finally:
        print("The finally clause is executed")

main()