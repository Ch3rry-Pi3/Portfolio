# ☕ **Coffee Machine (OOP Version) 🚀**  

## Overview  
This project is an **Object-Oriented Programming (OOP)** implementation of the **Coffee Machine Program**. Unlike the **procedural version**, which handled everything in a single script, this version uses classes to **modularise** the logic, making the code **more reusable, scalable, and maintainable**.  

This project helps you:  
1. 🧠 **Practice Object-Oriented Programming (OOP)** – improve your Python skills by structuring code into classes.  
2. 🏗️ **Understand Software Design** – separate concerns into different modules for clarity and reusability.  
3. ☕ **Simulate a Real-World Coffee Machine** – interact with a virtual coffee maker just like a real one!  

## 🌟 **Why OOP?** (vs. Procedural Programming)  

| **Feature**        | **Procedural Programming** ☕ | **Object-Oriented Programming (OOP)** 🚀 |
|--------------------|-----------------------------|------------------------------------------|
| **Code Structure**  | Linear, step-by-step logic. | Organised into objects with methods. |
| **Reusability**  | Limited – functions repeat in different parts of the code. | High – objects encapsulate logic for easy reuse. |
| **Scalability**  | Becomes difficult to manage as the program grows. | Easily extendable by adding new classes or modifying existing ones. |
| **Encapsulation** | Variables and functions exist independently. | Objects bundle data (attributes) and behavior (methods) together. |
| **Example**  | A single script processing orders, payments, and resources. | Separate `CoffeeMaker`, `Menu`, and `MoneyMachine` classes for cleaner code. |

In short, **OOP provides better code organisation, modularity, and reusability**, making it ideal for **complex and scalable applications** like this one! 🚀  

## 🎯 **How It Works**  

1. **Select a Drink**:  
   - Choose between **espresso**, **latte**, or **cappuccino**.  

2. **Check Resources**:  
   - The machine ensures there are enough **water, milk, and coffee** before proceeding.  

3. **Insert Coins**:  
   - Pay using **quarters, dimes, nickels, and pennies**.  
   - If you insert too much, the machine gives you **change**!  

4. **Enjoy Your Coffee**:  
   - If all conditions are met, the coffee is served. ☕  

## 📌 **How to Run**  

1. Open a terminal or command prompt. 💻  
2. Navigate to the project folder. 📂  
3. Run the program using:  
   ```bash
   python coffee_machine_oop.py
   ```  

## 📝 **Example Gameplay**  

### ✅ Ordering a Coffee:  
```plaintext
What would you like? (latte/espresso/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $7.50 in change.
Here is your latte ☕️. Enjoy!
```

### 📊 Checking Resources:  
```plaintext
What would you like? (latte/espresso/cappuccino): report
Water: 250ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

### 🚫 Not Enough Ingredients:  
```plaintext
What would you like? (latte/espresso/cappuccino): cappuccino
Sorry, there is not enough water.
```

### 🔌 Turning Off the Machine:  
```plaintext
What would you like? (latte/espresso/cappuccino): off
Shutting down the coffee machine. Have a great day! ☕️
```

## 🏗️ **Project Structure**  

This project is organised into **four classes**, each with a specific responsibility:  

### `coffee_machine_oop.py`  
- **Main program file**  
- Handles user input and coordinates other classes.  

### `menu.py`  
- **Contains drink data**  
- Stores `MenuItem` class (individual drinks).  
- Stores `Menu` class (manages all available drinks).  

### `coffee_maker.py`  
- **Manages machine resources**  
- Checks ingredient availability.  
- Deducts ingredients when a drink is made.  

### `money_machine.py`  
- **Handles payments**  
- Accepts and calculates coins.  
- Checks if the payment is sufficient and returns change if needed.  

## 📁 **Folder Structure**  

```
coffee_machine_oop/
├── coffee_machine_oop.py  # Main program logic
├── menu.py                # Manages drink menu
├── coffee_maker.py        # Handles coffee machine functionality
├── money_machine.py       # Handles money transactions
```

## 🌟 **Key Features**  

1. **☕ Three Coffee Options** – Latte, Espresso, and Cappuccino.  
2. **🔄 OOP Implementation** – Uses classes for better organisation.  
3. **💰 Realistic Coin System** – Accepts **quarters, dimes, nickels, and pennies**.  
4. **📊 Machine Reports** – Shows remaining **water, milk, coffee**, and **money earned**.  
5. **🚀 Scalable Design** – Easily extendable for new features.  

## 💡 **Additional Notes**  

- 🛠️ Modify the `Menu` class to **add more drinks** or **adjust pricing**.  
- 📊 Enhance the `CoffeeMaker` class to **add refill functionality**.  
- 🎉 Challenge yourself to **refactor the code further** or add a **GUI version**!  

**🚀 Enjoy coding and have fun with your virtual coffee machine! ☕🔥**  