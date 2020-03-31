-- create database loginDatabase;
-- create table users (
--     id SERIAL NOT NULL PRIMARY KEY,
--     username VARCHAR(50) NOT NULL UNIQUE,
--     password VARCHAR(300) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

create table articles {
    id SERIAL NOT NULL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    srcLink VARCHAR(150) NOT NULL,
    img VARCHAR(100),
    description VARCHAR(300),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
};