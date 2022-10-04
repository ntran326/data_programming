# Nhu Tran

foot = 1
meter = 20

def footMeter(foot):
    return foot * 0.305

def meterFoot(meter):
    return round((meter/.305),3)

print ("Feet \t Meters | Meters \t Feet")

for foot, meter in zip(range(1, 11), range(20, 75, 6)):
    print (foot, '\t' , footMeter(foot), '\t|' , meter, '\t\t' , meterFoot(meter))
