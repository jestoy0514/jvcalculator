#!/usr/bin/env python3
#
#  jvparser.py
#
#  Copyright (c) 2015 Jesus Vedasto Olazo <jessie.olazo@mail.com>
#
#  License: General Public License version 2

"""

The intention of this module was to provide easy
access to eval() function capabilities like
mathematical computation. It is originally for
created for a simple calculator so that it will
be very easy to integrate into a GUI application
like that tkinter module.

Ex:

>>> from jvparser import JVParser
>>> #  Print the result 9.
>>> JVParser("4+2+3").calculate()
9
>>>

Ex: This time using eval()

>>> eval("4+2+3")
9
>>>

"""

from time import time

class JVParser:

    def __init__(self, inp_string):
        self.inp_string = inp_string

    def make_list(self):
        #  Check whether the start of the string is negative.
        if self.inp_string[0] == "-":
            temp_str = "-"
            self.inp_string = self.inp_string[1:]
        else:
            temp_str = ""
        
        temp_list = []
        for char in self.inp_string:
            if char in "0123456789.":
                temp_str = temp_str + char
            elif char in "+-/*":
                temp_list.append(temp_str)
                temp_list.append(char)
                temp_str = ""
        temp_list.append(temp_str)
        return temp_list

    def calculate(self):
        #  Convert the string to list for further breakdown.
        mylist = self.make_list()

        if len(mylist) == 1:
            result = float(mylist[0])
            if int(result) != 0:
                if result/int(result) > 1:
                    return result
                elif result/int(result) == 1:
                    return int(result)
            else:
                return result

        #  The oper variable will be used to determine which operator to use in the created sub equation.
        oper = ""
        #  Loop to the mylist to be able to breakdown it into smaller pieces.
        while True:
            counter = 0
            #  Test if the below given operators is available in the sub equation.
            #  If available it will generate the position of the operator and which operator will be using.
            if "*" in mylist and "/" in mylist:
                pos_mul = mylist.index("*")
                pos_div = mylist.index("/")
                if pos_mul < pos_div:
                    pos = pos_mul
                    oper = "mul"
                else:
                    pos = pos_div
                    oper = "div"
            elif "*" in mylist:
                pos = mylist.index("*")
                oper = "mul"
            elif "/" in mylist:
                pos = mylist.index("/")
                oper = "div"
            elif "+" in mylist and "-" in mylist:
                pos_add = mylist.index("+")
                pos_sub = mylist.index("-")
                if pos_add < pos_sub:
                    pos = pos_add
                    oper = "add"
                else:
                    pos = pos_sub
                    oper = "sub"
            elif "+" in mylist:
                pos = mylist.index("+")
                oper = "add"
            elif "-" in mylist:
                pos = mylist.index("-")
                oper = "sub"
            
            #  Create a temporary list.
            another_list = []
            another_list.append(mylist[pos-1])
            another_list.append(mylist[pos])
            another_list.append(mylist[pos+1])

            #  Variable for remebering the possiton where the new value will be inserted inside mylist list.
            rem_pos = pos - 1

            #  Operations which will be used with respect to variable oper.
            if oper == "mul":
                num1 = float(mylist[pos-1])
                num2 = float(mylist[pos+1])
                ans = str(num1 * num2)
            elif oper == "div":
                num1 = float(mylist[pos-1])
                num2 = float(mylist[pos+1])
                ans = str(num1 / num2)
            elif oper == "add":
                num1 = float(mylist[pos-1])
                num2 = float(mylist[pos+1])
                ans = str(num1 + num2)
            elif oper == "sub":
                num1 = float(mylist[pos-1])
                num2 = float(mylist[pos+1])
                ans = str(num1 - num2)
        
            #  Delete the elements inside mylist to make way
            #  to the newly created result.
            del mylist[pos]
            del mylist[pos]
            del mylist[pos-1]

            #  Insert the result of the operation in mylist.
            mylist.insert(rem_pos, ans)
            another_list = []

            #  Loop through the mylist to record the number of elements inside.
            for char in mylist:
                if char in "*/+-":
                    counter += 1

            #  Test whether counter is equal to zero, if yes exit from the loop.
            if counter == 0:
                break

        result = float(mylist[0])

        if int(result) != 0:
            if result/int(result) > 1:
                return result
            elif result/int(result) == 1:
                return int(result)
        else:
            return result

def main():
    str_inp = "4+2+3*45/400-56"
    time1 = time()
    print("JVParser:", JVParser(str_inp).calculate())
    time2 = time()
    print(time2-time1)
    time3 = time()
    print("Eval:", eval(str_inp))
    time4 = time()
    print(time4-time3)


#  Standard Boilerplate Template
if __name__ == "__main__":
    main()
