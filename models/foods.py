from odoo import api, fields, models

class Lunch(models.Model):
    _name = "food.foods"
    _description = "اضافه کردن نام و نوع غذا"

    name = fields.Char(string="نام غذا")
    food_type = fields.Selection([('poloyi','پلو'),('khorak' , 'خوراک')] , string="پلو یا خوراک" )
    day_id = fields.Many2many('food.days', string='روز')
    # week_id = fields.Many2one('food.weeks', string='هفته')

