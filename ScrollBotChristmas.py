import datetime
import time
import signal
import scrollphathd
from scrollphathd.fonts import font5x7
import signal
import sys
import time

def sigterm_handler(signal, frame):
    sys.exit(0)
    
signal.signal(signal.SIGTERM, sigterm_handler)

str_len=0
scroll_x=0

scrollphathd.rotate(180)

while True:
    xmas= datetime.datetime(2020, 12, 25) - datetime.datetime.now()
    daysleft= xmas.days
    hoursleft = xmas.seconds/3600
    
    scrollphathd.set_brightness(0.5)
    scrollphathd.clear()
    
    str_len = scrollphathd.write_string(" Mom and Dad! It's %i days and %i hours until Christmas" %(daysleft, hoursleft), x=0, y=0, font=font5x7)
    
    
    scrollphathd.scroll_to(scroll_x,0)
    scrollphathd.show()
    time.sleep(0.05)
    scroll_x+= 3
    if scroll_x >= str_len:
        scroll_x=0
             
scrollphathd.set_clear_on_exit()
