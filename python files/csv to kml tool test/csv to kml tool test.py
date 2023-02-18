import csv

import simplekml

kml = simplekml.Kml()

#Paramaters from name-lat are index parameters of your row
def csvToKML(yesName, yesDescription, name, desc, lon, lat):
    print("Type Exit for either rawDirectory or csvFileTarget if you want to stop the program!")
    while (True):
        rawDirectoryInput = input("Type in the directory of where your csv files are stored: ")
        csvFileTarget = input("Type in the file you want to make a kml file out of: ")
        if csvFileTarget == "Exit" or rawDirectoryInput == "Exit":
            break
        fileName = rawDirectoryInput + "\\" + csvFileTarget
        data = csv.reader(open(fileName + ".csv", 'r'))
        #This will skip headers
        for row in list(data)[1:]:
            if yesName and yesDescription:
                kml.newpoint(name=row[name], description=row[desc], coords=[(row[lon], row[lat])])
            elif not yesName and not yesDescription:
                kml.newpoint(coords=[(row[lon], row[lat])])
            elif not yesName and yesDescription:
                kml.newpoint(description=row[desc], coords=[(row[lon], row[lat])])
            elif yesName and not yesDescription:
                kml.newpoint(name=row[name], coords=[(row[lon], row[lat])])
        kml.save(csvFileTarget + ".kml")
        print("File " + csvFileTarget + ".kml has been created and saved!")
        print("File will show up, once you exit the program!")
 #Take a look at the csv test file to understand 
csvToKML(True, True, 0, 1, 3, 2)
