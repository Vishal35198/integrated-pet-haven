from faker import Faker
from app import db,app
from app import Pet

fake = Faker()

unique_breeds = ['Labrador', 'Poodle', 'Bulldog', 'Beagle', 'German Shepherd', 'Golden Retriever', 'Dachshund', 'Shih Tzu', 'Boxer', 'Chihuahua']

def create_fake_pets(num_pets):
    with app.app_context():
        for i in range(num_pets):
            pet = Pet(
                breed=unique_breeds[i % len(unique_breeds)],
                age_months=fake.random_int(min=1, max=120),
                health_records=fake.text(max_nb_chars=200),
                price=fake.random_number(digits=5, fix_len=True),
                availability_status=fake.random_element(elements=('Available', 'Adopted', 'Pending')),
                achivement=fake.sentence(nb_words=6),
                image=fake.image_url(),
                description=fake.text(max_nb_chars=200)
            )
            db.session.add(pet)
        db.session.commit()

# Create 10 fake pets
create_fake_pets(10)
