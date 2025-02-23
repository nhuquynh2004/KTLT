import xml.etree.ElementTree as ET
tree = ET.parse( "employees.xml" )
root = tree.getroot()
idSearch=4
newName= "Trần Phạm Mẫn Nhi"
for item in root.findall( 'employee' ):
    id = item.find( 'id' ).text
    if int (id) ==idSearch:
        name = item.find( 'name' )
        name.text=newName
tree.write( 'employees.xml' , encoding= 'utf-8' )