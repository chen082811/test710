"""
找出比经历收入高的员工：
示例 1:
输入:
Employee 表:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
输出:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
解释: Joe 是唯一挣得比经理多的雇员。
"""



DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Shi.010828',
    'database': 'cccc',
    'port': 3306
}
def find_higher_employee():

    try:
        with pymysql.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                    query = """
                    select a.name from cccc.employee a join cccc.employee b
                    on a.manager_id = b.id 
                    where a.salary > b.salary    
                    """
                    cursor.execute(query)
                    results =  cursor.fetchall()

                    for row in results:
                        print(row[0])

    except pymysql.MySQLError as e:
        print(f"数据库错误: {e}")
        return None


if __name__ == '__main__':
    find_higher_employee()



