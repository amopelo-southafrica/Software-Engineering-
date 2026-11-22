swimming = int(input("How many minutes did it take for you to complete swimming?"))
cycling = int(input("How many minutes did it take for you to complete swimming?"))
running = int(input("How many minutes did it take for you to complete swimming?"))
total_time = (swimming + cycling+  running)
print(total_time)

if (total_time <= 100):
    print("Provincial colours")

elif (total_time >= 101 and 105):
    print("Provincial half colours")

elif (total_time >= 106 and 110):
     print("Provinicial scroll")

elif total_time > 111:
     print("No reward")


    