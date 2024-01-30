from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'llibreria.categoria'
    _description = 'Categoría de llibre'

    nom = fields.Char(string='Nom', required=True, help='Introduïx el nom de la categoria')
    descripcio = fields.Text(string='Descripció')

class Llibre(models.Model):
    _name = 'llibreria.llibre'
    _description = 'Llibre'

    nom = fields.Char(string='Nom', required=True)
    preu = fields.Float(string='Preu')
    exemplars = fields.Integer(string='Exemplars')
    rotura_estoc = fields.Boolean(string='Rotura Estoc', compute='_hi_ha_estoc')
    data = fields.Data(string='Data')
    segonama = fields.Boolean(string='Segonama')
    estat = fields.Selection([('bo', 'Bo'), ('regular', 'Regular'), ('dolent', 'Dolent')],
                             string='Estat', default='bo')

    def _hi_ha_estoc(self):
    	for record in self:
			record.rotura_estoc = record.exemplars < 10