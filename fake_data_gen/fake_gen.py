import os, random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aph.settings")

import django

django.setup()

from accounts.models import User
from listings.models import Listing
from django.shortcuts import get_object_or_404

fake = Faker()



		
def gen_user():
	""" 
	Generate random user base on the shema and add the user to db
	"""
	name = fake.name()
	email = fake.email()
	phone = fake.msisdn()
	is_seller = bool(random.getrandbits(1))
	joined = fake.date()

	user = User(
		name=name, email=email, phone=int(phone), is_seller=is_seller, joined=joined
	)
	user.save()
	print(name)
	return user

def gen_listing(how_many):
    """ 
	Generate random listing base on the shema and add the user to listing
	"""
    listings = 0
    while listings < how_many:
        title = fake.street_name()
        address = title
        city = fake.city()
        state = fake.state()
        zipcode = fake.postalcode()

        description = ""
        price = random.randint(50000,10000000)

        bedrooms = random.randint(1,10)
        bathrooms = random.randint(1,5)
        garage = random.randint(1,3)
        square_feet = random.randint(500,1000)
        main_img = fake.file_path(depth=1, category=None, extension=None)
        """ 
		img_1 = models.ImageField(upload_to='media/imgs/', blank=True)
		img_2 = models.ImageField(upload_to='media/imgs/', blank=True)
		img_3 = models.ImageField(upload_to='media/imgs/', blank=True)
		img_4 = models.ImageField(upload_to='media/imgs/', blank=True)
		img_5 = models.ImageField(upload_to='media/imgs/', blank=True) 
		"""
        is_published = bool(random.getrandbits(1))
        paid_fee = True
        list_date = fake.past_date(start_date="-10y")
        seller = gen_user()

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
			is_published=is_published,
			paid_fee=paid_fee,
			list_date=list_date,
			seller=seller
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

