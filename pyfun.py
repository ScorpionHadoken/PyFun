"""

A simplified python brainfuck, with real-time memory block visualizer

Author : Turboluck102
Date : 11/20/2022

"""

import sys, pgc, msvcrt, os


def readOp(t):
    global blocks
    global ptr
    global plus
    
    if t in ops:
        match (t):
            case ">":
                ptr += 1
                plus += 3 # plus is used for visualizer pointer placement
                
                
            case "<":
                ptr -= 1
                plus -= 3
                
                
            case "+":
               blocks[ptr] += 1
               
               
            case "-":
                blocks[ptr] -= 1
            
            
            case "[":
                # TODO: Loops
                pass
            
            
            case "]":
                # TODO: Loops
                pass
                
            
            case ",":
                blocks[ptr] = ord(msvcrt.getch()) # Get a character and turn it into it's ascii value for the current mem blk
            
            
            case ".":
                pgc.pAPI.Insert(6,6,''.join(chr(i) for i in blocks))
        
                

def MemBlock():
    global plus
    
    x, y = 2, 2
    pgc.pAPI.Insert(plus + ptr, 3,"^") # Show where the pointer is
    
    for b in blocks:
        pgc.pAPI.Insert(x,y,str(b))
        
        x += 4
        
def operate():
    while True:
        os.system('cls') # Used to use pgc.pAPI.clr() but it wont listen to me :(
        pgc.pAPI.Insert(2,9,"Clearing Screen")
        
        MemBlock()
        pgc.pAPI.Insert(2,9,"Called MemBlock")
        pgc.pAPI.Insert(2,4,"") # To move input statement
        token = input("")
        
        pgc.pAPI.Insert(2,9,"Got Token")
        
        try:
            token = token[0]
        except Exception as e:
            pgc.pAPI.Insert(2,8,str(e))
            
        readOp(token)
        pgc.pAPI.Insert(2,9,"Read Token")



# Setting Up Global Variables



try:
    blkamt = int(input("Memory Blocks : "))
    if blkamt > 30000:
        sys.stdout.write("Regular BF does not exceed 30,000 blocks . . . You are not an exception\n")
        blkamt = 30000
except Exception as e:
    sys.stdout.write(f"Error : {e}\n")
    blkamt = 8
    


blocks = [0]*blkamt
ptr = 0 # The pointer location in blocks
plus = 2 # Used for memory vlock visualizer placement

# Operators ===========================
ops = (">","<","+","-","[","]",",",".")
# =====================================


operate()
