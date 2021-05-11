from exc_16.dictionary import Dictionary

states = Dictionary()
states.set("Oregon", "OR")
states.set('Florida', 'FL')
states.set('California', 'CA')
states.set('New York', 'NY')
states.set('Michigan', 'MI')


cities = Dictionary()
cities.set("CA", "San Francisco")
cities.set("MI", "Detroit")
cities.set("FL", "Jacksonville")
cities.set("NY", "New York")
cities.set("OR", "Portland")

print("-" * 10)
print("NY State has %s" % cities.get("NY"))
print("OR State has %s" % cities.get("OR"))

print("-" * 10)
print("Michigan's abbreviation is %s" % states.get("Michigan"))
print("Florida's abbreviation is %s" % states.get("Florida"))

print("-" * 10)
print("Michigan has %s" % cities.get(states.get("Michigan")))
print("Florida has %s" % cities.get(states.get("Florida")))

print("-" * 10)
states.list()

print("-" * 10)
cities.list()

print("-" * 10)
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

city = cities.get("TX", "Does not exist.")
print("The city for the state 'TX' is: %s" % city)
