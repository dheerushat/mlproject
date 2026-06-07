from setuptools import find_packages,setup
from typing import List

def get_requirement(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirement = []

    with open(file_path) as file_obj:
        requirement= file_obj.readlines()
        requirement=[req.replace('\n', "")for req in requirement]

    return requirement


setup(
    name="django-redis-cache",
    version="3.0.0",
    author = "dheerusha",
    author_email = "dheerushat@gmail.com",
    package = find_packages(),
    install_requires = get_requirement('requirement.txt')       
)