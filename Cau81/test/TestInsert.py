import xml.etree.ElementTree as ET
tree = ET.parse( "employees.xml" )
root = tree.getroot()
emp = ET.Element( "employee" )
empId = ET.Element( "id" )
empId.text= '113'
emp.append(empId)
empName = ET.Element( "name" )
empName.text= "Trần Duy Thanh"
emp.append(empName)
root.append(emp)
tree.write( 'employees.xml' , encoding= 'utf-8' )