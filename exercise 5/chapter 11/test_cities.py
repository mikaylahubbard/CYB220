#! /usr/bin/python3
#11.1 city country
from chapter11 import *
def test_city_country():
    """test the city_county function with Paris, France"""
    formatted = city_country("paris", "france")
    assert formatted == "Paris, France"
    
#11.2 population
def test_city_country_popualtion():
    """test the city_country_population function"""
    formatted = city_country_population("santiago", "chile", 5000000)
    assert formatted == "Santiago, Chile - population: 5000000"
