# MODULE-02-DATASCIENCE(Web Scraping + SQLite + Pandas)

##  Project Overview

This project demonstrates a complete data workflow using Python:

* Web Scraping from a website
* Storing and managing data using SQLite database
* Data analysis using Pandas
* SQL queries with JOIN operations

This project is useful for beginners who want to understand how real-world data pipelines work.

---

##  Features

### 1. Web Scraping

* Extract book titles and prices from website
* Clean and structure data using Pandas
* Calculate average price of books
* Export data to CSV file

### 2. SQLite Database

* Create and manage database using SQLite3
* Insert user records into database
* Fetch data using SQL queries
* Convert SQL data into Pandas DataFrame

### 3. Data Analysis (Pandas)

* Sort data by age
* Calculate mean marks
* Filter students above average marks
* Find lowest scoring students

### 4. SQL JOIN Operations

* Join student and faculty tables
* Count students per faculty
* Calculate revenue per subject
* Use GROUP BY and LEFT JOIN

---

##  Technologies Used

* Python 🐍
* SQLite3 🗄️
* Pandas 📊
* BeautifulSoup 🍲
* Requests 🌐

---

##  Project Structure

```
project-folder/
│
├── web_scraper.py
├── database_analysis.py
├── student_faculty_analysis.py
├── pandas_analysis.py
├── example.db
├── books.csv
├── requirements.txt
└── README.md
```

---

##  Installation

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

---

##  How to Run

Run each file separately:

```bash
python web_scraper.py
python database_analysis.py
python student_faculty_analysis.py
python pandas_analysis.py
```

---

##  Output Example

* Scraped book data with title & price
* SQLite user database with records
* DataFrame showing student marks
* SQL join results between students & faculty

---

##  Learning Outcomes

After completing this project, you will learn:

* Web scraping using BeautifulSoup
* Working with databases in Python
* Writing SQL queries
* Data analysis using Pandas
* Real-world project structuring


## ⭐ Future Improvements

* Add data visualization (Matplotlib / Seaborn)
* Create Flask API for database
* Add dashboard UI
