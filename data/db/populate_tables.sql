-- We need to first populate the database with our referenced tables: Student, Faculty, and Term.

\copy Student FROM '../work_study_studentIDs.csv' DELIMITER ',' CSV HEADER;

\copy Faculty FROM '../faculties_reformatted.csv' DELIMITER ',' CSV HEADER;

\copy Term FROM '../work_study_terms.csv' DELIMITER ',' CSV HEADER;

-- Finally, we can populate the database with our big association table, Application.

\copy Application FROM '../work_study_db_ready.csv' DELIMITER ',' CSV HEADER;