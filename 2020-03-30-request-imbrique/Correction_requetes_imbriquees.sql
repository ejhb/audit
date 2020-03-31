
# Mis en pratique
# selectionner tout les acteurs ayat joué dans les films ou à joué 'MCCONAUGHEY CARY'


select distinct concat(last_name, ' ', first_name) as acteur from actor
	join film_actor on actor.actor_id = film_actor.actor_id
    join film on film_actor.film_id = film.film_id
    where film.film_id in (
		select film_id from film_actor
			join actor on film_actor.actor_id = actor.actor_id
		and concat(last_name, ' ', first_name) = 'MCCONAUGHEY CARY');


select distinct concat(last_name, ' ', first_name) as acteur from actor
	join film_actor on actor.actor_id = film_actor.actor_id
    join film on film_actor.film_id = film.film_id
    where film.film_id not in (
		select film_id from film_actor
			join actor on film_actor.actor_id = actor.actor_id
		and concat(last_name, ' ', first_name) = 'MCCONAUGHEY CARY');
    


# Afficher Uniquement le nom du film qui contient le plus d'acteur et le nombre d'acteurs associé sans LIMT
        
select title, count(actor_id) as nb from film
	join film_actor on film.film_id = film_actor.film_id
    group by film.film_id
    having nb = (
		select max(a.cnt) from (
			select count(actor_id) as cnt from film_actor
				group by film_id) a);


# Afficher les acteurs ayant jouer uniquement dans des films d’actions (Utiliser EXISTS)

select distinct concat(last_name, ' ', first_name) as nom from actor
	join film_actor fa on actor.actor_id = fa.actor_id
	where exists (
		select film.film_id from film
			join film_category on film.film_id = film_category.film_id
            join category on film_category.category_id = category.category_id
            where category.name = 'Action'
				and fa.film_id = film.film_id);
