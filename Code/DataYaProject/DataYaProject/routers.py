class AppRouter:
    """
    A router to control all database operations on models for different databases.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'accounts':
            return 'accounts_db'
        if model._meta.app_label == 'analytics':
            return 'analitycs_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'accounts':
            return 'accounts_db'
        if model._meta.app_label == 'analytics':
            return 'analitycs_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'accounts' or obj2._meta.app_label == 'accounts':
            return True
        elif obj1._meta.app_label == 'analytics' or obj2._meta.app_label == 'analytics':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'accounts':
            return db == 'accounts_db'
        if app_label == 'analytics':
            return db == 'analitycs_db'
        return None


