from django.apps import apps
from django.contrib.contenttypes.models import ContentType


def get_asset_model(asset_category):
    model_dict = {
        "entry": "entries",
        "article": "articles",
    }
    app_name = model_dict.get(asset_category)

    if app_name is not None:
        asset_model = apps.get_model(
            app_label=app_name,
            model_name=asset_category,
        )
        asset_model = ContentType.objects.get_for_model(asset_model)
    else:
        asset_model = None

    return asset_model
