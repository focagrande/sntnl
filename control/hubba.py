import random

from control.exceptions import HubbaException

class Hubba(object):

	def __init__(self):
		pass

	def bang(self):
		raise HubbaException('Hubba Bang! {}'.format(random.randint(0, 999)))