class AppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'accounts':
            return 'accounts_db'
        elif model._meta.app_label == 'analytics':
            return 'analytics_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'accounts':
            return 'accounts_db'
        elif model._meta.app_label == 'analytics':
            return 'analytics_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'accounts' and obj2._meta.app_label == 'accounts':
            return True
        elif obj1._meta.app_label == 'analytics' and obj2._meta.app_label == 'analytics':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'

