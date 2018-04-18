from random import sample, randrange, choice, shuffle
from datetime import timedelta
from string import ascii_uppercase
from faker import Faker

fake = Faker()
amount = [400, 20, 20] #  amounts of passengers, staff, and flights
amount.append(amount[0] / amount[1]) #  max amount of passengers on flight if spread even


def main():
	with open("sample.sql", "w") as f:
		f.write("USE qms;\n\n")

		# passengers
		f.write("DELETE FROM passengers;\n")
		f.write("INSERT INTO passengers (firstname, lastname, dob) VALUES\n")
		i = 0
		for person in people(amount[0]):
			i += 1
			if i < amount[0]:
				f.write("('{}', '{}', '{}'), ".format(person["firstname"], person["lastname"], person["dob"]))
			else:
				f.write("('{}', '{}', '{}');\n".format(person["firstname"], person["lastname"], person["dob"]))

		# employees
		f.write("DELETE FROM staff;\n")
		f.write("INSERT INTO staff (job, pay) VALUES\n")
		for employee in employees(amount[1]):
			if i < amount[1]:
				f.write("('{}', '{}'),\n".format(employee["job"], employee["pay"]))
			else:
				f.write("('{}', '{}');\n".format(employee["job"], employee["pay"]))

		# flights
		f.write("DELETE FROM flights;\n")
		f.write("INSERT INTO flights (destination, departure, arrival) VALUES\n")
		for flight in flights(amount[2]):
			if i < amount[2]:
				f.write("('{}', '{}', '{}'),\n".format(flight["destination"], flight["departure"], flight["arrival"]))
			else:
				f.write("('{}', '{}', '{}');\n".format(flight["destination"], flight["departure"], flight["arrival"]))

		# bookings
		passengers = [range(1, amount[0] + 1)]
		shuffle(passengers)

		i = 0
		for flight in range(amount[2]):
			f.write("INSERT INTO bookings (passenger_id, flight_id) VALUES\n")
			for passenger in range(1, randrange(amount[3] // 1.25, amount[3]) + 1)
				if i < amount[3]:
					f.write("({}, {}), ".format(passenger, flight))
				else:
					f.write("({}, {});\n".format(passenger, flight))
					
				


def people(num=1):
	output = []
	for i in range(num):
		item = dict()

		item["firstname"] = fake.first_name()
		item["lastname"] = fake.last_name()
		item["dob"] = str(fake.date_between(start_date="-40y", end_date="-20y"))
		output.append(item)

	if num > 1:
		return output
	else:
		return output[0]


def employees(num=1):
	output = []
	for i in range(num):
		item = dict()
		jobs = ["Flight Attendant", "Purser"]
		item["job"] = choice(jobs)
		item["pay"] = fake.bothify(text="?#", letters="ABCDE")
		output.append(item)

	if num > 1:
		return output
	else:
		return output[0]


def flights(num=1):
	output = []
	for i in range(num):
		item = dict()

		item["destination"] = "".join(sample(ascii_uppercase, 3))
		depart = fake.future_datetime(end_date="+30d")
		item["departure"] = str(depart)
		# add somewhere between 6-12 hours and 0-60 minutes to get the arrival
		item["arrival"] = str(depart + timedelta(hours=randrange(6, 12), minutes=randrange(0, 60)))
		output.append(item)

	if num > 1:
		return output
	else:
		return output[0]


if __name__ == '__main__':
	main()
