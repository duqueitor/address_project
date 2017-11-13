# -*- coding: utf-8 -*-
#Autor: Adrian Duque Anguera
#Mail: adrian.duque@hotmail.es
#Tlf: 689263795

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from .models import Usuarios, Direccion


def home(request):
	return render(request, 'home.html', {})


def agregar_usuario(request):
	c = {}
	if request.method == 'POST':
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		web = request.POST.get('web')
		locality = request.POST.get('locality')
		country = request.POST.get('country')
		cp = request.POST.get('postal_code')
		comunity = request.POST.get('comunity')
		route = request.POST.get('route')

		try:
			new_address = Direccion()
			new_address.calle = route
			new_address.poblacion = locality
			new_address.pais = country
			new_address.CP = cp
			new_address.save()

			new_register = Usuarios()
			new_register.nombre = firstname
			new_register.apellidos = lastname
			new_register.email = email
			new_register.tlf = phone
			new_register.web = web
			new_register.direccion = new_address
			new_register.save()
			c['result'] = 'OK'
		except Exception as e:
			print e
			c['result'] = 'KO'

	return render(request, 'add_user.html', c)


def buscar_usuario(request):
	c = {}
	if request.method == 'POST':
		busqueda = request.POST.get('browser')
		if request.POST.get('update') == 'si':
			user_id = request.POST.get('user_id')

			nombre = request.POST.get('nombre')
			apellidos = request.POST.get('apellidos')
			poblacion = request.POST.get('poblacion')
			email = request.POST.get('email')
			pais = request.POST.get('pais')
			cp = request.POST.get('cp')

			user_update = Usuarios.objects.get(id=user_id)
			user_update.nombre = nombre
			user_update.apellidos = apellidos
			user_update.email = email
			
			register_update = Direccion.objects.get(
				id=user_update.direccion.id)
			register_update.CP = cp
			register_update.poblacion = poblacion
			register_update.pais = pais

			register_update.save()
			user_update.save()
			c['update'] = True
			c['user_id'] = int(user_id)

		users = busqueda_query(busqueda)
		c['busqueda'] = busqueda
		c['users'] = users
		c['total_users'] = len(users)
	else:
		c['init'] = True

	return render(request, 'search_user.html', c)


def busqueda_query(busqueda):
	users = Usuarios.objects.filter(
		Q(nombre__icontains=busqueda) |
		Q(email__icontains=busqueda) |
		Q(direccion__poblacion__icontains=busqueda) |
		Q(direccion__CP__icontains=busqueda) |
		Q(direccion__pais__icontains=busqueda))

	return users


