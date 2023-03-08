CREATE TABLE IF NOT EXISTS USER_LOGIN
    (
        USER_LOGIN_ID integer primary key,
        USER_ID integer,
        LOGIN_DATETIME TEXT(20)
    );