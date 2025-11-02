{
'name': 'Biblioteca',
'summary': "Un módulo para gestionar libros y autores.",
'version': '1.0',
'category': 'Uncategorized',
'author': 'Lázaro',
'website': '',
'depends': ['base', 'web'],
'data': [
    # Seguridad
    'security/ir.model.access.csv',
    # Vistas
    'views/libro_views.xml',
],
'demo': [],
'application': True,
'installable': True,
'auto_install': False,
}