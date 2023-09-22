from tortoise import fields
from tortoise.models import Model
from pydantic import BaseModel

# Customers Table
class Test_table(Model):
    __tablename__ = "test_table"
    #id = fields.IntField(pk=True)
    item_name = fields.CharField(max_length=100)
    item_value = fields.IntField()

class UTest_table(BaseModel):
    item_name:str
    item_value:int