# 🎯 **True or False Quiz Game** 🧠  

## Overview  
The **True or False Quiz Game** is a fun, interactive Python program that tests your knowledge with a series of **True/False** questions. The game is implemented using **Object-Oriented Programming (OOP)** for better structure and modularity. 🚀  

This project helps you:  
1. 🏗 **Understand OOP principles** – classes, objects, and methods.  
2. 🔄 **Improve program flow** – efficiently handle a quiz using a `QuizBrain` class.  
3. 🎮 **Enjoy an engaging coding challenge** – test yourself with fun facts!  

## 🛠️ **How It Works**  

1. **Start the Quiz** 🎬  
   - The program loads a **bank of True/False questions** from `data.py`.  
   - It initializes the **quiz system** with a **question model** and a **quiz controller**.  

2. **Answer Questions** 📝  
   - Each question is displayed one by one.  
   - The user inputs `"True"` or `"False"`.  

3. **Check Answers** ✅❌  
   - If correct, the score **increases**.  
   - If incorrect, the correct answer is shown.  

4. **Continue Until the Quiz Ends** 🎯  
   - The game runs **until all questions are answered**.  
   - The final **score is displayed** at the end.  

## 📌 **How to Run**  

1. Open a terminal or command prompt. 💻  
2. Navigate to the folder containing the files. 📂  
3. Run the program using:  
   ```bash
   python main.py
   ```  

## 📝 **Example Gameplay**  

```plaintext
Q.1: A slug's blood is green. (True/False) True
You got it right!
The correct answer was: True.
Your current score is 1/1.

Q.2: The loudest animal is the African Elephant. (True/False) True
That's incorrect.
The correct answer was: False.
Your current score is 1/2.
```

```plaintext
Thanks for completing the quiz!
Your final score is: 8/12
```

## 🏗️ **Project Structure**  

This project is structured using **four modules**, each handling a different aspect of the quiz:  

### `main.py`  
- **Runs the quiz program**  
- Loads questions and starts the game loop  

### `data.py`  
- **Contains the question bank**  
- Stores **True/False questions** in a dictionary format  

### `question_model.py`  
- **Defines the `Question` class**  
- Stores the **text and answer** for each question  

### `quiz_brain.py`  
- **Manages the quiz flow**  
- Handles **question progression, answer checking, and scoring**  

## 📁 **Folder Structure**  

```
quiz_game/
├── main.py              # Main quiz execution
├── data.py              # List of questions
├── question_model.py    # Question class
├── quiz_brain.py        # Quiz logic (game flow)
```

## 🚀 **Key Features**  

1. **🎯 Dynamic Quiz System** – Easily expand the question bank.  
2. **🧠 Object-Oriented Programming** – Modular, maintainable, and scalable.  
3. **🔄 Automatic Question Handling** – No need to manually loop through questions.  
4. **✅ Score Tracking** – See your score after every question.  
5. **📝 Fun & Educational** – Learn new facts while coding!  

## 🌟 **Additional Notes**  

- 🛠️ Modify `data.py` to **add more questions**.  
- 🎨 Customize `quiz_brain.py` to **add different question formats**.  
- 🔥 Try making a **multiple-choice version** for an extra challenge!  

**🎉 Enjoy playing the True or False Quiz! Good luck! 🏆**  