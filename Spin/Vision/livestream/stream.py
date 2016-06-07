import socket
import sys

class LiveStream:		
	socket = socket.socket()		
	conn = 0

	def __init__(self, camera):
		self.cam = camera

	# Set up the socket and wait for connection
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

	# To be used in a loop, returns true while streaming
	def streaming(self):		
		try:
			self.cam.start_recording(self.conn, format='h264')
			self.cam.wait_recording(1)
			self.cam.stop_recording()		
			return True		
		except socket.error, e:
			 print "Connection terminated"
		except KeyboardInterrupt, e:
			print "Connection terminated by server"
		except: 
			print("Unexpected error:", sys.exc_info())						
			self.socket.close()
			return False