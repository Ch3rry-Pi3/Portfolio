# 🔑 **Caesar Cipher Program** 🛡️

## Overview  
The **Caesar Cipher Program** is a Python implementation of the classic encryption technique attributed to Julius Caesar. This program allows you to **encrypt** or **decrypt** messages by shifting the letters of the alphabet. It’s simple, fun, and secure for lightweight cryptography!

This project helps you:
1. 🧠 Practice Python programming with loops, conditionals, and modular functions.  
2. ✨ Build a fully interactive command-line tool.  
3. 📜 Learn about historical cryptography and its principles.

## How It Works  

1. **Encrypt a Message**:  
   - Shift each letter in your message forward by a specified number of places in the alphabet.  

2. **Decrypt a Message**:  
   - Reverse the process by shifting each letter backward using the same shift number.  

3. **Interactive Design**:  
   - The program keeps running until you choose to exit, allowing for repeated use.  

## How to Run  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the program with the following command:  
   ```bash
   python main.py
   ```

## Example Usage  

### Encryption  
**Input**:  
```plaintext
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
```

**Output**:  
```plaintext
Here is the encoded result: mjqqt btwqi
```

### Decryption  
**Input**:  
```plaintext
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt btwqi
Type the shift number:
5
```

**Output**:  
```plaintext
Here is the decoded result: hello world
```

## Key Features  

1. **🔄 Bidirectional Operation**:  
   - Encrypt (`encode`) or decrypt (`decode`) any message.  

2. **⚡ Smart Shift Handling**:  
   - Wraps around the alphabet seamlessly, ensuring accurate results for both encoding and decoding.  

3. **🎨 Modular Design**:  
   - Uses a clean and reusable function for Caesar cipher operations.  

4. **🚀 Continuous Interaction**:  
   - Allows repeated encryption or decryption until the user chooses to exit.  

5. **🔤 Handles Non-Alphabet Characters**:  
   - Leaves spaces, numbers, and symbols untouched for readability.  

## Behind the Scenes  

### `caesar_cipher.py`  
The core program that:
- Accepts user input for the operation (`encode` or `decode`), message, and shift amount.  
- Passes this data to the `caesar()` function for processing.  
- Handles the loop to allow users to restart or exit the program.  

### `art.py`  
Contains the ASCII art logo for the program, displayed at startup. 🎨  

## Folder Structure  

Ensure the following files are in the same directory:  

```
8. caesar_cipher/
├── caesar_cipher.py    # The main program logic
├── art.py              # Contains the ASCII art logo
```

## Additional Notes  

- 🛠️ Modify the `alphabet` list in `main.py` to add more characters or customise it for different languages.  
- 🔧 You can use this program to create secret codes or decrypt hidden messages with friends!  
- 🎉 A great project to practice Python fundamentals while building something fun and practical!  

**✨ Have fun encrypting and decrypting messages, and enjoy your cryptography journey!** 🛡️📜🔐 