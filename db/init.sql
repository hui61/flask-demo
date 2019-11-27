create database demo;
use demo;

create table user
(
    id       int auto_increment
        primary key,
    name     varchar(20)   not null,
    password varchar(42)   not null,
    role     int default 0 not null
);

insert into user (name, password, role)
VALUES ('huiliuyi', '123456', 1);