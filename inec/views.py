
from django.shortcuts import render, redirect
from .models import State, LGA, PollingUnit, AnnouncedPUResults, AnnouncedStateResults, PollingUnit, Party
from .forms import PollingUnitForm, ResultForm
from django.db.models import Sum


def index(request):
    form = PollingUnitForm()
    results = []
    lga_results = []
    grand_total = 0
    lga=''
    total_polling_units = 0
    if request.method == 'POST':
        form = PollingUnitForm(request.POST)
        if form.is_valid():
            lga = form.cleaned_data.get('lga')
            results = PollingUnit.objects.filter(lga=lga).annotate(
                total_score=Sum('announcedpuresults__party_score')
            )
            lga_results = (
                PollingUnit.objects.filter(lga=lga)
                .values('lga')
                .annotate(total_score=Sum('announcedpuresults__party_score'))
                .order_by('lga')
            )
            grand_total = sum(result['total_score'] for result in lga_results if result['total_score'])
            
            polling_units = PollingUnit.objects.filter(lga=lga)
            total_polling_units = polling_units.count() 
    
    return render(request, 'index.html', {'form': form, 'results': results, 'grand_total': grand_total, 'lga':lga, 'total_polling_units':total_polling_units })


def load_lgas(request):
    state_id = request.GET.get('state')
    lgas = LGA.objects.filter(state_id=state_id).order_by('lga_name')
    return render(request, 'lga_dropdown_list_options.html', {'lgas': lgas})



def store_results(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_results')  # Redirect to the same page after saving

    else:
        form = ResultForm()

    # Fetch all results
    results = AnnouncedPUResults.objects.all().order_by('polling_unit__polling_unit_name', 'party_abbreviation')

    return render(request, 'store_results.html', {'form': form, 'results': results})
