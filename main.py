Habits = []
def show_menu():
    print("\n Habit Tracker Menu:")
    print(" 1. Add a new Habit")
    print(" 2. View all Habits")  
    print(" 3. Mark a Habit as Completed")
    print(" 4. Exit")

def get_choice():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            habit = input ("Enter the new habit: ")
            Habits.append(habit)
            print ( " Habit : " + habit + " has been added successfully!")
            
        elif choice == "2":
            print("\nList of Habits:")
            if Habits:
                for habit in Habits:
                    print("\n",habit)
            else:   
                print("No habits found. Please add a habit first.")     
                
        elif choice == "3":
            print("Mark Habit as Completed feature coming soon!")
        elif choice == "4":
            print("Exiting Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        get_choice()