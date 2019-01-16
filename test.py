import os
import sys

try:
    if (os.environ['TEST'] == True):
        print ("1st the value of Test is " + str(os.environ['TEST']))
    if (os.environ['TEST'] is True):
        print ("2nd the value of Test is " + str(os.environ['TEST']))
    if (os.environ['TEST']):
        print ("3rd the value of Test is " + str(os.environ['TEST']))
    if (os.environ['TEST'] == False):
        print ("4th the value of Test is " + str(os.environ['TEST']))
    if (os.environ['TEST'] is False):
        print ("5th the value of Test is " + str(os.environ['TEST']))
    if (os.environ['TEST' != True]):
        print ("6th the value of Test is " + str(os.environ['TEST']))

except:
    print ("Running post admin_login only ! Exception: " + str(sys.exc_info()))


