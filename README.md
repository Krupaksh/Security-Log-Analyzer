# Security Log Analyzer (Level 3)

A structured, class-based log analysis tool built in Python.

This project parses structured log files, validates basic log format integrity, dynamically classifies severity levels, and generates a formatted summary report via a command-line interface.

---

## 🚀 Features

- Object-Oriented Design (Class-based architecture)
- Minimal structured log validation
- Dynamic severity detection (no hardcoded severity types)
- Graceful error handling (FileNotFoundError, PermissionError)
- Sorted severity output (highest frequency first)
- Command-line argument support
- Defensive state reset for repeated analysis

---

## 📂 Expected Log Format

Each log line should follow a structured format:
YYYY-MM-DD HH:MM:SS SEVERITY Message...


Example:
2026-02-21 19:00:01 ERROR Invalid password
2026-02-21 19:00:03 INFO User logged in


---

## 🛠 How It Works

1. Reads file line by line.
2. Performs minimal structural validation:
   - At least 3 fields
   - Date contains "-"
   - Time contains ":"
   - Severity is alphabetic
3. Classifies severity dynamically.
4. Tracks:
   - Total lines
   - Valid entries
   - Malformed entries
   - Severity distribution
5. Prints formatted summary report.

---

## 🧪 Usage

Run from terminal:

```bash
python log_analyzer.py <filename>
```

Example:
python log_analyzer.py Serverlog.txt

If no filename is provided:
Usage: python log_analyzer.py <filename>

Example Output :
===== Log Summary =====

Total Lines      : 10
Valid Entries    : 7
Malformed Lines  : 3

Severity Counts:
ERROR        : 3
INFO         : 2
WARNING      : 1
DEBUG        : 1



