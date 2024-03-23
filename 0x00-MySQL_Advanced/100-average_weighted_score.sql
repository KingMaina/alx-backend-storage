-- SQL script creates a stored procedure that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_weight_score FLOAT;

    -- Calculate the average weighted score:
    -- sum(correction_scores * project_weight) / sum(project_weights)
    SET avg_weight_score = (
        SELECT SUM(c.score * p.weight) / SUM(weight)
        FROM corrections AS c
        JOIN users AS u ON u.id = c.user_id
        JOIN projects AS p ON p.id = c.project_id
        WHERE u.id = user_id);

    -- Update user's average score table 
    UPDATE users
    SET average_score = avg_weight_score
    WHERE id = user_id;
END//

DELIMITER ;