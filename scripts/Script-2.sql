COPY FoodTrucks (foodtruck_id, name, cuisine_type, city)
FROM 'C:\Users\Maxde\Documents\DS Course\M2\FoodTrucks-DB\data\foodtrucks.csv'
DELIMITER ','
CSV HEADER;

COPY Products (product_id, foodtruck_id, name, price, stock)
FROM 'C:\Users\Maxde\Documents\DS Course\M2\FoodTrucks-DB\data\products.csv'
DELIMITER ','
CSV HEADER;

COPY Orders (order_id, foodtruck_id, order_date, status, total)
FROM 'C:\Users\Maxde\Documents\DS Course\M2\FoodTrucks-DB\data\orders.csv'
DELIMITER ','
CSV HEADER;

COPY OrderItems (order_item_id, order_id, product_id, quantity)
FROM 'C:\Users\Maxde\Documents\DS Course\M2\FoodTrucks-DB\data\order_items.csv'
DELIMITER ','
CSV HEADER;

COPY Locations (location_id, foodtruck_id, location_date, zone)
FROM 'C:\Users\Maxde\Documents\DS Course\M2\FoodTrucks-DB\data\locations.csv'
DELIMITER ','
CSV HEADER;
