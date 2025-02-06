from faker import Faker
from random import randint, choice
from app import app,db,Service_Provider,Service,User

# Initialize the Faker instance
fake = Faker("en_IN")  # Generate Indian context data

# Generate and insert fake data
with app.app_context():
    service_provider : Service_Provider = Service_Provider.query.all()
    services : Service = Service.query.all()
    fake = Faker()
    for _ in range(10):
        full_name = fake.name()
        name_list = full_name.split()
        if len(name_list) == 1:
            email = f"{full_name}@gmail.com".lower()
        else:
            first_name , last_name = full_name.split()
            email = f"{first_name}{last_name}@gmail.com".lower()
        user = User(
            fullname = full_name,
            email = email,
            password = "C*@6muWs",
            role = "customer",
            service_type = "None",
            location = "None",
            hourly_rate = 1,
            certifications = "None",
            certification_path =  "None",
            experience = "None",
            id_proof_path = "None",
            qualification_path = "None"    
        )
        db.session.add(user)
        db.session.commit()
    print("added the user")
        
        
#  Run the script to add fake data 