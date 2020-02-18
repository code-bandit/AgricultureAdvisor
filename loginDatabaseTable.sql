-- create database loginDatabase;
create table users (
    id SERIAL NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(300) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);