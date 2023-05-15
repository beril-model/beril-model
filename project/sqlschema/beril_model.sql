

CREATE TABLE "DnaExtract" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	mass_g FLOAT, 
	color VARCHAR(5), 
	PRIMARY KEY (id)
);

CREATE TABLE "InformationArtifact" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	size_in_bytes INTEGER, 
	md5 TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	mass_g FLOAT, 
	color VARCHAR(5), 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThingCollection" (
	material_entities TEXT, 
	processes TEXT, 
	PRIMARY KEY (material_entities, processes)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	first_name TEXT, 
	last_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "PersonCollection" (
	people TEXT, 
	PRIMARY KEY (people)
);

CREATE TABLE "Process" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	inputs TEXT, 
	outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SoilSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	mass_g FLOAT, 
	color VARCHAR(5), 
	PRIMARY KEY (id)
);
