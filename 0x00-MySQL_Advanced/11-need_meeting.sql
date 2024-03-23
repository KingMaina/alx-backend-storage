-- SQL script that creates a view that lists all students that have
-- a score under 80 (strict) and no last_meeting or more than 1 month.
CREATE VIEW need_meeting (name)
AS SELECT name
FROM students
WHERE (score < 80)
AND (last_meeting IS NULL
    -- OR TIMESTAMPDIFF(MONTH, last_meeting, CURDATE()) >= 1
    OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
