import sys,string

name = raw_input('What is your name?: ')
family_name =  raw_input('What is your family name?: ')
phone =  raw_input('What is your phone number?: ')
home_address = raw_input('What is your home address?: ')
email_address = raw_input('What is your email address?: ')

output_file = open(name.lower()+family_name+'.txt', 'w')
output_file.write(("Your Name is %s \n Your Family Name is %s Your Phone Number is %s \n Your Home Address is %s \n Your Email Address is %s") % (name, family_name, phone, home_address, email_address))
output_file.close()
