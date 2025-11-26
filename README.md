# TFT Personal Stats Tracker

Simple tracker to record your TFT matches and view a dashboard (Flask) with average placement per composition.

> Repo URL: https://github.com/brunoantunesc/TFT-Personal-Stats-Tracker.git

## Requirements
- Python 3.14.

## Features

This is a personal TFT stats tracker, built with the idea to log my own games (portal, augments, compositions) to keep record of every game made through the season. The intent behind it is to find weakness/strenghts in game plan and augment choice and learn how and where to search for improvement.

For now, the act of logging a game is made manually through a terminal. Future plans include adding a method of uploading your game through screenshots (one for the augments, one for the final game position), table search and deploying it online (letting users create an account to save their data).

This is not intended to handle large volumes of data and is also not intended as a bootleg global augments stat tracker.

## Quick start

1. **Clone the repository**
```bash
git clone https://github.com/brunoantunesc/TFT-Personal-Stats-Tracker.git
cd TFT-Personal-Stats-Tracker
```

2. **Install Python 3.14**
Download and install from the official site if needed: https://www.python.org/

3 **Create a virtual environment**
```bash
python -m venv .venv
```

4. **Activate the virtual environment**
- macOS / Linux (bash/zsh):
```bash
source .venv/bin/activate
```
- Windows (PowerShell):
```bash
.venv\Scripts\Activate.ps1
```
- Windows (Command Prompt):
```bash
.venv\Scripts\activate
```
If you see permission errors on PowerShell, run: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

5. **Install dependencies**
```bash
pip install -r requirements.txt
```

6. **Initialize the database**
```bash
python src/init_db.py
```
7. **Run the Flask app**
```bash
python src/app.py
```
By default Flask runs at http://127.0.0.1:5000. Open that URL in your browser.

8. **Add match records from the terminal**
```bash
python src/register.py
```

## Notes & troubleshooting

Make sure the virtualenv is active before installing packages or running scripts.

If the dashboard shows no data but register.py says it inserted a record, check that both scripts use the same tft.db path (project root). If you run scripts from different working directories, the DB path resolution may differ.

If you want to remove the DB and start fresh:
```bash
rm tft.db          # macOS/Linux
del tft.db         # Windows CMD}
```

