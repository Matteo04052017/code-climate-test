# -*- coding: utf-8 -*-

"""Define function placeholders and test function examples."""


# TODO: Replace all the following code with the desired functionality for the package
def example():
    """Example: Define non return function for subsequent test."""


def testing_example():
    """Example: Define function for subsequent test with specific return value."""
    return 2

	
def crazy_posting_api(value):
	if value:
		return 0
	return 1
	
	
def crazy_posting_api2(value, value1, value2, value3, value4, value5, value6):
	if value:
		return 0
	return 1
	
class CrazyApiConsumer(object):
	def __init__(self, value):
		self.value = value
		
	def post(self):
		z = 10000
		response = crazy_posting_api(self.value)
		return not bool(response)
	
cac1 = CrazyApiConsumer("hello")
print(cac1.post())
cac2 = CrazyApiConsumer("")
print(cac2.post())
		