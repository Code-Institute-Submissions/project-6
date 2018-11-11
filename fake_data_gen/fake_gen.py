import os, random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aph.settings")

import django

django.setup()

from accounts.models import UserProfile
from listings.models import Listing
from django.contrib.auth.models import User

fake = Faker()


def gen_user_and_profile():
    """ 
	Generate random user base on the schema and add the user to db
	"""
    
    user_name = fake.first_name()
    first_name = user_name
    last_name = fake.last_name()
    email = fake.email()
    phone = fake.msisdn()
    
    is_seller = True
    joined = fake.past_date(start_date="-4y", tzinfo=None)
    user = User.objects.get_or_create(email=email, username=user_name, 
			first_name=first_name, last_name=last_name)
    user = User.objects.get(email=email)
	
    

    new_profile = UserProfile(
        user=user,  phone=int(phone), is_seller=is_seller, joined=joined
    )
    
    
    new_profile.save()
    return user


def gen_listing(how_many):
    """ 
	Generate random listing base on the schema and add the user to listing
	"""
    listings = 0
    while listings < how_many:
        title = fake.street_name()
        city = fake.city()
        state = fake.state()
        zipcode = fake.postalcode()

        description = ""
        price = random.randint(100000, 500000)

        bedrooms = random.randint(1, 4)
        bathrooms = random.randint(1, 2)
        garage = random.randint(0, 1)
        square_feet = random.randint(500, 1000)
        main_img = f"fake_data/main/1 ({listings + 1}).jpeg"
        img_1 = f"fake_data/others/1 ({listings + 1}).jpeg"
        img_2 = f"fake_data/others/1 ({listings + 1}).jpeg"
        img_3 = f"fake_data/others/1 ({listings + 1}).jpeg"
        img_4 = f"fake_data/others/1 ({listings + 1}).jpeg"
        img_5 = f"fake_data/others/1 ({listings + 1}).jpeg"
		
        is_published = bool(random.getrandbits(1))
        paid_fee = True
        list_date = fake.past_date(start_date="-2y", tzinfo=None)
        seller = gen_user_and_profile()

        listing = Listing(
            title=title,
            address=title,
            city=city,
            state=state,
            zipcode=zipcode,
            description=description,
            price=price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            garage=garage,
            square_feet=square_feet,
            main_img=main_img,
            img_1=img_1,
            img_2=img_2,
            img_3=img_3,
            img_4=img_4,
            img_5=img_5,
            is_published=is_published,
            paid_fee=paid_fee,
            list_date=list_date,
            seller=seller,
        )
        listing.save()
        print(title)
        listings += 1


def fake_data():

    gen_listing(int(input("How many ?")))


def main():
    fake_data()


if __name__ == "__main__":
    main()

