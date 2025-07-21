# 🖥️ My Custom Python Web Server

A lightweight web server built entirely from scratch using Python's `socket` module — no external libraries or frameworks required.

---

## 🚀 Features

- Serves static HTML files (like `index.html`)
- Serves JSON content dynamically (`books.json`)
- Handles basic HTTP GET requests
- Clean, educational structure to understand how HTTP works under the hood

---

## 📁 Project Structure

My-own-custom-python-server/
├── server.py # Main Python server file
├── books.json # JSON data served at /book
├── static/
│ └── index.html # Static HTML file served at /
└── README.md # You're reading it!


---

## 🧪 How to Run

1. Make sure you have **Python 3.9+** installed.
2. Clone or download this repository.
3. Navigate to the project folder:

```bash
cd My-own-custom-python-server

#Start the server:

python server.py

#Open your browser and visit:

http://127.0.0.1:8080/ → Welcome page

http://127.0.0.1:8080/book → JSON data of books

📘 Sample JSON Response

[
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
  }
]


🎯 Learning Objectives
Understand how HTTP headers and content types work

Learn to serve both static and dynamic content without a framework

Explore how Python sockets can handle basic networking

🙌 Contributions
This project was created for learning and demonstration purposes. Feel free to fork and improve it!

📝 License
MIT License. Do whatever you want with it, but give credit if you share it!

✍️ Author
Rishikalpo Dey
💼 BCA Student | 💡 Learning Web & Systems Development
📧 rishikalpo721@gmail.com