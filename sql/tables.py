from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, Float

metadata = MetaData()

ingredients = Table("ingredients", metadata,
                    Column('id', Integer, primary_key=True),
                    Column('en_name', String(200), nullable=False),
                    Column('ru_name', String(200), nullable=False),
                    Column('kcal', Float, nullable=False),
                    Column('protein', Float, nullable=False),
                    Column('carbohydrate', Float, nullable=False),
                    Column('fat', Float, nullable=False)
                    )
