# Temporary sensor input
sensors = [23.0, 24.0, 701]

# Going to need special sensor-values like: clock, external variable, internet/website-result etc....

# Interprete number of pins affected (separated by - or , )
def interpreter(immigrant):
	if "-" in immigrant:
		immigrant = immigrant.split("-")
		newlist = []
		for i in range(int(immigrant[0]), int(immigrant[1])+1):
			newlist.append(i)
		immigrant = newlist
	elif "," in immigrant:	
		immigrant = immigrant.split(",")
		for i in range(len(immigrant)):
			immigrant[i] = int(immigrant[i])
	else:
		immigrant = [int(immigrant)]
		
	return immigrant

# Compare value of sensor to setting
def value(sensorValue, settingValue):
	sensorValue = float(sensorValue)
	settingValue = float(settingValue)
	
	if(sensorValue < settingValue): # less
		return -1
	elif(sensorValue > settingValue): # more
		return 1
	else:
		return 0
		
# Return the relative value based on settings (less, exactly, more)
def relative(value):
	if(value == "less"):
		return -1
	elif(value == "more"):
		return 1
	else:
		return 0
		
# Is it dependent, meaning that if the requirement is false
# the value is going to be the opposite ?
def dependent(value):
	if(value == "else"):
		return True
	else:
		return False

# TO-DO Fix for real input on raspberry pi
# Return sensor value
def getSensorValue(pin):
	return sensors[int(pin)-9]

# Get boolean value based on settings ON/OFF
def getStatus(status):
	if(status=="ON"):
		return True
	else:
		return False

# Update status on GPIO-pins based on list and a common action
def performAction(pins, action):
	for pin in pins:
		print(str(pin) + " is "+ str(action))

# Update output values (GPIO pins)
def output(settings):
	
	for line in settings:
		sensorValue = getSensorValue(line[1])
		settingValue = line[2]
		if(value(sensorValue, settingValue) == relative(line[3])):
			performAction(interpreter(line[0]), getStatus(line[4]))
			#print(str(interpreter(line[0]))+ " is now "+ line[4])
		elif((value(sensorValue, settingValue) != relative(line[3])) and dependent(line[5])):
			performAction(interpreter(line[0]), not getStatus(line[4]))
			#print(str(interpreter(line[0]))+ " is now not "+ line[4])

# Read all settings and update board
def main():
	file = open("settings", "r")
	settings = file.readlines()
	
	for i in range(len(settings)):
		settings[i] = settings[i].replace("\n", "").split("|")
	
	output(settings)

if __name__=="__main__":
    main()
