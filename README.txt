CSCE 828 Project 2
Derek Weitzel

src/pyCFL.py
    This file is the python source of the Context free language parser
    It takes input from stdin, sending to stdout.
    
tests/*
    This directory contains the tests that where distributed on the class
    website.
    
Building Instructions:
Since the program is written in python, there is no building required.


Execution Instructions:
Run the program by invoking the script with python:
python src/pyCFL.py < input.txt

The program will read in the context free language in the first few lines of 
input. Each successive line will be treated as input that will be fed into the 
context free language parser.  


This parser iteratively parses the string.  When it encounters a variable, it 
creates a new PDA instance for each variable's rule, and continues parsing.
When it encounters an situation it cannot resolve, such as a constant that 
doesn't match the string, it will terminate the pda execution.

