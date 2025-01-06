from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    def save(self, session):
        session.add(self)
        session.commit()
