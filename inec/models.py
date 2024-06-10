from django.db import models

# Create your models here.
from django.db import models

class Party(models.Model):
    partyid = models.CharField(max_length=11, unique=True)
    partyname = models.CharField(max_length=11)

    class Meta:
        db_table = 'party'
        verbose_name = 'Party'
        verbose_name_plural = 'Parties'
    def __str__(self):
        return self.partyid

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'states'
        verbose_name = 'State'
        verbose_name_plural = 'States'
    
    def __str__(self):
        return self.state_name
        
class LGA(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=50)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'lga'
        verbose_name = 'LGA'
        verbose_name_plural = 'LGAs'
        
    def __str__(self):
        return self.lga_name
        
        
class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    ward_description = models.TextField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=50)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'ward'
        verbose_name = 'Ward'
        verbose_name_plural = 'Wards'
    def __str__(self):
    	return self.ward_name
        
        
class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField(blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    entered_by_user = models.CharField(max_length=50, blank=True, null=True)
    date_entered = models.CharField(max_length=50, blank=True, null=True)
    user_ip_address = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'polling_unit'
        verbose_name = 'Polling Unit'
        verbose_name_plural = 'Polling Units'
        
    def __str__(self):
        return self.polling_unit_name
     

class AgentName(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    pollingunit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE, db_column='pollingunit_uniqueid')

    class Meta:
        db_table = 'agentname'
        verbose_name = 'Agent Name'
        verbose_name_plural = 'Agent Names'

class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    ward_name = models.ForeignKey(Ward, on_delete=models.CASCADE, db_column='ward_name')
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=50, blank=True, null=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_ward_results'
        verbose_name = 'Announced Ward Result'
        verbose_name_plural = 'Announced Ward Results'

class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE, db_column='state_name')
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=50, blank=True, null=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_state_results'
        verbose_name = 'Announced State Result'
        verbose_name_plural = 'Announced State Results'

class AnnouncedPUResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE, db_column='polling_unit_uniqueid')
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=50, blank=True, null=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_pu_results'
        verbose_name = 'Announced PU Result'
        verbose_name_plural = 'Announced PU Results'

class AnnouncedLGAResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    lga_name = models.ForeignKey(LGA, on_delete=models.CASCADE, db_column='lga_name')
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.CharField(max_length=50, blank=True, null=True)
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = 'announced_lga_results'
        verbose_name = 'Announced LGA Result'
        verbose_name_plural = 'Announced LGA Results'
