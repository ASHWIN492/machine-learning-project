from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_reqirements(file_path:str)->List[str]:
    '''this function will written list of requirmnts
    '''
    reqirements = []
    with open(file_path) as file_obj:
        reqirements=file_obj.readlines()
        reqirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in reqirements:
            reqirements.remove(HYPEN_E_DOT)
            
    return reqirements        

setup(
    name = 'machine learning project',
    version = '0.0.1',
    author='ashwin',
    author_email='ashwinkumar0528@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)