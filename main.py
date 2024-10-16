def main():
    
    number = int(input("Enter an integer: "))
    binary = ""
    
    if number == 0:
        binary = "0"
        
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
        
    print(f"The binary representation is {binary}")
    
main()