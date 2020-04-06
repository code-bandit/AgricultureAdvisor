create database loginDatabase;
create table users (
    id SERIAL NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(300) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table articles (
    id SERIAL NOT NULL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    srcLink VARCHAR(150) NOT NULL,
    img VARCHAR(100),
    description VARCHAR(300),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

create table profileUser (
    id SERIAL NOT NULL PRIMARY KEY,
    soilType VARCHAR(50) NOT NULL,
    soilPh VARCHAR(50),
    state VARCHAR(50),
    district VARCHAR(50),
    village VARCHAR(50),
    weather VARCHAR(50),
    FOREIGN KEY (id) REFERENCES users(id)
);

create table areaDetails (
    id SERIAL NOT NULL PRIMARY KEY,
    soilType VARCHAR(50) NOT NULL,
    soilPh VARCHAR(50),
    weatherConditions VARCHAR(50),
    FOREIGN KEY (id) REFERENCES users(id)
);

create table farmerDerivedAttributes (
    id SERIAL NOT NULL PRIMARY KEY,
    state VARCHAR(50),
    district VARCHAR(50),
    village VARCHAR(50),
    FOREIGN KEY (id) REFERENCES users(id)
);