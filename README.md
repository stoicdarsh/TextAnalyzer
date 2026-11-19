# TextAnalyzer
Our Python Powered Text Analyzer digs deeper, uncovers hidden details, and turns ordinary text into meaningful insights.
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,18,24&height=200&section=header&text=Text%20Analyzer&fontSize=60&fontColor=ffffff&animation=fadeIn&desc=Analyze%20any%20text%20in%20seconds&descSize=20&descAlignY=72" alt="Text Analyzer banner" width="100%"/>

**A menu-driven Python program that analyzes typed text or `.txt` files, and logs every result for you.**

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📥 Flexible Input
- ✍️ Type a paragraph directly
- 📄 Load any `.txt` file by name

### 🔢 Counting Tools
- 🔤 Characters (with and without whitespace)
- 📝 Words
- 📍 Sentences
- 🅰️ Vowels and consonants

</td>
<td width="50%">

### 🧠 Smart Analysis
- 📊 Word-frequency dictionary
- 🏆 Most frequent word
- 📏 Longest word in **UPPER**, **lower** and **Title** case
- 🔁 Palindrome checker for words and phrases

### 💾 Auto Logging
- Results from options 1-6 are saved to `new.txt`
- Log is displayed when you exit

</td>
</tr>
</table>

---

## 🚀 Quick Start

### 📦 Requirements

| Requirement | Details |
|-------------|---------|
| 🐍 Python | **3.10 or higher** (uses `match-case`) |
| 📚 Libraries | None, standard library only |

### ▶️ Run it

```bash
python text_analyzer.py
```

### 🧭 Usage

1. **Choose an input mode**
   ```
   1. Write & Analyze Text
   2. Analyze Text File
   ```
   > 💡 For option 2, enter the file name **without** `.txt` (e.g. `notes` for `notes.txt`). The file must be in the same folder as the script.

2. **Pick an analysis** from the options menu
3. **Repeat** as often as you like, then choose `8` to exit

---

## 📋 Menu Options

| # | 🎯 Action | 💾 Saved to `new.txt` |
|:-:|-----------|:---------------------:|
| 1️⃣ | Count characters (with and without whitespace) | ✅ |
| 2️⃣ | Count words | ✅ |
| 3️⃣ | Count sentences | ✅ |
| 4️⃣ | Count vowels and consonants | ✅ |
| 5️⃣ | Word-frequency dictionary and most frequent word | ✅ |
| 6️⃣ | Longest word in different cases | ✅ |
| 7️⃣ | Check palindrome word/phrase | ❌ |
| 8️⃣ | Exit and show `new.txt` | n/a |

---

## 📸 Demo

```text
###......OPTIONS....###
1.Count Characters in File
2.Count Words
3.Count Sentences
4.Count Vowels and Consonant
5.Show Word-Frequency Dictionary with most Frequent Words
6.Show longest word; Show it in Different Word-Cases
7.Check Palindrome Words/Phrases
8.Exit

Enter your Choice[1-8]: 2
Total Words: 12
```

---

## 🗂️ Project Structure

```text
📦 text-analyzer
 ┣ 📜 text_analyzer.py   ← main program
 ┣ 📝 new.txt            ← results log (created on first save)
 ┗ 📖 README.md
```

> 📌 `new.txt` is appended to on every run and never cleared. Delete it manually for a fresh log.

---

## ⚠️ Known Limitations

<details>
<summary><b>Click to expand 👇</b></summary>

<br>

- 🔸 Sentences are counted by splitting on `.` only, so `!` and `?` are ignored and a trailing full stop adds an extra empty sentence
- 🔸 Word frequency splits on spaces, so punctuation stays attached (`hello,` and `hello` count separately)
- 🔸 A non-numeric value at a menu prompt raises an error
- 🔸 The palindrome check is case- and space-sensitive

</details>

---

## 🔮 Possible Improvements

- [ ] Strip punctuation before counting words and finding the longest word
- [ ] Treat `!` and `?` as sentence endings
- [ ] Validate menu input with `try/except`
- [ ] Normalize case and spaces in the palindrome check
- [ ] Save palindrome results to the log

---

<div align="center">

### 📜 License
Open for personal and educational use.

Made with ❤️ and 🐍 Python

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,18,24&height=100&section=footer" alt="footer" width="100%"/>

</div>
