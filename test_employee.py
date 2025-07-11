import pymysql
import unittest

class TestFindHigherEmployee(unittest.TestCase):
    def setUp(self):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Shi.010828',
            'database': 'cccc',
            'port': 3306
        }
        self.conn = pymysql.connect(**self.db_config)
        self.cursor = self.conn.cursor()
        self.create_table()
        self.insert_data()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                id INT PRIMARY KEY,
                name VARCHAR(50),
                salary INT,
                manager_id INT
            )
        """)
        self.conn.commit()

    def insert_data(self):
        self.cursor.execute("TRUNCATE TABLE employee")
        self.cursor.executemany("""
            INSERT INTO employee (id, name, salary, manager_id) VALUES (%s, %s, %s, %s)
        """, [
            (1, 'Joe', 70000, 3),
            (2, 'Henry', 80000, 4),
            (3, 'Sam', 60000, None),
            (4, 'Max111333', 90000, None)
        ])
        self.conn.commit()

    def test_find_higher_employee(self):
        with self.conn.cursor() as cursor:
            query = """
                SELECT a.name FROM employee a JOIN employee b
                ON a.manager_id = b.id 
                WHERE a.salary > b.salary    
            """
            cursor.execute(query)
            results = cursor.fetchall()
            expected_results = (('Joe',),)
            self.assertEqual(results, expected_results)

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
