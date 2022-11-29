import secrets
from enum import Enum
import string

class CharacterOptions(Enum):
    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    ALPHANUMERIC = string.ascii_letters + string.digits
    MIXED = f'{string.ascii_letters + string.digits}{"$_@!^&%*)(-?"}'

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
        character_result = self.upcase_option(self.characters)
        for character in (CharacterOptions):
            if character.name == character_result:
                return ''.join(secrets.choice(character.value) for _ in range(self.length))

    def upcase_option(self, character_option: str) -> str:
        ''' Make all characters uppercase to compare to Enum member name '''
        return character_option.upper()


            
