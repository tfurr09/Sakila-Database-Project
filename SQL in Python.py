#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Author: Taylor Furry
# Date: 11/7/2022


# In[1]:


import pymysql
import pandas as pd


# In[2]:


db = pymysql.connect(host = "localhost",user = "root", password = "rootroot",database = "sakila" )

cursor = db.cursor()


# In[3]:


# a) Show the list of databases.
# SHOW databases; is how I would do this in mysql but since I had to connect to a database earlier, I'm not sure I can actually do this in python


# In[4]:


# b) Select sakila database.
# USE sakila; Same as cell above. I don't think I could actually do this in python since I have already connected to sakila in cell 2


# In[5]:


# c) Show all tables in the sakila database.

sql = "SHOW TABLES"
cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'table'})


# In[6]:


# d) Show each of the columns along with their data types for the actor table.
sql = "SHOW COLUMNS FROM actor"
cursor.execute(sql)

myresult = cursor.fetchall()
    
df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'field', 1:'Type', 2: 'Null', 3:'Key', 4:'Default', 5:'Extra'})


# In[7]:


# e) Show the total number of records in the actor table.
sql = "SELECT COUNT(*) FROM actor"

cursor.execute(sql)

myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Total'})


# In[8]:


# f) What is the first name and last name of all the actors in the actor table ?

sql = "SELECT first_name, last_name FROM actor LIMIT 10"

cursor.execute(sql)

myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'firstName', 1:'lastName'})


# In[9]:


# g) Insert your first name and middle initial ( in the last name column ) into the actors 
#table.
sql = "INSERT INTO actor (first_name, last_name) VALUES (%s, %s)"
val = ("James", "T")
cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record(s) inserted.")


# In[10]:


# h) Update your middle initial with your last name in the actors table.
sql = "UPDATE actor SET last_name = %s WHERE last_name = %s"
val = ("Furry", "T", )
cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "record(s) updated.")


# In[11]:


# i) Delete the record from the actor table where the first name matches your first name

sql = "DELETE FROM actor WHERE first_name = %s AND last_name = %s"
val = ("James", "Furry", )

cursor.execute(sql, val)
db.commit()
print(cursor.rowcount, "record(s) updated.")


# In[12]:


# j) Create a table payment_type with the following specifications and appropriate data 
#types
# Table Name : “Payment_type”
# Primary Key: "payment_type_id”
# Column: “Type” 

cursor = db.cursor()

cursor.execute("CREATE TABLE payment_type (payment_type_id INT AUTO_INCREMENT PRIMARY KEY, Type VARCHAR(30))")


# In[13]:


# j) Insert the values into the table
sql = "INSERT INTO payment_type (payment_type_id, `Type`) VALUES(%s, %s)" 

val = [
    (1, 'Credit Card'), 
    (2, 'Cash'), 
    (3, 'Paypal'), 
    (4, 'Cheque')
]

cursor.executemany(sql, val)

db.commit()

print(cursor.rowcount, "records(s) inserted.")


# In[14]:


# j) continued. Check to make sure everything worked
sql = "SELECT * FROM payment_type"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'PaymentTypeID', 1:'Type'})


# In[15]:


# k) Rename table payment_type to payment_types.
sql = "RENAME TABLE Payment_type TO payment_types"

cursor.execute(sql)


# In[16]:


# k) Continued. Check to make sure it worked. We can see the table titled payment_types at number 18
sql = "SHOW TABLES"
cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'table'})


# In[17]:


# l) Drop the table payment_types
sql = "DROP TABLE Payment_types"

cursor.execute(sql)


# In[18]:


# l) continued. Make sure the table payment_types was droped
sql = "SHOW TABLES"
cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'table'})


# In[19]:


######## QUESTION 2 ######## – { 10 Points }

# a) List all the movies ( title & description ) that are rated PG-13 ?
    
sql = "SELECT title, description FROM film_list WHERE rating = 'PG-13'"

cursor.execute(sql)

myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Title', 1:'Desciption'})


# In[20]:


