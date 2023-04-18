from .models import BaseTimestampedModel, BaseSoftDeletionModel


class ExtendedModelMixin(BaseTimestampedModel, BaseSoftDeletionModel):
    class Meta:
        abstract = True
