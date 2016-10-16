#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import math
from poi_email_addresses import poiEmails

knownEmails = poiEmails()
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "Number of People:", len(enron_data)
print "Number of Features:", len(enron_data["SKILLING JEFFREY K"])
print "Avaliable features:", dict.keys(enron_data["SKILLING JEFFREY K"])

poiNum = 0
peopleWithSalary = 0
peopleWithKnownEmail = 0
peopleWithTotalPayments = 0
poiWithTotalPayments = 0
for people in enron_data:
    if (enron_data[people]["poi"] == 1):
        poiNum+=1
    if (enron_data[people]["salary"] != "NaN"):
        peopleWithSalary+=1
    if (enron_data[people]["email_address"] in knownEmails):
        peopleWithKnownEmail+=1
    if (enron_data[people]["total_payments"] != "NaN"):
        peopleWithTotalPayments+=1
        if(enron_data[people]["poi"] == 1):
            poiWithTotalPayments+=1
print "Number of POI:", poiNum

poiNum = 0
poi_names = open('../final_project/poi_names.txt')
for line in poi_names:
    if "," in line:
        poiNum+=1
print "Number of POI in total:", poiNum

print "Total value of James Prentice's stock:", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Messages from Wesley Colwell to POI:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Stock exercised by Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Total payment of Kenneth Lay:", enron_data["LAY KENNETH L"]["total_payments"]
print "Total payment of Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Total payment of Andrew Fastow:", enron_data["FASTOW ANDREW S"]["total_payments"]
print "Total number of people with quantified salary:", peopleWithSalary
print "Total number of people with known email:",peopleWithKnownEmail
print "Total number of people with non-zero total payments:", peopleWithTotalPayments
print "Total number of POI with non-zero total payments:", poiWithTotalPayments
