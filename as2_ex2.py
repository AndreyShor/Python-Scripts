import math
import os

# Strip string for disBet
def place(p):
    helper=p.strip("\n").split(" ")
    place=(helper[0],helper[1],helper[2],helper[3])
    return place

# Search a city by name
def city():
    check=False
    print("Enter the city's name:")
    city=input().lower()
    for cityies in area:
        if cityies[0].lower() == city:
            show(cityies)
            check=True
    if check==False:
        print("No cities with this name try again!\n")
        

# Show list of cities in a given form
def show(p):
    helper=[]
    lengthC=len(p[3])
    for i in p[3]:
        if lengthC % 3 == 1:
            helper.append(i+",")
            lengthC-= 1
        else:
            helper.append(i)
            lengthC -= 1
    helper= "".join(helper).strip(",")
    print("{places:30} n. citizens: {popul:12}".format(places=p[0],popul=helper))

# View all cities in a range
def workingP():
    valid=False
    minimumPop=input("Enter the minimum population: ")
    try:
        minimumPop=int(minimumPop)
    except:
        print("Incorrect Input")
        workingP()
    maxmPop=input("Enter the maximum population: ")
    try:
        maxmPop=int(maxmPop)
    except:
        print("Incorrect Input")
        workingP()    
    if minimumPop > maxmPop:
        print("Max value is smaler then minimum")
        workingP()
    else:
        for i in area:
            helper=i[3]
            if minimumPop <= int(helper) <= maxmPop:
                show(i)
                valid=True
        if valid==False:
            print("No cities found with that population range!\n")

# View all within a 10 km radius
def distanceB():
    valid=False
    latitude =input("Enter latitude in km")
    try:
        latitude = int(latitude)
    except:
        print("Incorrect input")
        distanceB()
    longitude = input("Enter the longitude in km")
    try:
        longitude=int(longitude)
    except:
        print("Incorrect input")
        distanceB()
    for i in area:
        distance = math.sqrt(math.pow(int(i[1])-(latitude),2)+math.pow(int(i[2])-(longitude),2))
        if 10 >= distance:
            valid=True
            show(i)
    if valid==False:
        print("No Cities around")

# View the distence between two cities
def disBet():
    city=1
    able=[]
    picked=[]
    city=0
    print("Here is a list of the posible cities to choose from:\n")
    for i in area:
        print(str(city + 1)  + " : " + str(i[0]))
        able.append(i)
        city+=1
    print("")
    try:
        city=int(input("Choice city"))
        if city<1:
            print("Incorrect Input")
            disBet()
        elif city>len(able):
            print("Incorrect Input")
            disBet()
    except:
        print("Incorrect Input")
        disBet()
    city=city-1
    picked.append(able[city])
    del able[city]
    city=1
    for i in able:
        print(str(city) + ":" + str(i[0]) )
        city+=1
    print("")
    try:
        city2=int(input("Enter Second city: "))
        if city2<1:
            print("Incorrect Input")
            disBet()
        elif city2>len(able):
            print("Incorrect Input")
            disBet()
    except:
        print("Incorrect Input")
        disBet()
    city2=city2-1
    picked.append(able[city2])
    Fdistance = math.sqrt(math.pow(int(picked[1][1])-int(picked[0][1]),2)+math.pow(int(picked[1][2])-int(picked[0][2]),2))
    print("The distence of " + str(picked[0][0]) + " to " + str(picked[1][0]) + " is: " + str(Fdistance) + " km\n")

# ExitFile
def exitFile():
    file.close()
    exit()

# *********** Start of the program ********************
area=[]
print("Enter file name: ")
fileN=input()
cwd = os.getcwd()
fullPath = cwd + '/' + fileN

try:
    with open(fullPath,"r") as file:
        for i in file.readlines():
            area.append(place(i))
    for i in area:
            show(i)
except:
    print("Not a valid file name entered")
    input()
    exit()

# ******************************************************

# Show menu oprion
def main():
    print("Options:")
    print("1) Search a city by name, input 1")
    print("2) View all cities in a range, input 2")
    print("3) View all within a 10 km radius, input 3")
    print("4) View the distence between two cities, input 4")
    print("5) Exit, input 5")
    print("")
    option=input("Enter value: ")
    if option=="1":
        city()
    elif option=="2":
        workingP()
    elif option=="3":
        distanceB()
    elif option=="4":
        disBet()
    elif option.lower()=="5":
        exitFile()    
    else:
        print("Incorrect")
        
while True:
    main()
