# Habit Tracker Application
import json
import os
from datetime import date, timedelta

Habits_file = "habits.json"
def load_habits():
    if os.path.exists(Habits_file):
        with open(Habits_file, "r") as f:
            return json.load (f)
    return []

def save_habits():
        with open(Habits_file,"w") as f:
            json.dump(Habits,f, indent=4)

def calculate_streak(done_dates):
    current_day= date.today()
    streak =0 
    done_days_set = set (done_dates)
    while current_day.isoformat() in done_days_set:
        streak += 1
        current_day -= timedelta(days=1)
    return streak


Habits = load_habits()


def show_menu():
    print("\n Habit Tracker Menu:")
    print(" 1. Add a new Habit")
    print(" 2. View all Habits")  
    print(" 3. Mark a Habit as Completed")
    print(" 4. Exit")

def Main_fuction_get_choice():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            Name = input ("Enter the new habit: ")
            habit = { "Name": Name , "done_dates" : [] }
            Habits.append(habit)
            save_habits()
            print(f"Habit : {habit['Name']} has been added successfully!")
            
        elif choice == "2":
            print("\nList of Habits:")
            if Habits:
                today= date.today().isoformat()
                for habit in Habits:
                    status = "Done !" if today in habit["done_dates"]  else "Not done !"
                    streak= calculate_streak(habit["done_dates"])

                    print(f"\n { habit['Name']} ( {status}, Streak :{streak} days)")
            else:   
                print("No habits found. Please add a habit first.")     
                
        elif choice == "3":
            print("\n Select a habit to mark as completed.")
            for index, habit in enumerate(Habits):
                print(f" {index+1}. {habit['Name']} ")
            try:
                choice = int(input("Enter the number of habit "))-1
                if 0 <= choice < len(Habits):
                    last_done= date.today().isoformat()
                    if last_done not in Habits[choice]["done_dates"]:
                        Habits[choice]["done_dates"].append(last_done)
                        save_habits()
                        print(f"The Habit {Habits[choice]['Name']} has been marked as done on {last_done}")
                    else:
                        print(f"Habit already marked as done!")
                else :
                    print("Enter the correct number of the Habit that you want to mark as Done")
            except ValueError:
                print("Invalid number.")

        elif choice == "4":
            print("Exiting Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
        Main_fuction_get_choice()