-- Remove tables if they already exist;
DROP TABLE IF EXISTS Application;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Term;

-- Remove enumerated types if they already exist;
DROP TYPE IF EXISTS SEMESTER;
DROP TYPE IF EXISTS DECISION;

-- After clearing the database of the following tables and types involved
-- in this schema, we can start anew and create the schema as such.

-- All McGill students have a nine-digit student ID
-- In PostgreSQL, the INTEGER data type supports up to 10-digit student IDs
CREATE TABLE Student (
	StudentID INTEGER NOT NULL,
	PRIMARY KEY (StudentID)
);


CREATE TABLE Faculty (
	FacultyID CHAR(2) NOT NULL,
	Description VARCHAR(32) NOT NULL,
	PRIMARY KEY (FacultyID) 
);


--  For a calendar year X, the first term is winter, then summer, and lastly fall.
--  For example, the 2016 calendar year begins with Winter 2016, followed by Summer 2016,
--  and then Fall 2016.

-- This ordering is crucial for proper SQL ordering.
CREATE TYPE SEMESTER AS ENUM ('Winter', 'Summer', 'Fall');


CREATE TABLE Term (
	SemesterTerm SEMESTER NOT NULL,
	TermYear INTEGER NOT NULL,
	TermStart DATE NOT NULL,
	TermEnd DATE NOT NULL,
	PRIMARY KEY (SemesterTerm, TermYear)
);


-- Each work study application is associated with a decision.
CREATE TYPE DECISION AS ENUM ('Accepted', 'Pending', 'Refused', 'Revoked');


--  Due to the omissions in the original Work Study acceptance list, certain attributes are
--  permitted to be null.  Hopefully, this matter will be rectified as to have all information
--  available.

CREATE TABLE Application (
	StudentID INTEGER NOT NULL,
	FacultyID CHAR(2) NOT NULL,
	SemesterTerm SEMESTER NOT NULL,
	TermYear INTEGER NOT NULL,
	ApplicationDecision DECISION NOT NULL,
	WorkStart DATE,
	WorkEnd DATE,
	PRIMARY KEY (StudentID, SemesterTerm, TermYear),
	FOREIGN KEY (StudentID) REFERENCES Student,
	FOREIGN KEY (FacultyID) REFERENCES Faculty,
	FOREIGN KEY (SemesterTerm, TermYear) REFERENCES Term
);