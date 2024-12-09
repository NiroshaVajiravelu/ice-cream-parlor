import sqlite3
from typing import List, Optional
from models import Flavor, Ingredient, Allergen

class IceCreamDatabase:
    def __init__(self, db_name='ice_cream_parlor.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        # Create Flavors Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS flavors (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                description TEXT,
                is_seasonal BOOLEAN,
                price REAL
            )
        ''')

        # Create Ingredients Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ingredients (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                quantity INTEGER,
                unit TEXT
            )
        ''')

        # Create Allergens Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS allergens (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE
            )
        ''')

        self.conn.commit()

    def add_flavor(self, flavor: Flavor) -> int:
        try:
            self.cursor.execute('''
                INSERT INTO flavors (name, description, is_seasonal, price)
                VALUES (?, ?, ?, ?)
            ''', (flavor.name, flavor.description, flavor.is_seasonal, flavor.price))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Flavor {flavor.name} already exists.")
            return None

    def get_flavors(self, is_seasonal: Optional[bool] = None) -> List[Flavor]:
        query = 'SELECT * FROM flavors'
        params = []
        
        if is_seasonal is not None:
            query += ' WHERE is_seasonal = ?'
            params.append(is_seasonal)
        
        self.cursor.execute(query, params)
        flavors = []
        for row in self.cursor.fetchall():
            flavor = Flavor(
                id=row[0],
                name=row[1],
                description=row[2],
                is_seasonal=bool(row[3]),
                price=row[4]
            )
            flavors.append(flavor)
        return flavors

    def add_ingredient(self, ingredient: Ingredient) -> int:
        try:
            self.cursor.execute('''
                INSERT INTO ingredients (name, quantity, unit)
                VALUES (?, ?, ?)
            ''', (ingredient.name, ingredient.quantity, ingredient.unit))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Ingredient {ingredient.name} already exists.")
            return None

    def add_allergen(self, allergen: Allergen) -> int:
        try:
            self.cursor.execute('''
                INSERT OR IGNORE INTO allergens (name)
                VALUES (?)
            ''', (allergen.name,))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Allergen {allergen.name} already exists.")
            return None

    def search_flavors(self, keyword: str) -> List[Flavor]:
        self.cursor.execute('''
            SELECT * FROM flavors 
            WHERE name LIKE ? OR description LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))
        
        flavors = []
        for row in self.cursor.fetchall():
            flavor = Flavor(
                id=row[0],
                name=row[1],
                description=row[2],
                is_seasonal=bool(row[3]),
                price=row[4]
            )
            flavors.append(flavor)
        return flavors

    def close(self):
        self.conn.close()