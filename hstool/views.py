from django.views.generic import (
    ListView, CreateView, DetailView, DeleteView, UpdateView,
)
from django.core.urlresolvers import reverse_lazy, reverse

from hstool.models import (
    Source, Indicator, DriverOfChange, Country, GeographicalScope, Figure,
    Assessment,
)
from hstool.forms import (
    SourceForm, IndicatorForm, DriverForm, CountryForm, GeoScopeForm,
    FigureForm, CountryUpdateForm, AssessmentForm,
)


class ContextMixin(object):
    def get_success_url(self):
        return self.request.GET.get('next', reverse('home_view'))

    def get_context_data(self, **kwargs):
        context = super(ContextMixin, self).get_context_data(**kwargs)
        context.update({'cancel_url': self.get_success_url()})
        return context


class AssessmentsListView(ListView):
    template_name = 'tool/assessments_list.html'
    model = Assessment
    context_object_name = 'assessments'


class AssessmentsAddView(CreateView):
    template_name = 'tool/assessments_add.html'
    form_class = AssessmentForm
    success_url = reverse_lazy('home_view')


class AssessmentsUpdate(ContextMixin, UpdateView):
    template_name = 'tool/assessments_add.html'
    model = Assessment
    form_class = AssessmentForm
    success_url = reverse_lazy('home_view')


class AssessmentsDelete(ContextMixin, DeleteView):
    template_name = 'tool/object_delete.html'
    model = Assessment


class SourcesListView(ListView):
    template_name = 'tool/sources_list.html'
    model = Source
    context_object_name = 'sources'


class SourcesAddView(CreateView):
    template_name = 'tool/sources_add.html'
    form_class = SourceForm
    success_url = reverse_lazy('sources:list')


class SourcesUpdate(ContextMixin, UpdateView):
    template_name = 'tool/sources_add.html'
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('sources:list')


class SourcesDelete(ContextMixin, DeleteView):
    template_name = 'tool/object_delete.html'
    model = Source


class IndicatorsListView(ListView):
    template_name = 'tool/indicators_list.html'
    model = Indicator
    context_object_name = 'indicators'


class IndicatorsAddView(CreateView):
    template_name = 'tool/indicators_add.html'
    form_class = IndicatorForm
    success_url = reverse_lazy('indicators_list')


class IndicatorsUpdate(ContextMixin, UpdateView):
    template_name = 'tool/indicators_add.html'
    model = Indicator
    form_class = IndicatorForm
    success_url = reverse_lazy('indicators_list')


class IndicatorsDelete(ContextMixin, DeleteView):
    template_name = 'tool/object_delete.html'
    model = Indicator


class DriversListView(ListView):
    template_name = 'tool/drivers_list.html'
    model = DriverOfChange
    context_object_name = 'drivers'


class DriversAddView(CreateView):
    template_name = 'tool/drivers_add.html'
    form_class = DriverForm
    success_url = reverse_lazy('drivers:list')


class DriversUpdate(ContextMixin, UpdateView):
    template_name = 'tool/drivers_add.html'
    model = DriverOfChange
    form_class = DriverForm
    success_url = reverse_lazy('drivers:list')


class DriversDelete(ContextMixin, DeleteView):
    template_name = 'tool/object_delete.html'
    model = DriverOfChange


class FiguresListView(ListView):
    template_name = 'tool/figures_list.html'
    model = Figure
    context_object_name = 'figures'


class FiguresAddView(CreateView):
    template_name = 'tool/figures_add.html'
    form_class = FigureForm
    success_url = reverse_lazy('figures:list')


class FiguresUpdate(ContextMixin, UpdateView):
    template_name = 'tool/figures_add.html'
    model = Figure
    form_class = FigureForm
    success_url = reverse_lazy('figures:list')


class FiguresDelete(ContextMixin, DeleteView):
    template_name = 'tool/object_delete.html'
    model = Figure


class CountriesListView(ListView):
    template_name = 'tool/countries_list.html'
    model = Country
    context_object_name = 'countries'


class CountriesAddView(CreateView):
    template_name = 'tool/countries_add.html'
    form_class = CountryForm
    success_url = reverse_lazy('settings:countries_list')


class CountriesUpdate(ContextMixin, UpdateView):
    template_name = 'tool/countries_update.html'
    model = Country
    form_class = CountryUpdateForm
    success_url = reverse_lazy('settings:countries_list')


class CountriesDelete(ContextMixin, DeleteView):
    template_name = 'tool/object_delete.html'
    model = Country


class GeoScopesListView(ListView):
    template_name = 'tool/geo_scopes_list.html'
    model = GeographicalScope
    context_object_name = 'geo_scopes'


class GeoScopesAddView(CreateView):
    template_name = 'tool/geo_scopes_add.html'
    form_class = GeoScopeForm
    success_url = reverse_lazy('settings:geo_scopes_list')


class GeoScopesUpdate(ContextMixin, UpdateView):
    template_name = 'tool/geo_scopes_add.html'
    model = GeographicalScope
    form_class = GeoScopeForm
    success_url = reverse_lazy('settings:geo_scopes_list')


class GeoScopesDelete(ContextMixin, DeleteView):
    template_name = 'tool/object_delete.html'
    model = GeographicalScope


class ModelMixin(object):
    url_to_models = {
        'sources': Source,
        'figures': Figure,
        'indicators': Indicator,
        'drivers': DriverOfChange,
        'countries': Country,
        'geo_scales': GeographicalScope,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model_name = kwargs.pop('model', None)
        self.model = self.url_to_models.get(self.model_name)
        return super(ModelMixin, self).dispatch(request, *args, **kwargs)


class AddModal(ModelMixin, CreateView):
    template_name = 'tool/add_modal.html'

    urls_to_forms = {
        'sources': SourceForm,
        'figures': FigureForm,
    }

    def get_form_class(self):
        self.model_name = self.kwargs.get('model')
        return self.urls_to_forms.get(self.model_name)

    def get_success_url(self):
        return reverse(
            'add_modal_success', args=(self.model_name, self.object.id, )
        )


class AddModalSuccess(ModelMixin, DetailView):
    template_name = 'tool/add_modal_success.html'

    def get_context_data(self, **kwargs):
        context = super(AddModalSuccess, self).get_context_data()
        context.update({'model_name': self.model_name})
        return context
