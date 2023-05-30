use db;

CREATE TABLE students(
    StudentID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    Surname varchar(100) NOT NULL,
    PRIMARY KEY (StudentID)
);


-- CREATE TABLE jobs(
--     job_id int not null,
--     nob_name varchar(100) NOT NULL,
--     PRIMARY KEY (job_id)
-- );


-- CREATE TABLE migration(
-- yearmonth	        varchar(100),
-- monthofrelease	varchar(100),
-- passengertype	    varchar(100),
-- direction	        varchar(100),
-- sex	                varchar(100),
-- age	                varchar(100),
-- estimate	        int,
-- standarderror	    int,
-- statusmigration    varchar(100)
-- );



INSERT INTO students(FirstName, Surname)
VALUES("John", "Andersen"), ("Emma", "Smith");  

Select * from students;

-- Select * from migration;