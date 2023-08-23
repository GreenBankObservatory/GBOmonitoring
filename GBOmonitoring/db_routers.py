class DbRouter:
    # Map
    routes = {
        "dashboards": "default",
        "prometheus": "default",
    }

    def db_for_read(self, model, **hints):
        """Route model reads to correct DB.

        Suggest the database that should be used for read operations for objects of type model.

        If a database operation is able to provide any additional information that might assist in selecting a database,
        it will be provided in the hints dictionary. Details on valid hints are provided below.

        Returns None if there is no suggestion.
        """
        if model._meta.app_label in self.routes:
            return self.routes[model._meta.app_label]

        raise ValueError(f"No route defined for {model._meta.app_label}; you need to fix settings.DATABASE_ROUTERS")

    def db_for_write(self, model, **hints):
        """Attempts to write are handled exactly the same as reads.

        Suggest the database that should be used for writes of objects of type Model.

        If a database operation is able to provide any additional information that might assist in selecting a database,
        it will be provided in the hints dictionary.

        Returns None if there is no suggestion.
        """
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if a model in one of our apps is involved.

        Return True if a relation between obj1 and obj2 should be allowed, False if the relation should be prevented, or
        None if the router has no opinion. This is purely a validation operation, used by foreign key and many to many
        operations to determine if a relation should be allowed between two objects.

        If no router has an opinion (i.e. all routers return None), only relations within the same database are allowed.
        """
        # We are okay with the default behavior here
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Determine if the migration operation is allowed to run on the database with alias `db`. Return True if the
        operation should run, False if it shouldn’t run, or None if the router has no opinion.

        The `app_label` positional argument is the label of the application being migrated.

        `model_name` is set by most migration operations to the value of model._meta.model_name (the lowercased version
        of the model __name__) of the model being migrated. Its value is None for the RunPython and RunSQL operations
        unless they provide it using hints.

        hints are used by certain operations to communicate additional information to the router.

        When `model_name` is set, hints normally contains the model class under the key 'model'. Note that it may be a
        historical model, and thus not have any custom attributes, methods, or managers. You should only rely on _meta.

        This method can also be used to determine the availability of a model on a given database.

        makemigrations always creates migrations for model changes, but if allow_migrate() returns False, any migration
        operations for the `model_name` will be silently skipped when running migrate on the db. Changing the behavior
        of allow_migrate() for models that already have migrations may result in broken foreign keys, extra tables, or
        missing tables. When makemigrations verifies the migration history, it skips databases where no app is allowed
        to migrate.
        """
        if app_label in self.routes:
            return db == self.routes[app_label]

        raise ValueError(f"No route defined for {app_label}; you need to fix settings.DATABASE_ROUTERS")