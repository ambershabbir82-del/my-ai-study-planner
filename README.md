# My AI Study Planner

A beginner-friendly Python project that creates a personalized weekly study plan for a student learning about AI.

> **Note:** This project does not call an AI model or use an AI API. It uses basic Python input, calculations, lists, loops, functions, and file handling to create a simple study plan.

## Features

- Asks for the student's name
- Asks for their AI learning goal
- Asks how many days per week they can study
- Asks how many whole hours they will study each day
- Calculates total weekly study hours
- Displays a personalized weekly plan
- Saves the plan to `study_plan.txt`
- Checks that study days and hours are valid whole numbers

## Requirements

- Python 3
- No external packages required

## How to Run

1. Download or clone this repository.
2. Open a terminal or command prompt in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use:

   ```bash
   python3 main.py
   ```

4. Answer the questions. The program will display your plan and create `study_plan.txt` in the current folder.

## Example

```text
Welcome to My AI Study Planner!

What is your name? Amber
What is your AI learning goal? Learn Python for AI
How many days per week will you study (1-7)? 4
How many whole hours will you study each day? 2
```

The program calculates **8 study hours per week** and creates a plan for four study days.

## Project Files

- `main.py` — the Python program
- `README.md` — project information and instructions
- `study_plan.txt` — generated automatically when you run the program

## Concepts Practised

- Variables and user input
- Type conversion and validation
- Arithmetic calculations
- Lists and loops
- Functions
- File handling with `open()`

## Possible Future Improvements

- Let students choose their study days
- Add different activities for specific AI topics
- Track completed study sessions
