import cv2 as cv
import picamera as Camera
import socket
import time
import sys

class LiveStream:	
	cam = Camera.PiCamera()	
	socket = socket.socket()	
	con = 0

	def __init__(self, resolution, framerate):
		self.cam.resolution = resolution
		self.cam.framerate = framerate

	def start(self):					
		try:					
			print "Binding socket.."
			self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.socket.bind(('0.0.0.0', 9000))			
			print "Starting to listen.."
			self.socket.listen(0)			
			print "Waiting for connection.."			
			self.conn = self.socket.accept()[0].makefile("wb")
			return True
		except:
			print ("Failed to establish socket:", sys.exc_info())
			return False
			sys.exit()

	def streaming(self):		
		try:
			self.cam.start_recording(self.conn, format='h264')
			self.cam.wait_recording(10)
			self.cam.stop_recording()		
			return True		
		except: 
			print("Unexpected error:", sys.exc_info())						
			self.socket.close()
			return False