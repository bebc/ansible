#!/usr/bin/python



class SongBird():
	def sing(self):
		self.sound = '456!'
		print self.sound

bird = SongBird()
bird.sing()
print bird.sound
print bird.__dict__
