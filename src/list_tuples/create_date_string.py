

# create string of date using input of year, month, date

month_list = [

    "january",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

date_endings =    ["st", "nd", "rd"]+ 17 * ["th"]\
    + ["st", "nd", "rd"]+ 7 * ["th"]\
    + ["st"]




print month_list
print date_endings

year = raw_input("Enter current year: ")

month= raw_input("Enter current month: ")

date = raw_input("Enter current Date: ")

# convert  raw data to int

month_number = int (month)

date_number = int (date)

print "entered Date= ", date, "  month= ", month_number

month_name = month_list[month_number -1]

ordinal = date + date_endings[date_number - 1]

complete_date = month_name+ " " + ordinal + ", "+ year

print complete_date
