from django_extensions.collision_resolvers import AppNameSuffixCustomOrderCR


class SensibleCR(AppNameSuffixCustomOrderCR):
    @property
    def APP_PRIORITIES(self):
        from django.conf import settings

        priorities = getattr(settings, "INSTALLED_APPS", [])[::-1]
        print("priorities", priorities)

        return priorities