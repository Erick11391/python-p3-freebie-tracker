# models.py
from sqlalchemy import Table, ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

      # base class for declarative models
Base = declarative_base(metadata=metadata)


company_dev = Table(
    'companies_devs',
    Base.metadata,
    Column('company_id', ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', ForeignKey('devs.id'), primary_key=True),
    extend_existing=True,
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    # Relationships
    freebies = relationship('Freebie', backref='company')
    devs = relationship('Dev', secondary=company_dev, back_populates='companies')

    def __repr__(self):
        return f'<Company {self.name}>'

       # Class method for oldest company
    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()

    # Method to give a freebie to a dev
    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(freebie)
        session.commit()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

         # Relationships
    freebies = relationship('Freebie', backref='dev')
    companies = relationship('Company', secondary=company_dev, back_populates='devs')

    def __repr__(self):
        return f'<Dev {self.name}>'

    
    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)


    def give_away(self, other_dev, freebie):
        if freebie.dev == self:
            freebie.dev = other_dev
            session.commit()

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    company_id = Column(Integer(), ForeignKey('companies.id'))
    dev_id = Column(Integer(), ForeignKey('devs.id'))

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

# Database setup
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)



   #session
Session = sessionmaker(bind=engine)
session = Session()