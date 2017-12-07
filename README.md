# final-project

This project is a web application for a business database.

The database consists of two tables: customer and order.

Customer | Order
------------ | -------------
CustomerID  | OrderID
Customer Name | Order description
Customer Address| Order date
Orders| CustomerID FK

The database consists of an one-to-many relationship: one customer can place many orders and each order belongs to one customer.

**To Run the Application:**

To initialize the database:
```javascript
$ python manage.py deploy

```
To run the development server:
```javascript
$ python manage.py runserver -d

```

**To Use The Application**

To **Add** an Order:
1. Go to the Orders tab
2. Click **Add Order**
3. Enter the Name, Year, Customer, and Description of the order. If it is not an existing customer, one may be added using the "Add Customers Tab"
4. Press "Add Order" Button

To **Add** a Customer:
1. Go to the Customer tab
2. Click **Add Customer**
3. Enter the Name, and address of the customer. These can then be used for existing, or new orders
4. Press "Add Order" Button

To **Delete/Edit** a Customer:
1. Go to the customers tab
2. Choose from the Actions you would like
3. You will then be directed to a page where you may edit, or delete a record.
4. Press Save changes.
