# Script that runs the sql script in the alx table

# Drop users table
cat scripts/drop_users.sql | mysql -uroot -proot alx

# Create users table
cat 1-country_users.sql | mysql -uroot -proot alx

# Insert data
cat scripts/insert_users_country.sql | mysql -uroot -proot alx

# Display all the users
cat scripts/select_all_users.sql | mysql -uroot -proot alx

