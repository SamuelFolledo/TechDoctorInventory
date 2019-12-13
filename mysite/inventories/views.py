from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")




from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect #Part4 - HttpResponseRedirect takes a single argument: the URL to which the user will be redirected
from django.urls import reverse, reverse_lazy
# from django.views.generic import ListView
# from django.views.generic import DeleteView
from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views import View # Noob way #for create page view
from inventories.models import Device, Part
# from wiki.forms import CreatePageForm

class DeviceListView(ListView): #current index
    model = Device
    template_name = 'inventories/index.html'
    # context_object_name = 'latest_device_list'
    context_object_name = 'device_list'

    def get(self, request):
        """Return the last 20 published devices."""
        # return Device.objects.filter( pub_date__lte=timezone.now() ).order_by('-created')[:20]
        devices = self.get_queryset().all() #get all devices
        context = { 'devices': devices }
        return render(request, 'index.html', context)

class DeviceDetailView(DetailView):
    model = Device
    template_name = 'inventories/detail.html'
    def get(self, request, slug):
        # """ Excludes any devices that aren't published yet. """
        # return Device.objects.filter(pub_date__lte=timezone.now())
        device = self.get_queryset().get(slug__iexact=slug)
        context = { 'device': device }
        return render(request, 'page.html', context)

class DeviceResultsView(DetailView):
    model = Device
    template_name = 'inventories/results.html'
    

# class PageCreateView(View):
#     model = Page
#     def get(self, request):
#         # Code block for GET request
#         form = CreatePageForm()
#         context = { 'form':form }
#         return render(request, 'create.html', context)
#     def post(self, request):
#         # Code block for POST request
#         form = CreatePageForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             page = form.save()
#             # form.save()
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse_lazy('wiki:wiki-details-page', args=[page.slug])) #wiki is the app name and wiki-details-page is the name in urls.py
#         return render(request, 'create.html', {'form': form})
########### func-based view method
# def vote(request, question_id): #part 4
#     question = get_object_or_404(Device, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Part.DoesNotExist):
#         # Redisplay the question voting form.
#         context = {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         }
#         return render(request, 'polls/detail.html', context)
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))