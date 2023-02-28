# Alissa Sheikh 1623952

# a.
# Write a program that reads dates from input, one date per line. Each date's format must be as follows:
# March 1, 1990. Any date not following that format is incorrect and should be ignored. Use the find() method to
# parse the string and extract the date. The input ends with -1 on a line alone. Use the datetime module to get the
# current date. Ignore any dates that are later than the current date. Output each correct date as: 3/1/1990.

# b.
# After the program is working as above, modify the program so that it reads all dates from an input file
# “inputDates.txt” (an Example file is attached).

# c.
# Modify your program further so that after parsing all dates from the input file “inputDates.txt”, it writes out the
# correct ones into an output file called: “parsedDates.txt”. Reference : https://www.chegg.com/homework-help/questions-
# and-answers/programming-python-write-basic-program-performs-simple-file-mathematical-operations-write--q51831988?
# trackid=41dab4ef9d43&strackid=553c464df60b





# Create a dictionary to store months and values
month_dictionary = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
# Open parsedDates.txt & inputDates.txt
try:
    outFile = open('parsedDates.txt', 'w')
    with open('inputDates.txt', 'r') as file:

        # Loop for each date in file
        for date in file:
            date = date.strip()
            # If date is -1
            if date == '-1':
                break

            # Find the index
            monthindex = date.find(" ")
            dayindex = date[monthindex + 1:].find(", ")

            # If the month index and day index is not -1
            if monthindex != -1 and dayindex != -1:
                # extract from string for each
                month = date[:monthindex]
                day = date[monthindex + 1:][:dayindex]
                year = date[monthindex + 1:][dayindex + 2:]
                monthNum = month_dictionary[month]
                outFile.write(str(monthNum) + '/' + day + '/' + year + '\n')
except FileNotFoundError:
    print('Error')
