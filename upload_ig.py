from instabot import Bot 
from utils import *
username = 'fernandochen5566'
passw = 'chiou5917'
img_path = './img/uq_river_picasso_5.jpg'
caption = 'test post #artinbrissie'
logo_path = './logo/mm_logo_160x160.png'

# add logo
imge_logo_path = embedlogo(img_path, logo_path)

bot = Bot() 
bot.login(username = username, password = passw) 
bot.upload_photo(imge_logo_path, caption = caption) 

