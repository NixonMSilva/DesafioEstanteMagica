from pydantic import BaseModel

# The purpose of this custom base model is to
# remove null values when working with the schema classes

class CustomBaseModel(BaseModel):
    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        d = {k: v for k, v in d.items() if v is not None}
        return d