import pymysql

class AuthModel:
    def create(self, connection, data):
        query = """
            INSERT INTO users(
                email,
                nickname,
                password,
                created_at,
                is_deleted
            )
            VALUES(
                %(email)s,
                %(nickname)s,
                %(password)s,
                NOW(),
                False
                )
            """

        with connection.cursor() as cursor:
            cursor.execute(query, data)

            return cursor.lastrowid

    def get_user_info(self, connection, data):
        query = """
            SELECT 
                id, email, nickname, created_at, is_deleted
            FROM 
                users
            WHERE
                id = %s
            """
        
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query, data)

            return cursor.fetchone()