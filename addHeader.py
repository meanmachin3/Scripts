import os


def addHeader(filename):
	with open(filename, "r+") as f:
		old = f.read()
		f.seek(0)
		f.write(headerToAppend + old)



for filename in os.listdir(os.getcwd()):
	headerToAppend = """/**
 * --------------------------------------------------------------------------------------------------
 * 							COMPANY NAME
 * 
 * Product				: 
 * Application			: 
 * Module				: 
 * File					: """+ filename +"""
 * Author				: 
 * Date(DD/MM/YYYY)		: 
 * Purpose				: 
 * 
 * Functions Defined	:
 * 
 * EXPORTED FUNCTIONS
 * 
 * LOCAL FUNCTIONS
 * 
 * Change History
 * Date:				Name:  					Comment:
 * --------------------------------------------------------------------------------------------------
 * 						
 * -------------------------------------------------------------------------------------------------- 
 */
 """
	addHeader(filename)
