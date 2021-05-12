import pytest

from exc_16.dictionary import Dictionary

@pytest.fixture
def states_dict():
    states = Dictionary()
    states.set("Oregon", "OR")
    states.set('Florida', 'FL')
    states.set('California', 'CA')
    states.set('New York', 'NY')
    states.set('Michigan', 'MI')
    return states


@pytest.fixture
def cities_dict():
    cities = Dictionary()
    cities.set("CA", "San Francisco")
    cities.set("MI", "Detroit")
    cities.set("FL", "Jacksonville")
    cities.set("NY", "New York")
    cities.set("OR", "Portland")

    return cities

def test_dictionary_set_and_get_values(states_dict):
    assert states_dict.get("Oregon") == "OR"
    assert states_dict.get("Florida") == "FL"
    assert states_dict.get("California") == "CA"
    assert states_dict.get("New York") == "NY"
    assert states_dict.get("Michigan") == "MI"


def test_dictionary_can_get_based_on_get_from_different_dict(states_dict, cities_dict):
    assert cities_dict.get(states_dict.get("Michigan")) == "Detroit"
    assert cities_dict.get(states_dict.get("Florida")) == "Jacksonville"

    
def test_dictionary_list(states_dict, cities_dict):
    states_dict.list()
    cities_dict.list()

def test_dicitionary_no_key(states_dict):
     assert states_dict.get("Texas") is None

def test_dicitionary_key_returns_default_value(cities_dict):
    default_value = "Does not exist."
    assert default_value == cities_dict.get("TX", default_value)
