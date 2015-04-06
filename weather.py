#!/bin/usr/env python
import urllib
import json
import webbrowser
""" Function holds dictionary with Contry to name mapping and vice versa."""

def country_name(name):
	#print name
	dict={'IN': 'India','UK': 'London','US':'United Sates','Australia': 'Australia','india':'in','London':'UK','United Sates':'US'}
	print "Country :", dict.get(name)

"""" The main Function where city and country code is passed to the api to fetch the weather details. """"

def weather_today(input1,input2):
	print "Fetching Data....."
	print "================================="
	#API call
	request=urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+input1 +","+input2) 
	output=request.read()
	request.close()	
	#Response from API is a json 
	json_objects=json.loads(output)
	#Extracting required information fro json like max , min temperatures, Description of today weather etc..
	country=json_objects.get('sys')
	tofun=country.get('country')
	country_name(tofun)
	description=json_objects.get('weather')
	minnmax=json_objects.get('main')	
	print "City: " ,json_objects.get('name')
	print "Howz it Today?:" ,
	print description[0].get('description')
	print "Maximum Temperature:", (minnmax.get('temp_max'))/10
	print "Minimum Temperature:", (minnmax.get('temp_min'))/10
	
""" This is where the program interacts with user to get inputs like city and country. """
def input_to_program():
	print "Please Enter the State for which you need the weather report"
	input1=raw_input()
	print "Please Enter the Country which the state belongs to"
	input2=raw_input()
	weather_today(input1,input2)
input_to_program()

