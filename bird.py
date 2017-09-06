#!/usr/local/bin/python3

class SongBird():
	def __init__(self):
		self.__color = 'red'

	def sing(self):
		self.sound = '456!'
		print (self.sound)

bird = SongBird()
bird.sing()
print (bird._SongBird__color)
bird._SongBird__color = 'blue'
bird.eat = 'aaa'
print (bird.sound)
print (bird.__dict__)
