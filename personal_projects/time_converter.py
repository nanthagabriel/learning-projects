# Time Converter -> Convert seconds into hours, minutes and seconds.

# User input of total number of seconds.
seconds = (input("Enter the number of seconds to covert: ")).strip()

# Convert input into an integer
total_secs = int(seconds)

# Conversion
hours = total_secs // 3600
secs_remaining = total_secs % 3600
minutes = secs_remaining // 60
secs_finally_remaining = secs_remaining % 60

# Display out put of breakdown respectively
print("Hours:",hours)
print("Minutes:",minutes)
print("Seconds:",secs_finally_remaining)

# TODO
# Improve - interaction and usability.
# Option for hours and minutes.
# Value error.