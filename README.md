# 🛡️ CTF Helper Toolkit v2.0

> **Created by Najaf Ali **

A powerful, fully-featured CTF (Capture The Flag) helper tool for the terminal.
Beautiful neon terminal UI, pure Python — no external dependencies required.
Designed for **Kali Linux** and any Python 3.6+ system.

---

## ✨ Features

### 🔵 Module 1 — Encoding / Decoding
- Base64 Encode / Decode
- Hex Encode / Decode
- ROT13
- Caesar Cipher — Encrypt, Decrypt, Brute Force all 25 shifts
- Vigenère Cipher — Encrypt / Decrypt
- Binary ↔ ASCII Converter
- URL Encode / Decode

### 🟣 Module 2 — Hashing
- Generate MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512
- Generate ALL hashes at once
- Hash Identifier — auto-detect hash type by pattern

### 🟡 Module 3 — Crypto Helpers
- XOR Cipher (Text key or Hex key)
- Frequency Analysis
- Frequency Analysis vs English language distribution

### 🟢 Module 4 — Steganography
- Extract File Metadata / EXIF data
- LSB (Least Significant Bit) Steganography Detector
- Magic Bytes / File Signature Checker
- Hex Dump — first 256 bytes of any file

### 🔴 Module 5 — Misc Utilities
- String Reverse
- Full Hex Dump of text
- Magic Bytes Reference Table
- String ↔ Decimal ASCII codes
- Morse Code Encoder / Decoder
- Bit Manipulation — AND, OR, XOR, NOT
- Integer Base Converter — Decimal / Hex / Octal / Binary

---

## 🚀 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/NajafAli40/ctf-helper-toolkit-v2.0.git

# Navigate into the folder
cd ctf-helper-toolkit-v2.0

# Run the tool
python3 ctf_helper_v2.py
```

> **No pip install needed!** Uses only Python standard library.
>
> Optional: install `Pillow` for full EXIF / LSB image support:
> ```bash
> pip install Pillow
> ```

---

## 📋 Requirements

| Item | Detail |
|------|--------|
| Python | 3.6 or higher |
| OS | Kali Linux, Ubuntu, Parrot OS, macOS, Windows (ANSI terminal) |
| Dependencies | None (stdlib only) |
| Optional | Pillow (for image EXIF/LSB analysis) |

---

## 📸 Terminal Preview


<img width="917" height="610" alt="image" src="https://github.com/user-attachments/assets/75dfc205-cb3b-4988-b4f8-de242ab10ebc" />


## 🗂️ Project Structure

```
ctf-helper-toolkit/
│
├── ctf_helper_v2.py     ← Main tool (run this)
└── README.md            ← This file
```

---

## ⚖️ Legal Disclaimer

This tool is intended for **educational purposes** and **legal CTF competitions only**.
Do **not** use this tool against systems you do not own or have explicit permission to test.
The author is not responsible for any misuse of this software.

---

## 📄 License

MIT License — Free to use, modify, and distribute with attribution.

---

**✦ Happy Hacking! (ethically 😄) — Najaf Ali**
