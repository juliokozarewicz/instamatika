# imports
# ----------------------------------------------------------------------------
from instagram_controller import Instagram_controller
import json
from datetime import datetime
from random import randint
# ----------------------------------------------------------------------------

with open("dados_usuarios.json", encoding='utf-8') as dados_usuarios:
    dados_usuarios = json.load(dados_usuarios)

# main script
# ----------------------------------------------------------------------------
for usuario in dados_usuarios.keys():

    data_atual = datetime.now()

    instamatik = Instagram_controller(

        dados_usuarios[usuario]['id_usuario'],
        usuario,
        dados_usuarios[usuario]['insta_email'],
        dados_usuarios[usuario]['insta_senha'],
        dados_usuarios[usuario]['insta_target']

        )

    if data_atual.isoweekday() == 1:

        instamatik.timeline_user()
        instamatik.seguir_95_user(randint(70, 80))
        instamatik.deixar_de_seguir(randint(5, 10))
        instamatik.curtir_posts()
        instamatik.close_webdriver()

    if data_atual.isoweekday() == 2:

        instamatik.timeline_user()
        instamatik.seguir_95_user(randint(5, 10))
        instamatik.deixar_de_seguir(randint(70, 80))
        instamatik.curtir_posts()
        instamatik.close_webdriver()

    if data_atual.isoweekday() == 3:

        instamatik.timeline_user()
        instamatik.seguir_95_user(randint(70, 80))
        instamatik.deixar_de_seguir(randint(5, 10))
        instamatik.curtir_posts()
        instamatik.close_webdriver()

    if data_atual.isoweekday() == 4:

        instamatik.timeline_user()
        instamatik.seguir_95_user(randint(5, 10))
        instamatik.deixar_de_seguir(randint(70, 80))
        instamatik.curtir_posts()
        instamatik.close_webdriver()

    if data_atual.isoweekday() == 5:

        instamatik.timeline_user()
        instamatik.seguir_95_user(randint(70, 80))
        instamatik.deixar_de_seguir(randint(5, 10))
        instamatik.curtir_posts()
        instamatik.close_webdriver()

    if data_atual.isoweekday() == 6:

        instamatik.timeline_user()
        instamatik.seguir_95_user(randint(70, 80))
        instamatik.deixar_de_seguir(randint(5, 10))
        instamatik.curtir_posts()
        instamatik.close_webdriver()

    if data_atual.isoweekday() == 7:

        instamatik.timeline_user()
        instamatik.seguir_95_user(randint(5, 10))
        instamatik.deixar_de_seguir(randint(70, 80))
        instamatik.curtir_posts()
        instamatik.close_webdriver()

# ----------------------------------------------------------------------------
