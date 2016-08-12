from app import db

class Students(db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	city = db.Column(db.String(50))
	addr = db.Column(db.String(200))
	pin = db.Column(db.String(10))



	def __init__(self, name, city, addr, pin):
		self.name = name
		self.city = city
		self.addr = addr
		self.pin = pin