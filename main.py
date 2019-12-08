import shelve
from faker import Faker
from faker.providers import BaseProvider
from collections import OrderedDict


class Provider(BaseProvider):
    def medical_provider(self, full=False):

        titles = \
        {"AuD" :"Doctor of Audiology",
        "DC" :"Doctor of Chiropractic",
        "DDS" :"Doctor of Dental Surgery",
        "DMD" :"Doctor of Dental Medicine",
        "DO" :"Doctor of Osteopathic Medicine",
        "DPM" :"Doctor of Podiatric Medicine",
        "DPT" :"Doctor of Physical Therapy",
        "DScPT" :"Doctor of Science in Physical Therapy",
        "DSN" :"Doctor of Science in Nursing",
        "DVM" :"Doctor of Veterinary Medicine",
        "ENT" :"Earnose and throat specialist",
        "GP" :"General Practitioner",
        "GYN" :"Gynecologist",
        "MD" :"Doctor of Medicine",
        "MS" :"Master of Surgery",
        "OB/GYN" :"Obstetrician and Gynecologist",
        "PharmD" :"Doctor of Pharmacy"}

        if full:
            return self.random_element(titles.values())
        else:
            return self.random_element(titles.keys())


# with shelve.open('providers') as d:

#     fake = Faker()
#     fake.add_provider(d['medical'])
#     print(fake.medical_provider())
