Hello, my name is Jeremy Bullis and contained inside this GitHub repository
is the code required for my microservice for CS-361. As well as my communication
contract for my partner and a UML diagram showing how the program will function.

The MicroTides.py program is self-contained and will use data transfer via text files.
It will begin by reading in a date (today's date) or a range of dates (start - end)
in the format of MM/DD/YYYY.

I have included these two text files with sample data pre-loaded so you can get an
idea of what is expected. The date_range.txt file is meant to be changed by the user,
while the tide_info.txt file will change based on that information.

Once the program is executed with a proper date_range.txt file, it will make use of
the NOAA free API CO-OP data web service to request the relevant tide information.
This will be returned to the program in the form of JSON file and will be parsed into
a containing all this information but formatted just a little differently.

At this point the program will finally write the generated output list to a text file
to be used again in the larger user program. It will end without any user input needed

Please refer to the Micro-UML for a visual aid



*Communication Contract:


