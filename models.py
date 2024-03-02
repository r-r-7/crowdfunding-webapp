from django.db import models

# Create your models here.

class Fundraiser(models.Model):
    RETURNS = (
        ('Shares', 'Shares'),
        ('Interest','Interest')
        )
    campaign_title = models.CharField(max_length=200,null=True)
    desc = models.CharField(max_length=200,null=True)
    capital_to_be_raised = models.IntegerField()
    minimum_invest = models.IntegerField()
    returns_opt = models.CharField(max_length=200,choices=RETURNS)
    contact_mail = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.campaign_title
    
class Startup(models.Model):
    company_name = models.CharField(max_length=200, null=True)
    capital_needed = models.IntegerField()
    no_of_investors = models.IntegerField(null=True)
    description = models.CharField(max_length=500,null=True)
    date_invested = models.DateTimeField(auto_now_add=True)
    fundraiser_title = models.ForeignKey(Fundraiser,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Investor(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    company_invested = models.ForeignKey(Startup, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name