def check_squares(start, end):
    odd_squares = []
    even_squares = []
    
    for number in range(start, end + 1):
        square = number * number 
        
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
            
    print(f"Even Squares: {even_squares}")
    print(f"Odd Squares: {odd_squares}")

check_squares(int(input("Sttart: ")), int(input("End: ")))