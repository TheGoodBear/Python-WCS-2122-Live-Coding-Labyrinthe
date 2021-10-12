# coding: utf-8

# imports
import json
import Variables as Var
import RichConsole as RC

# variables


# functions
def LoadFromFile(MapNumber=1):
    """
        Load map from text file

        Map with specified number from MapFolder

        MapNumber -> int : number of the map to load
    """
    
    try:
        # load map data from text file
        with open(f"{Var.MapFolder}Map {MapNumber}", "r", encoding="utf-8") as MyFile:
            MapData = MyFile.readlines()

        # reste actual map
        Var.MapData = []

        # parse map data into 2D list
        # for each line in map data
        for Y, MapLine in enumerate(MapData):
            # define empty list for current line
            CurrentLine = []
            # for each character in line
            for X, Character in enumerate(MapLine):
                # if character is not end of line
                # add it to current line list
                if Character != "\n":
                    CurrentLine.append(Character)
                    if Character == "E":
                        # this is player entry point
                        Var.PlayerData["Y"] = Y + 1
                        Var.PlayerData["X"] = X + 1
            # add current line to map data
            Var.MapData.append(CurrentLine)

        # save test position under map
        Var.TextLine = len(Var.MapData) + 2

    except:
        print(f"\nERREUR lors du chargement de la carte numéro {MapNumber}")


def LoadMapElementDataFromFile():
    """
        Load map elements data from JSON file
    """

    try:

        # open json file
        with open(f"{Var.DataFolder}MapElements.json", "r", encoding="utf-8") as MyFile:
            # load file data into MapElements dictionary
            Var.MapElements = json.load(MyFile)

    except:
        print(f"\nERREUR lors du chargement des éléments de carte")


def DrawMap():
    """
        Draw map on screen from MapData 2D list
    """

    RC.ClearConsole()

    # each line in 2D list
    for Y, Line in enumerate(Var.MapData):
        # for each column in current line
        for X, Character in enumerate(Line):
            # get map element data from dictionnary
            # matching current character in 2D list
            MapElement = Var.MapElements[Character]
            # print map element at coordinates
            RC.ColorPrintAt(
                MapElement["Symbol"],
                MapElement["Foreground"],
                MapElement["Background"],
                Y+1,
                X+1)

    # print player position
    # RC.ColorPrintAt(
    #     f"Position = {Var.PlayerData['Y']} / {Var.PlayerData['X']}",
    #     Y=Var.TextLine,
    #     X=1)


# code starts here
# if __name__ == "__main__":
#     Main()