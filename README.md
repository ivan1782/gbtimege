# test globant
##
To run ..
1.- clone te repository
2.- open terminal 
3.- acces to path proyect into terminal 
3.- run this command into the terminal --> docker compose up
4.- the image start to build and create the database if not exists and run the app to load the csv files to the database previuosly created and run the backup avreo files into image path, you can see the log into the terminal.

ASSETS:
1.- docker-compose.yml : this document provide configuration of the applications and create the network to comunicate between the services
2.- mysql folder : 
  2.1.- dockerfile : Create the nysql image and copy files into the container
  2.1.- database.sql : inizalizate the database to use, if you need create a previos tablas you cluld use this script, for this case is not necesary
3.- python folder:
  3.1- dockerfile : run the image and copy jars into the container repository to run after create the image.
  3.2- app.py: this app read csv, write into the mysql database and create a backup avro files into the image container.
  3.3- csv files: csv files to load.
  3.4- jar's to create the connection with mysql and generate the avro files to backup.

