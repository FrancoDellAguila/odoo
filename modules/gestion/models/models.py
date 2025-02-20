# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Franquicia(models.Model):
    _name = "gestion.franquicia"
    _description = "Franquicia"

    name = fields.Char(string='Nombre de la Franquicia', required=True)
    ciudad = fields.Char(string='Ciudad de la Franquicia')