from sqlalchemy.exc import IntegrityError
from functools import wraps
from utils import HttpStatus,gerar_mensagem_de_erro
from models import Session



class NotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

def tratar_erros(funcao):
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)
        except ValueError as e:
            return gerar_mensagem_de_erro(str(e)), HttpStatus.BAD_REQUEST
        except IntegrityError as e:
            return gerar_mensagem_de_erro(str(e)), HttpStatus.CONFLICT
        except NotFoundError as e:
            return gerar_mensagem_de_erro(str(e)), HttpStatus.NOT_FOUND
        except Exception as e:
            return gerar_mensagem_de_erro(str(e)), HttpStatus.INTERNAL_SERVER_ERROR
    return wrapper


def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = Session()
        try:
            # injeta a session como último argumento
            return func(*args, session=session, **kwargs)
        except ValueError as e:
            raise ValueError(e)
        except IntegrityError as e:
            raise IntegrityError(e)
        except NotFoundError as e:
            raise NotFoundError(e)
        finally:
            session.close()
    return wrapper
