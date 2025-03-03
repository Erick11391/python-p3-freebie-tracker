# debug.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base, session

# Test companies
print("Companies:")
companies = session.query(Company).all()
for company in companies:
    print(f"{company.name} (Founded: {company.founding_year})")




    # Test devs
print("\nDevs:")
devs = session.query(Dev).all()
for dev in devs:
    print(dev.name)

    

   # Test freebies
print("\nFreebies:")
freebies = session.query(Freebie).all()
for freebie in freebies:
    print(f"{freebie.item_name} (Value: {freebie.value}) - Owned by {freebie.dev.name} from {freebie.company.name}")

# Test relationships
print("\nTesting Relationships:")
company = session.query(Company).filter_by(name="Devcast").first()
if company:
    print(f"Devs associated with {company.name}:")
    for dev in company.devs:
        print(dev.name)

dev = session.query(Dev).filter_by(name="Bobette Beaufoy").first()
if dev:
    print(f"\nFreebies collected by {dev.name}:")
    for freebie in dev.freebies:
        print(freebie.item_name)

# Test methods
print("\nTesting Methods:")
freebie = session.query(Freebie).first()
if freebie:
    print(f"Freebie details: {freebie.print_details()}")

oldest_company = Company.oldest_company()
if oldest_company:
    print(f"Oldest company: {oldest_company.name}")

dev = session.query(Dev).filter_by(name="Elijah Shiel").first()
if dev:
    print(f"Has Elijah received a Mouse? {dev.received_one('Mouse')}")