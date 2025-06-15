-- The percent sign % represents zero, one, or multiple characters
-- The underscore sign _ represents one, single character


-- 1. Find students born after 2007-01-01 AND whose first name starts with 'A'
SELECT * FROM students
WHERE age > '2007-01-01' AND name LIKE 'A%';

-- 2. Find students whose last name begins with 'N' OR whose first name begins with 'J'
SELECT * FROM students
WHERE lastname LIKE 'N%' OR name LIKE 'J%';

-- 3. Find courses where the description does not contain the word 'math'
SELECT * FROM courses 
WHERE courseName NOT LIKE '%math%';

-- 4. Use INNER JOIN to list each student’s full name and the course name they are enrolled in

SELECT students.name || ' ' || students.lastname AS fullname, courses.coursename
 -- concatenates them with a space in between to create a single 'fullname' field 'AS fullname'
FROM students
INNER JOIN courses ON students.course_id = courses.id;
-- fullname | courseName
-- for students who have a valid course assigned.
-- If a student’s course_id is null or doesn’t match a courses.id, they’re excluded because it’s an INNER JOIN.
