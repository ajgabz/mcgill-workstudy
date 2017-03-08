-- We need to first populate the database with our referenced tables: Student, Faculty, and Term.

\copy student FROM '../work_study_studentIDs.csv' DELIMITER ',' CSV HEADER;

\copy faculty FROM '../faculties_reformatted.csv' DELIMITER ',' CSV HEADER;

\copy term(academic_season, year, start_date, end_date) FROM '../work_study_terms.csv' DELIMITER ',' CSV HEADER;

-- Finally, we can populate the database with our big association table, Application.

\copy workstudy_application FROM '../work_study_db_ready.csv' DELIMITER ',' CSV HEADER;