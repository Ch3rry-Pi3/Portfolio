# 🚀 SayHello - A Simple Flask Greeting App

Welcome to **SayHello**! 🎉 This is a simple web application built with **Flask**, allowing users to enter their name and receive a warm greeting. The app is styled using **CSS** and features **flashed messages** for dynamic updates.

## 🌍 Live Demo

This app is hosted on **[Heroku](https://www.heroku.com/)**. You can deploy and run your own instance easily!

## 📸 Preview

Here is what the app looks like in action:

![SayHello Web App](images/webapp.jpg)

## ✨ Features

✅ Flash messages for user-friendly interaction  
✅ Simple and intuitive user interface  
✅ Styled with **CSS** for a modern look  
✅ Hosted on **Heroku** for easy deployment  
✅ Lightweight and easy to set up  

## 🛠 Tech Stack

- **Backend:** Flask (Python) 🐍
- **Frontend:** HTML, CSS 🎨
- **Hosting:** Heroku ☁️

## 📂 Directory Structure

```
SayHello/
│── images/                 # Stores preview images
│── static/css/             # CSS stylesheets
│   ├── main.css            # Main stylesheet
│── templates/              # HTML templates
│   ├── index.html          # Main webpage
│── app.py                  # Flask application
│── Procfile                # Heroku deployment file
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

## 💻 Installation & Setup

To run the project locally, follow these steps:

### 1️⃣ Clone the repository
```sh
$ git clone https://github.com/your-username/SayHello.git
$ cd SayHello
```

### 2️⃣ Create a virtual environment (optional but recommended)
```sh
$ python -m venv venv
$ source venv/bin/activate  # On macOS/Linux
$ venv\Scripts\activate     # On Windows
```

### 3️⃣ Install dependencies
```sh
$ pip install -r requirements.txt
```

### 4️⃣ Run the application
```sh
$ python app.py
```
The app will be available at **http://127.0.0.1:5000/hello**

## 🚀 Deploying to Heroku

To deploy your app to **Heroku**, follow these steps:

### 1️⃣ Install Heroku CLI
Download and install from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

### 2️⃣ Login to Heroku
```sh
$ heroku login
```

### 3️⃣ Create a Heroku app
```sh
$ heroku create your-app-name
```

### 4️⃣ Deploy the app
```sh
$ git add .
$ git commit -m "Initial commit"
$ git push heroku main
```

### 5️⃣ Open your app
```sh
$ heroku open
```

## 📜 License

This project is open-source and available under the **MIT License**.

---
🎯 **Contributions are welcome!** If you’d like to improve the project, feel free to submit a pull request.