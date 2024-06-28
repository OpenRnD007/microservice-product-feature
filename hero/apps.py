from django.apps import AppConfig


class HeroConfig(AppConfig):
    """
    Configuration class for the 'hero' application.

    This class is used to set up any application-specific configurations such as
    the default auto field type and the application name. It is also the place
    to include any application initialization code.
    """
    default_auto_field = 'django.db.models.BigAutoField' # Sets the type of auto field to use as a primary key.
    name = 'hero' # Defines the name of the application.
