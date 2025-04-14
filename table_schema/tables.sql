create table users (
user_id int not null primary key,
fname varchar(255) not null,
lname varchar(255) not null,
mname varchar(255),
gender varchar(50) not null,
email varchar(255) unique not null,
telephone varchar(20),
usertype varchar(50) not null,
userstatus varchar(50) not null,
password varchar(255) not null
);




-- 	1001291	Brian	Hall	brianhall@gmail.com	IT	Active	1234
--  620141010	Damion	Henry	damionedu@gmail.com	Student	Active	1234

SELECT * FROM users;

INSERT INTO users (user_id, fname, lname, mname, gender, email, telephone, usertype, userstatus, password)
values (1001291, 'Brian', 'Hall','','Male', 'brianhall@gmail.com','18764445555', 'IT', 'Active', '1234');

INSERT INTO users (user_id, fname, lname, mname, gender, email, telephone, usertype, userstatus, password)
values (620141010, 'Damion', 'Henry','Junior','Male', 'damionedu@gmail.com','18764216318', 'Student', 'Active', '1234');


select user_id, email from users where user_id = 620141010 or email= 'brianhall@gmail.com'