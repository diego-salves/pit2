# Data Dictionary for Cakemania Database

## Table: Customers
| Column          | Data Type        | Description                        |
|-----------------|------------------|------------------------------------|
| CustomerID      | INT              | Primary Key, Auto Increment        |
| FirstName       | VARCHAR(50)      | Customer's first name              |
| LastName        | VARCHAR(50)      | Customer's last name               |
| Email           | VARCHAR(100)     | Customer's email, unique           |
| PasswordHash    | VARCHAR(255)     | Hashed password                    |
| RegisteredAt    | TIMESTAMP        | Timestamp of account creation      |
| ProfileUpdatedAt| TIMESTAMP        | Timestamp of last profile update   |

## Table: Products
| Column          | Data Type        | Description                        |
|-----------------|------------------|------------------------------------|
| ProductID       | INT              | Primary Key, Auto Increment        |
| Name            | VARCHAR(100)     | Product name                       |
| Description     | TEXT             | Product description                |
| Price           | DECIMAL(10, 2)   | Product price                      |
| Stock           | INT              | Available stock                    |
| CreatedAt       | TIMESTAMP        | Timestamp of product creation      |
| UpdatedAt       | TIMESTAMP        | Timestamp of last product update   |

## Table: Orders
| Column          | Data Type        | Description                        |
|-----------------|------------------|------------------------------------|
| OrderID         | INT              | Primary Key, Auto Increment        |
| CustomerID      | INT              | Foreign Key referencing Customers  |
| OrderDate       | TIMESTAMP        | Timestamp of order creation        |
| Status          | VARCHAR(50)      | Order status                       |
| TotalAmount     | DECIMAL(10, 2)   | Total order amount                 |

## Table: OrderDetails
| Column          | Data Type        | Description                        |
|-----------------|------------------|------------------------------------|
| OrderDetailID   | INT              | Primary Key, Auto Increment        |
| OrderID         | INT              | Foreign Key referencing Orders     |
| ProductID       | INT              | Foreign Key referencing Products   |
| Quantity        | INT              | Quantity of the product in this order|
| Price           | DECIMAL(10, 2)   | Price of the product at the time of order|

## Table: Payments
| Column          | Data Type        | Description                        |
|-----------------|------------------|------------------------------------|
| PaymentID       | INT              | Primary Key, Auto Increment        |
| OrderID         | INT              | Foreign Key referencing Orders     |
| PaymentDate     | TIMESTAMP        | Timestamp of payment               |
| Amount          | DECIMAL(10, 2)   | Payment amount                     |
| PaymentMethod   | VARCHAR(50)      | Payment method                     |
| Status          | VARCHAR(50)      | Payment status                     |

## Table: Addresses
| Column          | Data Type        | Description                        |
|-----------------|------------------|------------------------------------|
| AddressID       | INT              | Primary Key, Auto Increment        |
| CustomerID      | INT              | Foreign Key referencing Customers  |
| AddressLine1    | VARCHAR(255)     | First line of the address          |
| AddressLine2    | VARCHAR(255)     | Second line of the address         |
| City            | VARCHAR(100)     | City                               |
| State           | VARCHAR(100)     | State                              |
| ZipCode         | VARCHAR(20)      | Zip code                           |
| Country         | VARCHAR(100)     | Country                            |

## Table: Admins
| Column          | Data Type        | Description                        |
|-----------------|------------------|------------------------------------|
| AdminID         | INT              | Primary Key, Auto Increment        |
| Username        | VARCHAR(50)      | Admin username, unique             |
| PasswordHash    | VARCHAR(255)     | Hashed password                    |
| CreatedAt       | TIMESTAMP        | Timestamp of admin account creation|