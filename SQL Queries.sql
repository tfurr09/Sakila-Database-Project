# a) Show the list of databases.
SHOW databases;
# b) Select sakila database.
USE sakila;
# c) Show all tables in the sakila database.
SHOW TABLES;
# d) Show each of the columns along with their data types for the actor table.
SHOW COLUMNS FROM actor;
# e) Show the total number of records in the actor table.
SELECT 
    COUNT(*)
FROM
    actor;
# f) What is the first name and last name of all the actors in the actor table ?
SELECT 
    first_name, last_name
FROM
    actor;
# g) Insert your first name and middle initial ( in the last name column ) into the actors 
#table.
INSERT INTO actor (first_name, last_name)
VALUES ('James', 'T');
# h) Update your middle initial with your last name in the actors table.
UPDATE actor 
SET 
    last_name = 'Furry'
WHERE
    actor_id = 201;
# i) Delete the record from the actor table where the first name matches your first name
DELETE FROM actor 
WHERE
    first_name = 'James'
    AND last_name = 'Furry';
    
# j) Create a table payment_type with the following specifications and appropriate data 
#types
# Table Name : “Payment_type”
# Primary Key: "payment_type_id”
# Column: “Type” 
CREATE TABLE Payment_type (
	payment_type_id int,
	Type varchar(30),
	PRIMARY KEY (payment_type_id)
);

# Insert following rows in to the table: 
# 1, “Credit Card” ; 2, “Cash”; 3, “Paypal” ; 4 , “Cheque” 

INSERT INTO Payment_type (payment_type_id, `Type`)
VALUES(1, 'Credit Card'), 
(2, 'Cash'), 
(3, 'Paypal'), 
(4, 'Cheque');

# k) Rename table payment_type to payment_types.
RENAME TABLE Payment_type TO payment_types;

# l) Drop the table payment_types
DROP TABLE Payment_type;

######## QUESTION 2 ######## – { 10 Points }

# a) List all the movies ( title & description ) that are rated PG-13 ?
SELECT 
    title, description
FROM
    film_list
WHERE
    rating = 'PG-13';
    
# b) List all movies that are either PG OR PG-13 using IN operator ?
SELECT 
    title
FROM
    film_list
WHERE
    rating IN ('PG' , 'PG-13');
    
# c) Report all payments greater than and equal to 2$ and Less than equal to 7$ ?
# Note : write 2 separate queries conditional operator and BETWEEN keyword
SELECT 
    *
FROM
    payment
WHERE
    amount >= 2 AND amount <= 7;

SELECT * FROM payment WHERE amount between 2 AND 7;

# d) List all addresses that have phone number that contain digits 589, start with 140 or end with 589
SELECT 
    *
FROM
    address
WHERE
    phone LIKE '140%' OR phone LIKE '%589'
        OR phone LIKE '%589%';
# e) List all staff members ( first name, last name, email ) whose password is NULL ?
SELECT 
    first_name, last_name, email
FROM
    staff
WHERE
    password IS NULL;
    
# f) Select all films that have title names like ZOO and rental duration greater than or equal to 4 
SELECT 
    *
FROM
    film
WHERE
    title LIKE '%ZOO%'
        AND rental_duration >= 4;
# g) What is the cost of renting the movie ACADEMY DINOSAUR for 2 weeks ? 
SELECT 
    rental_rate * 14 AS Rate # This assumes that rental_rate is per day
FROM
    film
WHERE
    title = 'ACADEMY DINOSAUR';
# Note : use of column alias
# h) List all unique districts where the customers, staff, and stores are located
SELECT DISTINCT # This assumes that the addresses of customers, staff and stores are all stored in the address table
    district
FROM
    address
WHERE
    district IS NOT NULL;
# Note : check for NOT NULL values 
# i) List the top 10 newest customers across all stores

SELECT 
    *
FROM
    customer
ORDER BY customer_id DESC
LIMIT 10; # Because all the cells in create_date and last_update are the same, I assume that customer 599 came after customer 598 and thus 590-599 are the newest customers

