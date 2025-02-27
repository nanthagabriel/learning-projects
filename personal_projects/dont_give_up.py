
# I'm currently working on this 
required_foundations = ["CS106A", "CS50P", "Python Specialization", "Algebra"]

# Check requirements and completions
def check_foundations(completed_foundations):
    missing_foundations = set(required_foundations) - set(completed_foundations)

    # Only if i complete, which i will, i'll proceed to machine learning and data science  
    if missing_foundations:
        print("\nMissing foundations:", ", ".join(missing_foundations))
        print("No excuses! ..Finish them before you move on to Data Science.")
    else:
        print("All done! Proceed to Data Science, Good luck Gabriel!")

# Pace yourself man, one at a time
def main():
    completed_foundations = ["CS106A"] 
    check_foundations(completed_foundations)

# Execute phase 2
main()
