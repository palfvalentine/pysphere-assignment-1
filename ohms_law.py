# ohms_law.py
def main():
    print("Ohm's Law Calculator: V = I × R")
    try:
        # Get user input with validation
        current = float(input("Enter the current (in A): "))
        resistance = float(input("Enter the resistance (in ohms): "))
        
        # Calculate and display voltage
        voltage = current * resistance
        print(f"The voltage is: {voltage} volts")
        
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()