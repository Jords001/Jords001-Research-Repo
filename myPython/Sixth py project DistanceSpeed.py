distance = float(input("Distance meters: ")) ##Input variable for distance in meters
timeHours = float(input("Time Hours: ")) ##Input variable for time in hours
timeMinutes = float(input("Time Minutes: ")) ##Input variable for time in minutes
timeSeconds = float(input("Time Seconds: ")) ##Input variable for time in seconds

timeHoursSeconds = timeHours * 3600 ##Convers hours to seconds
timeMinutesSeconds = timeMinutes * 60 ## Converts seconds to minutes
timeMinutesHours = timeMinutes / 60 ##converts hours to minutes
timeSecondsHours = timeSeconds /3600 ##converts seconds to hours
totalSeconds = timeSeconds + timeMinutesSeconds + timeHoursSeconds ##Add all seconds
totalHours = timeHours + timeSecondsHours + timeMinutesHours ##Add all hours
mps = distance / totalSeconds ## Meters per second, distance divided by total seconds
distanceKm = distance / 1000 ## Distance of meters divided by 1000 to create km
kmph = distanceKm / totalHours ##Distance kilometers per hour, distance km divided by total hours
distanceMi = distanceKm * 0.621371 ##Times km distance by 0.621371 to get miles per hour
miph = distanceMi / totalHours ##Miles per hour is distance in miles divided by total hours

print("Your speed in mps =" + str(mps))
print("Your speed in kmph =" + str(kmph))
print("Your speed in mph =" + str(miph))

### This one felt pretty straight forward, I probably could have used more maths and less strings but this felt easier to me
