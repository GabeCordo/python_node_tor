import node
from pynodetor.utils import linkerJSON
from pynodetor.bitstream import basic

class Balancer(node.Node, linkerJSON.Handler):
	
	def __init__(self, ip, directoryKeyPrivate, directoryKeyPublic, nodesJSON):
		'''(Balancer, list of strings) -> None
			:constuctor for the Balancer class takes a list of ip-addresses 
			 representing the available entry Nodes.
		'''
		node.Node.__init__(self, ip, directoryKeyPrivate, directoryKeyPublic)
		linkerJSON.Handler.__init(self, nodesJSON)
		
		self.entryNodes = self.data[0]
		self.trackers = [0] * len(entryNodes)
	
	def track(self, ip):
		'''(Balancer, string) -> (string)
		'''
		index = self.entryNodes.index(ip)
		return self.trackers[index]
		
	def redirect(self):
		'''(Balancer) -> (string)
		'''
		index = self.trackers.index( min( self.trackers ) )
		self.trackers[index] = self.trackers[index] + 1
		return self.entryNodes[index]
		
	def synatxValidator(self, message):
		'''(Balancer, string) -> (boolean)
		'''
		check = basic.Parser(message)
	
	def specialFunctionality(self, message, connectingAddress):
		'''(Balancer, string, string) -> (boolean)
		'''
		try:
			self.synatxValidator(message)
			entry = self.redirect()
			#if the syntax is valid and we have a new entry node, send the message into the network
			self.send(entry, message)
		except:
			print(f'Console: Received bad reciept from {connectingAddress}')
		#we always want this to return False, there is NO need to have any other functionality
		return False