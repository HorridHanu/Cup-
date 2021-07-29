import string
import random
from itertools import product

print('[+]')

def generate_wordlist_from_profile(profile):
    CONFIG = {}

    chars = CONFIG["global"]["chars"]
    years = CONFIG["global"]["years"]
    numfrom = CONFIG["global"]["numfrom"]
    numto = CONFIG["global"]["numto"]




    profile["spechars"] = []

    if profile["spechars1"] == "y":
        for spec1 in chars:
            profile["spechars"].append(spec1)
            for spec2 in chars:
                profile["spechars"].append(spec1 + spec2)
                for spec3 in chars:
                    profile["spechars"].append(spec1 + spec2 + spec3)

    print("\r\n[+] Now making a dictionary...")

   # Now me must do some string modifications...

    # Birthdays first

    birthdate_yy = profile["birthdate"][-2:]
    birthdate_yyy = profile["birthdate"][-3:]
    birthdate_yyyy = profile["birthdate"][-4:]
    birthdate_xd = profile["birthdate"][1:2]
    birthdate_xm = profile["birthdate"][3:4]
    birthdate_dd = profile["birthdate"][:2]
    birthdate_mm = profile["birthdate"][2:4]

    wifeb_yy = profile["wifeb"][-2:]
    wifeb_yyy = profile["wifeb"][-3:]
    wifeb_yyyy = profile["wifeb"][-4:]
    wifeb_xd = profile["wifeb"][1:2]
    wifeb_xm = profile["wifeb"][3:4]
    wifeb_dd = profile["wifeb"][:2]
    wifeb_mm = profile["wifeb"][2:4]

    kidb_yy = profile["kidb"][-2:]
    kidb_yyy = profile["kidb"][-3:]
    kidb_yyyy = profile["kidb"][-4:]
    kidb_xd = profile["kidb"][1:2]
    kidb_xm = profile["kidb"][3:4]
    kidb_dd = profile["kidb"][:2]
    kidb_mm = profile["kidb"][2:4]



    # Convert first letters to uppercase...

    nameup = profile["name"].title()
    surnameup = profile["surname"].title()
    nickup = profile["nick"].title()
    wifeup = profile["wife"].title()
    wifenup = profile["wifen"].title()
    kidup = profile["kid"].title()
    kidnup = profile["kidn"].title()
    petup = profile["pet"].title()
    companyup = profile["company"].title()

    wordsup = []
    wordsup = list(map(str.title, profile["words"]))

    word = profile["words"] + wordsup


    # reverse a name

    rev_name = profile["name"][::-1]
    rev_nameup = nameup[::-1]
    rev_nick = profile["nick"][::-1]
    rev_nickup = nickup[::-1]
    rev_wife = profile["wife"][::-1]
    rev_wifeup = wifeup[::-1]
    rev_kid = profile["kid"][::-1]
    rev_kidup = kidup[::-1]

    reverse = [
        rev_name,
        rev_nameup,
        rev_nick,
        rev_nickup,
        rev_wife,
        rev_wifeup,
        rev_kid,
        rev_kidup,
    ]
    rev_n = [rev_name, rev_nameup, rev_nick, rev_nickup]
    rev_w = [rev_wife, rev_wifeup]
    rev_k = [rev_kid, rev_kidup]
    # Let's do some serious work! This will be a mess of code, but... who cares? :)

    # Birthdays combinations

    bds = [
        birthdate_yy,
        birthdate_yyy,
        birthdate_yyyy,
        birthdate_xd,
        birthdate_xm,
        birthdate_dd,
        birthdate_mm,
    ]






























































# Name = str(input('Enter The Name: '))
# Nickname = str(input('Enter The Nickname: '))
# DateOfBirth = input('Enter The Date Of Birth: ')
#
# PartnerName = str(input('\nEnter Partner Name: '))
# PartnerNickName = str(input('\nEnter Partner NickName: '))
# PartnerDateOfBirth = str(input('\nEnter Partner Date Of Birth: '))
#
#
# Password = []
# Password.extend(list(Name))
# Password.extend(list(Nickname))
# Password.extend(list(DateOfBirth))
#
# Password.extend(list(PartnerName))
# Password.extend(list(PartnerNickName))
# Password.extend(list(PartnerDateOfBirth))
#
# random.shuffle(Password)
# print(Password)
#
# PPassword = Name+DateOfBirth
#
#
# min_lenght = 4
# max_lenght = int(input('Enter The Maximum Length: '))
#
# Filename = input('Enter the file name: ')
# print("Please Wait While Tool is creating Password List .")
# # print(file)
# counter = 0
# file_open = open(Filename, 'w')
# for i in range(min_lenght, max_lenght):
#     for j in product(Password, repeat=i):
#         word = "".join(j)
#         file_open.write(word)
#         file_open.write('\n')
#
#         counter += 1
# file_open.write(PPassword)
# print("Password list is created".format(counter))

