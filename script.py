#script.py
#
#Author: flourtowel
#Date:   12 Mar 2019
#
#This is the project The Boredless Tourist from codecademy PRO
#

#List of destinations
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

#List for test traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#Function takes in a destination and return the list index from the list destinations
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#Function takes in a traveler and return the index of the travelers location in the list destinations
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

print(test_destination_index)

for destination in destinations:
    print(destination)
