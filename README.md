
# 📘 Automated Question Extraction from PDF Documents

A Python tool to extract **Multiple Choice Questions (MCQs)** and **Descriptive Questions** from any **text-based PDF** using `PyPDF2` and `Regex`.

🎯 Perfect for **Educators**, **Students**, and **Developers** who need to extract exam or textbook questions in seconds.

---

## ✨ Features

✅ **MCQ Extraction** — Detects choices like `(a)`, `(b)`, `(c)`, `(d)`  
✅ **Descriptive Questions** — Extracts any line ending with a `?`  
🧹 **Auto Cleanup** — Filters noisy PDF text  
🧠 **Regex-Based** — No AI/ML models needed  
⚡ **Fast & Lightweight** — Handles even large PDFs  
🛠 **Customizable** — Modify patterns in `main.py`

---

## 📂 Project Structure

```

pdf-question-extractor/
├── main.py              # Main script for extraction
├── requirements.txt     # List of Python packages
├── README.md            # Project documentation
└── MCQS Workbook.pdf    # Sample PDF input file

````

---

## 🚀 Getting Started

### 📌 Prerequisites

- Python 3.6 or higher

```bash
python3 --version
````


### 🛠 Installation Guide

#### 1️⃣ Clone This Repository

```bash
git clone https://github.com/yourusername/pdf-question-extractor.git
cd pdf-question-extractor
```

#### 2️⃣ (Optional) Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

#### 3️⃣ Add Your PDF File

Copy your **text-based PDF** (e.g., `MCQS Workbook.pdf`) into the project folder.

Ensure the filename inside `main.py` matches your PDF name.

#### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5️⃣ Run the Script

```bash
python3 main.py
```

---

## 💡 How It Works

1. 📥 **Read PDF** using `PyPDF2`
2. 🧾 **Extract Text** from each page
3. 🔍 **Apply Regex** to detect:

   * MCQs with patterns like `(a)...(b)...(c)...(d)...`
   * Descriptive questions ending with `?`
4. 📤 **Print Output** in clean format

---

## 🧪 Example Output

```
Total pages in PDF: 12

--- Extracted Multiple Choice Questions (MCQs) ---

MCQ 1: What is the capital of France?
(a) Berlin
(b) Madrid
(c) Paris
(d) Rome

--- Extracted Descriptive Questions ---

Descriptive Question 1: Explain the process of photosynthesis?
```

---

## 📦 Dependencies

Install via:

```bash
pip install -r requirements.txt
```

**requirements.txt**

```text
PyPDF2==3.0.1
```

---

## ⚠️ Notes & Limitations

⚠️ Only works with **text-based** PDFs
❌ Does **NOT** support scanned/image-based PDFs
🧩 Regex in `main.py` may need editing for non-standard formats

> For OCR support, consider integrating with Tesseract or EasyOCR (not included here).

---

## 👨‍💻 Author Info

Made with ❤️ by **Pavan**

* 🔗 [LinkedIn Profile](https://www.linkedin.com/in/pavan-dokku-045617243)
* 📧 Email: [pavandokku2021@gmail.com](mailto:pavandokku2021@gmail.com)

---

## 🤝 Contribute

Pull requests are welcome!
Feel free to:

* 🔧 Add OCR Support
* 💬 Improve Regex Logic
* 📜 Polish Output or UI
* 📚 Help Enhance Documentation

```bash
# Fork the repo
# Make changes
# Submit a pull request
```

🚀 *Happy extracting!* ✨

