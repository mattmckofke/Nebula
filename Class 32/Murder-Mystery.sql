/*
Getting information

SELECT *
FROM crime_scene_report
WHERE type = "murder" AND date = 20180115 AND city = "SQL City";

description = Security footage shows that there were 2 witnesses. The first witness lives
at the last house on "Northwestern Dr". The second witness, named Annabel, lives
somewhere on "Franklin Ave".
*/

/*
First Witness

SELECT *
FROM person
WHERE address_street_name = "Northwestern Dr"
ORDER BY address_number DESC
LIMIT(1);

id = 14887
name = Morty Shapiro
licese_id = 118009
address_number = 4919
address_street_name = Northwestern Dr
ssn = 111564949
*/

/*
Second Witness

SELECT *
FROM person
WHERE address_street_name = "Franklin Ave" AND name LIKE "Annabel%"
ORDER BY name ASC;

id = 16371
name = Annabel Miller
license_id = 490173
address_number = 103
address_street_name = Franklin Ave
ssn = 318771143
*/

/*
Interviews

SELECT *
FROM interview
WHERE person_id = 14887 OR person_id = 16371;

int_1 = I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag.
The membership number on the bag started with "48Z". Only gold members have those bags.
The man got into a car with a plate that included "H42W".

int_2 = I saw the murder happen, and I recognized the killer from my gym when I was
working out last week on January the 9th.

Killer is male, goes to the gym, has a gold membership starting with 48Z, got into a car
with H42W, was present in the gym on Janurary 9th
*/

/*
Suspects with 48Z id

SELECT *
FROM get_fit_now_member
WHERE membership_status = "gold" AND id LIKE "48Z%";

id = 48Z7A
person_id = 28819
name = Joe Germuska
membership_start_date = 20160305
membership_status = gold

id = 48Z55
person_id = 67318
name = Jeremy Bowers
membership_start_date = 20160101
membership_status = gold
*/

/*
Suspects check in on the 9th

SELECT *
FROM get_fit_now_check_in
WHERE membership_id = "48Z7A" OR membership_id = "48Z55";

membership_id = 48Z7A
check_in_date = 20180109
check_in_time = 1600
check_out_time = 1730

membership_id = 48Z55
check_in_date = 20180109
check_in_time = 1530
check_out_time = 1700
*/

/*
Witness 2 member id

SELECT *
FROM get_fit_now_member
WHERE name = "Annabel Miller";

id = 90081
person_id = 16371
name = Annabel 
membership_start_date = 20160208
membership_status = gold
*/

/*
Witness 2 gym check in

SELECT *
FROM get_fit_now_check_in
WHERE membership_id = "90081";

membership_id = 90081
check_in_date = 20180109
check_in_time = 1600
check_out_time = 1700

Both suspects present at gym during this time
*/

/*
Suspects with plate containing H42W

SELECT *
FROM drivers_license
WHERE gender = "male" AND (plate_number LIKE "H42W%%" OR
						   plate_number LIKE "%H42W%" OR 
						   plate_number LIKE "%%H42W");

id = 423327
age = 30
height = 70
eye_color = brown
hair_color = brown
gender = male
plat_number = 0H42W2
car_make = Chevrolet
car_model = Spark LS

id = 664760
age = 21
height = 71
eye_color = black
hair_color = black
gender = male
plat_number = 4H42WR
car_make = Nissan
car_model = Altima
*/

/*
Compare license_id of suspects to licenses with H42W

SELECT *
FROM person
WHERE name = "Joe Germuska" OR name = "Jeremy Bowers";

id = 28819
name = Joe Germuska
license_id = 173289
address_number = 111
address_street_name = Fisk Rd
ssn = 138909730

id = 67318
name = Jeremy Bowers
license_id = 423327
address_number = 530
address_street_name = Washington Pl, Apt 3A
ssn = 871539279

Jeremy Bowers is the murderer.
*/

/*
Ok it says to check his interview

SELECT *
FROM interview
WHERE person_id = 67318;

transcript = I was hired by a woman with a lot of money. I don't know her name but I know
she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S.
I know that she attended the SQL Symphony Concert 3 times in December 2017.

Suspect has a high income, is 5'5" (65") to 5'7" (67"), has red hair, drives a
Tesla Model S, attended SQL Symphony Concert 3 times in December 2017.
*/

/*
New suspect

SELECT *
FROM drivers_license
WHERE gender = "female" AND height > 64 AND height < 68 AND hair_color = "red" AND
car_make = "Tesla" AND car_model = "Model S";

id = 202298
age = 68
height = 66
eye_color = green
hair_color = red
gender = female
plate_number = 500123
car_make = Tesla
car_model = Model S

id = 291182
age = 65
height = 66
eye_color = blue
hair_color = red
gender = female
plate_number = 08CM64
car_make = Tesla
car_model = Model S

id = 918773
age = 48
height = 65
eye_color = black
hair_color = red
gender = female
plate_number = 917UU3
car_make = Tesla
car_model = Model S
*/