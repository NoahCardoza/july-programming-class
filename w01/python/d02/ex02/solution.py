recharge = 180
distanceToBase = 8500
distanceToRange = distanceToBase - 1000
ships = 5

token = input("Enter your access token: ")

if token != 'CMDR':
    print ("ERROR: token invalid.")
    print ("This incident will be reported.")
    exit()

print ("Verifying...")
print ("Wellcome to iBoom!\nWith this program you can easily alienate Imperial Starships with just a few clicks of you keybord.")
print ("WANNING: Galac-Tech Studios can not be held responsible for the loss of your planet due to crazy fast Imperial Starships.")

for ship in range(ships):
    print ("What is ship #" + str(ship + 1) + "'s speed in km/h?")
    velocity = float(input(">>> "))
    timeTillImpact = distanceToBase / velocity * 60 * 60
    if timeTillImpact < recharge:
        print ("ERROR: RUN!!!")
        break
    else:
        timeTillInRange = (distanceToRange / velocity * 60 * 60)
        if timeTillInRange >= recharge:
            timeTillShot = timeTillInRange
        else:
            timeTillShot = recharge
        print ("Fire in : " + str(timeTillShot) + " secconds!")
