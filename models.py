import secrets
from enum import Enum
import string
from pydantic import BaseModel, EmailStr
from datetime import datetime
import re

class CharacterOptions(Enum):
    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    ALPHANUMERIC = string.ascii_letters + string.digits
    MIXED = f'{string.ascii_letters + string.digits}{"$_@!^&%*)(-?"}'

class PasswordStrength(Enum):
    VERY_STRONG_LENGTH  = 16
    STRONG_LENGTH = 10

class PersonalInfo(BaseModel):
    name: str
    email: EmailStr
    profile_image: str
    account_creation: datetime = datetime.now()

class Notes(BaseModel):
    title: str
    category: str
    date_added: datetime = datetime.now()
    priority: str

class Accounts(BaseModel):
    name: str
    last_used: datetime = datetime.now()
    password: str
    category: str
    image: str
    password_quality: str


class Utilities:
    def upcase_option(character_option: str) -> str:
       ''' Make all characters uppercase to compare to Enum member name '''
       return character_option.upper()

    
    def detect_password_quality(password: str):
        ''' Evaluate the strength of a users account passwords '''
        very_strong = re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!#@$%^&*(_)+]).{16,48})', password)
        strong = re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!#@$%^&*(_)+]).{10,16})', password)
        weak = re.match('((\d*)([a-z]*)([A-Z]*)(![!#@$%^&*(_)+]).{8,10})', password)
        if len(password) >= PasswordStrength.VERY_STRONG_LENGTH.value and bool(very_strong) == True:
            print('very strong')
        elif len(password) < PasswordStrength.VERY_STRONG_LENGTH.value and bool(strong) == True:
            print('strong') 
        else:
            print('weak')



class PasswordGenerator:
    def __init__(self, length, characters):
        self.length = length
        self.characters = characters

    def generate_password(self) -> str:
        ''' 
             Iterate over the Enum, if the member name is the same as the value passed into 
             the constructor for the character property, get that enum members value and pass
             the sequence to secrets.choice(). Using the length property to give the desired
             number of random characters to be returned. 
        '''
        character_result = Utilities.upcase_option(self.characters)
        for character in (CharacterOptions):
            if character.name == character_result:
                return ''.join(secrets.choice(character.value) for _ in range(self.length))



            
