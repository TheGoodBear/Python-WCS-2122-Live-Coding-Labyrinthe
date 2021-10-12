# coding: utf-8

# imports
import Variables as Var
import RichConsole as RC
import Map as Map
import Player as Player

# variables


# functions
def Start():
    """
        Game start
    """
    
    RC.ClearConsole()

    print("Jeu du labyrinthe")
    print("-----------------")
    print("\nL'objectif est de faire sortir le personnage du labyrinthe en un minimum de coups.")
    print("\nActions possibles se déplacer vers le (H)aut, le (B)as, la (G)auche, la (D)roite ou (Q)uitter.")
    input("\nAppuie sur entrée quand tu es prêt...")

    Player.LoadDataFromFile()
    Map.LoadMapElementDataFromFile()
    Map.LoadFromFile(2)
    Map.DrawMap()
    Player.Draw()


def Run():
    """
        Main game loop
        Runs until exit conditions are met
    """

    while Var.GameIsRunning:
        RC.ColorPrintAt(f"", Y=Var.TextLine, X=1)
        Action = input("Prochaine action : ").upper()

        # repeat last player action if action is empty
        if Action == "":
            Action = Var.PlayerData["LastAction"]
        
        if Action in Var.PossibleActions.keys():
            # do action
            if Action == "H" or Action == "B" or Action == "G" or Action == "D":
                Player.Move(Action)
                Var.PlayerData["LastAction"] = Action
            
            elif Action == "Q":
                Var.GameIsRunning = False
                print("Tu abandonnes, lâche !")

        else:
            # wrong action
            print("Ceci n'est pas une action valable.")

    print("\nAu revoir")


# code starts here
# if __name__ == "__main__":
#     Main()