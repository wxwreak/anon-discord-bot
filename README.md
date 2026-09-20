<div align="center">

# 🤫 AnonBot

A sleek, modern Discord bot built with `discord.py` that allows users to send anonymous messages and confessions securely through slash commands. Features a gorgeous CLI startup interface powered by `rich`!

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## ✨ Features

- **Anonymous Submissions:** Users can execute `/send` to post secret messages or confessions.
- **Strict Channel Routing:** Messages can *only* be triggered from a designated input channel (`SEND_CHANNEL_ID`) and are automatically forwarded to a target announcement channel (`POST_CHANNEL_ID`).
- **Spam Prevention:** Built-in cooldown checker (5-second rate limit per user) to avoid flooding.
- **Stylish Console Output:** Utilizes the `rich` library for an eye-catching, structured terminal startup sequence and status logger.
- **Modular Design:** Uses Discord Cogs (`cogs/anonym.py`) for clean code architecture.

---

## 📸 Preview

> ![anonbot](https://github.com/wxwreak/anon-discord-bot/blob/main/anonbot.png)

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/wxwreak/anon-discord-bot.git
cd anon-discord-bot
```

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```
*(Alternatively, ensure you have `discord.py`, `rich`, and `python-dotenv` installed)*

### 3. Configure Environment Variables
Create a file named `.env` in the root directory and fill out your credentials and channel IDs:

```env
DISCORD_TOKEN=your_bot_token_here
GUILD_ID=your_development_guild_id_here
SEND_CHANNEL_ID=id_of_channel_where_users_type_command
POST_CHANNEL_ID=id_of_channel_where_messages_are_published
```

### 4. Run the Bot
```bash
python bot.py
```

---

## 🛠️ Commands

| Command | Description | Cooldown |
| :--- | :--- | :--- |
| `/send <message>` | Sends an anonymous message to the configured target channel. Can only be used in the designated input channel. | 5 seconds |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
