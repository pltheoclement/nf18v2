CREATE TABLE Espèces (
  nom VARCHAR CHECK (nom in('felin','canide','reptile','rongeur','oiseau','autre')),
  PRIMARY KEY (nom)
);

CREATE 	TABLE Animaux (
  DossierMed INTEGER,
  nom VARCHAR NOT NULL,
  dtNaiss DATE NOT NULL,
  numPuce INTEGER,
  numPasseport INTEGER,
  espece VARCHAR,
  FOREIGN KEY (espece) REFERENCES Espèces(nom),
  PRIMARY KEY (DossierMed)
);

CREATE TABLE Clients (
  id INTEGER,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  dtNaiss DATE NOT NULL,
  adresse VARCHAR NOT NULL,
  tel INTEGER NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Personnel (
  id INTEGER,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  dtNaiss DATE NOT NULL,
  adresse VARCHAR NOT NULL,
  tel INTEGER NOT NULL,
  poste VARCHAR CHECK (poste in ('vétérinaire','assistant')),
  PRIMARY KEY (id)
);

CREATE TABLE Médicaments (
  id INTEGER,
  molecule VARCHAR NOT NULL,
  effets VARCHAR NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Compatible (
  espece VARCHAR,
  medicament INTEGER,
  FOREIGN KEY (espece) REFERENCES Espèces(nom),
  FOREIGN KEY (medicament) REFERENCES Médicaments(id),
  PRIMARY KEY (espece,medicament)
);

CREATE TABLE Spécialité (
  personnel INTEGER,
  espece VARCHAR,
  FOREIGN KEY (personnel) REFERENCES Personnel(id),
  FOREIGN KEY (espece) REFERENCES Espèces(nom),
  PRIMARY KEY (personnel,espece)
);


CREATE TABLE Traitements (
  id INTEGER,
  dtDebut DATE NOT NULL,
  dtSaisie DATE NOT NULL,
  num_dossier INTEGER,
  prescripteur INTEGER,
  FOREIGN KEY (num_dossier) REFERENCES Animaux(DossierMed),
  FOREIGN KEY (prescripteur) REFERENCES Personnel(id),
  PRIMARY KEY (id)
);


CREATE TABLE Resultats_analyse (
  lien VARCHAR,
  dtSaisie DATE NOT NULL,
  num_dossier INTEGER,
  FOREIGN KEY (num_dossier) REFERENCES Animaux(DossierMed),
  PRIMARY KEY (lien)
);

CREATE TABLE Consulter (
  id INTEGER,
  dateConsult DATE NOT NULL,
  observation VARCHAR,
  dtSaisie DATE NOT NULL,
  num_dossier INTEGER,
  personnel INTEGER,
  FOREIGN KEY (num_dossier) REFERENCES Animaux(DossierMed),
  FOREIGN KEY (personnel) REFERENCES Personnel(id),
  PRIMARY KEY (id)
);

CREATE TABLE Procedures (
  id INTEGER,
  description VARCHAR NOT NULL,
  dtSaisie DATE NOT NULL,
  num_dossier INTEGER,
  personnel INTEGER,
  FOREIGN KEY (num_dossier) REFERENCES Animaux(DossierMed),
  FOREIGN KEY (personnel) REFERENCES Personnel(id),
  PRIMARY KEY (id)
);

CREATE TABLE Poids (
  mesure INTEGER CHECK (mesure > 0 ),
  dtSaisie DATE NOT NULL,
  num_dossier INTEGER,
  FOREIGN KEY (num_dossier) REFERENCES Animaux(DossierMed),
  PRIMARY KEY (dtSaisie,num_dossier)
);

CREATE TABLE Taille (
  mesure INTEGER CHECK (mesure > 0 ),
  dtSaisie DATE NOT NULL,
  num_dossier INTEGER,
  FOREIGN KEY (num_dossier) REFERENCES Animaux(DossierMed),
  PRIMARY KEY (dtSaisie,num_dossier)
);


CREATE TABLE Appartenir (
  animal INTEGER,
  client INTEGER,
  debut_periode DATE NOT NULL,
  fin_periode DATE NOT NULL,
  FOREIGN KEY (animal) REFERENCES Animaux(DossierMed),
  FOREIGN KEY (client) REFERENCES Clients(id),
  PRIMARY KEY (animal,client)
);

CREATE TABLE Prise_medicament (
  duree INTEGER NOT NULL CHECK (duree > 0),
  quantite_jour INTEGER NOT NULL CHECK (quantite_jour > 0),
  traitement INTEGER,
  medicament INTEGER,
  FOREIGN KEY (traitement) REFERENCES Traitements(id),
  FOREIGN KEY (medicament) REFERENCES Médicaments(id),
  PRIMARY KEY (traitement,medicament)
);

CREATE TABLE Suivre (
  debut_suivi DATE NOT NULL,
  fin_suivi DATE NOT NULL,
  animal INTEGER,
  personnel INTEGER,
  FOREIGN KEY (animal) REFERENCES Animaux(DossierMed),
  FOREIGN KEY (personnel) REFERENCES Personnel(id),
  PRIMARY KEY (animal,personnel)
);
