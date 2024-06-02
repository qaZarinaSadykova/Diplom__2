import uuid
data_exist_user = {
    "email": 'tets_2503@yandex.ru',
    "password": "password",
    "name": "Username"
}

data_positive = {
    "email": 'zarina_sadykova_5_555.yandex.ru',
    "password": "555zar",
}

data_failed = {
    "email": 'tets_76543567@yandex.ru',
    "password": "password",
}

data_without_email = {
    "email": '',
    "password": "password",
    "name": "Username"
}

data_without_password = {
    "email": 'tets_2503@yandex.ru',
    "password": "",
    "name": "Username"
}

data_without_name = {
    "email": 'tets_2503@yandex.ru',
    "password": "password",
    "name": ""
}

unique_email = f"user_{uuid.uuid4()}@example.com"
data_updated = {
    "email": unique_email,
    "password": "password",
    "name": "Test"
}


data_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
}

data_not_ingredients = {
        "ingredients": []
    }

data_ingredients_wrong_hash = {
    "ingredients": ["60d3b41abdacab0026a733c6g", "609646e4dc916e00276b2870g"]
}