# b) List all movies that are either PG OR PG-13 using IN operator ?
    
sql = "SELECT title FROM film_list WHERE rating IN ('PG', 'PG-13')"

cursor.execute(sql)

myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Title'})


# In[21]:


# c) Report all payments greater than and equal to 2$ and Less than equal to 7$ ?

    
sql = "SELECT payment_id, amount FROM payment WHERE amount >= 2 AND amount <= 7"

cursor.execute(sql)

myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'PaymentID', 1:'Amount'})


# In[22]:


# C Continued with between clause

sql = "SELECT payment_id, amount FROM payment WHERE amount between 2 AND 7"

cursor.execute(sql)

myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'PaymentID', 1:'Amount'})


# In[23]:


# d) List all addresses that have phone number that contain digits 589, start with 140 or end with 589
sql = "SELECT address_id, address, address2, district, city_id, postal_code FROM address WHERE phone LIKE '140%' OR phone LIKE '%589' OR phone LIKE '%589%'"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'address_id', 1:'address', 2:'address2', 3:'district', 4:'city_id', 5:'postal_code'})


# In[24]:


# e) List all staff members ( first name, last name, email ) whose password is NULL ?
sql = "SELECT first_name, last_name, email FROM staff WHERE password is NULL"

cursor.execute(sql)

myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'firstName', 1:'lastName', 2: 'email'})


# In[25]:


# f) Select all films that have title names like ZOO and rental duration greater than or equal to 4 

sql = "SELECT title FROM film WHERE title LIKE '%ZOO%' AND rental_duration >= 4"

cursor.execute(sql)
myresult = cursor.fetchall()
    
df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'title'})


# In[26]:


# g) What is the cost of renting the movie ACADEMY DINOSAUR for 2 weeks ? 

# The assumption here is that rental_rate is per day

sql = "SELECT rental_rate * 14 as Rate FROM film WHERE title = %s"
val = 'ACADEMY DINOSAUR'

cursor.execute(sql, val)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Rate'})


# In[27]:


# h) List all unique districts where the customers, staff, and stores are located
# Note : check for NOT NULL values 
sql = "SELECT DISTINCT district FROM address WHERE district IS NOT NULL"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'District'})


# In[28]:


# i) List the top 10 newest customers across all stores

sql = "SELECT customer_id, store_id, first_name, last_name, create_date FROM customer ORDER BY customer_id DESC LIMIT 10"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'CustomerID', 1:'StoreId', 2:'FirstName', 3:'LastName', 4:'CreateDate'})


# In[29]:


######## QUESTION 3 ######## – { 10 Points }
# a) Show total number of movies

sql = "SELECT COUNT(*) FROM film"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Total'})


# In[30]:


# b) What is the minimum payment received and max payment received across all transactions ?

sql = "SELECT MIN(amount) AS MinimumAmount, MAX(amount) AS MaximumAmount FROM payment"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'MinAmount', 1:'MaxAmount'})


# In[31]:


# c) Number of customers that rented movies between Feb-2005 & May-2005 ( based on paymentDate ).

sql = "SELECT COUNT(*) FROM payment WHERE payment_date BETWEEN CAST('2005-02-01' AS DATE) AND CAST('2005-05-31' AS DATE)"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Total'})


# In[32]:


# d) List all movies where replacement_cost is greater than 15$ or rental_duration is between 6 & 10 days

sql = "SELECT title FROM film WHERE replacement_cost >15 OR rental_duration BETWEEN 6 AND 10"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Title'})


# In[33]:


