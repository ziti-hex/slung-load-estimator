#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
import Adafruit_DHT

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
class Data(object):
    Hoehe  = -1
    Hinten = -1 
    Links  = -1     
    Vorne  = -1
    Rechts = -1
    Feuchte= -1
    Temp   = -1
    def __init__(self):
        self.Hoehe  = self.distanz_hoehe()
        self.Hinten = self.distanz_hinten() 
        self.Links  = self.distanz_links()      
        self.Vorne  = self.distanz_vorne() 
        self.Rechts = self.distanz_rechts()
        self.Feuchte= -1 
        self.Temp   = -1

    def distanz_hoehe(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO Pins zuweisen
        
        GPIO_TRIGGER_DOWN = 17
        GPIO_ECHO_DOWN = 27
        
        #Richtung der GPIO-Pins festlegen (IN / OUT)
        GPIO.setup(GPIO_TRIGGER_DOWN, GPIO.OUT)
        GPIO.setup(GPIO_ECHO_DOWN, GPIO.IN)
        
        # setze Trigger auf HIGH
        GPIO.output(GPIO_TRIGGER_DOWN, True)
 
        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER_DOWN, False)
 
        StartZeit = time.time()
        StopZeit = time.time()
 
        # speichere Startzeit
        while GPIO.input(GPIO_ECHO_DOWN) == 0:
            StartZeit = time.time()
 
        # speichere Ankunftszeit
        while GPIO.input(GPIO_ECHO_DOWN) == 1:
            StopZeit = time.time()
 
        # Zeit Differenz zwischen Start und Ankunft
        
        TimeElapsed = StopZeit - StartZeit
        
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        
        distanz_hoehe = (TimeElapsed * 34300) / 2
        return distanz_hoehe-4
        
    def distanz_hinten(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO Pins zuweisen
        
        GPIO_TRIGGER_BACK = 5
        GPIO_ECHO_BACK = 6
        
        #Richtung der GPIO-Pins festlegen (IN / OUT)        
        
        GPIO.setup(GPIO_TRIGGER_BACK, GPIO.OUT)
        GPIO.setup(GPIO_ECHO_BACK, GPIO.IN)
        
        # setze Trigger auf HIGH
        GPIO.output(GPIO_TRIGGER_BACK, True)
 
        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER_BACK, False)
 
        StartZeit = time.time()
        StopZeit = time.time()
 
        # speichere Startzeit
        while GPIO.input(GPIO_ECHO_BACK) == 0:
            StartZeit = time.time()
 
        # speichere Ankunftszeit
        while GPIO.input(GPIO_ECHO_BACK) == 1:
            StopZeit = time.time()
 
        # Zeit Differenz zwischen Start und Ankunft
        TimeElapsed = StopZeit - StartZeit
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        distanz_hinten = (TimeElapsed * 34300) / 2
        return distanz_hinten
    def distanz_links(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO Pins zuweisen        
        
        GPIO_TRIGGER_LEFT = 19
        GPIO_ECHO_LEFT = 26
        
        #Richtung der GPIO-Pins festlegen (IN / OUT)
        
        GPIO.setup(GPIO_TRIGGER_LEFT, GPIO.OUT)
        GPIO.setup(GPIO_ECHO_LEFT, GPIO.IN)
        
        # setze Trigger auf HIGH
        
        GPIO.output(GPIO_TRIGGER_LEFT, True)
 
        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER_LEFT, False)
 
        StartZeit = time.time()
        StopZeit = time.time()
 
        # speichere Startzeit
        while GPIO.input(GPIO_ECHO_LEFT) == 0:
            StartZeit = time.time()
 
        # speichere Ankunftszeit
        while GPIO.input(GPIO_ECHO_LEFT) == 1:
            StopZeit = time.time()
 
        # Zeit Differenz zwischen Start und Ankunft
        TimeElapsed = StopZeit - StartZeit
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        distanz_links = (TimeElapsed * 34300) / 2
        return distanz_links
    def distanz_vorne(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO Pins zuweisen
        
        GPIO_TRIGGER_NOSE = 23
        GPIO_ECHO_NOSE = 24
        
        #Richtung der GPIO-Pins festlegen (IN / OUT)
        
        GPIO.setup(GPIO_TRIGGER_NOSE, GPIO.OUT)
        GPIO.setup(GPIO_ECHO_NOSE, GPIO.IN)
        
        # setze Trigger auf HIGH
        GPIO.output(GPIO_TRIGGER_NOSE, True)
 
        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER_NOSE, False)
 
        StartZeit = time.time()
        StopZeit = time.time()
 
        # speichere Startzeit
        while GPIO.input(GPIO_ECHO_NOSE) == 0:
            StartZeit = time.time()
 
        # speichere Ankunftszeit
        while GPIO.input(GPIO_ECHO_NOSE) == 1:
            StopZeit = time.time()
 
        # Zeit Differenz zwischen Start und Ankunft
        TimeElapsed = StopZeit - StartZeit
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        distanz_vorne = (TimeElapsed * 34300) / 2
        return distanz_vorne
        
    def distanz_rechts(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO Pins zuweisen
                
        GPIO_TRIGGER_RIGHT = 16
        GPIO_ECHO_RIGHT = 20
        
        #Richtung der GPIO-Pins festlegen (IN / OUT)
        
        GPIO.setup(GPIO_TRIGGER_RIGHT, GPIO.OUT)
        GPIO.setup(GPIO_ECHO_RIGHT, GPIO.IN)
        
        # setze Trigger auf HIGH
        GPIO.output(GPIO_TRIGGER_RIGHT, True)
 
        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER_RIGHT, False)
 
        StartZeit = time.time()
        StopZeit = time.time()
 
        # speichere Startzeit
        while GPIO.input(GPIO_ECHO_RIGHT) == 0:
            StartZeit = time.time()
 
        # speichere Ankunftszeit
        while GPIO.input(GPIO_ECHO_RIGHT) == 1:
            StopZeit = time.time()
 
        # Zeit Differenz zwischen Start und Ankunft
        TimeElapsed = StopZeit - StartZeit
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        distanz_rechts = (TimeElapsed * 34300) / 2
        return distanz_rechts
        
    def feutemp(self,flag):
        TEMP_SENS = Adafruit_DHT.DHT11
        pin = 21
        hum, temp = Adafruit_DHT.read_retry(TEMP_SENS, pin)
        if flag == 1:
            return hum
        elif flag == 2:
            return temp
        
