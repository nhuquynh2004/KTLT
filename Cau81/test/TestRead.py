import xml.etree.ElementTree as ET

from models.Employee import Employee

tree = ET.parse("employees.xml")
root = tree.getroot()
for item in root.findall( 'employee' ):
    id = item.find( 'id' ).text
    name = item.find( 'name' ).text
    emp=Employee( int (id),name)
    print (emp)