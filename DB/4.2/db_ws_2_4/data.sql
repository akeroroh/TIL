CREATE TABLE transactions (
    user_id INTEGER NOT NULL,
    amount TEXT NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO transactions(user_id, amount, transaction_date)
VALUES
  (1, 100, '2020-01-14'),
  (2, 3043, '2034-01-14'),
  (3, 279348, '1923-08-29'),
  (4, 32789, '1988-09-03');

SELECT first_name, last_name, amount, transaction_date FROM users
INNER JOIN transactions ON id = user_id;

SELECT first_name, last_name, amount, transaction_date FROM users
INNER JOIN transactions ON id = user_id
WHERE transaction_date >= '2024-03-16';

SELECT first_name, last_name, sum(amount) FROM users
INNER JOIN transactions ON id = user_id
GROUP BY user_id;