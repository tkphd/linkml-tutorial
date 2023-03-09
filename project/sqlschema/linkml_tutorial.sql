

CREATE TABLE "Animal" (
	id TEXT NOT NULL, 
	age_in_years INTEGER, 
	birth_date DATE, 
	name TEXT, 
	species TEXT, 
	breed TEXT, 
	color TEXT, 
	weight_in_mgs INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnimalCollection" (
	animals TEXT, 
	PRIMARY KEY (animals)
);

CREATE TABLE "Person" (
	age_in_years INTEGER, 
	birth_date DATE, 
	name TEXT, 
	primary_email TEXT, 
	vital_status VARCHAR(7) NOT NULL, 
	pets TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "PersonCollection" (
	entities TEXT, 
	PRIMARY KEY (entities)
);