# e) What is the total amount spent by customers for movies in the year 2005 ?
sql = """SELECT 
    SUM(amount) AS TotalAmount
FROM
    payment
WHERE
    YEAR(payment_date) = 2005"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'TotalAmount'})


# In[34]:


# f) What is the average replacement cost across all movies ?

sql = "SELECT AVG(replacement_cost) AS AverageReplacementCost FROM film"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'AverageReplacementCost'})


# In[35]:


# g) What is the standard deviation of rental rate across all movies ?

sql = "SELECT STD(rental_rate) AS StDevRate FROM film;"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'StDevRate'})


# In[36]:


# h) What is the midrange of the rental duration for all movies

# Assumes that mid range is the min plus the max divided by 2
sql = "SELECT (MIN(rental_duration) + MAX(rental_duration))/2 as MidRange from film"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'MidRange'})


# In[37]:


######## QUESTION 4 ######## – { 10 Points }
# a) Customers sorted by first Name and last name in ascending order.

sql = "SELECT first_name, last_name FROM customer ORDER BY first_name asc, last_name asc"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'FirstName', 1:'LastName'})


# In[38]:


# b) Count of movies that are either G/NC-17/PG-13/PG/R grouped by rating.

sql = "SELECT rating, COUNT(*) FROM film GROUP BY rating"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Rating', 1: 'Total'})


# In[39]:


# c) Number of addresses in each district.

sql = "SELECT district, COUNT(*) FROM address GROUP BY district"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'District', 1:'Count'})


# In[40]:


# d) Find the movies where rental rate is greater than 1$ and order result set by descending order.

sql = "SELECT title, rental_rate FROM film WHERE rental_rate > 1 ORDER BY rental_rate desc"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Title', 1:'RentalRate'})


# In[41]:


# e) Top 2 movies that are rated R with the highest replacement cost ?

sql = "SELECT title, replacement_cost FROM film WHERE rating = 'R' ORDER BY replacement_cost desc LIMIT 2"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Title', 1:'ReplacementCost'})


# In[42]:


# f) Find the most frequently occurring (mode) rental rate across products.
sql = "SELECT rental_rate AS rentalRateMode FROM film GROUP BY 1 ORDER BY COUNT(1) desc LIMIT 1"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'RentalRate'})


# In[43]:


# g) Find the top 2 movies with movie length greater than 50mins and which has commentaries as a special features. 

sql = "SELECT title, length, special_features FROM film WHERE length > 50 AND special_features LIKE '%Commentaries%' ORDER BY length desc LIMIT 2"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Title', 1:'Length', 2:'SpecialFeatures'})


# In[44]:


# h) List the years which has more than 2 movies released.
sql = "SELECT release_year, COUNT(*) as Total FROM film GROUP BY release_year HAVING total > 2"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'ReleaseYear', 1:'Total'})


# In[45]:


######## QUESTION 1 ######## – { 20 Points }
# a) List the actors (firstName, lastName) who acted in more then 25 movies.
# Note: Also show the count of movies against each actor

sql = """SELECT  
    f.actor_id, first_name, last_name, COUNT(f.actor_id) AS Total
    FROM film_actor AS f
    INNER JOIN actor AS a ON f.actor_id = a.actor_id
    GROUP BY actor_id
    HAVING Total > 25"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'ActorID', 1:'FirstName', 2:'LastName', 3:'Total'})


# In[46]:


# b) List the actors who have worked in the German language movies. 
# Note: Please execute the below SQL before answering this question.
sql = "SET SQL_SAFE_UPDATES=0"

cursor.execute(sql)


# In[47]:


# b) Continued

sql = "UPDATE film SET language_id=6 WHERE title LIKE '%ACADEMY%'"

cursor.execute(sql)


# In[48]:


# b) Continued

sql = """SELECT 
    first_name, last_name, title, language_id
FROM
    film_actor AS fa
        INNER JOIN
    film AS f ON fa.film_id = f.film_id
        INNER JOIN
    actor AS a ON fa.actor_id = a.actor_id
WHERE
    f.language_id = 6"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'FirstName', 1:'LastName', 2:'Title', 3: 'LanguageID'})


# In[49]:


# c) List the actors who acted in horror movies.
# Note: Show the count of movies against each actor in the result set.

sql = """SELECT 
    a.actor_id, first_name, last_name, c.name, count(first_name)
