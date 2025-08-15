
# 🎮 Python Tic-Tac-Toe (2 Player Console Game)
<img width="100" height="102" alt="ChatGPT Image Aug 15, 2025, 01_27_44 PM" src="https://github.com/user-attachments/assets/de3c4171-e6a7-481f-9747-632afbfcab1f" />

A simple **Tic-Tac-Toe** game built in Python for two players to play in the console.  
This project is a great starting point to understand **loops, conditionals, lists, and game logic** in Python.

---

## 📌 Features
- 3×3 grid-based game board
- Player vs Player mode
- Input validation (prevents invalid moves)
- Win detection for:
  - Rows
  - Columns
  - Diagonals
- Draw detection
- Clean and easy-to-read board display

---

## 🛠 Requirements
- Python 3.x installed on your system

---

## ▶️ How to Run
1. Save the code in a file named `tic_tac_toe.py`.
2. Open a terminal or command prompt in the file's directory.
3. Run the game:
   ```bash
   python tic_tac_toe.py
🎯 How to Play

The game board has rows and columns numbered 0–2.

Player X goes first, followed by Player O.

On your turn:

Enter the row and column numbers (e.g., 1 2 means row 1, column 2).

The first player to align three marks in a row, column, or diagonal wins.

If the board is full and no one has won → It's a draw.

🧠 Game Logic

Board Representation: 3×3 list of lists, initialized with spaces ' '.

Move Validation: Ensures moves are within bounds and the chosen cell is empty.

Win Detection: Checks all rows, columns, and both diagonals for matching symbols.

Draw Detection: If all cells are filled without a winner.

Player Switching: Alternates between 'X' and 'O'.


