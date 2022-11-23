import sys, os
os.system("") # For some reason ANSI escape code don't work without this

class pAPI:

    def clr(loc = (0,0)):
        sys.stdout.write(chr(27) + f"[{loc[0]};{loc[1]}f") # loc to move cursor to whereever you want on clear

    def Insert(x, y, char):
        sys.stdout.write("\033["+str(y)+";"+str(x)+"H"+char) # This is much faster than print, no need to make a new line.

    def scroll(txt, spd):
        for x in txt:
            sys.stdout.write(x)
            time.sleep(spd)
