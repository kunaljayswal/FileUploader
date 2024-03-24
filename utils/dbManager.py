from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from app.models.fileDbModel import Base
import config

# Define a class responsible for managing database setup
class DatabaseManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = None
        self.connection = None
        self.connect()

    def connect(self):
        try:
            # Create the engine
            self.engine = create_engine(self.connection_string, echo=True)
            self.create_tables()
            print("Connected to the database successfully!")
        except OperationalError as e:
            print(f"Failed to connect to the database: {e}")

    def create_tables(self):
        # Create the tables in the database (if they don't exist already)
        Base.metadata.create_all(self.engine, checkfirst=True)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to the database closed.")

# Define the connection string for your PostgreSQL database
connection_string: str = config.connection_string

# Create a DatabaseManager instance
db_manager = DatabaseManager(connection_string)