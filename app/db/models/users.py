from fastapi import FastAPI
from tortoise import fields
from tortoise.models import Model


app = FastAPI()

# Customers Table
class Customer(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    applications = fields.ReverseRelation["Application"]
    policies = fields.ReverseRelation["Policy"]
    beneficiaries = fields.ReverseRelation["Beneficiary"]
    claims = fields.ReverseRelation["Claim"]


# Applications Table
class Application(Model):
    id = fields.IntField(pk=True)
    status = fields.CharField(max_length=50)
    customer = fields.ForeignKeyField('models.Customer', related_name='applications')
    policy = fields.OneToOneField('models.Policy', related_name='application', null=True)


# Policies Table
class Policy(Model):
    id = fields.IntField(pk=True)
    start_date = fields.DateField()
    end_date = fields.DateField()
    plan = fields.ForeignKeyField('models.Plan', related_name='policies')
    customer = fields.ForeignKeyField('models.Customer', related_name='policies')

# Plans Table
class Plan(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    policies = fields.ReverseRelation["Policy"]

# Beneficiaries Table
class Beneficiary(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    relationship = fields.CharField(max_length=50)
    customer = fields.ForeignKeyField('models.Customer', related_name='beneficiaries')

# Claims Table
class Claim(Model):
    id = fields.IntField(pk=True)
    status = fields.CharField(max_length=50)
    amount = fields.FloatField()
    customer = fields.ForeignKeyField('models.Customer', related_name='claims')


"""
class Policy(BaseModel):
    application_id: str
    policy_start_date: str
    policy_end_date: str
"""

