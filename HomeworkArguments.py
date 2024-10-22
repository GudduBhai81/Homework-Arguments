import os

# Function to define shutdown based on user input
def shutdown_system(choice):
    # Check the argument passed
    if choice.lower() == 'yes':
        print("Shutting down the system...")
        # Uncomment the following line for actual shutdown (be careful when testing)
        # os.system("shutdown /s /t 1")  # For Windows
        # os.system("sudo shutdown -h now")  # For Linux/Mac
    elif choice.lower() == 'no':
        print("Shutdown aborted.")
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

# Main program execution
if __name__ == "__main__":
    # Get the user's choice (yes or no)
    user_input = input("Do you want to shut down the system? (yes/no): ")
    
    # Pass the input to the shutdown_system function
    shutdown_system(user_input)