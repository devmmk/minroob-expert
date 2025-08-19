# 🧠 Minroob Expert - Telegram Minesweeper Bot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)](https://telegram.org/)

An intelligent Telegram bot that automatically plays and wins Minesweeper games! This bot uses advanced algorithms to analyze the game board and make optimal moves, achieving near-perfect win rates.

## 🎮 Demo


https://github.com/user-attachments/assets/063e797e-a215-40d0-9be8-549494916469



> ✨ Watch the bot in action! The video shows the bot automatically detecting its turn and making smart moves to win the game.

## 🌟 Features

- **Smart Algorithm**: Uses constraint-based analysis to determine safe moves and mine locations
- **Probability Engine**: When certainty isn't possible, employs probability calculations to make the safest guess
- **Automatic Play**: Detects when it's your turn and plays automatically
- **Real-time Analysis**: Analyzes the board state in real-time after each move
- **Configurable Delays**: Adjustable delays to mimic human-like playing speed
- **Telegram Integration**: Seamlessly integrates with Telegram's Minesweeper games

## 🧠 How It Works

The bot uses a sophisticated algorithm that:

1. **Parses the Board**: Converts the emoji-based game board into a data structure
2. **Constraint Analysis**: Uses numbered cells as constraints to identify mine locations
3. **Probability Calculation**: When constraints aren't definitive, calculates mine probabilities
4. **Optimal Move Selection**: Chooses the safest available move based on analysis

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- A Telegram account
- Telegram API credentials

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/devmmk/minroob-expert.git
   cd minroob-expert
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the bot:
   - Add your Telegram API credentials:
     ```
     {
       "api_id": YOUR_API_ID,
       "api_hash": "YOUR_API_HASH",
       "session_name": "minsweeper",
       "min_delay": 1,
       "max_delay": 3
     }
     ```
   - Get your API credentials from https://my.telegram.org

4. Run the bot:
   ```bash
   python main.py
   ```

### Configuration

| Parameter     | Description                     | Default |
|---------------|---------------------------------|---------|
| `api_id`      | Your Telegram API ID            | -       |
| `api_hash`    | Your Telegram API Hash          | -       |
| `session_name`| Telegram session name           | minsweeper |
| `min_delay`   | Minimum delay between moves (s) | 0       |
| `max_delay`   | Maximum delay between moves (s) | 5       |

## 🎯 Usage

1. Start a game of Minesweeper in any Telegram chat
2. Invite your bot to the game
3. The bot will automatically detect its turn and play
4. Watch as it analyzes the board and makes optimal moves!

## 🛠️ Technical Details

The bot implements several key algorithms:

- **Constraint Satisfaction**: Uses numbered cells as constraints to identify mine locations with 100% certainty
- **Probability Analysis**: Calculates the probability of each unopened cell containing a mine
- **Neighbor Analysis**: Examines all 8 neighbors of each numbered cell to determine safe moves

## 📊 Performance

The bot achieves a high win rate by:
- Making only safe moves when certainty is possible
- Using probability to minimize risk when guessing is required
- Never making random moves when logical moves are available

## 👨‍💻 Author

- Telegram: [@devmmk](https://t.me/devmmk)
- GitHub: [devmmk](https://github.com/devmmk)

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## ⭐ Show Your Support

If you like this project, please give it a star on GitHub!
