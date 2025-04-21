# 🔐 Username Generator by Pattern

A flexible username generator that takes a list of last names and produces login names based on customizable patterns. Perfect for OSINT, red teaming, internal reconnaissance, and building wordlists that match corporate username formats.

---

## 📦 Features

- ✅ Accepts a list of surnames from a text file
- ✅ Generates usernames based on selected patterns (e.g., `i.ivanov`, `ivanov_i`, `ivanov`)
- ✅ Allows specifying which patterns to use
- ✅ Supports UTF-8 input by default
- ✅ Can output to file or stdout

---

## 🚀 Installation

```
git clone https://github.com/ladnoyaponyal/russian_wordlist.git
cd russian_wordlist
python3 word_gen.py --help
```

> ⚠️ Requires only Python 3 (no external dependencies)

---

## 📄 Input Format

A plain text file with one surname per line:

```
ivanov
petrov
sidporpv
```

---

## 🛠 Usage Examples

📌 **Generate usernames using all default patterns:**

```
python3 word_gen.py wordlists.txt
```

📌 **Save output to a file:**

```
python3 word_gen.py wordlists.txt -o usernames.txt
```

📌 **Generate usernames using specific patterns:**

```
python3 word_gen.py wordlists.txt -p i.s,is,s.i
```

📌 **List available patterns:**

```
python3 word_gen.py --list-patterns
```

---

## 🔣 Available Patterns

| Pattern | Example (`ivanov`) |
|---------|--------------------|
| `i.s`   | `a.ivanov`         |
| `i_s`   | `a_ivanov`         |
| `is`    | `aivanov`          |
| `si`    | `ivanova`          |
| `s_i`   | `ivanov_a`         |
| `s.i`   | `ivanov.a`         |
| `s`     | `ivanov`           |

> All patterns are combined with each letter of the alphabet (`a-z`) per surname.

---

## 🔍 Use Cases

- OSINT and recon
- Username enumeration in corporate environments
- Wordlist generation for brute-force
- Social engineering & red team preparation

---


## ✍️ Author

[🔗 @profileusername](https://t.me/profileusername)

Pull requests, feature suggestions, and contributions are welcome!
