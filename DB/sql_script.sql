-- Table: Customers
CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY,         -- Primary Key, Auto Increment
    FirstName VARCHAR(50),                 -- Customer's first name
    LastName VARCHAR(50),                  -- Customer's last name
    Email VARCHAR(100) UNIQUE,             -- Customer's email, unique
    PasswordHash VARCHAR(255),             -- Hashed password
    RegisteredAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    ProfileUpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of last profile update
);

-- Table: Products
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY,          -- Primary Key, Auto Increment
    Name VARCHAR(100),                     -- Product name
    Description TEXT,                      -- Product description
    Price DECIMAL(10, 2),                  -- Product price
    Stock INT,                             -- Available stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of last product update
);

-- Table: Orders
CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY,            -- Primary Key, Auto Increment
    CustomerID INT,                        -- Foreign Key referencing Customers(CustomerID)
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    Status VARCHAR(50),                    -- Order status (e.g., Pending, Shipped, Delivered)
    TotalAmount DECIMAL(10, 2),            -- Total order amount
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Table: OrderDetails
CREATE TABLE OrderDetails (
    OrderDetailID SERIAL PRIMARY KEY,      -- Primary Key, Auto Increment
    OrderID INT,                           -- Foreign Key referencing Orders(OrderID)
    ProductID INT,                         -- Foreign Key referencing Products(ProductID)
    Quantity INT,                          -- Quantity of the product in this order
    Price DECIMAL(10, 2),                  -- Price of the product at the time of order
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Table: Payments
CREATE TABLE Payments (
    PaymentID SERIAL PRIMARY KEY,          -- Primary Key, Auto Increment
    OrderID INT,                           -- Foreign Key referencing Orders(OrderID)
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of payment
    Amount DECIMAL(10, 2),                 -- Payment amount
    PaymentMethod VARCHAR(50),             -- Payment method (e.g., Credit Card, PayPal)
    Status VARCHAR(50),                    -- Payment status (e.g., Pending, Completed)
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Table: Addresses
CREATE TABLE Addresses (
    AddressID SERIAL PRIMARY KEY,          -- Primary Key, Auto Increment
    CustomerID INT,                        -- Foreign Key referencing Customers(CustomerID)
    AddressLine1 VARCHAR(255),             -- First line of the address
    AddressLine2 VARCHAR(255),             -- Second line of the address
    City VARCHAR(100),                     -- City
    State VARCHAR(100),                    -- State
    ZipCode VARCHAR(20),                   -- Zip code
    Country VARCHAR(100),                  -- Country
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Table: Admins
CREATE TABLE Admins (
    AdminID SERIAL PRIMARY KEY,            -- Primary Key, Auto Increment
    Username VARCHAR(50) UNIQUE,           -- Admin username, unique
    PasswordHash VARCHAR(255),             -- Hashed password
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of admin account creation
);

INSERT INTO Customers (FirstName, LastName, Email, PasswordHash) VALUES
('John', 'Doe', 'john.doe@example.com', 'hashed_password_1'),
('Jane', 'Smith', 'jane.smith@example.com', 'hashed_password_2'),
('Alice', 'Johnson', 'alice.johnson@example.com', 'hashed_password_3'),
('Bob', 'Brown', 'bob.brown@example.com', 'hashed_password_4'),
('Carol', 'Davis', 'carol.davis@example.com', 'hashed_password_5');

INSERT INTO Products (Name, Description, Price, Stock) VALUES
('Chocolate Cupcake', 'Delicious chocolate cupcake', 2.99, 50),
('Vanilla Cupcake', 'Classic vanilla cupcake', 2.49, 100),
('Red Velvet Cupcake', 'Rich red velvet cupcake with cream cheese frosting', 3.49, 75),
('Lemon Cupcake', 'Tangy lemon cupcake', 2.99, 60),
('Carrot Cupcake', 'Healthy carrot cupcake with a hint of spice', 3.29, 80),
('Strawberry Cupcake', 'Sweet strawberry cupcake with fresh strawberries', 3.19, 40),
('Coffee Cupcake', 'Coffee-flavored cupcake for caffeine lovers', 3.39, 90),
('Mint Chocolate Cupcake', 'Refreshing mint with chocolate chips', 3.49, 55),
('Peanut Butter Cupcake', 'Peanut butter cupcake with a creamy center', 3.59, 45),
('Coconut Cupcake', 'Tropical coconut cupcake', 2.99, 70);

INSERT INTO Orders (CustomerID, OrderDate, Status, TotalAmount) VALUES
(1, CURRENT_TIMESTAMP, 'Pending', 15.96),
(2, CURRENT_TIMESTAMP, 'Shipped', 9.98),
(3, CURRENT_TIMESTAMP, 'Delivered', 19.95),
(4, CURRENT_TIMESTAMP, 'Pending', 13.47),
(5, CURRENT_TIMESTAMP, 'Shipped', 8.98);

INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Price) VALUES
(1, 1, 2, 2.99),
(1, 2, 2, 2.49),
(2, 3, 2, 3.49),
(3, 4, 3, 2.99),
(3, 5, 3, 3.29),
(4, 6, 1, 3.19),
(4, 7, 2, 3.39),
(5, 8, 3, 3.49),
(5, 9, 1, 3.59);

INSERT INTO Payments (OrderID, PaymentDate, Amount, PaymentMethod, Status) VALUES
(1, CURRENT_TIMESTAMP, 15.96, 'Credit Card', 'Completed'),
(2, CURRENT_TIMESTAMP, 9.98, 'PayPal', 'Completed'),
(3, CURRENT_TIMESTAMP, 19.95, 'Credit Card', 'Completed'),
(4, CURRENT_TIMESTAMP, 13.47, 'Credit Card', 'Pending'),
(5, CURRENT_TIMESTAMP, 8.98, 'PayPal', 'Completed');

INSERT INTO Addresses (CustomerID, AddressLine1, AddressLine2, City, State, ZipCode, Country) VALUES
(1, '123 Main St', 'Apt 1', 'New York', 'NY', '10001', 'USA'),
(2, '456 Elm St', 'Suite 2', 'Los Angeles', 'CA', '90001', 'USA'),
(3, '789 Oak St', 'Floor 3', 'Chicago', 'IL', '60601', 'USA'),
(4, '101 Pine St', 'Unit 4', 'Houston', 'TX', '77001', 'USA'),
(5, '202 Maple St', 'Room 5', 'Phoenix', 'AZ', '85001', 'USA');

INSERT INTO Admins (Username, PasswordHash) VALUES
('admin1', 'admin_password_hash_1'),
('admin2', 'admin_password_hash_2');
