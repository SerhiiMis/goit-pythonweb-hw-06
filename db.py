from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://postgres:567234@localhost:5432/postgres"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
