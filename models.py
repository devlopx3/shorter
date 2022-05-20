from run import db


class url_data(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original_url = db.Column(db.String(200), unique=True, nullable=False)
	short_url = db.Column(db.String(6), unique=True)
	visits = db.Column(db.Integer, default=0)




	def __repr__(self):
		return f"urls_data'{self.original_url}','{self.short_url}',{self.visits}"

class info(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	userIP = db.Column(db.String(50), nullable=False)
	country = db.Column(db.String(50), nullable=False)
	city = db.Column(db.String(50), nullable=False)
	for_short = db.Column(db.String(50), nullable=False)
	time = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		return f"info'{self.userIP}','{self.country}',{self.city},'{self.for_short}','{self.time}'"