######## QUESTION 3 ######## – { 10 Points }
# a) Show total number of movies
SELECT 
    COUNT(*)
FROM
    film;
# b) What is the minimum payment received and max payment received across all transactions ?
SELECT 
    MIN(amount) AS MinimumAmount, MAX(amount) AS MaximumAmount
FROM
    payment;
# c) Number of customers that rented movies between Feb-2005 & May-2005 ( based on paymentDate ).
SELECT 
    count(*)
FROM
    payment
WHERE
    payment_date BETWEEN CAST('2005-02-01' AS DATE) AND CAST('2005-05-31' AS DATE);
# d) List all movies where replacement_cost is greater than 15$ or rental_duration is between 6 & 10 days
SELECT 
    *
FROM
    film
WHERE
    replacement_cost > 15
        OR rental_duration BETWEEN 6 AND 10;
# e) What is the total amount spent by customers for movies in the year 2005 ?
SELECT 
    SUM(amount) AS TotalAmount
FROM
    payment
WHERE
    YEAR(payment_date) = 2005;
# f) What is the average replacement cost across all movies ?
SELECT 
    AVG(replacement_cost) AS AverageReplacementCost
FROM
    film;
# g) What is the standard deviation of rental rate across all movies ?
SELECT 
    STD(rental_rate) AS StDevRate
FROM
    film;
# h) What is the midrange of the rental duration for all movies
SELECT (MIN(rental_duration) + MAX(rental_duration))/2 as MidRange
from film;

######## QUESTION 4 ######## – { 10 Points }
# a) Customers sorted by first Name and last name in ascending order.
SELECT * FROM customer ORDER BY first_name asc, last_name asc;
# b) Count of movies that are either G/NC-17/PG-13/PG/R grouped by rating. 
SELECT rating, COUNT(*) FROM film GROUP BY rating;
# c) Number of addresses in each district.
SELECT district, COUNT(*) FROM address GROUP BY district;
# d) Find the movies where rental rate is greater than 1$ and order result set by descending order.
SELECT * FROM film WHERE rental_rate > 1 ORDER BY rental_rate desc;
# e) Top 2 movies that are rated R with the highest replacement cost ? 
SELECT * FROM film WHERE rating = 'R' ORDER BY replacement_cost desc LIMIT 2;
# f) Find the most frequently occurring (mode) rental rate across products. 
SELECT rental_rate AS rentalRateMode, count(rental_rate) as Total FROM film GROUP BY 1 ORDER BY COUNT(1) desc LIMIT 1;
# g) Find the top 2 movies with movie length greater than 50mins and which has commentaries as a special features. 
SELECT * FROM film WHERE length > 50 AND special_features LIKE '%Commentaries%' ORDER BY length desc LIMIT 2;
# h) List the years which has more than 2 movies released.
SELECT release_year, COUNT(*) as total FROM film GROUP BY release_year HAVING total > 2;

######## QUESTION 1 ######## – { 20 Points }
# a) List the actors (firstName, lastName) who acted in more then 25 movies.
# Note: Also show the count of movies against each actor
SELECT 
    f.actor_id,
    first_name,
    last_name,
    COUNT(f.actor_id) AS Total
FROM
    film_actor AS f
        INNER JOIN
    actor AS a ON f.actor_id = a.actor_id
GROUP BY actor_id
HAVING Total > 25
ORDER BY Total desc;
# b) List the actors who have worked in the German language movies. 
# Note: Please execute the below SQL before answering this question.
SET SQL_SAFE_UPDATES=0;
UPDATE film SET language_id=6 WHERE title LIKE "%ACADEMY%";
SELECT 
    first_name, last_name, title, language_id
FROM
    film_actor AS fa
        INNER JOIN
    film AS f ON fa.film_id = f.film_id
        INNER JOIN
    actor AS a ON fa.actor_id = a.actor_id
WHERE
    f.language_id = 6;
