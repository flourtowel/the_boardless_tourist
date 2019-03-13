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

#Empty list of lists using list comprehesion on the list destinations
attractions = [[] for destination in destinations]

#Function takes in a destination and attraction it coverts the destination to an index of the list
#destinations. Then it adds the attraction in the form (location,[attraction, [category]]) to the
#attractions list
def add_attraction(destination, attraction):
	#TODO: We are ignoring the case where the passed destination isn't in the destinatino list
	try:
		destination_index = get_destination_index(destination)
	except ValueError:
		print("That destination isn't available yet.")
		return
	attractions_for_destination = attractions[destination_index]
	attractions_for_destination.append(attraction)
	return

#Adding attractions or the attractions list using the add_attraction function
add_attraction('Los Angeles, USA', ['Venic Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])
print(la_arts)
