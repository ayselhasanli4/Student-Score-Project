create table telebe(
t_id int primary key,
t_ad varchar2(20),
t_soyad varchar2(20));

select * from telebe;
insert into telebe values (&t_id,'&t_ad','&t_soyad');

create table qiymet(
q_id int primary key,
t_id int,
foreign key (t_id) references telebe(t_id));

select * from qiymet;
insert into qiymet values (&q_id,&t_id);
