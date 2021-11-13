import sys, socket

from ServerWorker import ServerWorker

class Server:	
	
	def main(self):
		try:
			SERVER_PORT = int(sys.argv[1])
		except:
			print("[Usage: Server.py Server_port]\n")
		rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# regis socket name, '' = localhost
		rtspSocket.bind(('', SERVER_PORT))
		# maximum 5 connections
		rtspSocket.listen(5)        

		# Receive client info (address,port) through RTSP/TCP session
		while True:
			clientInfo = {}
			# rtspSocket {ClientConnect, ClientAddress}
			clientInfo['rtspSocket'] = rtspSocket.accept()
			ServerWorker(clientInfo).run()		

if __name__ == "__main__":
	(Server()).main()


