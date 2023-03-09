from .threadlocal import get_thread_local
from app.settings.local import DATABASES


class Cableado:

    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        # if model._meta.app_label in DATABASE_ROUTERS:
        using = get_thread_local('using_db', 'default')

        if using not in DATABASES:
            # return model._meta.app_label
            using = 'default'
        return using

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        # if model._meta.app_label in DATABASE_ROUTERS:

        using = get_thread_local('using_db', 'default')
        if using not in DATABASES:
            # return model._meta.app_label
            using = 'default'
        return using

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True