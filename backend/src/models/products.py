class Product:
    def __init__(self, name=None, description=None, price=None):
        self.name = name
        self.description = description
        self.price = price

    def update_sql_fields(self):
        sql = ""
        if self.price is not None:
            sql = sql + " price=" + self.price + ","
        if self.name is not None:
            sql = sql + " name='" + self.name + "',"
        if self.description is not None:
            sql = sql + " description='" + self.description + "'"
        return sql.rstrip(",")
