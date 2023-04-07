#! /usr/bin/env python3

#############################################################################
# python 3 script to convert invalid datetime to correct datetime
# where correct date and time are held in different location in file
#
# Copyright University Corporation for Atmospheric Research (2023)
#
# Author: Taylor M. Thomas
#
############################################################################
input_file = "N2022080401.21"
intermediate_file = input_file + "intermediate"
output_file = input_file + "converted"

#initialize empty lists for date and correct_time
list_correct_date = []
list_correct_time = []

#input file
mtp_in = open(input_file, "rt")
for line in mtp_in:
        # check if line begins with IWG1
        # IWG1 contains the correct datetime
    if line.startswith('IWG1'):
        # extract the datetime
        correct_datetime = line[5:20]
        # subset the datetime string to get date
        correct_date = correct_datetime[0:8]
        # append the date string to the date list
        list_correct_date.append(correct_date)
        # subset the datetime string to get the time
        correct_time = correct_datetime[9:11] + ':' + correct_datetime[11:13] + ':' + correct_datetime[13:15]
        # append the time string to the time list
        list_correct_time.append(correct_time)
        print(list_correct_time)
mtp_in.close()

mtp_in2 = open(input_file, "rt")
mtp_out = open(intermediate_file, "wt")

counter= 0
for line in mtp_in2:
    if line.startswith('A'):
        try:
            print(list_correct_date[counter]) 
            # replace with the good date and time
            mtp_out.write(line.replace(line[2:10], list_correct_date[counter]))
            # check to see if you should increment counter again or not
            counter = counter + 1
        except Exception as e:
            print(e)
    else:
        mtp_out.write(line)

#close input and output files
mtp_in2.close()
mtp_out.close()

mtp_in3 = open(intermediate_file, "rt")
mtp_out2 = open(output_file, "wt")

new_counter = 0
for line in mtp_in3:
    if line.startswith('A'):
        print(line[11:19])
        print(list_correct_time[new_counter])
        # replace with the good date and time
        mtp_out2.write(line.replace(line[11:19], list_correct_time[new_counter]))
        # check to see if you should increment counter again or not
        new_counter = new_counter + 1
    else:
        mtp_out2.write(line)

#close input and output files
mtp_in3.close()
mtp_out2.close()
