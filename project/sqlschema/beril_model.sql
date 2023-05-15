

CREATE TABLE "DnaExtract" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type_value TEXT NOT NULL, 
	mass_g FLOAT, 
	color VARCHAR(5), 
	PRIMARY KEY (id)
);

CREATE TABLE "InformationArtifact" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type_value TEXT NOT NULL, 
	size_in_bytes INTEGER, 
	md5 TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MaterialEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type_value TEXT NOT NULL, 
	mass_g FLOAT, 
	color VARCHAR(5), 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type_value TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThingCollection" (
	material_entities TEXT, 
	processes TEXT, 
	PRIMARY KEY (material_entities, processes)
);

CREATE TABLE "NonProcess" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type_value TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Observation" (
	raw_value TEXT, 
	PRIMARY KEY (raw_value)
);

CREATE TABLE "Process" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type_value TEXT NOT NULL, 
	inputs TEXT, 
	outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "SoilSample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	type_value TEXT NOT NULL, 
	mass_g FLOAT, 
	color VARCHAR(5), 
	PRIMARY KEY (id)
);
