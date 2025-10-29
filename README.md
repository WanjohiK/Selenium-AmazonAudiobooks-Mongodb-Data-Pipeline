# Selenium-AmazonAudiobooks-Mongodb-Data-Pipeline
# 🤖 Selenium Amazon Audiobooks MongoDB Data Pipeline

An automated **data pipeline** built with **Python**, **Selenium**, and **MongoDB** to extract audiobook information from [Audible (an Amazon company)](https://www.audible.com/search).  

This project demonstrates a complete **end-to-end data workflow** — web automation, data extraction, processing, and database storage — ideal for showcasing **Python automation and data engineering** skills.

---

## 🚀 Features

- Scrapes audiobook data such as:
  - ✅ Title  
  - ✅ Author  
  - ✅ Length (runtime)
- Automatically handles multi-page navigation (pagination)
- Stores data into:
  - A **CSV file** for local analysis  
  - A **MongoDB Atlas** collection for scalable cloud storage

---

## 🧰 Tech Stack

- **Python 3**
- **Selenium WebDriver**
- **Pandas**
- **MongoDB (PyMongo)**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Selenium-AmazonAudiobooks-MongoDB-Data-Pipeline.git
cd Selenium-AmazonAudiobooks-MongoDB-Data-Pipeline

---

### ** 2️⃣ Create a Virtual Environment**

python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows

---

### **3️⃣ Install Dependencies**

pip install -r requirements.txt

---

### **4️⃣ Configure MongoDB Connection**

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/?appName=Cluster0")

---

### ▶️ Run the Script

python audible_scraper.py

---





