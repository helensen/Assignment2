current_time = int(input("Enter the current time : "))
wait_time = int(input("Enter the number of hours to wait: "))

alarm_t = (current_time + wait_time) % 24

print(f"The alarm will go off at: {alarm_t}:00")
