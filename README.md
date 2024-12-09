
# **Ice Cream Parlor Management System**

The Ice Cream Parlor Management System is a Python application designed to help ice cream parlors streamline their operations. It offers tools for managing flavors, ingredients, allergens, and customer orders, all through an interactive command-line interface.

# **Table of Contents**


Here’s how the updated Table of Contents section should look in your README.md for a clear, line-by-line structure as you requested:

Table of Contents
Overview
Features
Technologies Used
Installation
Usage
Test Steps
Docker Integration
File Structure
Code Documentation
Contributing
License

# **Overview**

This project focuses on providing an intuitive and efficient system for ice cream parlor management. It allows staff to handle inventory, customer orders, and allergen information in a centralized and persistent manner, ensuring seamless service.

# **Features**

**1. Flavor Management**

Add new flavors with detailed descriptions, seasonal labels, and pricing.   
   View all available flavors or filter by seasonal options.
   Search for specific flavors using keywords.

**2. Ingredient Management**

Add and maintain ingredients with quantities and measurement units.
Keep track of ingredient availability for inventory purposes.

**3. Allergen Management**

Track and update allergen information for customer safety.
Prevent duplication with unique allergen records.

**4. Customer Cart Management**

Add or remove flavors to/from a shopping cart.
View cart contents with real-time price calculation.
Clear the cart when starting a new transaction.

**5. Database Integration**

Uses SQLite for persistent data storage.
Data is retained across sessions, ensuring reliability.

# **File Structure**

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

# **Technologies Used**

Language: Python (3.8 or later)
Database: SQLite
Modules: Python's built-in libraries, including dataclasses and sqlite3

# **Installation**

**Prerequisites**

Python 3.8 or newer must be installed.
SQLite is required (pre-installed with Python).

**Steps**

**1.Clone the Repository**

bash code             

    git clone https://github.com/NiroshaVajiravelu/ice-cream-parlor.git
    cd ice-cream-parlor
    
**2.Install Dependencies**

(This project does not use external dependencies. Python's standard library suffices.)

**3.Run the Application**

Execute the following command to start:

bash code

         python main.py

         
# **How to Use**

**1.Launch the Application**

Run python main.py to start the system.

**2.Navigate the Menu**

The main menu offers various options, such as managing flavors, ingredients, allergens, and the cart. Enter the number corresponding to the desired action.

**3.Examples of Operations**
  **Adding a Flavor**

bash code

Enter flavor name: Strawberry
Enter flavor description: Fresh strawberries blended to perfection.
Is this a seasonal flavor? (y/n): y
Enter price: 5.0

  **Viewing Cart**
  
bash code

--- Current Cart ---
Name: Strawberry, Price: $5.00
Total Price: $5.00

# **Project Structure**

**models.py:** Contains class definitions for core entities like flavors, ingredients, allergens, and the shopping cart.

**database.py:** Handles interactions with the SQLite database, including table creation and CRUD operations.

**main.py:** Provides the user interface through a menu-driven command-line system, linking user input to database and business logic.

# **Future Enhancements**

**Web Interface:** Add a web-based front end for easier accessibility and a modern user experience.

**User Accounts:** Implement multi-user functionality with authentication for staff and administrators.

**Reporting Tools:** Generate sales, inventory, and allergen reports to aid business analysis.

# **Contributing**

Contributions are welcome to enhance the system further. Follow these steps to contribute:

Fork this repository.

Create a new branch for your feature

Commit your changes 

Push to the branch

Open a pull request.

# **License**

This project is licensed under the MIT License. See the LICENSE file for details.
