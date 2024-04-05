

CREATE TABLE "CatalogueRecord" (
	date TEXT, 
	language TEXT, 
	"pointOfContact" TEXT NOT NULL, 
	PRIMARY KEY (date, language, "pointOfContact")
);

CREATE TABLE "NapMetadata" (
	uid TEXT NOT NULL, 
	name TEXT, 
	"pointOfContact" TEXT NOT NULL, 
	PRIMARY KEY (uid)
);
