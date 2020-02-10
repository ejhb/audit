USE sakila;

WITH act_count AS 
(
	SELECT
	a.first_name
	,a.last_name
    ,COUNT(*) nb_film
	FROM actor a 
	INNER JOIN film_actor  ON fa.actor_id = a.action_id
	GROUP BY 
	a.first_name
	,a.last_name
)
SELECT * 
FROM act_count a
WHERE NOT EXISTS
;


-- film jamais joué 
SELECT 
f.title
,f.release_year
FROM film f
LEFT JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON r.inventory_id = i.inventory_id
WHERE r.rental_id IS NULL;


-- Film jamais loué avec "NOT IN"
SELECT 
f.title
,f.release_year
FROM film f
WHERE f.film_id NOT IN 
(
	SELECT f2.film_id
	FROM film f2
	INNER JOIN inventory i on f2.film_id = i.film_id
	INNER JOIN rental r on r.inventory_id = i.inventory_id
);

-- Temps moyen de restitution d'un film 

SELECT AVG(ABS(DATEDIFF(return_date,rental_date)))
FROM rental;

-- Temps moyen de restitution d'un film par client (classement du plus long au plus court)


SELECT 
c.first_name
,c.last_name
,AVG(ABS(DATEDIFF(return_date,rental_date))) avg_duration
FROM rental r 
INNER JOIN customer c
ON c.customer_id = r.customer_id
GROUP BY 
c.first_name
,c.last_name
ORDER BY 3 DESC
;

-- Temps moyen de restitution d'un film par client (classement du plus long au plus court) Si au dessus de la moyenne = mauvais si en dessous = bon 

SELECT r.first_name
,r.last_name
,AVG(ABS(DATEDIFF( return_date , rental_date))),
CASE 
    WHEN AVG(ABS(DATEDIFF( return_date , rental_date))) <= 5 THEN 'Good customer'
    ELSE 'Bad customer'
END AS quality
FROM rental r 
INNER JOIN customer c 
ON r.customer_id = c.customer_id
GROUP BY first_name, last_name;

-- L'acteur préféré de chaque client

SELECT 
c.client_id
,c.first_name || ' ' || c.last_name as client_name
,a.actor_id
,a.first_name || ' ' || a.last_name as actor_name
,COUNT(*) nb_occurence
FROM customer c
INNER JOIN rental r ON r.customer_id = c.customer_id
INNER JOIN inventory i on i.inventory_id = r.inventory_id
INNER JOIN film f ON f.film_id = i.film_id
INNER JOIN film_actor fa on fa.film_id - f.film_id
INNER JOIN actor a on a.actor_id = fa.actor_id
GROUP BY c.client_id
,c.first_name
,c.last_name
,a.first_name
,a.last_name
;
