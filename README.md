# ice-cream-parlor
**
**Ice Cream Parlor Management System****

The Ice Cream Parlor Management System is a comprehensive solution for managing an ice cream parlor's inventory, flavors, allergens, and customer orders. This system is built with Python and SQLite for backend operations, and it provides a command-line interface for efficient management.

**Features**

**Flavor Management**

Add new flavors with descriptions, seasonal tags, and pricing.
View all available flavors or filter by seasonal availability.
Search for flavors using keywords.

**Ingredient Management**

Maintain a database of ingredients with quantities and units.
Add new ingredients to the inventory.

**Allergen Management**

Maintain a list of allergens for customer safety.
Add allergens to the system.

**Customer Cart Management**

Add or remove flavors to/from the customer's cart.
View cart contents and calculate the total price.
Clear the cart when required.

**Persistent Database**

SQLite database to store all flavors, ingredients, and allergens.
Data integrity ensured through constraints like unique flavor names.

**File Structure**

**1. models.py**
   
Defines data models for the system:
  Flavor, Ingredient, Allergen, and Cart.
Provides methods for cart operations like adding and removing items.

**2. database.py**

Implements database interactions using SQLite.
Handles CRUD operations for flavors, ingredients, and allergens.
Provides search capabilities for flavors.

**3. main.py**

Entry point for the application.
Implements a user-friendly command-line interface.
Integrates flavor, ingredient, allergen, and cart management.

**Prerequisites**

Python 3.8 or later
SQLite (pre-installed with Python)

**Setup and Installation**

**1.Clone the Repository**

bash code
        git clone <repository_url>
        cd ice-cream-parlor

**2.Install Dependencies**

(No additional Python packages required as it uses only the standard library.)

**3.Initialize the Database**

Run the application once to automatically create the SQLite database (ice_cream_parlor.db) and the required tables.

**Usage**

**1.Start the Application**

bash code
      python main.py

**2.Follow the Menu Options**
The main menu provides options for managing flavors, ingredients, allergens, and the cart.

**3.Database**
The database file ice_cream_parlor.db will store all data persistently.

**Example**

**Adding a Flavor**

bashcode

--- Ice Cream Parlor Management ---
1. Add Flavor
...
Enter flavor name: Chocolate
Enter flavor description: Rich dark chocolate
Is this a seasonal flavor? (y/n): n
Enter price: 3.5
Flavor Chocolate added successfully!

**Viewing Flavors**
bash code
---  Ice Cream Parlor Management ---
3. View Flavors
View seasonal flavors only? (y/n): n
ID: 1, Name: Chocolate, Description: Rich dark chocolate, Seasonal: No, Price: $3.50

****Project Highlights****

**Object-Oriented Design:** Efficiently organized code for scalability and maintainability.
**Database Integration:** Uses SQLite for lightweight, persistent data management.
**Command-Line Interface:** Simple and interactive, suitable for a proof-of-concept or small-scale application.
**Extensibility:** Modular design allows easy addition of features like user accounts or reporting tools.

**Contribution**
Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

