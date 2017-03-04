DROP FUNCTION IF EXISTS workstudy_point_query(INTEGER, CHAR(2), SEASON, INTEGER, DECISION, DATE, DATE);
DROP FUNCTION IF EXISTS get_searchable_faculties();
DROP FUNCTION IF EXISTS get_searchable_terms(BOOLEAN);


-------------------------------------------------------------------------------
--
-- NAME: workstudy_point_query
--
-- NOTES: Description to be added later.
--
--
-------------------------------------------------------------------------------  


CREATE OR REPLACE FUNCTION workstudy_point_query(
    _student_id   INTEGER = NULL,
    _faculty_id   CHAR(2) = NULL,
    _term_season  SEASON = NULL,
    _term_year    INTEGER = NULL,
    _status       DECISION = NULL,
    _start_date   DATE = NULL,
    _end_date     DATE = NULL)
  RETURNS TABLE(student_id INTEGER, faculty_id CHAR(2), term_season SEASON, 
                term_year INTEGER, status DECISION, start_date DATE, end_date DATE) AS
$func$

SELECT workstudy_application.student_id, workstudy_application.faculty_id, 
       term.academic_season, term.year, workstudy_application.status,
       workstudy_application.start_date, workstudy_application.end_date
FROM workstudy_application
INNER JOIN term ON workstudy_application.term_id = term.id
WHERE ($1 IS NULL OR workstudy_application.student_id = $1)
AND ($2 IS NULL OR workstudy_application.faculty_id = $2)
AND ($3 IS NULL OR term.academic_season = $3)
AND ($4 IS NULL OR term.year = $4)
AND ($5 IS NULL OR workstudy_application.status = $5)
AND ($6 IS NULL OR workstudy_application.start_date = $6)
AND ($7 IS NULL OR workstudy_application.end_date = $7);

$func$ LANGUAGE sql;



-------------------------------------------------------------------------------
--
-- NAME: get_searchable_faculties
--
-- INPUT: (None)
--
-- RETURNS: A sorted list of all the faculty IDs, along with their respective
--          descriptions.
--
-- NOTES: List is sorted in ascending order by faculty ID.
--
--
-------------------------------------------------------------------------------  

CREATE OR REPLACE FUNCTION get_searchable_faculties()
  RETURNS TABLE(faculty_id CHAR(2), faculty_description VARCHAR(32)) AS
$func$

SELECT id, description FROM faculty ORDER BY id;

$func$ LANGUAGE sql;



-------------------------------------------------------------------------------
--
-- NAME: get_searchable_terms
--
-- INPUT: chronological_order BOOLEAN (Default value of NULL)
--        Indicates if chronological ordering should be applied.
--
--        If TRUE, chronological ordering (Past to Present) is applied.
--        If FALSE, reverse chronological ordering (Present to Past) is applied.
--        If NULL, no ordering is performed.
--
-- RETURNS: A sorted list of all the terms as represented by their season
--          and year.  
--
--
-------------------------------------------------------------------------------  


CREATE OR REPLACE FUNCTION get_searchable_terms(chronological_order BOOLEAN = NULL)
  RETURNS TABLE(term_season SEASON, term_year INTEGER) AS
$func$

BEGIN

  IF chronological_order = TRUE THEN
    RETURN QUERY SELECT academic_season, year FROM term ORDER BY year, academic_season;
  ELSIF chronological_order = FALSE THEN
     RETURN QUERY SELECT academic_season, year FROM term ORDER BY year DESC, academic_season DESC;
  ELSE
    RETURN QUERY SELECT academic_season, year FROM term;
  END IF;

END;
$func$ LANGUAGE plpgsql;
