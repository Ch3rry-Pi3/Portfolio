# 🧮 **Calculator Application** ✨

## Overview  
The **Calculator Application** is a simple Python program that allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division. Users can choose to continue calculations with the current result or start a new calculation. It's a fun and interactive way to practice Python programming while creating a practical tool! 🎉  

This project helps you:  
1. 🧠 Practice Python basics like functions, loops, and user input.  
2. 🛠️ Build a reusable and interactive application.  
3. ✨ Create something functional and fun to use!  

## How It Works  

1. **Choose an Operation**:  
   - Select one of the four basic arithmetic operations: `+`, `-`, `*`, `/`.  

2. **Perform Calculations**:  
   - Enter the numbers to calculate the result.  

3. **Continue or Restart**:  
   - Choose to continue calculations with the current result or start fresh with new numbers.  

## How to Run  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the program with the following command:  
   ```bash
   python calculator.py
   ```

## Example Usage  

### Program Start:  
```plaintext
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

What is the first number?: 10
+
-
*
/
Pick an operation: *
What is the next number?: 5
10.0 * 5.0 = 50.0
Type 'y' to continue calculating with 50.0, or type 'n' to start a new calculation: y
```

### Continue Calculation:  
```plaintext
+
-
*
/
Pick an operation: +
What is the next number?: 25
50.0 + 25.0 = 75.0
Type 'y' to continue calculating with 75.0, or type 'n' to start a new calculation: n
```

### Start New Calculation:  
```plaintext
What is the first number?: 20
+
-
*
/
Pick an operation: /
What is the next number?: 4
20.0 / 4.0 = 5.0
Type 'y' to continue calculating with 5.0, or type 'n' to start a new calculation: n
```

## Key Features  

1. **🔢 Basic Arithmetic**:  
   - Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).  

2. **🔄 Continuation Option**:  
   - Allows users to continue calculations with the current result.  

3. **🎨 Interactive Interface**:  
   - Displays available operations and accepts user input for an intuitive experience.  

4. **✨ Modular Design**:  
   - Uses separate functions for each operation, making the code easy to read and maintain.  

## File Details  

### `calculator.py`  
The main program file that:  
- Handles user input for numbers and operations.  
- Performs calculations using functions stored in a dictionary.  
- Allows users to continue or restart calculations.  

### `art.py`  
Contains the ASCII art logo for the program, displayed at the start. 🎨  

## Folder Structure  

Ensure the following files are in the same directory:  

```
calculator/
├── calculator.py    # The main program logic
├── art.py           # Contains the ASCII art logo
```

## Additional Notes  

- 🛠️ Modify the `operations` dictionary in `calculator.py` to add more operations like exponentiation (`**`).  
- 🎉 A great project to practice Python fundamentals and build a reusable tool!  

**🎉 Have fun calculating, and enjoy using your interactive calculator!** 🧮✨🔢  