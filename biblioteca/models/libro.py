from odoo import models, fields

#clase Libro
# Esta clase hereda de models.Model
class Libro(models.Model):
    # Aqui estamos definiendo el modelo
    _name = 'bibliteca.libro'
    _description = 'Libro'
    # Aqui estan los campos del modelo
    name = fields.Char(string='Title', required=True)
    autor = fields.Char(string='Autor', required=True)
    fecha_publicacion = fields.Date(string='Publish date', required=True)
    precio = fields.Float(string='Price', required=True)
