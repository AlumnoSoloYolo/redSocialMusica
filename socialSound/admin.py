from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Album)
admin.site.register(Cancion)
admin.site.register(Comentario)
admin.site.register(Seguidores)
admin.site.register(Playlist)
admin.site.register(Like)
admin.site.register(Etiqueta)
admin.site.register(Guardado)
admin.site.register(MensajePrivado)
admin.site.register(Reporte)


