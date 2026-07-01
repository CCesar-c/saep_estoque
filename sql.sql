create database saep_estoque;
use saep_estoque;
CREATE TABLE produto(
id int auto_increment primary key,
nome Varchar(100) not null,
categoria varchar(100) not null,
quantidade int not null,
preco decimal(10,2) not null
);
select * from produto
show tables