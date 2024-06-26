# launchpad functions

# for my reference
# bottom left corner is (0,0)
# to lright corner is (7,7)


import time
import numpy as np
import mido
from mido import Message

# we know which device we want to talk to
portname = "Launchpad MK2"

# open it as an output port
port = mido.open_output(portname)


def everything_off():
    notes = []
    for i in range(1, 9):
        for j in range(1,9):
            notes.append(i*10+j)
    
    for n in notes:
        off = Message('note_off', note=n)
        port.send(off)


def light_up_column(column, height, color, on_time):
    # column = vertical line; left most row = 0; right most = 7
    # height = how many pads in that column need to be on
    # color = color of the column

    # Notes in column 0 are 11, 21, 31 ... 81
    # column 1 = 12, 22, 32 ... 82
    # column 7 = 18, 28, 38 ... 88

    # lets get the notes (pads) you need to light up
    notes = []
    for j in range(1,height+1):
        notes.append(j*10+column)
    print(notes)

    for n in notes:
        on = Message('note_on', note=n, velocity=color)
        port.send(on)
    
    time.sleep(on_time)
    
    everything_off()


all_positions = np.zeros((8,8))
for i in range(1, 9):
    for j in range(1,9):
        all_positions[i-1,j-1] = i*10+j

# light up the board according a given 8x8 matrix
def light_up_matrix(position_matrix, color):
    notes = position_matrix * all_positions
    for i in range(8):
        for j in range(8):
            on = Message('note_on', note=int(notes[i,j]), velocity=color)
            port.send(on)

#light_up_column(2, 8, 12, 1)
#print('done')