FROM
    actor AS a
        INNER JOIN
    film_actor AS fa ON a.actor_id = fa.actor_id
        INNER JOIN
    film AS f ON f.film_id = fa.film_id
        INNER JOIN
    film_category AS fc ON fc.film_id = fa.film_id
        INNER JOIN
    category AS c ON fc.category_id = c.category_id
WHERE
    c.category_id = 11
GROUP BY first_name"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'ActorID', 1:'FirstName', 2:'LastName', 3: 'Name', 4:'Total'})


# In[50]:


# d) List all customers who rented more than 3 horror movies.

sql = """SELECT 
    c.first_name,
    c.last_name,
    c.customer_id,
    COUNT(c.customer_id) AS total
FROM
    rental AS r
        INNER JOIN
    inventory AS i ON r.inventory_id = i.inventory_id
        INNER JOIN
    customer AS c ON c.customer_id = r.customer_id
        INNER JOIN
    film_category AS fc ON fc.film_id = i.film_id
        INNER JOIN
    category AS cat ON cat.category_id = fc.category_id
WHERE
    cat.category_id = 11
GROUP BY c.customer_id
HAVING total > 3
ORDER BY total desc"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'FirstName', 1:'LastName', 2: 'CustomerID', 3:'Total'})


# In[51]:


# e) List all customers who rented the movie which starred SCARLETT BENING

sql = """SELECT 
    c.customer_id, c.first_name, c.last_name, i.film_id
FROM
    actor AS a
        INNER JOIN
    film_actor AS fa ON a.actor_id = fa.actor_id
        INNER JOIN
    inventory AS i ON fa.film_id = i.film_id
        INNER JOIN
    rental AS r ON i.inventory_id = r.inventory_id
        INNER JOIN
    customer AS c on r.customer_id = c.customer_id
WHERE a.first_name = 'Scarlett' AND a.last_name = 'Bening'"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'CustomerID', 1:'FirstName', 2:'LastName', 3:'FilmID'})


# In[52]:


# f) Which customers residing at postal code 62703 rented movies that were Documentaries.

sql = """SELECT 
    c.first_name, c.last_name, cat.name, a.postal_code
FROM
    address AS a
        INNER JOIN
    customer AS c ON a.address_id = c.address_id
        INNER JOIN
    rental AS r ON c.customer_id = r.customer_id
        INNER JOIN
    inventory AS i ON r.inventory_id = i.inventory_id
        INNER JOIN
    film_category AS fc ON i.film_id = fc.film_id
        INNER JOIN
    category AS cat ON fc.category_id = cat.category_id
WHERE
    cat.name = 'Documentary'
        AND a.postal_code = '62703'"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'CustomerID', 1:'FirstName', 2:'Category', 3:'PostalCode'})


# In[53]:


# g) Find all the addresses where the second address line is not empty (i.e., contains some text), and return these second addresses sorted.

# In this particular case, all second address lines are null or empty with no text. That's why this doesn't give us any data
sql = "SELECT address_id, address FROM address where address2 is not null and address2 like '%[a-zA-Z]%'"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'AddressID', 1:'Address'})


# In[54]:


# h) How many films involve a “Crocodile” and a “Shark” based on film description ?

sql = "SELECT count(*) FROM film where description LIKE '%crocodile%' AND description LIKE '%shark%'"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'Total'})


# In[55]:


# i) List the actors who played in a film involving a “Crocodile” and a “Shark”, along with the release year of the movie, sorted by the actors’ last names. 

sql = """SELECT 
    a.first_name, a.last_name, f.release_year
FROM
    film AS f
        INNER JOIN
    film_actor AS fa ON f.film_id = fa.film_id
        INNER JOIN
    actor AS a ON a.actor_id = fa.actor_id
WHERE
    f.description LIKE '%crocodile%'
        AND description LIKE '%shark%'
ORDER BY a.last_name"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'FirstName', 1:'LastName', 2:'ReleaseYear'})


# In[56]:


# j) Find all the film categories in which there are between 55 and 65 films. Return the names of categories and the number of films per category, sorted from highest to lowest by the number of films.

