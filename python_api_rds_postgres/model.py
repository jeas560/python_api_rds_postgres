from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dotenv_values("../.env.development")
Base = declarative_base()

url_object = URL.create(
    "postgresql+psycopg2",
    username=config["POSTGRES_USER"],
    password=config["POSTGRES_PASSWORD"],
    host=config["POSTGRES_HOST"],
    port=config["POSTGRES_PORT"],
    database=config["POSTGRES_DB"],
)


class Coins(Base):
    __tablename__ = "Coins"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    symbol = Column(String)
    date_added = Column(DateTime)
    last_updated = Column(DateTime)
    price = Column(Float)
    volume_24h = Column(Integer)

    def start():
        engine = create_engine(url_object)
        Session = sessionmaker(bind=engine)
        session = Session()
        Base.metadata.create_all(engine)
        print("\nTable created on database")
        return session, engine
