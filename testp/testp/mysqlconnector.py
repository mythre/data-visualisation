import re
import mysql.connector


class MySQLConnector():

    def __init__(self):

        self.conn = mysql.connector.connect(host='swift.gai.net',
                                            user='teamhack1',
                                            passwd='T#am@001',
                                            db='ukllis',
                                            port=3306,
                                            autocommit=True)

        self.cursor = self.conn.cursor(dictionary=True, buffered=True)

    def __formatargs(self, query, arguments):
        """
        Format arguments
        """
        if isinstance(arguments, tuple):
            arguments = list(arguments)
        if isinstance(arguments, list):
            find_idx = 0
            end_idx = 0
            query = re.sub('\([ ]*%[ ]*s[ ]*\)', '(%s)', query)
            for i, value in enumerate(arguments):
                if isinstance(value, tuple) or isinstance(value, list):
                    len_ = len(value)
                    find_idx = query.index('(%s)', end_idx)
                    end_idx = find_idx + len("(%s)")
                    query = list(query)
                    query[find_idx:end_idx] = '(%s' + ', %s' * (len_ - 1) + ')'
                    query = ''.join(query)
                    arguments.remove(value)
                    for ele in value:
                        arguments.insert(i, ele)
                        i += 1
        else:
            pass
        return query, arguments

    def execute_query(self, query, arguments=None):
        """
        Execute the query
        """

        if arguments:
            query, arguments = self.__formatargs(query, arguments)

        print query, arguments

        self.cursor.execute(query, arguments)

        response = self.cursor.fetchall()

        if not response:
            return {}

        return response

    def get_user_config(self):

        query = "select * from internal_contactusmodel where id = %s"

        args = (57586,)

        print self.execute_query(query, args)


if __name__ == '__main__':
    MySQLConnector().get_user_config()