sql = """SELECT 
    cat.name, COUNT(film_id) AS NumberOfFilms
FROM
    film_category AS fc
        INNER JOIN
    category AS cat ON fc.category_id = cat.category_id
GROUP BY cat.name
HAVING NumberOfFilms BETWEEN 55 AND 65
ORDER BY NumberOfFilms DESC"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'Category', 1:'NumberOfFilms'})


# In[57]:


# k) In which of the film categories is the average difference between the film replacement cost and the rental rate larger than 17$? 

sql = """SELECT 
    cat.name, AVG(replacement_cost - rental_rate) AS Difference
FROM
    film_category AS fc
        INNER JOIN
    category AS cat ON fc.category_id = cat.category_id
        INNER JOIN
    film AS f ON f.film_id = fc.film_id
GROUP BY cat.name
HAVING Difference > 17"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'Category', 1:'Difference'})


# In[58]:


# l) Many DVD stores produce a daily list of overdue rentals so that customers can be 
#contacted and asked to return their overdue DVDs. To create such a list, search the rental 
#table for films with a return date that is NULL and where the rental date is further in the 
#past than the rental duration specified in the film table. If so, the film is overdue and we 
#should produce the name of the film along with the customer name and phone number.

# Ananth and I worked on this one together because we were having a little trouble doing it ourselves

sql = """SELECT 
    r.rental_id,
    r.customer_id,
    r.rental_date,
    r.return_date,
    f.rental_duration,
    DATEDIFF(r.return_date, r.rental_date) AS CustomerRentalDuration,
    CASE
        WHEN DATEDIFF(r.return_date, r.rental_date) > f.rental_duration THEN 'Yes'
        WHEN DATEDIFF(r.return_date, r.rental_date) IS NULL THEN 'Yes'
        ELSE 'No'
    END AS is_late
FROM
    rental AS r
        INNER JOIN
    inventory AS i ON r.inventory_id = i.inventory_id
        INNER JOIN
    film AS f ON i.film_id = f.film_id
WHERE
    (DATEDIFF(r.return_date, r.rental_date) > f.rental_duration)
        OR return_date IS NULL"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'RentalID', 1:'CustomerID', 2:'RentalDate', 3:'ReturnDate', 4:'RentalDuration', 5:'CustomerRentalDuration', 6:'IsLate'})


# In[59]:


# m) Find the list of all customers and staff given a store id 
# Note : use a set operator, do not remove duplicates

sql = """SELECT c.store_id, c.first_name, c.last_name, "Customer" as Job
from customer as c
where c.store_id = 1
union
SELECT s.store_id, s.first_name, s.last_name, "Staff" as Job
from staff as s
where s.store_id = 1"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'StoreID', 1:'FirstName', 2:'LastName', 3:'Job'})


# In[60]:


######## QUESTION 2 ######## – { 10 Points }
# a) List actors and customers whose first name is the same as the first name of the actor with ID 8.


sql1 = """SELECT a.first_name, a.last_name, "Actor" as Job
from actor as a
where first_name = 'Matthew'
union 
SELECT c.first_name, c.last_name, 'Customer' as Job
from customer as c
where first_name = 'Matthew'"""

cursor.execute(sql1)
myresult1 = cursor.fetchall()

df1 = pd.DataFrame( [[ij for ij in i] for i in myresult1] )
df1.rename(columns={0:'FirstName', 1:'LastName'})


# In[61]:


# b) List customers and payment amounts, with payments greater than average the payment amount

sql = """SELECT 
    customer_id,
    amount
FROM
    payment
WHERE
    amount > (SELECT 
            AVG(amount)
        FROM
            payment)"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'CustomerID',1:'Amount'})


# In[62]:


# c) List customers who have rented movies atleast once 
# Note: use IN clause

sql = """SELECT 
    customer_id,
	first_name,
    last_name
FROM
    customer
WHERE
    customer_id IN (SELECT 
            customer_id
        FROM
            rental)"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'CustomerID', 1:'FirstName', 2:'LastName'})


# In[63]:


# d) Find the floor of the maximum, minimum and average payment amount

