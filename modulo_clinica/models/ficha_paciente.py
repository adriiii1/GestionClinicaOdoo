from odoo import models, fields, api

class Ficha(models.Model):
    _name = 'ficha.ficha'
    
    paciente_id = fields.Many2one('res.partner', string='Paciente')
    
    observaciones_medicas = fields.Text(u'Observaciones Médicas')
    diagnostico = fields.Text(u'Diagnóstico')
    fecha_nacimiento = fields.Date('Fecha de nacimiento',
                                   related='paciente_id.fecha_nacimiento')
    edad_paciente = fields.Integer('Edad', related='paciente_id.edad')
    
    medico_id = fields.Many2one('res.users', u'Médico a cargo')
    

class FichaConsulta(models.Model):
    _name = 'ficha.consulta'
    
    fecha_consulta = fields.Datetime('Fecha de la consulta', required=True)
    
    tipo_consulta = fields.Selection([('periodico','Periodico'),
                                       ('retorno','Retorno'),
                                       ('emergencia','Emergencia')],
                                       'Tipo de Consulta')
    
    paciente_id = fields.Many2one('res.partner', string='Paciente')
    
    ficha_id = fields.Many2one('ficha.ficha', string='Paciente')
    
    local_consulta = fields.Selection([('sede','Sede'),
                                       ('unidad','Unidad')],
                                      'Local de consulta')
    
    
        
    
    