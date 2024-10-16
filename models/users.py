from odoo import api, fields, models

class EnterFoods(models.Model):
    _name = "food.users"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'employees'
    _description = "صفحه لاگین کاربر"

    employees = fields.Many2one('res.users', string='نام و نام خانوادگی کارمند', default = lambda self:self.env.user, readonly = True)
    visitant = fields.Selection([('visitant','میهمان دارم'),('no_visitant', 'میهمان ندارم')], string='آیا میهمان دارید ؟', default='no_visitant')
    food_id = fields.Many2one('food.foods', string='نام غذا',tracking=True)
    day_id = fields.Many2one('food.days', string='روز',tracking=True)
    week_id = fields.Many2one('food.weeks', string='هفته',tracking=True)

# در این api با استفاده از حلقه for و self که به همین مدل اشاره دارد ارور را قرار دادیم در صورتی که در api پایینی که از object استفاده شده است و چون در همین مدل داریم از object برای همین مدل استفاده می کنیم در نتیجه اون api اشتباه است

    @api.onchange('day_id')
    def check_same_day(self):

        for rec in self.day_id :
            if len(rec.users_is) != 0 :
                raise models.ValidationError(" .روز انتخابی از قبل وجود دارد ")