sql = """SELECT 
    FLOOR(MIN(amount)) AS min,
    FLOOR(MAX(amount)) AS max,
    FLOOR(AVG(amount)) AS avg
FROM
    payment"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'FloorMax', 1:'FloorMin', 2:'FloorAvg'})


# In[64]:


######## QUESTION 3 ######## – { 5 Points }
# a) Create a view called actors_portfolio which contains information about actors and films ( including titles and category).
# drops the actors_portfolio view if it already exists

sqlfirst = 'DROP VIEW IF EXISTS actors_portfolio'
cursor.execute(sqlfirst)


# In[65]:


######## QUESTION 3 ######## – { 5 Points }
# a) Create a view called actors_portfolio which contains information about actors and films ( including titles and category).
# Continued
sql = """CREATE VIEW actors_portfolio AS
SELECT 
    a.first_name, a.last_name, f.title, f.film_id, cat.name as category
FROM
    film_category AS fc
        INNER JOIN
    film_actor AS fa ON fc.film_id = fa.film_id
        INNER JOIN
    film AS f ON fa.film_id = f.film_id
        INNER JOIN
    actor AS a ON fa.actor_id = a.actor_id
		INNER JOIN
	category as cat ON fc.category_id = cat.category_id"""

cursor.execute(sql)


# In[66]:


# b) Describe the structure of the view and query the view to get information on the actor ADAM GRANT 

sql = "DESCRIBE actors_portfolio"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'Field', 1:'Type', 2:'Null', 3:'Key', 4:'Default', 5:'Extra'})


# In[67]:


# b) continued

sql = "SELECT * FROM actors_portfolio WHERE first_name = 'Adam' and last_name = 'grant'"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0: 'FirstName', 1:'LastName', 2:'Title', 3:'FilmID', 4:'Category'})


# In[68]:


# c) Insert a new movie titled Data Hero in Sci-Fi Category starring ADAM GRANT 

# So I tried doing this and several of my teammates had difficulties with it too. 
# I feel like this should have worked based on what I saw online. I know you can't insert
# things to a view with multiple tables but I thought this code should work and it doesn't
# I will comment it out since it will just give an error but I haven't been able to figure
# out why it doesn't work

# INSERT INTO actors_portfolio(first_name, last_name) VALUES('ADAM', 'GRANT');
# INSERT INTO actors_portfolio(film_id, title) VALUES(1001, 'Data Hero');
# INSERT INTO actors_portfolio(category) VALUES('Sci-Fi');

# In mysql I thought this should have worked because it separated everything out into it's separate tables
# Any help or explanation as to why this doesn't work would be appreciated


# In[69]:


######## QUESTION 4 ######## – { 5 Points }
# a) Extract the street number ( characters 1 through 4 ) from customer addressLine1

sql = """SELECT 
    address, SUBSTRING(address, 1, 4) AS streetNumber
FROM
    address"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Address', 1: 'StreetNumber'})


# In[70]:


# b) Find out actors whose last name starts with character A, B or C.

sql = """SELECT 
    actor_id, first_name, last_name
FROM
    actor
WHERE
    last_name REGEXP '^(A|B|C)'
ORDER BY last_name"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'ActorID', 1: 'FirstName', 2:'LastName'})


# In[71]:


# c) Find film titles that contains exactly 10 characters

sql = """SELECT 
    film_id, title
FROM
    film
WHERE
    title REGEXP '^.{10}$'"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'FilmID', 1: 'Title'})


# In[72]:


# d) Format a payment_date using the following format e.g "22/1/2016"

sql = "SELECT date_format(payment_date, '%d/%c/%Y') from payment"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'FormatedDate'})


# In[73]:


# e) Find the number of days between two date values rental_date & return_date

