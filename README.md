# Settle-UP 💸  
*A Group Expense Management Web Application*

Splitify is a web-based group expense management system built using Flask.  
It helps users manage shared expenses during trips or group activities by allowing them to create trips, add members, split expenses fairly, and generate settlements easily.

---

## ✨ Features

- 🧳 Create and manage multiple trips
- 👥 Add and remove members from a trip
- 💰 Add expenses and split costs among members
- ⚖️ Automatic settlement calculation to minimize transactions
- ✔️ Mark trips as settled
- 🗑 Delete trips when no longer needed
- 📧 Send settlement details to members via email
- 🎨 Clean, responsive, and animated user interface

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask)  
- **Template Engine:** Jinja2  
- **Email Service:** EmailJS  

---

## 📂 Project Structure

splitify/
│
├── app.py
├── templates/
│ ├── index.html
│ ├── trip.html
│ └── settlement.html
│
├── static/
│ ├── style_index.css
│ └── app.js
│
└── README.md

yaml
Copy code

---

## 🧮 How Settlement Works

1. Expenses are recorded for a trip.
2. Costs are split among the involved members.
3. Each member’s balance is calculated.
4. Creditors and debtors are matched to minimize the number of transactions.
5. Final settlement instructions are generated and displayed.

---## 🧮 How Settlement Works

1. Expenses are recorded for a trip.
2. Costs are split among the involved members.
3. Each member’s balance is calculated.
4. Creditors and debtors are matched to minimize the number of transactions.
5. Final settlement instructions are generated and displayed.

---

## ▶️ How to Run the Project

1. Install Flask:
```
pip install flask
Run the application:


python app.py
Open your browser and visit:


http://127.0.0.1:5000/ 
```

🎯 Use Cases

Group trips with friends

Roommate expense management

College project demonstration

Small group bill splitting

🚀 Future Enhancements

Database integration for persistent storage

Unequal expense splitting

User authentication system

Mobile-friendly or app version

👤 Author
Gaurab Chowdhury

B.Tech in Computer Science & Engineering



