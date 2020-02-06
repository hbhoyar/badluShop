DROP TABLE IF EXISTS orderHistory;
DROP TABLE IF EXISTS addaUsers;

CREATE TABLE addaUsers(
    loginName VARCHAR(50),
    password VARCHAR(50),
    PRIMARY KEY (loginName)
);

CREATE TABLE orderHistory(
    orderId SERIAL,
    loginName VARCHAR(50), 
    dateTime TIMESTAMP, 
    item VARCHAR(6), 
    itemQuantity SMALLINT,
    PRIMARY KEY (orderId),
    FOREIGN KEY (loginName) REFERENCES addaUsers ON DELETE CASCADE,
    CHECK (item in ('idli', 'chai', 'samosa'))
);