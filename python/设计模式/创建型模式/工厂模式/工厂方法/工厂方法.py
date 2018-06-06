# Author: Jason Lu
import xml.etree.cElementTree as etree
import json

# import xml.etree.cElementTree as ET
#
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
# print(root.tag)

class JSONConnector:

    def __init__(self, filePath):
        self.data = dict()
        with open(filePath, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:

    def __init__(self, filePath):
        self.tree = etree.parse(filePath)

    @property
    def parsed_data(self):
        return self.tree


def connector_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))

    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connector_factory(filepath)
    except ValueError as e:
        print(e)

    return factory


def main():
    jsonFactory = connect_to("jperson.json")
    json_data = jsonFactory.parsed_data
    print(json_data)
    print("found: {} person".format(len(json_data)))
    person = json_data
    print("firstname:", person["firstName"])
    print("lastname:", person["lastName"])
    print("phoneNumber:", person['phoneNumber'])
    [print("phone number ({}) {}".format(p['type'], p['number'])) for p in person['phoneNumber']]

    print()

    xmlFactory = connect_to("person.xml")
    xml_data = xmlFactory.parsed_data
    print(xml_data.getroot())
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Smith'))
    print('found: {} persons'.format(len(liars)))
    print(liars)

    for liar in liars:
        print("first name: {}".format(liar.find('firstName').text))
        print("last name: {}".format(liar.find('lastName').text))
        [print("phone number ({}) {}".format(p.find('type').text, p.find('number').text)) for p in liar.findall('phoneNumber')]

if __name__ == '__main__':
    main()






