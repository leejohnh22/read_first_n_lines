# John Lee		4/18/2019
# Last updated	5/4/2019
# Read first n lines of a file where n is specified by the user

# Input
#	num_lines_to_read (number of lines to read, specified by user)
# Output
#	write to standard out lines read

# Import libraries
import IOExceptions

def main():
	# initialize variables
	file_name = ''
	opened_file = ''
	file_mode = 'r'
	num_lines_to_read = 0
	num_lines_in_file = 0
	result = 1

	# Ask user what is the name of text file
	file_name = input("What is the name of the file to read? ")

	# Try opening the file, make sure it can be read
	result = IOExceptions.open_file(file_name, file_mode)

	if result == 0:
		with open(file_name, file_mode) as opened_file:

			# Count the number of lines in the file
			num_lines_in_file = count_num_lines(opened_file)

			# Get number of lines to read from user
			num_lines_to_read = input("Enter number of lines to be read from the file : ")

			# Error check
			# Make sure it is a digit
			while num_lines_to_read.isdigit() == False:
				num_lines_to_read = input("Please enter a digit : ")

			# Make sure it is not negative
			while int(num_lines_to_read) <= 0:
				num_lines_to_read = input("Please enter a number greater than 0 : ")

			# Make sure it does not exceed the number of lines in the file itself
			while int(num_lines_to_read) > num_lines_in_file:
				num_lines_to_read = input("This file contains %i lines. Enter number less than or equal to %i : " % ( num_lines_in_file, num_lines_in_file))
			
			print()
			# Read n number of lines in the file and print to stdout
			read_and_print_lines(opened_file, int(num_lines_to_read))

		# Close file
	
# Define function to count num lines in a file
# Return number of lines in file
def count_num_lines(file):
	num_lines = sum(1 for line in file)
	return num_lines

# Define function to read n number of lines and print to stdout
def read_and_print_lines(file, num_lines):
	# Set read pointer to top of file
	file.seek(0)
	# Read and print number of lines specified
	for i in range(num_lines + 1):
		line = file.readline().rstrip('\n')
		print(line)

	print()

# Run program
main()

# END OF PROGRAM