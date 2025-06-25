 #sound frequency
import time
import winsound

print("Please enter the frequency (in Hz) and duration (in milliseconds).")
print("For example: Frequency: 1000 and Duration: 500")

try:
    # Get input from the user and convert to integers
    frequency = int(input(" Sound Frequency (Hz): "))
    duration = int(input(" Sound Duration (milliseconds): "))

    # Validate the ranges
    if frequency < 37 or frequency > 32767:
        print(" Frequency must be between 37 and 32767 Hz.")
    elif duration <= 0:
        print(" Duration must be greater than zero.")
    else:
        print(" Playing sound...")
        winsound.Beep(frequency, duration)  #  Corrected line
        print(" Sound played successfully.")

except ValueError:
    print(" Please enter valid numbers only (no letters or symbols).")

time.sleep(1.5)
print("Program ended.")