sql = """SELECT
rental_id, rental_date, return_date, DATEDIFF(return_date, rental_date) as Days
FROM
    rental"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'RentalID', 1: 'RentalDate', 2:'ReturnDate', 3:'Days'})


# In[74]:


######## QUESTION 5 ######## – { 20 Points } 
 
# Provide 5 additional queries, data visualizations and indicate the business use 
#cases/insights they address. Please refer to the in class exercises relating to Python Jupyter 
#Notebook with the SQL/Plotly code
#Note: Insights should not be a flavor of the previously addressed queries within 
#Assignment 2


# In[75]:


# Query 1

# This query goes through the payment table and plots a histogram showing the amounts for each transaction. This gives
# us an idea of the distribution of the payments and can clearly show that there are 3 amounts that have the most 
# transactions. Gives us the insight into how much could be charged for a particular movie

sql = "SELECT amount FROM payment"

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'Amount'})

df = df.rename(columns = {0:'Amount'})

amount = df["Amount"]
amount.hist()


# In[76]:


from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objects as go
import plotly.graph_objects as go
import cufflinks as cf


# In[77]:


# Query 2

# Goes through the address and country tables and extracts the countries that have at least 10 cities in the database
# It then gives a pie chart showing those countries and their respective percentage of the whole. This could be
# useful to see where to target customers or look at other geographical tendencies

sql = """SELECT 
    c.country_id AS country_id,
    country,
    count(c.country_id) as TOTAL
FROM
    address AS a
        INNER JOIN
    city AS ci ON a.city_id = ci.city_id
        INNER JOIN
    country AS c ON ci.country_id = c.country_id
    GROUP BY c.country_id
    HAVING Total > 10
    ORDER BY TOTAL desc
    """

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df = df.rename(columns={0:'CountryID', 1:'Country', 2:'Total'})
df

labels = df['Country']
values = df['Total']

trace=go.Pie(labels=labels,values=values, marker=dict(colors=['skyblue']),hoverinfo="value")
data = [trace]
layout = go.Layout(title="Pie Chart - Distribution")
fig = go.Figure(data = data,layout = layout)

iplot(fig)


# In[78]:


# Query 3

# This takes all of the film categories and plots them in a pie chart. Helps us see the distribution of categories
# throughout our database. Could be useful to cross check against categories where the most money is brought in.
# You could then target those categories and try to increase revenue.

sql = """SELECT 
name, COUNT(*)
FROM
    film AS f
        INNER JOIN
    film_category AS fc ON f.film_id = fc.film_id
        INNER JOIN
    category AS c ON fc.category_id = c.category_id
GROUP BY name"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df = df.rename(columns={0:'Category', 1:'Total'})
df

labels = df['Category']
values = df['Total']

trace=go.Pie(labels=labels,values=values, marker=dict(colors=['skyblue']),hoverinfo="value")
data = [trace]
layout = go.Layout(title="Pie Chart - Distribution")
fig = go.Figure(data = data,layout = layout)

iplot(fig)


# In[79]:


# Query 4

# This query takes the customers in the payment table and adds up how many payments they made. It then orders by the total
# in a descending way, skips the first ten and gives the next ten. This could be useful to see the customers to target.
# Perhaps the top 10 customers with the most transactions are all members. We aren't as concerned with them because 
# they are regular customers. But maybe the next 10 aren't members and we could try to target them and try to get 
# them to use a membership. Thus, we skip the most paying customers and give us the next most paying to focus on them.

sql = """SELECT 
    customer_id, COUNT(*) AS Total
FROM
    payment
GROUP BY customer_id
ORDER BY Total DESC
LIMIT 10 , 10"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'CustomerID', 1:'Total'})


# In[80]:


# Query 5

# This query goes through all of the films and gives the number of characters in the description and only keeps the 
# films that have under 100 characters. This could be useful if you are a business and are only able to display 
# 100 characters or less. In this case, it will show you which movie descriptions you could display.

sql = """SELECT 
    film_id, title, description, CHAR_LENGTH(description) AS DescChar
FROM
    film_text
    GROUP BY title
    HAVING DescChar <= 100
    ORDER BY DescChar desc"""

cursor.execute(sql)
myresult = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in myresult] )
df.rename(columns={0:'FilmID', 1:'Title', 2:'Description', 3:'DescChar'})

