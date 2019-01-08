import re
import pprint

dt = open("FastFoodRestaurants.csv")
dt.readline()
line_num = 1


def getel(line):
    result = re.split(r",", line, maxsplit=1)
    element = result[0].strip("\"")
    return element, result[1]


def getaddress(line):
    address, line = getel(line)
    return address, line


def getcity(line):
    city, line = getel(line)
    return city, line


def getcountry(line):
    country, line = getel(line)
    return country, line


def getkeys(line):
    keys, line = getel(line)
    return keys, line


def getlatitude(line):
    latitude, line = getel(line)
    return latitude, line


def getlongitude(line):
    longitude, line = getel(line)
    return longitude, line


dataset = {}
for line in dt:
    line = line.strip().rstrip()
    address, line = getaddress(line)
    city, line = getcity(line)
    country, line = getcountry(line)
    keys, line = getkeys(line)
    latitude, line = getlatitude(line)
    if keys[9:30] in latitude:
        latitude, line = getlatitude(line)
    longitude, line = getlongitude(line)
#    print(line_num, country, keys, latitude, longitude)
    line_num += 1
    if country not in dataset:
        dataset[country] = {}
    if keys not in dataset[country]:
        dataset[country][keys] = dict()
    if latitude not in dataset[country][keys]:
        dataset[country][keys][latitude] = dict()
    dataset[country][keys][latitude] = longitude

pprint.pprint(dataset)
dt.close()
