# coding: utf-8

import RichConsole as RC

# general game data
DataFolder = "Data/"
MapFolder = "Maps/"
GameIsRunning = True
PossibleActions = {
    "H" : { "DeltaY" : -1, "DeltaX" : 0}, 
    "B" : { "DeltaY" : 1, "DeltaX" : 0}, 
    "G" : { "DeltaY" : 0, "DeltaX" : -1}, 
    "D" : { "DeltaY" : 0, "DeltaX" : 1}, 
    "Q" : { "DeltaY" : 0, "DeltaX" : 0}
}
PlayerData = None
TextLine = 0

# map elements
MapElements = None

# map data (2D list)
MapData = []
