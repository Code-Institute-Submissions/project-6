import os
import random
from faker import Faker
from django.contrib.auth.models import User
from listings.models import Listing
from accounts.models import UserProfile



""" 
If DEBUG
	visit host/fake-data
"""

class FakeData:

    """
    Fake the data for local testing
    """

    def __init__(self):
        self.fake = Faker()
        self.fake_data()

    def gen_user_and_profile(self):
        """
        Generate random user base on the schema and add the user to db
        """

        user_name = self.fake.first_name()
		# Check if user name already exist as must be unique
        while True:            
            try:
                User.objects.get(username=user_name)
                user_name = self.fake.first_name()
            except User.DoesNotExist:
                break

        first_name = user_name
        last_name = self.fake.last_name()
        email = self.fake.email()
        phone = self.fake.msisdn()

        terms = True
        joined = self.fake.past_date(start_date="-4y", tzinfo=None)

        self.user = User.objects.get_or_create(
            email=email,
            username=user_name,
            first_name=first_name,
            last_name=last_name
        )

        user = User.objects.get(email=email)

        new_profile = UserProfile(user=user,  phone=phone, terms=terms, joined=joined)

        new_profile.save()
        return user

    def gen_secondary_imgs(self):
        """ 
        Randomize secondary images
        """
        self.imgs = [0]
        img = 0

        while len(self.imgs) is not 6:
            while img in self.imgs:
                img = random.randint(1, 28)
            self.imgs.append(img)
        del(self.imgs[0])
        return self.imgs

    def fake_data(self):
        """
        Generate User / Profile and listing depends on user 

        Generate random listing base on the schema and add the user to listing

        """

        listings = 1
        how_many = int(input("How many ?"))
        while listings < how_many:
            title = self.fake.street_name()
            city = self.fake.city()
            state = self.fake.state()
            zipcode = self.fake.postalcode()

            # description = self.fake.text(max_nb_chars=200, ext_word_list=None)
            description = ""
            price = random.randint(100000, 500000)

            bedrooms = random.randint(1, 4)
            bathrooms = random.randint(1, 2)
            garage = random.randint(0, 1)
            square_feet = random.randint(500, 1000)
            imgs = self.gen_secondary_imgs()
            main_img = f"fake_data/main/1 ({listings}).jpeg"
            img_1 = f"fake_data/others/1 ({imgs[0]}).jpeg"
            img_2 = f"fake_data/others/1 ({imgs[1]}).jpeg"
            img_3 = f"fake_data/others/1 ({imgs[2]}).jpeg"
            img_4 = f"fake_data/others/1 ({imgs[3]}).jpeg"
            img_5 = f"fake_data/others/1 ({imgs[4]}).jpeg"

            is_published = bool(random.getrandbits(1))
            paid_fee = True
            list_date = self.fake.past_date(start_date="-2y", tzinfo=None)
            seller = self.gen_user_and_profile()

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
            listings += 1
