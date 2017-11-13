# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime


class Direccion(models.Model):
	calle = models.CharField(max_length=30)
	poblacion = models.CharField(max_length=30)
	CP = models.CharField(max_length=30)
	pais = models.CharField(max_length=30)

	def __str__(self):              
		return str(self.poblacion)


class Usuarios(models.Model):
	nombre = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	direccion = models.OneToOneField(Direccion)
	email = models.CharField(max_length=30)
	web = models.CharField(max_length=30, blank=True)
	tlf = models.CharField(max_length=30, blank=True)

	def __str__(self):              
		return str(self.nombre)
