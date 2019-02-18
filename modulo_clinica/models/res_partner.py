from odoo import models, fields, api
import datetime

class res_partner_clinica(models.Model):
    _inherit = 'res.partner'
    
    fecha_nacimiento = fields.Date('Fecha de nacimiento')
    edad = fields.Integer('Edad', compute='_calc_fecha_nacimiento')
    sexo = fields.Selection([('m','Masculino'),
                             ('f','Femenino')],
                            'Sexo')
    
    alergias = fields.Text('Alergias')
    obs = fields.Text('Observaciones')
    consultas_ids = fields.One2many('ficha.consulta','paciente_id',
                                    string='Consultas')
    
    fichas_ids = fields.One2many('ficha.ficha', 'paciente_id',
                                      string='Fichas')
    
    count_consulta = fields.Integer('Nº de Consultas', compute='count_consultas')
    count_ficha = fields.Integer('Nº de Fichas', compute='count_consultas')
    
    
    
    @api.one
    def count_consultas(self):
        consultas = 0
        fichas = 0
        for c in self.consultas_ids:
            consultas += 1
        for p in self.fichas_ids:
            fichas += 1
        self.count_consulta = consultas
        self.count_ficha = fichas
        
    
    @api.multi
    def open_ficha_action(self):
        action = self.env.ref('clinica_modulo.action_ficha_tree_view')
        result = action.read()[0]
        result['domain'] = [('paciente_id', '=', self.ids)]
        return result
    
    @api.multi
    def open_consulta_action(self):
        action = self.env.ref('clinica_modulo.action_consulta_tree_view')
        result = action.read()[0]
        result['domain'] = [('paciente_id', '=', self.ids)]
        return result
    
    @api.one
    def _calc_fecha_nacimiento(self):
        today = datetime.datetime.now()
        if self.fecha_nacimiento:
            nasc = datetime.datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d").date()
            nueva_edad = today.year - nasc.year
            self.edad = nueva_edad
        else:
            self.edad = 0
        