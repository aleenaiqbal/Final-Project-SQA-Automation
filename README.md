# 🧪 Final Project – SQA Automation

## 📌 Project Overview

This repository contains an **automated test suite** developed as a **final project for Software Quality Assurance (SQA)**. The project focuses on validating core functionalities of the **Gin & Juice Shop** website using **Python, Selenium, and Pytest**.

The goal of this project is to demonstrate:

* Strong understanding of **manual to automation transition**
* Use of **Pytest framework**
* Real‑world web automation scenarios
* Clean and structured test implementation

---

## 🧰 Technologies & Tools Used

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Pytest Markers** (sanity, regression, etc.)
* **Explicit Waits (WebDriverWait)**
* **Chrome WebDriver**

---

## 🌐 Application Under Test (AUT)

**Website:** [https://ginandjuice.shop/](https://ginandjuice.shop/)

---

## 🗂️ Project Structure

```
Final-Project-SQA-Automation/
│
├── test_login.py          # Login page test cases
├── test_blogPage.py       # Blog page validations
├── test_productPage.py    # Product & catalog page tests
├── test_ourStoryPage.py   # Our Story page tests
├── test_GinAndJuice.py    # Homepage & navigation tests
├── conftest.py            # Pytest fixtures & driver setup
├── __pycache__/           # Python cache files
└── .idea/                 # IDE configuration files
```

---

## 🧪 Test Scenarios Covered

### 🔐 Login Tests

* Verify login page accessibility
* Validate login functionality

### 🏠 Home Page Tests

* Verify home page title
* Validate navigation links
* Check page redirections

### 🛍️ Product Page Tests

* Verify catalog page load
* Validate product listing
* Click and open product details

### 📰 Blog Page Tests

* Verify blog page navigation
* Validate content visibility

### 📖 Our Story Page Tests

* Verify page load
* Validate page content

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/aleenaiqbal/Final-Project-SQA-Automation.git
```

### 2️⃣ Navigate to Project Directory

```bash
cd Final-Project-SQA-Automation
```

### 3️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux
```

### 4️⃣ Install Dependencies

```bash
pip install pytest selenium pytest-check
```

---

## ▶️ How to Run Tests

### Run All Tests

```bash
pytest -v
```

### Run Tests Using Marker (Example: Sanity)

```bash
pytest -v -m sanity
```

---

## 🧠 Key Concepts Implemented

* Pytest fixtures using `conftest.py`
* Explicit waits for stability
* Test case separation by feature
* Assertions & soft assertions
* Clean and readable test code

---

## 📌 Author

**Aleena Iqbal**
SQA Engineer | QA Analyst

---

## ⭐ Purpose of This Project

This project was created for **learning, practice, and portfolio demonstration** in the field of **Software Quality Assurance Automation**.

---

✅ *Feel free to explore, clone, and learn from this project!*
