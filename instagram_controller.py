from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from random import randint, sample
from os.path import basename
from con_db import Database_connect
from config import db_conect


class Instagram_controller:
    """
    Class responsible for automating navigation through Instagram.
    """

    def __init__(

            self,
            id_usuario,
            usuario,
            insta_email,
            insta_senha,
            insta_target

            ):

        self.db_database = db_conect['db_database']

        self.id_usuario = id_usuario

        self.usuario = usuario

        self.insta_email = insta_email

        self.insta_senha = insta_senha

        self.insta_target = insta_target

        self.db_query = Database_connect()

        options = Options()

        # options.add_argument('--headless')

        self.navegador = webdriver.Firefox(

            options=options

        )

        try:

            self.navegador.get(

                f'https://www.instagram.com/'
                f'accounts/login/?next=%2F{self.insta_target}'
                f'%2F&source=desktop_nav'

            )

            sleep(randint(7, 9))

            input_email = self.navegador.find_element(

                By.XPATH,
                '//*[@id="loginForm"]/div/div[1]/div/label/input'

            )

            input_email.send_keys(str(self.insta_email))

            input_senha = self.navegador.find_element(

                By.XPATH,
                '//*[@id="loginForm"]/div/div[2]/div/label/input'

            )

            input_senha.send_keys(str(self.insta_senha))

            sleep(randint(2, 3))

            clica_login = self.navegador.find_element(

                By.XPATH,
                '//*[@id="loginForm"]/div/div[3]/button/div'

            )

            clica_login.click()

            sleep(randint(40, 50))

        except Exception as error:

            error = error

            sql_nao_loga_insta = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - Instagram_controller',
                '{self.usuario} not logging in instagram.',
                '{self.id_usuario}',
                4,
                9

            );

            """

            self.db_query.db_commit(sql_nao_loga_insta)

            return

    def timeline_user(self):
        """
        Method that collects user information (number of followers and
        following) and sets up a timeline.
        """

        try:

            inicia_timeline_user = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - timeline_user',
                '{self.usuario} started the "timeline_user" method.',
                '{self.id_usuario}',
                2,
                1

            );

            """

            self.db_query.db_commit(inicia_timeline_user)

        except Exception as error:

            error = error

            nao_inicia_seguir = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - timeline_user',
                '{self.usuario} failed to start method "timeline_user".',
                '{self.id_usuario}',
                4,
                1

            );

            """

            self.db_query.db_commit(nao_inicia_seguir)

            return

        try:

            self.navegador.get(f"https://www.instagram.com/{self.usuario}/")

            sleep(5)

            publicacoes = self.navegador.find_element(

                By.XPATH,
                "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]"
                "/div[1]/div[2]/section/main/div/header/section/ul/li[1]"
                "/div/span/span"

            ).text

            seguidores = self.navegador.find_element(

                By.XPATH,
                "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]"
                "/div[1]/div[2]/section/main/div/header/section/ul/li[2]"
                "/a/div/span/span"

            ).text

            seguindo = self.navegador.find_element(

                By.XPATH,
                "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]"
                "/div[1]/div[2]/section/main/div/header/section/ul/li[3]"
                "/a/div/span/span"

            ).text

            data_atual = datetime.now().date()

            sql_commit_timelineuser = f"""

            INSERT INTO {self.db_database}.timeline_user (

                id,
                data,
                seguidores,
                seguindo,
                publicacoes,
                web_usuarios_id

                )

            VALUES (

                {int(str(data_atual).replace('-','') + str(self.id_usuario))},
                '{data_atual}',
                {seguidores},
                {seguindo},
                {publicacoes},
                {self.id_usuario}

                )

            ON DUPLICATE KEY UPDATE

                seguidores = {seguidores},
                seguindo = {seguindo},
                publicacoes = {publicacoes};


                """

            self.db_query.db_commit(sql_commit_timelineuser)

        except Exception as error:

            error = error

            nao_colta_infos = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - timeline_user',
                '{self.usuario} is not collecting user information.',
                '{self.id_usuario}',
                4,
                1

            );

            """

            self.db_query.db_commit(nao_colta_infos)

            return

        termina_timeline_user = f"""

        INSERT INTO {self.db_database}.logs (

            usuario_email,
            arquivo,
            mensagem,
            web_usuarios_id,
            level_id,
            sublevel_id

        )

        VALUES (

            '{self.insta_email}',
            '{basename(__file__)} - timeline_user',
            '{self.usuario} finished the "timeline_user" method.',
            '{self.id_usuario}',
            2,
            1

        );

        """

        self.db_query.db_commit(termina_timeline_user)

        return

    def seguir_95_user(self, qtd_seguir):
        """
        Function that will carry out the process of following users on
        Instagram so that the algorithm does not detect unusual movement.
        """

        try:

            inicia_seguir = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - seguir_95_user',
                '{self.usuario} started the "follow_95_user" method.',
                '{self.id_usuario}',
                2,
                1

            );

            """

            self.db_query.db_commit(inicia_seguir)

        except Exception as error:

            error = error

            nao_inicia_seguir = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - seguir_95_user',
                '{self.usuario} failed to start method "follow_95_user".',
                '{self.id_usuario}',
                4,
                1

            );

            """

            self.db_query.db_commit(nao_inicia_seguir)

            return

        try:

            self.navegador.get(

                f"https://www.instagram.com/{self.insta_target}"

                )

            sleep(randint(8, 12))

            clica_seguidores = self.navegador.find_element(

                By.XPATH,
                "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y "
                "xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm "
                "xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 "
                "x1hl2dhg xggy1nq x1a2a7pz _a6hd']//div[@class='_aacl _aacp "
                "_aacu _aacx _aad6 _aade']//span[@class='_ac2a']"

            )

            clica_seguidores.click()

        except Exception as error:

            error = error

            nao_clica_seguidores = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - seguir_95_user',
                '{self.usuario} is not accessing the followers of '
                '{self.insta_target}.',
                '{self.id_usuario}',
                4,
                5

            );

            """

            self.db_query.db_commit(nao_clica_seguidores)

            return

        try:

            data_atual = datetime.now().date()

            contador_seguidos = f"""

            INSERT IGNORE INTO {self.db_database}.contador_seguidos (

                id,
                data,
                total_seguidos_dia,
                web_usuarios_id

            )

            VALUES (

                {int(str(data_atual).replace('-','') + str(self.id_usuario))},
                '{data_atual}',
                0,
                {self.id_usuario}

            );

            """

            self.db_query.db_commit(contador_seguidos)

            rec_qtd_seguidos = f"""

            SELECT * FROM {self.db_database}.contador_seguidos

            WHERE (

                data = '{data_atual}'

            );

            """

            rec_seguidos_dia = self.db_query.db_fetchall(rec_qtd_seguidos)

            rec_seguidos_dia = rec_seguidos_dia[0][2]

            contador_iterador = 1

            random_seguidos = qtd_seguir

            while rec_seguidos_dia <= random_seguidos:

                sleep(randint(2, 4))

                try:

                    rota_usuario = self.navegador.find_element(

                        By.XPATH,
                        f"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]"
                        f"/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
                        f"/div[1]/div/div[{contador_iterador}]/div[2]/div[1]"
                        f"/div/div/span/a/span/div"

                    )

                    rota_seguir = self.navegador.find_element(

                        By.XPATH,
                        f"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]"
                        f"/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
                        f"/div[1]/div/div[{contador_iterador}]/div[3]"
                        f"/button/div/div"

                    )

                    if (rota_seguir.text.lower() == 'seguir' or
                            rota_seguir.text.lower() == 'follow'):

                        contador_iterador += 1

                        sql_commit_usuario_seguido = f"""

                        INSERT INTO {self.db_database}.usuarios_seguidos (

                            usuario_seguido,
                            web_usuarios_id

                        )

                        VALUES (

                            '{rota_usuario.text}',
                            '{self.id_usuario}'

                        );

                        """

                        self.db_query.db_commit(sql_commit_usuario_seguido)

                        sql_commit_contador_seguido = f"""

                        UPDATE
                        {self.db_database}.contador_seguidos

                        SET
                        total_seguidos_dia = '{rec_seguidos_dia + 1}'

                        WHERE
                        data = '{data_atual}' AND
                        web_usuarios_id = '{self.id_usuario}'

                        ;

                        """

                        self.db_query.db_commit(sql_commit_contador_seguido)

                        rec_qtd_seguidos = f"""

                        SELECT * FROM {self.db_database}.contador_seguidos

                        WHERE (

                            data = '{data_atual}'

                        );

                        """

                        rec_seguidos_dia = (

                            self.db_query.db_fetchall(rec_qtd_seguidos)

                            )

                        rec_seguidos_dia = rec_seguidos_dia[0][2]

                        rota_seguir.click()

                        sleep(randint(40, 60))

                    else:

                        contador_iterador += 1

                except Exception as error:

                    error = error

                    fBody = self.navegador.find_element(

                        By.XPATH,
                        "//div[@class='_aano']"

                    )

                    self.navegador.execute_script(

                        'arguments[0].scrollTop = arguments[0].scrollTop + '
                        'arguments[0].offsetHeight;',
                        fBody

                    )

            if rec_seguidos_dia >= random_seguidos:

                limite_seguir = f"""

                INSERT INTO {self.db_database}.logs (

                    usuario_email,
                    arquivo,
                    mensagem,
                    web_usuarios_id,
                    level_id,
                    sublevel_id

                )

                VALUES (

                    '{self.insta_email}',
                    '{basename(__file__)} - seguir_95_user',
                    '{self.usuario} reached the daily limit '
                    'for following users.',
                    '{self.id_usuario}',
                    2,
                    6

                );

                """

                self.db_query.db_commit(limite_seguir)

        except Exception as error:

            error = error

            nao_segue = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - seguir_95_user',
                '{self.usuario} is not following the followers of '
                '{self.insta_target}.',
                '{self.id_usuario}',
                4,
                6

            );

            """

            self.db_query.db_commit(nao_segue)

            return

        fecha_conexao = f"""

        INSERT INTO {self.db_database}.logs (

            usuario_email,
            arquivo,
            mensagem,
            web_usuarios_id,
            level_id,
            sublevel_id

        )

        VALUES (

            '{self.insta_email}',
            '{basename(__file__)} - seguir_95_user',
            '{self.usuario} finished the "follow_95_user" method.',
            '{self.id_usuario}',
            2,
            1

        );

        """

        self.db_query.db_commit(fecha_conexao)

        return

    def curtir_posts(self):
        """
        Method that is responsible for randomly liking posts from users
        selected from the list of users who were followed.
        """

        try:

            inicia_curtir_posts = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - curtir_posts',
                '{self.usuario} started the "curtir_posts" method.',
                '{self.id_usuario}',
                2,
                1

            );

            """

            self.db_query.db_commit(inicia_curtir_posts)

        except Exception as error:

            error = error

            nao_inicia_curtir_posts = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - curtir_posts',
                '{self.usuario} failed to start method "curtir_posts".',
                '{self.id_usuario}',
                4,
                1

            );

            """

            self.db_query.db_commit(nao_inicia_curtir_posts)

            return

        try:

            rec_users_like_post = f"""

            SELECT * FROM {self.db_database}.usuarios_seguidos

            WHERE (

                web_usuarios_id = {self.id_usuario}

            );

            """

            tupla_seguidores = self.db_query.db_fetchall(rec_users_like_post)

            lista_seguindo_todos = []

            lista_seguindo_curtir = []

            for tupla in tupla_seguidores:

                lista_seguindo_todos.append(list(tupla)[2])

            lista_seguindo_todos = list(dict.fromkeys(lista_seguindo_todos))

            num_seguidos_max = range(0, len(lista_seguindo_todos))

            sorteio_seguidos = sample(num_seguidos_max, 131)

            for numero in sorteio_seguidos:

                if numero == len(lista_seguindo_todos):

                    numero = numero - 1

                lista_seguindo_curtir.append(

                    lista_seguindo_todos[numero]

                    )

            lista_seguindo_curtir = list(dict.fromkeys(lista_seguindo_curtir))

            for user_seg_curtir in lista_seguindo_curtir:

                sleep(3)

                self.navegador.get(f"https://www.instagram.com/"
                                   f"{user_seg_curtir}")

                sleep(randint(2, 5))

                try:

                    sleep(randint(5, 8))

                    post_1_capa = self.navegador.find_element(

                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[1]/div/div/div"
                        "/div[1]/div[1]/div[2]/section/main/div/div[3]"
                        "/article/div/div/div[1]/div[1]"

                    )

                    sleep(randint(5, 8))

                    post_1_capa.click()

                    sleep(randint(2, 4))

                    curti_1_capa = self.navegador.find_element(

                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]"
                        "/div/div[3]/div/div/div/div/div[2]/div/article/div"
                        "/div[2]/div/div/div[2]/section[1]/span[1]/button"

                    )

                    sleep(1)

                    curti_1_capa.click()

                    sleep(1)

                except Exception as error:

                    error = error

                    print(error)

                    nao_curti_post1 = f"""

                    INSERT INTO {self.db_database}.logs (

                        usuario_email,
                        arquivo,
                        mensagem,
                        web_usuarios_id,
                        level_id,
                        sublevel_id

                    )

                    VALUES (

                        '{self.insta_email}',
                        '{basename(__file__)} - curtir_posts',
                        '{self.usuario} did not like the post 1 of '
                        '{user_seg_curtir}.',
                        '{self.id_usuario}',
                        3,
                        15

                    );

                    """

                    self.db_query.db_commit(nao_curti_post1)

                    continue

                sleep(3)

                self.navegador.get(f"https://www.instagram.com/"
                                   f"{user_seg_curtir}")

                try:

                    sleep(randint(5, 8))

                    post_2_capa = self.navegador.find_element(

                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[1]/div/div/div"
                        "/div[1]/div[1]/div[2]/section/main/div/div[3]"
                        "/article/div/div/div[1]/div[2]"

                    )

                    sleep(randint(5, 8))

                    post_2_capa.click()

                    sleep(randint(2, 4))

                    curti_2_capa = self.navegador.find_element(

                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]"
                        "/div/div[3]/div/div/div/div/div[2]/div/article/div"
                        "/div[2]/div/div/div[2]/section[1]/span[1]/button"

                    )

                    sleep(1)

                    curti_2_capa.click()

                    sleep(1)

                except Exception as error:

                    error = error

                    nao_curti_post2 = f"""

                    INSERT INTO {self.db_database}.logs (

                        usuario_email,
                        arquivo,
                        mensagem,
                        web_usuarios_id,
                        level_id,
                        sublevel_id

                    )

                    VALUES (

                        '{self.insta_email}',
                        '{basename(__file__)} - curtir_posts',
                        '{self.usuario} did not like the post 2 of '
                        '{user_seg_curtir}.',
                        '{self.id_usuario}',
                        3,
                        15

                    );

                    """

                    self.db_query.db_commit(nao_curti_post2)

                    continue

                sleep(3)

                self.navegador.get(f"https://www.instagram.com/"
                                   f"{user_seg_curtir}")

                try:

                    sleep(randint(5, 8))

                    post_3_capa = self.navegador.find_element(

                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[1]/div/div/div"
                        "/div[1]/div[1]/div[2]/section/main/div/div[3]"
                        "/article/div/div/div[1]/div[3]"

                    )

                    sleep(randint(5, 8))

                    post_3_capa.click()

                    sleep(randint(2, 4))

                    curti_3_capa = self.navegador.find_element(

                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]"
                        "/div/div[3]/div/div/div/div/div[2]/div/article/div"
                        "/div[2]/div/div/div[2]/section[1]/span[1]/button"

                    )

                    sleep(1)

                    curti_3_capa.click()

                    sleep(1)

                except Exception as error:

                    error = error

                    nao_curti_post3 = f"""

                    INSERT INTO {self.db_database}.logs (

                        usuario_email,
                        arquivo,
                        mensagem,
                        web_usuarios_id,
                        level_id,
                        sublevel_id

                    )

                    VALUES (

                        '{self.insta_email}',
                        '{basename(__file__)} - curtir_posts',
                        '{self.usuario} did not like the post 3 of '
                        '{user_seg_curtir}.',
                        '{self.id_usuario}',
                        3,
                        15

                    );

                    """

                    self.db_query.db_commit(nao_curti_post3)

                    continue

        except Exception as error:

            error = error

            nao_curtindo = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - seguir_95_user',
                '{self.usuario} is not able to like other posts.',
                '{self.id_usuario}',
                4,
                15

            );

            """

            self.db_query.db_commit(nao_curtindo)

            return

        termina_curtir = f"""

        INSERT INTO {self.db_database}.logs (

            usuario_email,
            arquivo,
            mensagem,
            web_usuarios_id,
            level_id,
            sublevel_id

        )

        VALUES (

            '{self.insta_email}',
            '{basename(__file__)} - curtir_posts',
            '{self.usuario} finished the "curtir_posts" method.',
            '{self.id_usuario}',
            2,
            1

        );

        """

        self.db_query.db_commit(termina_curtir)

        return

    def deixar_de_seguir(self, qtd_unfollow):
        """
        Method responsible for unfollowing users after a period of time.
        """

        try:

            inicia_deixar_seguir = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - deixar_de_seguir',
                '{self.usuario} started the "deixar_de_seguir" method.',
                '{self.id_usuario}',
                2,
                1

            );

            """

            self.db_query.db_commit(inicia_deixar_seguir)

        except Exception as error:

            error = error

            nao_inicia_deixa_seguir = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - deixar_de_seguir',
                '{self.usuario} failed to start method "deixar_de_seguir".',
                '{self.id_usuario}',
                4,
                1

            );

            """

            self.db_query.db_commit(nao_inicia_deixa_seguir)

            return

        try:

            range_date = randint(20, 25)

            rec_users_unfollow = f"""

            SELECT

            id, data, usuario_seguido, web_usuarios_id,

            DATEDIFF(CURDATE(), DATE(data)) > {range_date}

            FROM {self.db_database}.usuarios_seguidos

            WHERE (

            web_usuarios_id = {self.id_usuario}

            );

            """

            tupla_seguidores = self.db_query.db_fetchall(rec_users_unfollow)

            lista_seguindo_unfollow = []

            for tupla in tupla_seguidores:

                lista_seguindo_unfollow.append(list(tupla)[2])

            lista_seguindo_unfollow = list(

                dict.fromkeys(lista_seguindo_unfollow)

                )

            num_unfollow_max = range(0, len(lista_seguindo_unfollow))

            random_unfollow = qtd_unfollow

            sorteio_unfollow = sample(num_unfollow_max, random_unfollow)

            for user_unfollow in sorteio_unfollow:

                user_unfollow = lista_seguindo_unfollow[user_unfollow]

                sleep(3)

                self.navegador.get(f"https://www.instagram.com/"
                                   f"{user_unfollow}")

                sleep(randint(2, 5))

                data_atual = datetime.now().date()

                contador_unfollow_ = f"""

                INSERT IGNORE INTO {self.db_database}.contador_unfollow (

                    id,
                    data,
                    total_unfollow_dia,
                    web_usuarios_id

                )

                VALUES (

                    {int(

                        str(data_atual).replace('-','') + str(self.id_usuario)

                    )},
                    '{data_atual}',
                    0,
                    {self.id_usuario}

                );

                """

                self.db_query.db_commit(contador_unfollow_)

                rec_qtd_unfollow = f"""

                SELECT * FROM {self.db_database}.contador_unfollow

                WHERE (

                    data = '{data_atual}'

                );

                """

                rec_unfollow_dia = self.db_query.db_fetchall(rec_qtd_unfollow)

                rec_unfollow_dia = rec_unfollow_dia[0][2]

                while rec_unfollow_dia <= random_unfollow:

                    try:

                        deixa_de_seguir = self.navegador.find_element(

                            By.XPATH,
                            "/html/body/div[2]/div/div/div/div[1]/div/div/div"
                            "/div[1]/div[1]/div[2]/section/main/div/header"
                            "/section/div[1]/div[1]/div/div[1]/button"

                        )

                        if (

                            deixa_de_seguir.text.lower() == 'seguir'
                            or deixa_de_seguir.text.lower() == 'follow'

                                ):

                            deleta_nao_seguido = f"""

                            DELETE FROM {self.db_database}.usuarios_seguidos

                            WHERE (

                            web_usuarios_id = {self.id_usuario} AND
                            usuario_seguido = '{user_unfollow}'

                            );

                            """

                            self.db_query.db_commit(deleta_nao_seguido)

                            break

                        pass

                    except Exception as error:

                        error = error

                        nao_acha_seguir = f"""

                        INSERT INTO {self.db_database}.logs (

                            usuario_email,
                            arquivo,
                            mensagem,
                            web_usuarios_id,
                            level_id,
                            sublevel_id

                        )

                        VALUES (

                            '{self.insta_email}',
                            '{basename(__file__)} - deixar_de_seguir',
                            '{self.usuario} is not finding the button for the '
                            'unfollow board on home page.',
                            '{self.id_usuario}',
                            4,
                            24

                        );

                        """

                        self.db_query.db_commit(nao_acha_seguir)

                        break

                    try:

                        deixa_de_seguir.click()

                        if (

                            deixa_de_seguir.text.lower() == 'solicitado'
                            or deixa_de_seguir.text.lower() == 'requested'

                                ):

                            sleep(randint(2, 5))

                            unfollow_solicitado = self.navegador.find_element(

                                By.XPATH,
                                "/html/body/div[2]/div/div/div/div[2]/div/div"
                                "/div[1]/div/div[2]/div/div/div/div/div[2]"
                                "/div/div/div[3]/button[1]"

                            )

                            sleep(randint(10, 11))

                            unfollow_solicitado.click()

                            deleta_solicitado = f"""

                            DELETE FROM {self.db_database}.usuarios_seguidos

                            WHERE (

                            web_usuarios_id = {self.id_usuario} AND
                            usuario_seguido = '{user_unfollow}'

                            );

                            """

                            self.db_query.db_commit(deleta_solicitado)

                            sleep(randint(2, 4))

                        if (

                            deixa_de_seguir.text.lower() == 'seguindo'
                            or deixa_de_seguir.text.lower() == 'following'

                                ):

                            sleep(randint(2, 5))

                            unfollow_seguindo = self.navegador.find_element(

                                By.XPATH,
                                "/html/body/div[2]/div/div/div/div[2]/div/div"
                                "/div[1]/div/div[2]/div/div/div/div/div[2]"
                                "/div/div/div/div[7]"

                            )

                            sleep(randint(10, 11))

                            unfollow_seguindo.click()

                            deleta_seguindo = f"""

                            DELETE FROM {self.db_database}.usuarios_seguidos

                            WHERE (

                            web_usuarios_id = {self.id_usuario} AND
                            usuario_seguido = '{user_unfollow}'

                            );

                            """

                            self.db_query.db_commit(deleta_seguindo)

                            sleep(randint(2, 4))

                            sql_commit_contador_unfollow = f"""

                            UPDATE
                            {self.db_database}.contador_unfollow

                            SET
                            total_unfollow_dia = '{rec_unfollow_dia + 1}'

                            WHERE
                            data = '{data_atual}' AND
                            web_usuarios_id = '{self.id_usuario}'

                            ;

                            """

                            self.db_query.db_commit(

                                sql_commit_contador_unfollow

                            )

                            rec_qtd_unfollow = f"""

                            SELECT * FROM {self.db_database}.contador_seguidos

                            WHERE (

                                data = '{data_atual}'

                            );

                            """

                            rec_unfollow_dia = (

                                self.db_query.db_fetchall(rec_qtd_unfollow)

                                )

                            rec_unfollow_dia = rec_unfollow_dia[0][2]

                    except Exception as error:

                        error = error

                        nao_segue_user = f"""

                        INSERT INTO {self.db_database}.logs (

                            usuario_email,
                            arquivo,
                            mensagem,
                            web_usuarios_id,
                            level_id,
                            sublevel_id

                        )

                        VALUES (

                            '{self.insta_email}',
                            '{basename(__file__)} - deixar_de_seguir',
                            '{self.usuario} is not unfollowing '
                            '{user_unfollow}.',
                            '{self.id_usuario}',
                            4,
                            1

                        );

                        """

                        self.db_query.db_commit(nao_segue_user)

                        break

                if rec_unfollow_dia > random_unfollow:

                    return

        except Exception as error:

            error = error

            nao_deixa_seguir = f"""

            INSERT INTO {self.db_database}.logs (

                usuario_email,
                arquivo,
                mensagem,
                web_usuarios_id,
                level_id,
                sublevel_id

            )

            VALUES (

                '{self.insta_email}',
                '{basename(__file__)} - deixar_de_seguir',
                '{self.usuario} is not unfollowing (major error).',
                '{self.id_usuario}',
                4,
                1

            );

            """

            self.db_query.db_commit(nao_deixa_seguir)

            return

        termina_deixa_seguir = f"""

        INSERT INTO {self.db_database}.logs (

            usuario_email,
            arquivo,
            mensagem,
            web_usuarios_id,
            level_id,
            sublevel_id

        )

        VALUES (

            '{self.insta_email}',
            '{basename(__file__)} - curtir_posts',
            '{self.usuario} finished the "deixar_de_seguir" method.',
            '{self.id_usuario}',
            2,
            1

        );

        """

        self.db_query.db_commit(termina_curtir)

        return

    def close_webdriver(self):

        self.navegador.close()

        return
