# 📄 Text Information Extractor

A beginner-friendly Python project that extracts useful information from raw text using **Regular Expressions (Regex)**.

---

## 🚀 Features

- 📧 Extract Email Addresses
- 📱 Extract Phone Numbers
- 📅 Extract Dates
- 🧹 Clean text using Regex
- 📊 Display extracted information in a structured format

---

## 🛠 Technologies Used

- Python 3
- re (Regular Expressions)

---

## 📌 Regex Patterns Used

### 📧 Email

```regex
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

**Matches**

- sampawar@gmail.com
- support@company.org

---

### 📱 Phone Number

```regex
(?:\+91[-\s]?)?[6-9]\d{9}
```

**Matches**

- 9921519195
- +91 9921519195

---

### 📅 Date

```regex
\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2})\b
```

**Matches**

- 30/06/2026
- 30-06-2026
- 2026-06-30

---

### 🧹 Text Cleaning

```python
re.sub(r"\s+", " ", text)
```

Removes extra spaces from the input text.

---

## 📁 Project Structure

```
Day-05-Regex-Text-Extractor/
│
├── text_extractor.py
├── sample_text.txt
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/your-username/Day-05-Regex-Text-Extractor.git
```

Move into the project

```bash
cd Day-05-Regex-Text-Extractor
```

Run the program

```bash
python text_extractor.py
```

---

## 💻 Sample Output

```
============================================================
TEXT INFORMATION EXTRACTOR
============================================================

📧 Email Addresses
------------------------------
sampawar@gmail.com
student.ai2026@college.edu
support@company.org

📱 Phone Numbers
------------------------------
9921519195
+91 9921519195

📅 Dates
------------------------------
30/06/2026
30-06-2026
2026-06-30

Summary
------------------------------
Total Emails : 3
Total Phones : 2
Total Dates  : 3
```

---

## 🎯 Learning Objectives

- Understand the `re` module
- Use `findall()`
- Use `sub()`
- Learn Regex pattern matching
- Process and clean text efficiently

---

## ⭐ Author

**Samruddhi Pawar**

If you found this project helpful, consider giving it a ⭐ on GitHub!
