DROP DATABASE IF EXISTS qms;
CREATE DATABASE qms;
USE qms;

CREATE TABLE staff (
    id INT PRIMARY KEY AUTO_INCREMENT,
    job VARCHAR(20),
    pay VARCHAR(20)
);

CREATE TABLE passengers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(20),
    lastname  VARCHAR(20),
    dob       DATE,
    staff_id  INT,
    FOREIGN KEY (staff_id) REFERENCES staff(id)
);

CREATE TABLE flights (
    id INT PRIMARY KEY AUTO_INCREMENT,
    destination VARCHAR(3),
    departure   TIME,
    arrival     TIME
);

CREATE TABLE bookings (
    id VARCHAR(20) PRIMARY KEY,
    passenger_id INT NOT NULL,
    flight_id    INT NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES passengers(id),
    FOREIGN KEY (flight_id)    REFERENCES flights(id)
);
