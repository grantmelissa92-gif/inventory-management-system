CREATE DATABASE inventory_db;

USE inventory_db;

CREATE TABLE equipment (
    equipment_id INT PRIMARY KEY AUTO_INCREMENT,
    asset_tag VARCHAR(20),
    device_type VARCHAR(50),
    brand VARCHAR(50),
    assigned_to VARCHAR(100),
    status VARCHAR(50),
    location VARCHAR(100)
);