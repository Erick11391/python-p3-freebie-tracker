#!/usr/bin/env python3

 
# seed.py
from models import Company, Dev, Freebie, company_dev, session


session.query(Company).delete()
session.query(Dev).delete()
session.query(Freebie).delete()
session.query(company_dev).delete()
session.commit()


session.query(Company).delete()
session.query(Dev).delete()
session.query(Freebie).delete()
session.query(company_dev).delete()
session.commit()

   #  companies 
companies_info = [
    {"name": "Safaricom", "founding_year": 1993},
    {"name": "M-pesa", "founding_year": 2010},
    {"name": "Kengen", "founding_year": 2008},
    {"name": "Telcom", "founding_year": 1984},
    {"name": "Royal Media", "founding_year": 1992},
    {"name": "KCB Group", "founding_year": 1998},
    {"name": "Agile", "founding_year": 2005},
    {"name": "Moringa", "founding_year": 1987},
    {"name": "E-Citizen", "founding_year": 2011},
    {"name": "H-Tech", "founding_year": 2004},
]

companies = [Company(**company) for company in companies_info]
session.add_all(companies)
session.commit()

# Seed devs
devs_info = [
    {"name": "Mary Karimi"},
    {"name": "William Ruto"},
    {"name": "ELLy Maina"},
    {"name": "Rose Ngara"},
    {"name": "Erick Mutai"},
    {"name": "Sam TOmashi"},
    {"name": "Dan Kirwa"},
    {"name": "Sasha Jeruto"},
    {"name": "Muhamed Zuma"},
    {"name": "Ellias Ngaara"},
]

devs = [Dev(**dev) for dev in devs_info]
session.add_all(devs)
session.commit()

# Seed freebies
freebie_info = [
    {"item_name": "Laptop", "value": 1500, "company_id": 3, "dev_id": 8},
    {"item_name": "Mouse", "value": 20, "company_id": 5, "dev_id": 2},
    {"item_name": "Keyboard", "value": 50, "company_id": 7, "dev_id": 6},
    {"item_name": "USB Drive", "value": 10, "company_id": 1, "dev_id": 9},
    {"item_name": "Headphones", "value": 30, "company_id": 9, "dev_id": 4},
    {"item_name": "Webcam", "value": 40, "company_id": 2, "dev_id": 7},
    {"item_name": "External Hard Drive", "value": 80, "company_id": 8, "dev_id": 1},
    {"item_name": "Monitor", "value": 200, "company_id": 4, "dev_id": 10},
    {"item_name": "Wireless Mouse", "value": 25, "company_id": 6, "dev_id": 5},
    {"item_name": "Graphics Card", "value": 300, "company_id": 10, "dev_id": 3},
]

freebies = [Freebie(**freebie) for freebie in freebie_info]
session.add_all(freebies)
session.commit()

      # Seed relationships (companies_devs)
relationships = [
    {"company_id": 3, "dev_id": 8},
    {"company_id": 7, "dev_id": 5},
    {"company_id": 2, "dev_id": 7},
    {"company_id": 6, "dev_id": 1},
    {"company_id": 9, "dev_id": 4},
    {"company_id": 1, "dev_id": 10},
    {"company_id": 4, "dev_id": 2},
    {"company_id": 8, "dev_id": 9},
    {"company_id": 5, "dev_id": 3},
    {"company_id": 10, "dev_id": 6},
]

            # Add relationships 
for rel in relationships:
    company = session.query(Company).filter_by(id=rel["company_id"]).first()
    dev = session.query(Dev).filter_by(id=rel["dev_id"]).first()
    if company and dev:
        company.devs.append(dev)

session.commit()

print("Database seeded successfully!")