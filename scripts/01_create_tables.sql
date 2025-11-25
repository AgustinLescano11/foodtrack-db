
create table FoodTrucks(
foodtruck_id serial primary key,
name varchar (100) not null,
cuisine_type varchar (50) not null,
city varchar (50) not null
);

create table products(
product_id serial primary key,
foodtruck_id int not null,
name varchar (20) not null,
price decimal (10,2) not null,
stock int not null,
foreign key (foodtruck_id) references FoodTrucks(foodtruck_id)
);

create table orders(
order_id serial primary key,
foodtruck_id int not null , 
order_date date not null,
status varchar (50) not null,
total decimal (10,2) not null,
foreign key (foodtruck_id) references FoodTrucks(foodtruck_id)
);

create table OrderItems(
order_item_id serial primary key,
order_id int not null,
product_id int not null, 
quantity int not null,
foreign key (order_id) references orders(order_id), 
foreign key (product_id) references products(product_id)
);

create table locations(
location_id serial primary key,
foodtruck_id int not null, 
location_date date not null,
zone varchar (50) not null,
foreign key (foodtruck_id) references FoodTrucks(foodtruck_id)
);


