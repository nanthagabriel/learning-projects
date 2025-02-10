# - MEAL TIME
# Ask user for the time
def main():
    time = input("What time is it? ")
    hours = convert(time)

    # Reply only within given time frames
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")
    else:
        print(" ")

# define convert(time)
def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60

if __name__ == "__main__":
    main()