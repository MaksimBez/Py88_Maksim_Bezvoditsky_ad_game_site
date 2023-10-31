from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from promocode.models import UserPromocode
from promocode.forms import RegistrationPromocodeForm
from promocode.counter import counter


class RegistrationPromocode(View):

    template_name = 'promocode.html'

    def get(self, request):
        form = RegistrationPromocodeForm()
        user = request.user
        number_of_available_promocodes = counter(user)
        context = {'form': form, 'number_of_available_promocodes': number_of_available_promocodes,
                   'error': None, 'error_2': None}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationPromocodeForm(request.POST)
        user = request.user
        number_of_available_promocodes = counter(user)
        if form.is_valid() and not UserPromocode.objects.filter(promocode=request.POST.get('promocode')).exists():
            form.save(user)
            messages.add_message(request, messages.SUCCESS, 'Промокод успешно добавлен')
            return redirect('promocode')
        context = {'form': form, 'number_of_available_promocodes': number_of_available_promocodes,
                   'error': True, 'error_2': None}
        if UserPromocode.objects.filter(promocode=request.POST.get("promocode")).exists():
            context["error_2"] = "Данный промокод уже существует"
        return render(request, self.template_name, context)
