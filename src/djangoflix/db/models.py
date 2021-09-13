from django.db import models


class PublishStateOptions(models.TextChoices):
    # CONSTANT = DB_VALUES, USER_DISPLAY_VALUES,
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'
    # UNLISTED = 'UN','Unlisted'
    # PRIVATE = 'PR','Private'

