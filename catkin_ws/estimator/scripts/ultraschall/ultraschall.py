from __future__ import print_function
from sensor import Data
import sys
import time
import RPi.GPIO as GPIO


if __name__ == '__main__':
    messung = Data()
    try:
        while True:
            messung.__init__()
            print('Hohe=%.1f cm Vorne=%.1f cm Hinten=%.1f cm  Links=%.1f cm  Rechts=%.1f cm \r' %(messung.Hoehe, messung.Vorne, messung.Hinten, messung.Links, messung.Rechts),end='')
            #print('Temperatur = %.1f C' %messung.Temp,end='')
            #print('Feuchte=%.1f %%' %messung.Feuchte,end='')
            sys.stdout.flush()
            time.sleep(0.1)
        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
