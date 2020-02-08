DROP TABLE IF EXISTS orderItem;
DROP TABLE IF EXISTS "order";
DROP TABLE IF EXISTS addaUsers;

CREATE TABLE addaUsers(
    loginName VARCHAR(64),
    password VARCHAR(64),
    PRIMARY KEY (loginName)
);

CREATE TABLE public.order(
    orderId SERIAL,
    loginName VARCHAR(64), 
    dateTime TIMESTAMP,
    PRIMARY KEY (orderId),
    FOREIGN KEY (loginName) REFERENCES addaUsers ON DELETE CASCADE
);

CREATE TABLE orderItem(
    orderId INTEGER,
    item VARCHAR(6), 
    itemQuantity INTEGER,
    PRIMARY KEY (orderId, item),
    FOREIGN KEY (orderId) REFERENCES public.order ON DELETE CASCADE,
    CHECK (item in ('idli', 'chai', 'samosa'))
);