from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView, View)

from .forms import AutorForm, LibroForm
from .models import Autor, Libro


class Inicio(TemplateView):
    template_name = "index.html"


class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado=True)


class ActualizarAutor(UpdateView):
    model = Autor
    template_name = "libro/autor/crear_autor.html"
    form_class = AutorForm
    success_url = reverse_lazy('autor:listar_autor')


class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('autor:listar_autor')


class EliminarAutor(DeleteView):
    model = Autor
    # logic delete

    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('autor:listar_autor')


class ListadoLibros(View):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html'

    def get_queryset(self):

        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = {}
        context['libros'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro:listado_libros')


class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html'
    success_url = reverse_lazy('libro:listado_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libros"] = Libro.objects.filter(estado=True)
        return context
    

class EliminarLibro(DeleteView):
    model = Libro

    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')