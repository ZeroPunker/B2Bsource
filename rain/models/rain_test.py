# -*- coding: utf-8 -*-
from openerp import models, api, _, fields
class rains_test(models.Model):
    _inherit="res.partner"
    test = fields.Char('test')
    username= fields.Char('username')
    
 