# coding: utf-8

# imports
import json
import Variables as Var
import RichConsole as RC
import Map as Map

# variables


# functions
def Move(Direction):
    """
        Moves player in specified direction

        Direction -> str : direction to move
    """

    print(f"Le joueur se déplace vers {Direction}")

    # save actual player position
    PlayerY = Var.PlayerData["Y"]
    PlayerX = Var.PlayerData["X"]

    # calculate new player position
    PlayerY += Var.PossibleActions[Direction]["DeltaY"]
    PlayerX += Var.PossibleActions[Direction]["DeltaX"]
    # if Direction == "H":
    #     PlayerY -= 1
    # elif Direction == "B":
    #     PlayerY += 1
    # elif Direction == "G":
    #     PlayerX -= 1
    # elif Direction == "D":
    #     PlayerX += 1

    # check if movement is valid
    MapElementAtPlayerPosition = Var.MapData[PlayerY - 1][PlayerX - 1]
    MapElementData = Var.MapElements[MapElementAtPlayerPosition]
    if MapElementData["CanWalk"]:
        Draw(True)
        Var.PlayerData["Y"] = PlayerY
        Var.PlayerData["X"] = PlayerX
        Draw()
        if MapElementAtPlayerPosition == "S":
            Var.GameIsRunning = False
            RC.ColorPrintAt(
                "\nBRAVO, tu as trouvé la sortie.",
                Y=Var.TextLine+2,
                X=1)
    else:
        # obstacle
        print(f"Aïe, un {MapElementData['Name']} !")


def Draw(Erase = False):
    """
        Draw player on map
    """

    Symbol = Var.PlayerData["Symbol"]
    FG = Var.PlayerData["Foreground"]
    BG = Var.PlayerData["Background"]

    MapElement = Var.MapElements[
        Var.MapData[Var.PlayerData["Y"] - 1]
        [Var.PlayerData["X"] - 1]]
    # check if player is beeing erased
    if Erase:
        Symbol = MapElement["Symbol"]
        FG = MapElement["Foreground"]
        BG = MapElement["Background"]

    # draw symbol at right place
    RC.ColorPrintAt(
        Symbol,
        FG,
        BG,
        Var.PlayerData["Y"],
        Var.PlayerData["X"])


def LoadDataFromFile():
    """
        Load player data from JSON file
    """

    try:

        # open json file
        with open(f"{Var.DataFolder}Player.json", "r", encoding="utf-8") as MyFile:
            # load file data into MapElements dictionary
            Var.PlayerData = json.load(MyFile)

    except:
        print(f"\nERREUR lors du chargement des données du joueur")


# code starts here
# if __name__ == "__main__":
#     Main()