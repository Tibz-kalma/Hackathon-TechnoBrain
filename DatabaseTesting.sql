SELECT * FROM Users WHERE CreatedDate >=30;

SELECT SUM(Email) FROM Users WHERE Email LIKE '%@example.com';

UPDATE Users SET ContactName='technob' WHERE Email='UserId';