from django.contrib import admin

# Register your models here.
#from django.contrib import admin
from .models import (
    Party, State, LGA, Ward, PollingUnit, AgentName,
    AnnouncedWardResults, AnnouncedStateResults, AnnouncedPUResults, AnnouncedLGAResults
)

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('partyid', 'partyname')
    search_fields = ('partyid', 'partyname')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'state_name')
    search_fields = ('state_name',)

@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display = ('uniqueid', 'lga_id', 'lga_name', 'state', 'entered_by_user', 'date_entered')
    search_fields = ('lga_name',)
    list_filter = ('state',)

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('uniqueid', 'ward_id', 'ward_name', 'lga', 'entered_by_user', 'date_entered')
    search_fields = ('ward_name',)
    list_filter = ('lga',)

@admin.register(PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ('uniqueid', 'polling_unit_id', 'ward', 'lga', 'polling_unit_number', 'polling_unit_name', 'entered_by_user', 'date_entered')
    search_fields = ('polling_unit_name',)
    list_filter = ('ward', 'lga')

@admin.register(AgentName)
class AgentNameAdmin(admin.ModelAdmin):
    list_display = ('name_id', 'firstname', 'lastname', 'email', 'phone', 'pollingunit')
    search_fields = ('firstname', 'lastname', 'email', 'phone')
    list_filter = ('pollingunit',)

@admin.register(AnnouncedWardResults)
class AnnouncedWardResultsAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'ward_name', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered')
    search_fields = ('ward_name__ward_name', 'party_abbreviation')
    list_filter = ('ward_name', 'party_abbreviation')

@admin.register(AnnouncedStateResults)
class AnnouncedStateResultsAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered')
    search_fields = ('state_name__state_name', 'party_abbreviation')
    list_filter = ('state_name', 'party_abbreviation')

@admin.register(AnnouncedPUResults)
class AnnouncedPUResultsAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'polling_unit', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered')
    search_fields = ('polling_unit__polling_unit_name', 'party_abbreviation')
    list_filter = ('polling_unit', 'party_abbreviation')

@admin.register(AnnouncedLGAResults)
class AnnouncedLGAResultsAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'lga_name', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered')
    search_fields = ('lga_name__lga_name', 'party_abbreviation')
    list_filter = ('lga_name', 'party_abbreviation')
