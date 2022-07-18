from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            # nenhum valor atual

            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    # filtra com base nos objetos que tenham os mesmos
                    # valores nos campos que estão em "for_fields"
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                # obtém o número de order no último item
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)