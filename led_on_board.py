# ledOnBoard.py

import machine, neopixel

PWR=const(10) # led is otherwise much too bright
class color:
    red=0,PWR,0
    green= PWR,0,0
    blue= 0,0,PWR
    nul=0,0,0
    white=PWR,PWR,PWR
    
class Led_on_board(color):
    def __init__(self):
        self.np = neopixel.NeoPixel(machine.Pin(16), 1, bpp=3)
        self.off()
    def __call__(self,x): # led(0) or led(1)
        if x >0:
            self.write(color.white)
        else:
            self.off()       
    def write(self,color):
        self.np[0] = color
        self.np.write()
    def green(self):
        self.write(color.green)
    def red(self):
        self.write(color.red)
    def blue(self):
        self.write(color.blue)
    def off(self):
        self.write(color.nul)
    def on(self):
        self.write(color.white)
        
