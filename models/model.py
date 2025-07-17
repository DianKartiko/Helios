import os
from dotenv import load_dotenv

load_dotenv()

"""Link Sosial Media"""
social_media = [
        {
            'name' : 'X',
            'url' : os.getenv('URL_X'),
            'icon' : "fa-x-twitter"
        },
        {
            'name' : 'Instagram',
            'url' : os.getenv('URL_INSTAGRAM'),
            'icon' : "fa-instagram"
        },
        {
            'name' : 'Github',
            'url' : os.getenv('URL_GITHUB'),
            'icon' : "fa-github"
        },
        {
            'name' : 'LinkedIn',
            'url' : os.getenv('URL_LINKEDIN'),
            'icon' : "fa-linkedin"
        }
    ]