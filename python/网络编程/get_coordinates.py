#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python 

from pygeocoder import Geocoder
import requests

def get_geocode(address):
    parm = {'address': address, 'sensor': 'false'}
    base = 'http://maps.google.com//maps/api/geocode/json'
    response = requests.get(base, params=parm)
    ret = response.json()
    print(ret)
    
get_geocode('上海市青浦区佳乐苑224号901室')
