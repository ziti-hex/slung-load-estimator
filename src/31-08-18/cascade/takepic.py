# Tobias Bak
# here is a aplication for creating
# positives and negatives sample

print('importing cv2, os, time, threading')
import threading
import cv2
import os
import time
print('import done')
	
	
class TakePicture:
	def __init__(self, ipath):
		self.path = ipath
		self.jpg = '.jpg'
		self.cap = cv2.VideoCapture(0)
	def checkdir(self): 
		ndir = str(self.path) + '/'
		print('checking dir ... %s' %ndir)
		if os.path.exists(str(ndir)) == False:
			os.makedirs(str(ndir))
			print('Dir not exists, created .. %s' %ndir)
		elif os.path.exists(str(ndir)):
			print('Dir allready exitsts\ndone')
		
	def readFrame(self):
		ok, frame = self.cap.read()
		if ok != True:
			print('errr.... somethng goes wrong! check your capture device!')
			return None
			pass
		return frame
		
	def readFrameGray(self):
		frame = self.readFrame()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		return gray
	
	def takePic(self, rate=0.25, pcount=10):
		if self.path == 'pos':
			x,y = input('pos frame bounds in float x,y: ')
		for i in range(pcount):
			filename = self.path + '/' + self.path + str(i) + self.jpg
			frame = self.readFrame()
			if self.path == 'pos':
				frame = self.readFrameGray()
				posframe = frame[x:y,x:y]
				cv2.imshow('posFrame',posframe)
				cv2.imwrite(filename, posframe)
			else:
				cv2.imshow('frame',frame)
				cv2.imwrite(filename, frame)
			print('writing ... %s \n sleeping' % filename)		
			time.sleep(rate)
		return filename, pcount
		
if __name__ == "__main__":
	ipath = str(input('input path; "pos" or "neg" it also set the mode: '))
	pic = TakePicture(ipath)
	pic.checkdir()
	i=0
	print('press "t" to start taking samples')
	while(True):
		cv2.imshow('main loop', pic.readFrameGray())
		if cv2.waitKey(1) & 0xFF == ord('t'):
			cv2.imshow('main loop', pic.readFrameGray())
			filename, pcount = pic.takePic()
			print('%d pictures stored' % pcount)
			break		
	# When everything done, release the capture
	print('we are done relaseing capture device')
	pic.cap.release()
	cv2.destroyAllWindows()
	print('done :)')
	
