# pysphere-assignment-1 - Prince Kwadwo Aduboffuor
 # Ohm's Law Calculator

This script calculates voltage using Ohm's Law (V = I × R).

## Usage
1. Ensure Python 3.x is installed
2. Run the script:
   ```bash
   python ohms_law.py

3. Enter values when prompted:
Current in Amperes (A)
Resistance in Ohms (Ω)

## Example

python ohms_law.py
Ohm's Law Calculator: V = I × R
Enter the current (in A): 4
Enter the resistance (in ohms): 15
The voltage is: 60.0 volts

## Key Features

1. **Input Validation**:
   - Uses `try/except` to handle non-numeric inputs
   - Converts inputs to floats for decimal support

2. **User Experience**:
   - Clear prompts with measurement units
   - Descriptive error messages
   - Friendly calculator introduction

3. **Error Handling**:
   - Catches `ValueError` for invalid inputs
   - Prevents program crashes on bad data

4. **Documentation**:
   - README provides setup and usage instructions
   - Includes execution example
   - Lists key features

To use this:
1. Save the Python code in `ohms_law.py`
2. Save the documentation in `README.md`
3. Run with `python ohms_law.py`