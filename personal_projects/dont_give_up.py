# DONT GIVE UP NANTHA -> A way to keep track of my study progress.

# I have to finish this first
required_foundations =[" CS50P", " Python Specialization", " Algebra"]

# Ok this is the setup
def check_foundations(completed_foundations):
    missing_foundations = set(required_foundations) - set(completed_foundations)

    # Only if i complete, which i will, i'll proceed to machine learning and data science  
    if missing_foundations:
        print("\nMissing foundations:",",".join(missing_foundations))
        print("No excuses! ..Finish them before you move on to Data Science.")
    else:
        print("All done! Proceed to Data Science, Good luck Gabriel!")

# Pace yourself man
def main(): 
    completed_foundations = [] 
    check_foundations(completed_foundations)

# Execute phase 2
main()
