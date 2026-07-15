# ⚖️ eJusticeBot – Legal Aid Chatbot for Indian Citizens

**eJusticeBot** is a Streamlit-based chatbot that helps Indian citizens navigate the legal system using plain language. It covers fundamental rights, IPC sections, how to file FIRs, consumer complaints, RTI applications, cybercrime reporting, and more — all in a clean, conversational interface.

---

## 🖥️ Demo

![eJusticeBot Preview](https://github.com/user-attachments/assets/76f87f39-f6b3-41d0-a19b-ad9b2cefa7d7)

---

## ✨ Features

- Interactive chat UI built with **Streamlit**
- Keyword-based intent matching powered by **NLTK**
- Covers 20+ legal topics, including:
  - Fundamental rights of Indian citizens
  - How to file an FIR
  - RTI application process
  - Consumer protection rights
  - Cybercrime reporting
  - Women's and children's rights
  - Property and inheritance laws
  - Key IPC sections (302, 376, 420, 498A, 144, and more)
  - Road accident legal procedure
- Chat history preserved within a session
- Easily extendable — add new topics by editing `intents.json`

---

## 🛠️ Tech Stack

| Layer         | Technology       |
|---------------|------------------|
| Language      | Python 3.10+     |
| UI Framework  | Streamlit        |
| NLP Engine    | NLTK             |
| Intent Data   | intents.json     |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sruthy1308/eJusticeBot.git
cd eJusticeBot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
eJusticeBot/
├── app.py           # Streamlit UI and chat logic
├── chatbot.py       # Intent matching and response engine
├── intents.json     # All legal topics, patterns, and responses
├── requirements.txt # Python dependencies
└── README.md
```

---

## 🧠 How It Works

1. The user types a legal question in the chat input.
2. `chatbot.py` cleans and tokenizes the input.
3. It compares the tokens against known patterns in `intents.json`.
4. The best-matching intent's response is returned to the user.
5. If no match is found, the bot asks the user to rephrase.

To add a new topic, just append an entry to `intents.json` with a `tag`, `patterns`, and `responses` field — no code changes needed.

---

## 📜 Legal Topics Covered

| Topic | Description |
|---|---|
| Fundamental Rights | Constitutional rights of Indian citizens |
| File an FIR | Step-by-step guide to registering a police complaint |
| Consumer Rights | Rights under the Consumer Protection Act |
| RTI | How to file a Right to Information request |
| Cybercrime | How to report online fraud, hacking, or harassment |
| Women's Rights | Domestic violence, dowry, assault laws |
| Child Rights | RTE, POCSO, child labour laws |
| Property Rights | Hindu Succession Act, daughters' inheritance rights |
| Court Case Status | How to check case status on eCourts |
| Legal Aid | How to get free legal representation via NALSA |
| IPC Sections | 302, 307, 34, 120B, 144, 354, 341, 376, 420, 498A |
| Road Accident | Immediate steps and legal procedure after an accident |

---

## 🙋‍♀️ Author

**Sruthy S**
B.Tech CSE Student · LBSITW, KTU
📧 sruthy0813@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/sruthy-s-149b12301) · [GitHub](https://github.com/sruthy1308)

---

## 🤝 Contributing

Contributions are welcome. To add new legal topics:

1. Fork the repository
2. Add your intent to `intents.json`
3. Open a pull request with a brief description

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> **Disclaimer:** eJusticeBot provides general legal information for awareness purposes only. It is not a substitute for professional legal advice. For specific legal matters, consult a qualified advocate.
