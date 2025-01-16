# ☕ **Coffee Machine Program** 🚀  

## Overview  
The **Coffee Machine Program** is a Python-based virtual coffee vending machine. Users can order delicious coffee drinks by inserting virtual coins, and the program manages resources, processes transactions, and serves coffee! Enjoy your cup of ☕ without leaving your terminal!  

This project helps you:  
1. 🧠 **Practice Python basics** – functions, loops, dictionaries, and conditionals.  
2. 🎮 **Create an interactive simulation** – a practical, real-world-inspired project.  
3. 💡 **Improve problem-solving skills** – handle inventory, transactions, and logic.  

## 🎯 How It Works  

1. **Select a Drink**:  
   - Choose from **espresso**, **latte**, or **cappuccino**.  

2. **Insert Coins**:  
   - Enter the number of quarters, dimes, nickels, and pennies.  
   - If you insert more money than needed, you get change.  

3. **Check Resources**:  
   - If the machine doesn’t have enough **water, milk, or coffee**, it informs you.  

4. **Enjoy Your Coffee**:  
   - If all goes well, the machine serves your coffee! ☕  

## 📌 How to Run  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the program using:  
   ```bash
   python coffee_machine.py
   ```  

## 📝 Example Gameplay  

### Program Start:  
```plaintext
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $7.50 in change.
Here is your latte ☕️. Enjoy!
```

### Checking Resources:  
```plaintext
What would you like? (espresso/latte/cappuccino): report
Water: 250ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

### Insufficient Funds:  
```plaintext
What would you like? (espresso/latte/cappuccino): cappuccino
Please insert coins.
How many quarters?: 2
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Sorry, that's not enough money. Money refunded.
```

### Running Out of Resources:  
```plaintext
What would you like? (espresso/latte/cappuccino): espresso
Sorry, there is not enough water.
```

### Turning Off the Machine:  
```plaintext
What would you like? (espresso/latte/cappuccino): off
```

## 🔑 Key Features  

1. **🍵 Three Coffee Options** – Espresso, Latte, and Cappuccino.  
2. **💰 Realistic Coin System** – Accepts **quarters, dimes, nickels, and pennies**.  
3. **📊 Machine Reports** – Shows remaining **water, milk, coffee**, and **money earned**.  
4. **🚀 Resource Management** – Prevents making coffee when ingredients run out.  
5. **✨ Transaction Handling** – Returns change and refunds if payment is insufficient.  
6. **🔄 Repeatable Gameplay** – Order coffee until you turn off the machine.  

## 📂 File Details  

### `coffee_machine.py`  
- **Main program** handling drink selection, resource tracking, and transactions.  

### `menu.py` *(Optional for Expansion)*  
- Defines available drinks, their ingredients, and costs.  

## 📁 Folder Structure  

```
coffee_machine/
├── coffee_machine.py    # Main program logic
├── menu.py              # Stores menu items and pricing (optional)
```

## 🌟 Additional Notes  

- 🛠️ Modify the `MENU` dictionary to **add new drinks** or **change prices**.  
- 💡 Experiment by **adjusting resources** for different game difficulties.  
- 🎉 Challenge your friends – Who can **earn the most money** before the machine runs out?  

**☕ Enjoy your virtual coffee break! Happy coding! 🚀**  