#******************************
# Week12 Example: Parsing XML
# Created by:  Phil White
# Updated on:  04/12/2022, PW
# Description: A basic example of how to work with XML data
#******************************

#%% Imports
import xml.etree.cElementTree as et
import os
import csv

#%% Change your directory 
os.chdir(r'c:/users/phwh9568/geog_4303/week12/data')

#%% open the class.xml file
xml = open('class.xml')

#%% use et.parse to make it into something Python understands:
data = et.parse(xml)

#%% Get the root element of the xml:
root = data.getroot()

print (root)
print (len(root))

#%% Let's examine the first element at index position 0:
person1 = root[0]

print (person1)

#%%
print (person1[0])

#%%
print (person1.attrib)

#%% get the 'firstname' element for the first item:
name = person1.find('firstName')
print (name)

#%% But if you want the actual data value:
print (name.text)

#%% Again for all of them:
firstName = person1.find('firstName').text
lastName = person1.find('lastName').text
role = person1.find('role').text
seat = person1.find('seatPosition').text
age = person1.find('age').text
print (firstName, lastName, role, seat, age)

#%% How do we get everything? Loop!
for person in root:
    print (person.find('firstName').text)
#%%
for person in root:
    print (person.attrib)

# Easy right? (Well, this is an easy file to work with...)

#%% Now let's create a csv and write our xml data into a csv:
newFile = open('people.csv', 'w', newline='')

#%% instantiate the writer object:
writer = csv.writer(newFile)

#%% Write the first row of the csv, which in this case will be a header:
writer.writerow(['id','firstName', 'lastName', 'role', 'seat', 'age'])

#%% Loop through the root and grab the data values for each element using the 
# Same methods as before. Then, write them to a new row in your csv:
for person in root:
    uid = person.attrib['id']
    firstName = person.find('firstName').text
    lastName = person.find('lastName').text
    role = person.find('role').text
    seat = person.find('seatPosition').text
    age = person.find('age').text
    writer.writerow([uid,firstName,lastName,role,seat,age])
    
newFile.close()
