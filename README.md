# SQL-to-GS-Automation
A script to run a SQL query and paste it into a Google Sheet

Please read the Requirements and follow the instructions below before running.

If you're not using Environmental Variables, enter your RedShift username and password into the db_credentials file

Get your own client-secret.json file by following the tutorial here:
https://blog.getcensus.com/how-to-hack-it-moving-customer-data-from-postgres-to-google-sheets-with-python/

Change the path of the service file on main.py to the path for your client-secret.json
Change the path for the User json files to match yours.

Main.py is where you start. This will open the Google Sheet, clear the contents, and access the User specific SQL saved in the USERNAME.json files.
This will flow to the Data.py file which will run the redshift connection and the SQL query.
Finally this returns to Main.py which will add the timestamp and inform you of completion.