# c) List the actors who acted in horror movies.
# Note: Show the count of movies against each actor in the result set.
SELECT 
    a.actor_id, first_name, last_name, c.name, count(first_name) as Total
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
GROUP BY first_name;
# d) List all customers who rented more than 3 horror movies.
SELECT 
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
ORDER BY total desc;
# e) List all customers who rented the movie which starred SCARLETT BENING
SELECT 
    distinct c.customer_id, c.first_name, c.last_name
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
WHERE a.first_name = 'Scarlett' AND a.last_name = 'Bening';

# f) Which customers residing at postal code 62703 rented movies that were Documentaries.
SELECT 
    distinct c.first_name, c.last_name, cat.name, a.postal_code
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
        AND a.postal_code = '62703';

# g) Find all the addresses where the second address line is not empty (i.e., contains some text), and return these second addresses sorted.
SELECT * FROM address where address2 is not null and address2 like '%[a-zA-Z]%';
# h) How many films involve a “Crocodile” and a “Shark” based on film description ?
SELECT count(*) FROM film where description like '%Crocodile%' and description like '%Shark%';
# i) List the actors who played in a film involving a “Crocodile” and a “Shark”, along with the release year of the movie, sorted by the actors’ last names. 
SELECT 
    a.first_name, a.last_name, f.release_year
FROM
    film AS f
        INNER JOIN
    film_actor AS fa ON f.film_id = fa.film_id
        INNER JOIN
    actor AS a ON a.actor_id = fa.actor_id
WHERE
    f.description LIKE '%crocodile%'
        or '%shark%'
ORDER BY a.last_name;
# j) Find all the film categories in which there are between 55 and 65 films. Return the names of categories and the number of films per category, sorted from highest to lowest by the number of films. 
SELECT 
    cat.name, COUNT(film_id) AS NumberOfFilms
FROM
    film_category AS fc
        INNER JOIN
    category AS cat ON fc.category_id = cat.category_id
GROUP BY cat.name
HAVING NumberOfFilms BETWEEN 55 AND 65
ORDER BY NumberOfFilms DESC;
# k) In which of the film categories is the average difference between the film replacement cost and the rental rate larger than 17$? 

SELECT 
    cat.name, AVG(replacement_cost - rental_rate) AS Difference
FROM
    film_category AS fc
        INNER JOIN
    category AS cat ON fc.category_id = cat.category_id
        INNER JOIN
    film AS f ON f.film_id = fc.film_id
GROUP BY cat.name
HAVING Difference > 17;

# l) Many DVD stores produce a daily list of overdue rentals so that customers can be contacted and asked to return their overdue DVDs. To create such a list, search the rental table for films with a return date that is NULL and where the rental date is further in the past than the rental duration specified in the film table. If so, the film is overdue and we should produce the name of the film along with the customer name and phone number.
SELECT 
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
        OR return_date IS NULL;


# m) Find the list of all customers and staff given a store id 
# Note : use a set operator, do not remove duplicates
SELECT * from customer as c
inner join store as s
on s.store_id = c.store_id
inner join staff as sf
on c.store_id = sf.store_id
where s.store_id in (1);

SELECT c.store_id, c.first_name, c.last_name, "Customer" as Job
from customer as c
where c.store_id = 1
union
SELECT s.store_id, s.first_name, s.last_name, "Staff" as Job
from staff as s
where s.store_id = 1;

######## QUESTION 2 ######## – { 10 Points }
# a) List actors and customers whose first name is the same as the first name of the actor with ID 8. 
SELECT 
    actor_id, first_name, last_name
FROM
    actor
WHERE
    first_name = (SELECT 
            first_name
        FROM
            actor
        WHERE
            actor_id = 8);
SELECT 
    customer_id, first_name, last_name
FROM
    customer
WHERE
    first_name = (SELECT 
            first_name
        FROM
            actor
        WHERE
            actor_id = 8);
