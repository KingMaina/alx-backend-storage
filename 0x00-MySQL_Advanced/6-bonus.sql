-- SQL procedure that adds a bonus to student scores
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE _project_id INT;

	-- Check if the project exists
	SELECT id INTO _project_id FROM projects WHERE name = project_name;

	-- If project does not exist, create it
	IF _project_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET _project_id = LAST_INSERT_ID();
	END IF;

	-- Add bonus score
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, _project_id, score);
END//

DELIMITER ;
