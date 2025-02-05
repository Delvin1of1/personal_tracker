def multiplication_table():
 try:
    number = int(input("Enter a number here: "))
    print(f"Multiplication table for {number}")

    for i in  int(input(range("input a number"))):
        result = number * i
        
        print(f"{number} x {i} = {result}")

 except ValueError:
    print("Invalid Input! Please enter a valid number.")

    # else:
    #     result = "Invalid Input!"

#calling multiplication table
multiplication_table()

