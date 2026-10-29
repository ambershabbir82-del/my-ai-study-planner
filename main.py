# My AI Study Planner
# A beginner-friendly Python project using only built-in features.

def get_positive_number(prompt, minimum, maximum=None):
    """Ask for a whole number within the allowed range."""
    while True:
        try:
            number = int(input(prompt))
            if number < minimum:
                print(f"Please enter a number of at least {minimum}.")
            elif maximum is not None and number > maximum:
                print(f"Please enter a number no greater than {maximum}.")
            else:
                return number
        except ValueError:
            print("Please enter a whole number, such as 3.")


def build_study_plan(name, goal, study_days, daily_hours):
    total_hours = study_days * daily_hours

    # A simple weekly structure based on common beginner learning steps.
    activities = [
        "Learn the basics and write short notes",
        "Continue learning and review your notes",
        "Practise with small exercises",
        "Work through a guided example",
        "Build a small project related to your goal",
        "Review difficult topics and fix mistakes",
        "Revise what you learned and note questions",
    ]

    lines = [
        "=" * 45,
        "MY AI STUDY PLANNER",
        "=" * 45,
        f"Student name: {name}",
        f"AI learning goal: {goal}",
        f"Study days per week: {study_days}",
        f"Daily study hours: {daily_hours}",
        f"Total weekly study hours: {total_hours}",
        "",
        "YOUR PERSONALIZED WEEKLY PLAN",
        "-" * 45,
    ]

    for day in range(1, study_days + 1):
        activity = activities[(day - 1) % len(activities)]
        lines.append(f"Study Day {day} ({daily_hours} hour(s))")
        lines.append(f"  Focus: {activity}")
        lines.append(f"  Goal connection: Make progress toward {goal}.")
        lines.append("")

    lines.extend([
        "TIPS",
        "- Take short breaks during longer study sessions.",
        "- Practise what you learn instead of only watching tutorials.",
        "- At the end of each week, review your progress.",
        "=" * 45,
    ])

    return "\n".join(lines), total_hours


def main():
    print("\nWelcome to My AI Study Planner!\n")

    name = input("What is your name? ").strip()
    while not name:
        name = input("Please enter your name: ").strip()

    goal = input("What is your AI learning goal? ").strip()
    while not goal:
        goal = input("Please enter your AI learning goal: ").strip()

    study_days = get_positive_number(
        "How many days per week will you study (1-7)? ", 1, 7
    )
    daily_hours = get_positive_number(
        "How many whole hours will you study each day? ", 1
    )

    plan, total_hours = build_study_plan(
        name, goal, study_days, daily_hours
    )

    print("\n" + plan)

    try:
        with open("study_plan.txt", "w", encoding="utf-8") as file:
            file.write(plan + "\n")
        print("\nYour study plan has been saved to study_plan.txt")
        print(f"You will study for {total_hours} hour(s) per week.")
    except OSError:
        print("\nSorry, the study plan could not be saved. Try another folder.")


if __name__ == "__main__":
    main()
