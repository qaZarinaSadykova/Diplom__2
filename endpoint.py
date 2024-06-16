class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'


class Endpoint:
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    MAKE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    endpoint = {"Content-Type": "application/json"}
