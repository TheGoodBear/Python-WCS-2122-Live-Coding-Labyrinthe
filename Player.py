# coding: utf-8

# imports
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


def Draw():
    """
        Draw player on map
    """

    RC.ColorPrintAt(
        Var.PlayerData["Symbol"],
        Var.PlayerData["Foreground"],
        Var.PlayerData["Background"],
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