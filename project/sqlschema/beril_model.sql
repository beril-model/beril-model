

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
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NonProcess" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	PRIMARY KEY (id)
);

CREATE TABLE "PersonCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "Process" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	inputs TEXT, 
	outputs TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Observation" (
	raw_value TEXT, 
	"MaterialEntity_id" TEXT, 
	PRIMARY KEY (raw_value, "MaterialEntity_id"), 
	FOREIGN KEY("MaterialEntity_id") REFERENCES "MaterialEntity" (id)
);
