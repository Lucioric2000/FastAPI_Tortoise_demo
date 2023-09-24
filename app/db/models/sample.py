from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


# Customers Table
class Test_table(Model):
    __tablename__ = "test_table"
    id = fields.IntField(pk=True)
    item_name = fields.CharField(max_length=100)
    item_value = fields.IntField()


Test_table_Pydantic = pydantic_model_creator(Test_table, name="Test_table")
Test_table_in_Pydantic = pydantic_model_creator(Test_table, name="Test_table_in", exclude_readonly=True)