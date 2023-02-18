import simplekml
import json

kml = simplekml.Kml()

def jsonToKML(features, geometry, coordinates, properties, name):
    print("Type Exit for either rawDirectory or jsonFileTarget if you want to stop the program!")
    while (True):
        rawDirectoryInput = input("Type in the directory of where your json files are stored: ")
        jsonFileTarget = input("Type in the file you want to make a kml file out of: ")
        if jsonFileTarget == "Exit" or rawDirectoryInput == "Exit":
            break
        fileName = rawDirectoryInput + "\\" + jsonFileTarget
        with open(fileName + ".json", 'r') as file:
            data = json.load(file)
        for feature in data[features]:
            location = feature[geometry][coordinates]
            kml.newpoint(name=feature[properties][name], coords=[(location[1], location[0])])
        kml.save(fileName + ".kml")
        print("File " + jsonFileTarget + ".kml has been created and saved!")
        print("File will show up, once you exit the program!")
