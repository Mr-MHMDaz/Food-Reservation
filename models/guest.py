from odoo import api, fields, models

class EnterFoods(models.Model):
    _name = "food.guest"
    _description = "برای میهمانان"

    name = fields.Char(string="نام میهمان")
    food_ids = fields.Many2many('food.foods', string='غذاها')
    week_id = fields.Many2one('food.weeks', string='هفته')
    day_ids = fields.Many2many('food.days', string='روز ها')
