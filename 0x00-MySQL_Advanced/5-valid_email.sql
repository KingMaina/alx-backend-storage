-- An SQL trigger that resets the `valid_email` attribute only whent he user's email changes
DELIMITER //

CREATE TRIGGER reset_user_email_validity_after_email_change
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		IF OLD.email != NEW.email THEN
			SET NEW.valid_email = 0;
		END IF;
	END//

DELIMITER ;
