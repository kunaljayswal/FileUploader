# * Import Python Module
import json
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from pydantic import ValidationError

# * Import User Defined Functions
from service.response import response
from service.genericError import GenericError


def error_handler(func):
    """Decorator used to catch certain types of Exceptions"""

    def validate(*args, **kwargs):
        try:
            to_return = func(*args, **kwargs)
        except ValidationError as e:
            errors = []
            errors_list = json.loads(e.json())
            for error in errors_list:
                errors.append({"attribute": error["loc"][0], "msg": error["msg"]})
            return response(400, errors)
        except GenericError as e:
            return e.serialize_response()
        except NoResultFound:
            return response(404, {"message": "Entity not found"})
        except SQLAlchemyError as e:
            return response(403, {"message": f"SOMETHING WENT WRONG {e}"})
        except Exception as e:
            raise e
        return to_return

    return validate
