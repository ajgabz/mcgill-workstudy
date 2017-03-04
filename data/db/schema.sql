-- Remove tables if they already exist;
DROP TABLE IF EXISTS workstudy_application;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS faculty;
DROP TABLE IF EXISTS term;

-- Remove enumerated types if they already exist;
DROP TYPE IF EXISTS SEASON;
DROP TYPE IF EXISTS DECISION;

-- After clearing the database of the following tables and types involved
-- in this schema, we can start anew and create the schema as such.

-- All McGill students have a nine-digit student ID
-- In PostgreSQL, the INTEGER data type supports up to 10-digit student IDs
CREATE TABLE student (
  id INTEGER PRIMARY KEY
);


CREATE TABLE faculty (
  id          CHAR(2) PRIMARY KEY,
  description VARCHAR(32) NOT NULL
);


--  For a calendar year X, the first term is winter, then summer, and lastly fall.
--  For example, the 2016 calendar year begins with Winter 2016, followed by Summer 2016,
--  and then Fall 2016.

--  For the sake of completeness, we are adding the 'spring' option.

-- This ordering is crucial for proper SQL ordering.
CREATE TYPE SEASON AS ENUM ('Winter', 'Spring', 'Summer', 'Fall');


CREATE TABLE term (
  id SERIAL PRIMARY KEY,
	academic_season SEASON NOT NULL,
	year INTEGER NOT NULL,
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
  UNIQUE (academic_season, year)
);


-- Each work study application is associated with a decision.
CREATE TYPE DECISION AS ENUM ('Accepted', 'Pending', 'Refused', 'Revoked');


--  Due to the omissions in the original Work Study acceptance list, certain attributes are
--  permitted to be null.  Hopefully, this matter will be rectified as to have all information
--  available.

CREATE TABLE workstudy_application (
	student_id INTEGER,
	faculty_id CHAR(2) NOT NULL,
	term_id INTEGER,
	status DECISION NOT NULL,
	start_date DATE,
	end_date DATE,
	PRIMARY KEY (student_id, term_id),
	FOREIGN KEY (student_id) REFERENCES student(id),
	FOREIGN KEY (faculty_id) REFERENCES faculty(id),
	FOREIGN KEY (term_id) REFERENCES term(id)
);

