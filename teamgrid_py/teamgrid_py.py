#       _                         __    __           __   __      __         __
#      (_)___  ____  ____  __  __/ /_  / /___ ______/ /__/ /___ _/ /_  ___  / /
#     / / __ \/ __ \/ __ \/ / / / __ \/ / __ `/ ___/ //_/ / __ `/ __ \/ _ \/ / 
#    / / /_/ / / / / / / / /_/ / /_/ / / /_/ / /__/ ,< / / /_/ / /_/ /  __/ /  
# __/ /\____/_/ /_/_/ /_/\__, /_.___/_/\__,_/\___/_/|_/_/\__,_/_.___/\___/_/   
#/___/                  /____/                                                 
#
#
# author: Johannes Kunze
# date: 2018-05-01   
# web: http://www.jonnyblacklabel.de/
# twitter: @jonnyblacklabel
# 

from .base import TeamGridPyBase
from .endpoints import Users, Times, Tasks, Projects, Teams, Contacts

class TeamGridPy():
	"""Teamgrid API
	
	Make calls to Teamgrid API

	Usage
	=====
	from teamgrid_py import TeamGridPy

	api_key = 'your api key'
	tgpy = TeamGridPy(api_key, verbose=True)

	user = tgpy.users().where(email='someone@example.com').get()
	"""

	def __init__(self, api_key, *args, **kwargs):

		self.__client = TeamGridPyBase(api_key, *args, **kwargs)


	def users(self):
		return Users(self.__client)
	def times(self):
		return Times(self.__client)
	def tasks(self):
		return Tasks(self.__client)
	def teams(self):
		return Teams(self.__client)
	def contacts(self):
		return Contacts(self.__client)
	def projects(self):
		return Projects(self.__client)




if __name__ == '__main__':
	pass