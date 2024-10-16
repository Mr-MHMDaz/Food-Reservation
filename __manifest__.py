
{
    'name': 'Foodreservation',
    'version': '1.0.0',
    'category': 'تمرین',
    'author': 'Mr.Food.Lover',
    'summary': ' انتخاب روزانه نهار کارمندان شرکت ',
    'description': "",
    'website': 'https://www.FoodLovers.ir',
    'depends': [ 'mail'
    ],
    'data': [
    'security/record_rules.xml',
    'views/users.xml',
    'views/weeks.xml',
    'views/days.xml',
    'views/guest.xml',
    'views/reservation_menu.xml',
    'views/food_reservation_view.xml',
    'security/ir.model.access.csv',

    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence' : -99999,

}
