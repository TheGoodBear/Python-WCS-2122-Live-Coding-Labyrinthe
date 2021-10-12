# coding: utf-8

# See details here : http://www.jchr.be/python/ecma-48.htm

# Imports
import os, sys

# Variables and constants
Prefix = "\x1b["
Style_Suffix = "m"
Reset = "0"
Colors = {
    "BLACK" : "0",
    "RED" : "1",
    "GREEN" : "2",
    "YELLOW" : "3",
    "BLUE" : "4",
    "PURPLE" : "5",
    "CYAN" : "6",
    "WHITE" : "7"
}
FG_Prefix = "3"
BG_Prefix = "4"
Position_Suffix = "H"


# Functions
def Main():
    os.system("")
    ClearConsole()
    print ("Blanc sur noir")
    # print (f"{Prefix}{FG}{BLUE}{Style_Suffix}Bleu sur noir{Prefix}{Reset}{Style_Suffix}")
    # print (f"{Prefix}{FG}{RED}{Style_Suffix}Rouge sur noir{Prefix}{Reset}{Style_Suffix}")
    # print (f"{Prefix}{FG}{RED};{BG}{GREEN}{Style_Suffix}Rouge sur vert{Prefix}{Reset}{Style_Suffix}")
    # print (f"{Prefix}{BG}{GREEN}{Style_Suffix}Blanc sur vert{Prefix}{Reset}{Style_Suffix}")
    ColorPrintAt("Bleu sur noir en 1,1", "BLUE", Y=1, X=1)
    ColorPrintAt("Rouge sur noir en 3,10", "RED", Y=3, X=10)
    ColorPrintAt("Rouge sur vert à la suite", "RED", "GREEN")
    ColorPrintAt("Blanc sur vert en 2,30", BG="GREEN", Y=2, X=30)


def ColorPrintAt(
    Text, 
    FG = "", 
    BG = "", 
    Y = None, 
    X = None):
    """
        Print a text with a specific foreground and background color
    
        Text -> str : text to be printed
        FG -> str : Foreground color
        BG -> str : Background color
        Y -> int : Line position
        X -> int : Column position
    """
    
    Separator = ""
    if FG != "":
        FG = f"{FG_Prefix}{Colors[FG]}"
    if BG != "":
        BG = f"{BG_Prefix}{Colors[BG]}"
    if FG != "" and BG != "":
        Separator = ";"

    Position = ""
    if Y != None and X != None:
        Position = f"{Prefix}{Y};{X}{Position_Suffix}"

    print (
        f"{Position}{Prefix}{FG}{Separator}{BG}{Style_Suffix}{Text}{Prefix}{Reset}{Style_Suffix}",
        end="",
        flush=True)


def ClearConsole():
    """
        Clear the console depending on OS
    """

    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")



# Code starts here
if __name__ == "__main__":
    Main()
