from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'nome', 'tel', 'dt_nasc')
    search_fields = ('id', )
    # list_filter = ('id',)
    list_per_page = 20


# class PointsAdmin(admin.ModelAdmin):
#     list_display = ('usuario',
#                     'point_1', 'point_2', 'point_3', 'point_4', 'point_5',
#                     'point_6', 'point_7', 'point_8', 'point_9', 'point_10',)
#     search_fields = ('id',)
#     list_per_page = 20


admin.site.register(Account, AccountAdmin)
# admin.site.register(Points, PointsAdmin)
