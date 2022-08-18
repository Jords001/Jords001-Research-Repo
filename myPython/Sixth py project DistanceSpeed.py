distance = float(input("Distance meters: "))
timeHours = float(input("Time Hours: "))
timeMinutes = float(input("Time Minutes: "))
timeSeconds = float(input("Time Seconds: "))

timeHoursSeconds = timeHours * 3600
timeMinutesSeconds = timeMinutes * 60
timeMinutesHours = timeMinutes / 60
timeSecondsHours = timeSeconds /3600
totalSeconds = timeSeconds + timeMinutesSeconds + timeHoursSeconds
totalHours = timeHours + timeSecondsHours + timeMinutesHours
mps = distance / totalSeconds
distanceKm = distance / 1000
kmph = distanceKm / totalHours
distanceMi = distanceKm * 0.621371
miph = distanceMi / totalHours

print("Your speed in mps =" + str(mps))
print("Your speed in kmph =" + str(kmph))
print("Your speed in mph =" + str(miph))

### This one felt pretty straight forward, I probably could have used more maths and less strings but this felt easier to me