SELECT a.first_name, a.last_name, "Actor" as Job
from actor as a
where first_name = 'Matthew'
union 
SELECT c.first_name, c.last_name, 'Customer' as Job
from customer as c
where first_name = 'Matthew';
# b) List customers and payment amounts, with payments greater than average the payment amount
SELECT 
    customer_id,
    amount
FROM
    payment
WHERE
    amount > (SELECT 
            AVG(amount)
        FROM
            payment);  
# c) List customers who have rented movies atleast once 
# Note: use IN clause
SELECT 
    customer_id,
	first_name,
    last_name
FROM
    customer
WHERE
    customer_id IN (SELECT 
            customer_id
        FROM
            rental);
# d) Find the floor of the maximum, minimum and average payment amount
SELECT 
    FLOOR(MAX(amount)) AS max,
    FLOOR(MIN(amount)) AS min,
    FLOOR(AVG(amount)) AS avg
FROM
    payment;
######## QUESTION 3 ######## – { 5 Points }
# a) Create a view called actors_portfolio which contains information about actors and films ( including titles and category).
CREATE VIEW actors_portfolio AS
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
	category as cat ON fc.category_id = cat.category_id;
# b) Describe the structure of the view and query the view to get information on the actor ADAM GRANT 
DESCRIBE actors_portfolio;
SELECT * FROM actors_portfolio;
SELECT * FROM actors_portfolio WHERE first_name = 'Adam' and last_name = 'grant';
# c) Insert a new movie titled Data Hero in Sci-Fi Category starring ADAM GRANT 
SET SQL_SAFE_UPDATES = 0;

INSERT INTO actors_portfolio(first_name, last_name, title, category)
VALUES('Adam', 'Grant', 'Data Hero', 'Sci-Fi');

INSERT INTO actors_portfolio(first_name, last_name) VALUES('ADAM', 'GRANT');
INSERT INTO actors_portfolio(film_id, title) VALUES(1001, 'Data Hero');
INSERT INTO actors_portfolio(category) VALUES('Sci-Fi');

SELECT * FROM film;
######## QUESTION 4 ######## – { 5 Points }
# a) Extract the street number ( characters 1 through 4 ) from customer addressLine1
SELECT 
    address, SUBSTRING(address, 1, 4) AS streetNumber
FROM
    address;
# b) Find out actors whose last name starts with character A, B or C.
SELECT 
    actor_id, first_name, last_name
FROM
    actor
WHERE
    last_name REGEXP '^(A|B|C)'
ORDER BY last_name;
# c) Find film titles that contains exactly 10 characters
SELECT 
    film_id, title
FROM
    film
WHERE
    title REGEXP '^.{10}$';
# d) Format a payment_date using the following format e.g "22/1/2016"
SELECT date_format(payment_date, '%d/%c/%Y') from payment;
# e) Find the number of days between two date values rental_date & return_date

SELECT
	rental_id,
	rental_date,
    return_date,
	DATEDIFF(return_date, rental_date) as Days
FROM
    rental;
######## QUESTION 5 ######## – { 20 Points } 
 
# Provide 5 additional queries, data visualizations and indicate the business use 
#cases/insights they address. Please refer to the in class exercises relating to Python Jupyter 
#Notebook with the SQL/Plotly code
#Note: Insights should not be a flavor of the previously addressed queries within 
#Assignment 2

SELECT 
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
    ORDER BY TOTAL desc;
    
SELECT 
    name, COUNT(*)
FROM
    film AS f
        INNER JOIN
    film_category AS fc ON f.film_id = fc.film_id
        INNER JOIN
    category AS c ON fc.category_id = c.category_id
GROUP BY name;

SELECT * FROM rental;
SELECT * FROM actor;
SELECT * FROM film_text WHERE description LIKE '%ba%';
SELECT * FROM address;
SELECT 
    customer_id, COUNT(*) AS Total
FROM
    payment
GROUP BY customer_id
ORDER BY Total DESC
LIMIT 10 , 10;
    
SELECT 
    film_id, title, CHAR_LENGTH(description) AS DescChar
FROM
    film_text
    WHERE DescChar <= 100;

SELECT * FROM payment;
