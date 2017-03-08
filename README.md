# mcgill-workstudy

## The "unofficial" McGill University Work Study Acceptance List Database & Web Client

This project was created to prototype a database-powered alternative to McGill's official simple and flat-file system for 
searching through the Acceptance/Rejected List for Work Study Applicants.


Full Disclosure:  This project is in NO WAY affliated with McGill University.  It was created for purely pedagogical purposes.


The [original list](http://www.is.mcgill.ca/studentaid/workstudy/StudentList.htm) consists of 140 (printed) pages of Student IDs,
alongside the work study dates that they've either been approved for or a notice that they've been refused for the terms they applied for.


A RDBMS solution is proposed with the schema found under `data/db/schema.sql' and implemented in PostgreSQL.


## Technologies Used in this Project
- Flask, for the backend
- PostgreSQL, for the database
- pl/pgSQL, for controlled information-retrieval via stored procedures
- AngularJS, for the "Advanced Search" form
- Bootstrap, jQuery, DataTables, for the frontend



