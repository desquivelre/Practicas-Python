# ---------------------------------------------------------------------------------------------------------------
# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

# Desired Output 
# 0.8475
# ---------------------------------------------------------------------------------------------------------------

# OPCION 1

# text = "X-DSPAM-Confidence:    0.8475"

# pos = int(len(text)) - 6
# num = float(text[pos:pos+6])

# print(num)

# OPCION 2

# text = "X-DSPAM-Confidence:    0.8475"

# pos = text.find("0")
# num = float(text[pos:pos+6])

# print(num)

# ---------------------------------------------------------------------------------------------------------------
# write any code you like in the window below. There are three files loaded and ready for you to open if you want to do file processing: "texto.txt".
# ---------------------------------------------------------------------------------------------------------------

# file_open = open("texto.txt", "r")

# count = 0

# for line in file_open:
#     print(line.strip())
#     count += 1
# print("\nEl texto tiene " + str(count) + " líneas")

# ---------------------------------------------------------------------------------------------------------------
# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
# ---------------------------------------------------------------------------------------------------------------

# fname = input("Enter file name: ")
# fh = open(fname)

# for line in fh:
#     print(line.upper().strip())

# ---------------------------------------------------------------------------------------------------------------
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

# Desired Output
# Average spam confidence: 0.7507185185185187
# ---------------------------------------------------------------------------------------------------------------

# fname = input("Enter file name: ")
# fh = open(fname)

# num = 0.0
# count = 0.0

# for line in fh:
#     if line.startswith("X-DSPAM-Confidence:"):
#         pos = line.find(":")
#         num += float(line[pos+2:pos+8])
#         count += 1

# prom = num / count
# print("Average spam confidence: " + str(prom))

# ---------------------------------------------------------------------------------------------------------------
# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# Desired Output
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
# ---------------------------------------------------------------------------------------------------------------

# fname = open("romeo.txt")
# list_text = list()

# for line in fname:
#     linea = line.strip().split()
#     for element in linea:
#         if element in list_text:
#             continue
#         else:
#             list_text.append(element)

# list_text.sort()
# print(list_text)

# ---------------------------------------------------------------------------------------------------------------
# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Desired Output
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# rjlowe@iupui.edu
# zqian@umich.edu
# rjlowe@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# gsilver@umich.edu
# gsilver@umich.edu
# zqian@umich.edu
# gsilver@umich.edu
# wagnermr@iupui.edu
# zqian@umich.edu
# antranig@caret.cam.ac.uk
# gopal.ramasammycook@gmail.com
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# louis@media.berkeley.edu
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word
# ---------------------------------------------------------------------------------------------------------------

# fname = open("mbox-short.txt")

# lst = list()
# contador = 0

# for line in fname:
#     if line.startswith("From "):
#       linea = line.strip().split()
#       lst.append(linea[1])
#       print(linea[1])
#       contador += 1

# print("There were " + str(contador) + " lines in the file with From as the first word")

# ---------------------------------------------------------------------------------------------------------------
# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Desired Output
# cwen@iupui.edu 5
# ---------------------------------------------------------------------------------------------------------------

# fname = open("mbox-short.txt")

# dtc = dict()
# update_dtc = dict()

# for line in fname:
#     if line.startswith("From "):
#       linea = line.strip().split()
#       if linea[1] in dtc:
#         update_dtc[linea[1]] = int(dtc.get(linea[1])) + 1
#         dtc.update(update_dtc)
#       else:
#         update_dtc[linea[1]] = 1
#         dtc.update(update_dtc)

# max_value = max(dtc.values())

# for element in dtc:
#     if dtc[element] == max_value:
#         correo = element
#         result = dtc.get(element)

# print(str(correo) + " " + str(result))

# ---------------------------------------------------------------------------------------------------------------
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Desired Output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
# ---------------------------------------------------------------------------------------------------------------

# fname = open("mbox-short.txt")

# lst = dict()
# lst_hours = list()

# for line in fname:
#     if line.startswith("From "):
#      linea = line.strip().split()
#      hour_variable = linea[5]
#      lst[hour_variable[0:2]] = lst.get(hour_variable[0:2], 0) + 1

# lst_sorteded = sorted(lst.items())

# for key, value in lst_sorteded:
#     print(key, value)

# ---------------------------------------------------------------------------------------------------------------
# Library re
# Sirve para que a través del texto puede realizar ciertas funciones
# ---------------------------------------------------------------------------------------------------------------

# import re

# hand = open("bigtext.txt")
# x=list()
# for line in hand:
#      y = re.findall('[0-9]+',line)
#      x = x+y

# sum=0
# for z in x:
#     sum = sum + int(z)

# print(sum)

# ---------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------

# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if data is None:
#         break
#     print(data.decode(),end='')

# mysock.close()

#--------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------

