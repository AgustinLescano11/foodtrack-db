# Homework L1 - FoodTrucks DB

## Modelo relacional

- FOODTRUCKS(foodtruck_id PK, name, cuisine_type, city)
- PRODUCTS(product_id PK, foodtruck_id FK, name, price, stock)
- ORDERS(order_id PK, foodtruck_id FK, order_date, status, total)
- ORDER_ITEMS(order_item_id PK, order_id FK, product_id FK, quantity)
- LOCATIONS(location_id PK, foodtruck_id FK, location_date, zone)
