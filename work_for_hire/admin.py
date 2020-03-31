from django.contrib import admin
from .models import p_service, port_folio, orders, order_chat, buyer_request


admin.site.register(buyer_request)
admin.site.register(order_chat)
admin.site.register(orders)
admin.site.register(port_folio)
admin.site.register(p_service)