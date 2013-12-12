#!/bin/bash

apt-get --purge remove postgresql.* 
rm -r /etc/postgresql
rm -r /etc/postpresql-common
rm -r /var/lib/postgresql
userdel -r postgres
groupdel postgres


#chmod u+rwx to give yourself permission to run this script / 
#for root


#Alternativly, you can have some problems when trying to remove an
#existing postgres installation , here is how you can process to
#solve the problem.

# apt-get --purge remove postgresql.* 
# rm -r /etc/postgresql
# rm -r /etc/postpresql-common
# rm -r /var/lib/postgresql
# userdel -r postgres
# groupdel postgres


apt-get install postgresql postgresql-client
su postgres -c 'psql -c  "create database mypgdb"'


# i am using the feature.py  to add some data
# into db ,so change the password to --test--  see the password
# used by feature.py to access to the database
su postgres -c  "psql -c \"alter user postgres with password 'test';\""

echo reloding
  
/etc/init.d/postgresql reload




