 Please check for python version i was using 3.8 and also created virtual environment of same with name cartenv

please install all the requirements which are present in requirements.txt

once done please add your database name, user name and password once just apply command 
python manage.py migrate ........to create all the tables 

also im sharing mydb.json file for your convience of data to test.
commands would be 
python manage.py loaddata mydb.json to load complete data present in json file to your database.
=============================================================================

I have Created 2 models one for Products and one for order

in views of index retreving all the data present in database 
and showing in form of datatable using js library

added functionality of plus and minus so that one can easliy add and remove product


also have created customized product view in admin panel using import export module.
