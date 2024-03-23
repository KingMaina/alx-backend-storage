-- SQL script creates a stored procedure that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE avg_weight_score FLOAT;

    -- Calculate the average weighted score:
    -- sum(correction_scores * project_weight) / sum(project_weights)
    UPDATE users AS u,
        (SELECT u.id, SUM(c.score * p.weight) / SUM(p.weight) AS w_avg
        FROM users AS u
        JOIN corrections AS c ON u.id = c.user_id
        JOIN projects AS p ON p.id = c.project_id
        GROUP BY u.id)
    AS WeightedAvg

    -- Update users average score records
    SET u.average_score = WeightedAvg.w_avg
    WHERE u.id = WeightedAvg.id;
END//

DELIMITER ;