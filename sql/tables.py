from sqlalchemy import create_engine, Integer, String, \
    Column, ForeignKey, Float, Boolean, ARRAY, Text

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts")

Base = declarative_base()


class Ingredients(Base):
    __tablename__ = "ingredient"
    id = Column(Integer(), primary_key=True)
    en_name = Column(String(200), nullable=False)
    ru_name = Column(String(200), nullable=False)
    kcal = Column(Float(), nullable=False),
    protein = Column(Float(), nullable=False),
    carbohydrate = Column(Float(), nullable=False)
    fat = Column(Float(), nullable=False)
    tablespoon = Column(Integer(), nullable=False)
    cup = Column(Integer(), nullable=False)
    vegetarian = Column(Boolean(), nullable=False)
    recipe = relationship("IngredientsInRecipe", backref='ingredient')


class Recipes(Base):
    __tablename__ = "recipe"
    id = Column(Integer(), primary_key=True)
    ru_name = Column(String(200), nullable=False)
    en_name = Column(String(200), nullable=False)
    kcal = Column(Float(), nullable=False),
    protein = Column(Float(), nullable=False),
    carbohydrate = Column(Float(), nullable=False)
    fat = Column(Float(), nullable=False)
    ingredients_ru = Column(ARRAY(String))
    ingredients_en = Column(ARRAY(String))
    description = Column(Text(), nullable=False)
    vegetarian = Column(Boolean(), nullable=False)
    ingredient = relationship("IngredientsInRecipe", backref='recipe')


class IngredientsInRecipe(Base):
    __tablename__ = "ingredients_in_recipe"
    id = Column(Integer, primary_key=True)
    recipe = Column(Integer(), ForeignKey("recipe.id"))
    ingredient = Column(Integer(), ForeignKey("ingredient.id"))
    extra_data = Column(String(100))


Base.metadata.create_all(engine)
