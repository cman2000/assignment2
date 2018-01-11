# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:21:50 2018

@author: christian
"""

#import functions
import csv
import matplotlib.pyplot
import random

# variables and lists
num_drunks = 25
pub = 1

#open and pull in data with drunks and pub location information 

f = open('drunk.plan') # opens csv of pub and drunks homes from file directory
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) # reads csv and ensures any non mueric characters quoted


#create drunkworld 2d list pulling in row values from reader
# Also creates densityworld containing 0's (blank layer) for adding drunks density data to
drunkworld = [] 
densityworld = []
for row in reader:	# A list of rows
    rowlist = [] #creates empty list for rows
    densityrow = []
    for value in row:	# A list of value from reader
        rowlist.append(value)  #move row values to row list
        densityrow.append(0)  	        
    drunkworld.append(rowlist)# append row lists to drunkworld list
    densityworld.append(densityrow)
f.close() # closes reader   

#find the pub coords but only prints the last coords in range, which will be used for the pub entrance int his program
for row_index, row in enumerate(drunkworld):	
    for col_index, value in enumerate(row):
        if value == pub:
            pub_coords = [col_index,row_index]
            
print ("Pub starting coordinate",pub_coords)# print starting pub coordinates for drunks

#show drunk world, the houses and pub starting point as a scatter point
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.imshow(drunkworld)
matplotlib.pyplot.scatter(pub_coords[0], pub_coords[1])#display pub location
matplotlib.pyplot.show() 

#move drunks - randomly

def move_drunk(drunk): #creates function to move drunk 
    board_size = 300
    if random.random() < 0.5:
        drunk[0] = (drunk[0] + 1) % board_size
    else:
        drunk[0] = (drunk[0] - 1) % board_size

    if random.random() < 0.5:
        drunk[1] = (drunk[1] + 1) % board_size
    else:
        drunk[1] = (drunk[1] - 1) % board_size

#function is criteria for when drunk is home - arrived at the value which equates to housenumber 
def is_drunk_home(drunk, drunkworld):
# a drunk is a list of three values -  x, y coordinates, house number    
    x = drunk[0]
    y = drunk[1]
    home = drunk[2] # home number value
    world_value = drunkworld[y][x] #would append/add valus to density world from world_value?
   
    if home == world_value: # is coordinate value equal to house number
        return True
    else:
        return False
  	

        
#Creates a drunk list with pub starting coordinates and house number, loop for all 25 drunks applying move if crieria not met, then for each move adds a value of 1 to denityworld

for drunk_num in range (num_drunks):
    drunk = [pub_coords[0], pub_coords[1], drunk_num * 10 + 10] # a drunk is a list of three values -  x, y coordinates, house number   
    while not is_drunk_home(drunk, drunkworld):
        move_drunk(drunk)
        densityworld[drunk[0]][drunk[1]] += 1 # add a value of 1 to each cell in density world every time a drunk goes though it
    #print ("Drunk with house number",[drunk[2]],"Has arrived at",[drunk[0], drunk[1]])#prints drunk final coordinate at home
    
    #plots home arrival for each drunk, as 25 plots, comment out unless needed
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.imshow(drunkworld)
    matplotlib.pyplot.scatter([drunk[0]], [drunk[1]])#display pub location
    print ("Drunk with house number",[drunk[2]],"Has arrived at home on coordinate",[drunk[0], drunk[1]])#prints drunk final coordinate at home
    matplotlib.pyplot.show()
    

# Write density values (density world) to 
with open("Drunk density.txt","w") as csv_file:
    csv_app = csv.writer(csv_file)
    
    csv_app.writerows(densityworld)
       
    


#shows density of where druks have travelled 
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.imshow(densityworld)
print("Denisty of drunks -  more have travelled in the lighter areas/cells and less in the dark")
matplotlib.pyplot.colorbar()
matplotlib.pyplot.show()


