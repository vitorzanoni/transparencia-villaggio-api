import psycopg
from psycopg.rows import dict_row


class BoletoRepository(object):

    def __int__(self):
        self.conn = psycopg.connect(host=None, database=None, user=None, password=None, row_factory=dict_row,
                                    autocommit=True)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def get_boleto(self, id_boleto: int = None) -> dict:
        return self.cursor.execute(None, id_boleto).fetchall()
