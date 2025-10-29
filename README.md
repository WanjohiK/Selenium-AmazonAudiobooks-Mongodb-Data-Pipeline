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
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MongoDB Connection
Edit your MongoDB URI in the script:
```python
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/?appName=Cluster0")
```

💡 **Ensure your MongoDB Atlas cluster is active and your IP address is whitelisted.**

---

## ▶️ Run the Script
```bash
python audible_scraper.py
```

---

## 📦 Output

After execution, you’ll have:

- `books_headless.csv` — local dataset of all scraped audiobooks  
- MongoDB database: `audible_db`  
- MongoDB collection: `audiobooks`

Example output:

| title | author | length |
|--------|---------|---------|
| Atomic Habits | James Clear | 5 hrs and 35 mins |
| The Power of Habit | Charles Duhigg | 10 hrs and 53 mins |

---

## 🧠 Notes

- To enable **headless mode** (browser runs in background):
  ```python
  options.headless = True
  ```
- Modify the search URL to target different audiobook categories.
- Adjust wait durations for slower network speeds.

⚠️ **This project is for educational and portfolio purposes only.**  
Always respect [Audible’s Terms of Service](https://www.audible.com/legal/conditions-of-use).

---

## 🧾 Requirements

**requirements.txt**
```
selenium
pandas
pymongo
```

---

## 💼 Why This Project

This project demonstrates:
- **Selenium web automation** for dynamic content  
- A full **data pipeline design**  
- **MongoDB Atlas integration** for cloud-based storage  
- Strong **Python scripting and data engineering** fundamentals  

Ideal for showcasing **Python + Selenium + MongoDB** expertise on **Upwork** and GitHub.

---

**Author:** [Kelvin Nyawira](https://github.com/<your-username>)  
**Repository:** `Selenium-AmazonAudiobooks-MongoDB-Data-Pipeline`
