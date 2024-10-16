from datetime import timedelta
from odoo import models, fields, api


class WeekOfYear(models.Model):
    _name = 'food.weeks'
    _description = 'هفته های سال'
    _rec_name = 'start_date'


    start_date = fields.Date(string='تاریخ شروع', default=fields.datetime.today())
    end_date = fields.Date(string='تاریخ پایان', compute='_complite_endweek')

    @api.depends('start_date')
    def _complite_endweek(self):
        for re in self:
            re.end_date = re.start_date + timedelta(days=7)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            day = record.start_date.strftime('%A')
            existing_week = self.search([('start_date', '=', record.start_date), ('id', '!=', record.id)])
            if  day != 'شنبه' :
                raise models.ValidationError("شروع هفته باید شنبه باشد")
            if record.start_date < fields.Date.today() or record.end_date < fields.Date.today():
                raise models.ValidationError("شما نم توانید تاریخ گذشته را انتخاب کنید")
            if existing_week:
                raise models.ValidationError("هفته انتخاب شده از قبل وجود دارد .")
