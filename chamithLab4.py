# Course: CIS 117 PythonProgramming
# Name:   Chamith Gamage
# Description:  Programming with Text Data, Files and Exceptions
# Application:  File I/O
# Development Environment:  macOSX 12.4
# Version:  Python 3.10.4
# Date:  09/19/22


# Program Source Statements


# validate if the correct input file is given
# else return an error msg
try:

	# file_in = open("lab3.txt","r")--> wrong file input

	file_in = open("lab4.txt","r")
except:
	print("No input file found!")


# define an opuput file
file_out = open("chamithLab4_out.txt","w")


# define an variable to hold the total value
total = 0

# iterate over the lines of the input file
for line in file_in:

	# filter out the lines only have item and price

	if(":" in line.rstrip()):

		# split line to item and price, asign to variables accodingly
		item_name = line.rstrip().split(":")[0]
		
		# format price to two decimal point flat values.
		item_price = "{:.2f}".format(float(line.rstrip().split(": ")[1]))


		# add price of each item to total
		total += float(item_price)

		# generate correctly alligned line with item name and price.
		line_new = f"{item_name:<15}{item_price:>15}"
		
		# write each line to output file.
		file_out.write(line_new + "\n")


# define data that to be added to final line.
final_line_desc = "Total :"
total_to_print = "{:.2f}".format(total)

# generate correctly alligned final line.
final_line = f"{final_line_desc:<15}{total_to_print:>15}"

# write the final line to output file.
file_out.write(final_line + "\n")


# close both input and ouput files.
file_in.close()
file_out.close()




### output 1(failed, wrong input file given) ## 
'''

chamithgamage@Chamiths-Air lab4 % python3 chamithLab4.py
No input file found!
Traceback (most recent call last):
  File "/Users/chamithgamage/Desktop/CSM- FALL-2022/Python/lab4/
  chamithLab4.py",line 31, in <module>
  for line in file_in:
NameError: name 'file_in' is not defined. Did you mean: 'file_out'?


'''


### output 2 (success)## 
'''
$ chamithLab4_out.txt
Apples                    0.57
Binder paper              2.29
Cheese                    1.59
Mop                       7.50
Scouring pads             5.00
Shampoo                   2.54
Conditioner               2.79
Ice Cream                 5.89
Total :                  28.17



'''
