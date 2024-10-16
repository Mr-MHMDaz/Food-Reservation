from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class DayOfWeek(models.Model):
    _name = 'food.days'
    _description = 'روز های هفته'

    name = fields.Char(string='روز' , compute='_complite_name')
    date = fields.Date(string='تاریخ',copy=False)
    week_id = fields.Many2one('food.weeks', string='هفته')
    food_id = fields.Many2many('food.foods', string='نام غذا',copy=False)
    food_type = fields.Selection(related = "food_id.food_type" )
    polo_count = fields.Integer(string='پلو', compute="compute_len_users_ids")
    khorak_count = fields.Integer(string='خوراک', compute="compute_len_users_ids")
    total_reserv = fields.Integer(string='مجموع رزرو ها', compute="compute_len_users_ids")
    users_is = fields.One2many('food.users', 'day_id', string='نام غذا')

    @api.depends('total_reserv', 'users_is', 'name')
    def compute_len_users_ids(self):
        for rec in self:
            polo = 0
            chelo = 0
            len_org = len(rec.users_is)
            rec.total_reserv = len_org
            for record in rec.users_is:
                if record.food_id.food_type == 'poloyi':
                    polo += 1
                else:
                    chelo +=1
            rec.polo_count = polo
            rec.khorak_count = chelo

    @api.depends('date') # اسم روز های هفته را به فارسی نشان می دهد
    def _complite_name(self):
        for re in self:
            if re.date:
                day = re.date.strftime('%A')
                re.name = day
            else:
                re.name = ''

    @api.onchange('date')
    def check_day(self):
        for record in self:
            if record.week_id:
                list_date=[]
                next_date=record.week_id.start_date
                for i in range(0,7):
                    list_date.append(next_date)
                    next_date=next_date+timedelta(days=1)
                if record.date >= list_date[0] and record.date <= list_date[6]:
                    pass
                else:
                    raise models.ValidationError("روز انتخاب شده خارج از هفته انتخابی می باشد.")

    @api.constrains('date')
    def _check_date(self):
        for record in self:
            if record.date < fields.Date.today():
                raise models.ValidationError(" نمی توانید تاریخ گذشته را انتخاب کنید. ")

    @api.onchange('date')
    def check_same_day(self):
        object = self.env["food.days"].search([("date","=",self.date)])
        if len(object) >= 1 :
            raise models.ValidationError(" .روز انتخابی از قبل وجود دارد ")

    @api.constrains("food_id")
    def _type_selecting(self):
        food_box = []
        for re in self.food_id:
            food_box.append(re.food_type)
        if len(food_box) > 2 and len(food_box) < 1:
            raise ValidationError('.برای هر روز تنها 2 نهار را میتوانید انتخاب کنید')

        if food_box[0] == food_box[1]:
            raise ValidationError('.بیش از یک نوع غذا انتخاب کردید')
