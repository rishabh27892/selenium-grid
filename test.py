import os
import sys

try:
    if (os.environ['TEST']):
        variable = str(os.environ['TEST'])
        if (str(os.environ['TEST']) == "true"):
            print ("3rd the value of Test is " + str(os.environ['TEST']))
        else:
            print ("4th the value of Test is " + str(os.environ['TEST']))
except:
    print ("Running post admin_login only ! Exception: " + str(sys.exc_info()))


