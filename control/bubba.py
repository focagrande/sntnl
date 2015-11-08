from control.exceptions import BubbaException

class Bubba(object):

	def __init__(self):
		pass

	def bang(self):
		raise BubbaException('Bubba Bang!')