def main():
	init_date = "01/01/1900"
	init_year = int(init_date[6:])
	init_month = int(init_date[3:5])
	init_day = int(init_date[6:])
	start_day = "Monday"
	print("Name:")
	name = input()
	print("Date:")
	dob = input()
	year = int(dob[6:])
	month = int(dob[3:5])
	day = int(dob[:2])
	list_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

	if year < init_year:
		start_day = "invalid date"
	else:
		if month == 2:
			if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
				if day > 29:
					start_day = "invalid date"
			else:
				if day > 28:
					start_day = "invalid date"
		elif month == 4 or month == 6 or month == 9 or month == 11:
			if day > 30:
				start_day = "invalid date"
		elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
			if day > 31:
				start_day = "invalid date"

	if start_day != "invalid date":
		for i in range(init_year, year):
			if (i % 400 == 0) or ((i % 4 == 0) and (i % 100 != 0)):
				num_days = 2
				start_day = list_days[(list_days.index(start_day) + num_days) % 7]
			else:
				num_days = 1	
				start_day = list_days[(list_days.index(start_day) + num_days) % 7]

		for i in range(1, month):
			if i == 2:
				if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
					num_days = 1
					start_day = list_days[(list_days.index(start_day) + num_days) % 7]
			elif i == 4 or i == 6 or i == 9 or i == 11:
				num_days = 2
				start_day = list_days[(list_days.index(start_day) + num_days) % 7]
			elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
				num_days = 3
				start_day = list_days[(list_days.index(start_day) + num_days) % 7]

		num_days = day % 7 - 1;
		start_day = list_days[(list_days.index(start_day) + num_days) % 7]
		print("Hello", name, ", you were born on a", start_day)
	else:
		print("Hello", name, ",", start_day)

if __name__ == '__main__':
        main()