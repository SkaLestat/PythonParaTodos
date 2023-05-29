import xml.etree.ElementTree as ET

data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>
'''
tree = ET.fromstring(data)
# print(tree)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))

data2 = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>'''
stuff = ET.fromstring(data2)
lst = stuff.findall("users/user")
print("User count:", len(lst))
for user in lst :
    # print("Name", user.attrib)
    print("Name", user.find("name").text)
    print("ID", user.find("id").text)
    print("Attribute", user.get("x"))
