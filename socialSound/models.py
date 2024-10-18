from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


# Modelo Usuario 
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  
    bio = models.TextField(blank=True)
    ciudad = models.CharField(max_length=150, blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True)
    fecha_nac = models.DateField()

        # Métodos para gestionar seguidores directamente desde el modelo intermedio
    def obtener_seguidores(self):
        return Seguidores.objects.filter(seguido=self)

    def obtener_seguidos(self):
        return Seguidores.objects.filter(seguidor=self)

    def __str__(self):
        return self.nombre_usuario
    
    
    # hasheo. Seguridad en password
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    

# modelo album
class Album(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    portada = models.ImageField(upload_to='album_portadas/', blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo


# Modelo de Canciones
class Cancion(models.Model):
    CATEGORIAS_CHOICES = [
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
        ('metal', 'Metal'),
        ('electronica', 'Electrónica'),
        ('pop', 'Pop'),
        ('hiphop', 'Hip-Hop'),
        ('reggae', 'Reggae'),
        ('blues', 'Blues'),
        ('classical', 'Clásica'),
        ('country', 'Country'),
        ('dance', 'Dance'),
        ('disco', 'Disco'),
        ('dubstep', 'Dubstep'),
        ('edm', 'EDM (Electronic Dance Music)'),
        ('funk', 'Funk'),
        ('gospel', 'Gospel'),
        ('grunge', 'Grunge'),
        ('hardrock', 'Hard Rock'),
        ('indie', 'Indie'),
        ('latin', 'Latina'),
        ('lofi', 'Lo-Fi'),
        ('opera', 'Ópera'),
        ('punk', 'Punk'),
        ('rnb', 'R&B (Rhythm and Blues)'),
        ('rap', 'Rap'),
        ('salsa', 'Salsa'),
        ('soul', 'Soul'),
        ('techno', 'Techno'),
        ('trance', 'Trance'),
        ('trap', 'Trap'),
        ('house', 'House'),
        ('ambient', 'Ambient'),
        ('acoustic', 'Acústica'),
        ('alternative', 'Alternativa'),
        ('chillout', 'Chillout'),
        ('drumandbass', 'Drum and Bass'),
        ('electro', 'Electro'),
        ('experimental', 'Experimental'),
        ('folk', 'Folk'),
        ('hardcore', 'Hardcore'),
        ('idm', 'IDM (Intelligent Dance Music)'),
        ('industrial', 'Industrial'),
        ('kpop', 'K-Pop'),
        ('metalcore', 'Metalcore'),
        ('newage', 'New Age'),
        ('noise', 'Noise'),
        ('progressiverock', 'Progressive Rock'),
        ('psytrance', 'Psytrance'),
        ('reggaeton', 'Reggaetón'),
        ('synthwave', 'Synthwave'),
        ('vaporwave', 'Vaporwave'),
        ('world', 'World Music'),
        ('ska', 'Ska'),
        ('tango', 'Tango'),
        ('grindcore', 'Grindcore'),
        ('postrock', 'Post-Rock'),
        ('drill', 'Drill'),
        ('shoegaze', 'Shoegaze'),
        ('glitch', 'Glitch'),
        ('breakbeat', 'Breakbeat'),
        ('emo', 'Emo'),
        ('christian', 'Cristiana'),
        ('jpop', 'J-Pop'),
        ('jrock', 'J-Rock'),
        ('futurebass', 'Future Bass'),
        ('progressivehouse', 'Progressive House'),
        ('moombahton', 'Moombahton'),
        ('dancehall', 'Dancehall'),
        ('dub', 'Dub'),
    ]
    etiqueta = models.CharField(
        max_length=50, 
        blank=False, 
        choices=CATEGORIAS_CHOICES
    )
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=100)
    duracion = models.DurationField()
    archivo_audio = models.FileField(upload_to='canciones/')
    portada = models.ImageField(upload_to='cancion_portadas/', blank=True)
    fecha_subida = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='canciones', null=True, blank=True)

    def __str__(self):
        return self.titulo



# Modelo de Comentarios
class Comentario(models.Model):
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.nombre_usuario} comentó en {self.cancion.titulo}'



# Modelo de Playlist
class Playlist(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.TextField(max_length=255)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    canciones = models.ManyToManyField(Cancion, through='CancionPlaylist', related_name='playlists')
    publica = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



# Modelo de Likes
class Like(models.Model):
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_like = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.usuario.nombre_usuario} le gustó {self.cancion.titulo}'



# Modelo de Mensajes Privados
class MensajePrivado(models.Model):
    emisor = models.ForeignKey(Usuario, related_name='emisor', on_delete=models.CASCADE)
    receptor = models.ForeignKey(Usuario, related_name='receptor', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f'Mensaje de {self.emisor.nombre_usuario} a {self.receptor.nombre_usuario}'



# Modelo de Seguidores
class Seguidores(models.Model):
    seguidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="seguidores_list")
    seguido = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='siguiendo_list')
    fecha_inicio = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('seguidor', 'seguido')

    def __str__(self):
        return f'{self.seguidor.nombre_usuario} sigue a {self.seguido.nombre_usuario}'  


# del modelo entidad relacion, la relación playlist contiene cancion crea una tabla intermedia:
class CancionPlaylist(models.Model):
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(default=0)
    fecha_agregada = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('cancion', 'playlist')  # Evita duplicación de canciones en la misma playlist

    def __str__(self):
        return f'{self.cancion.titulo} en {self.playlist.nombre}'
    

# Modelo de canciones guardadas
class Guardado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    fecha_guardado = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ('usuario', 'cancion')  # Evita que un usuario guarde la misma canción más de una vez

    def __str__(self):
        return f'{self.usuario.nombre_usuario} guardó {self.cancion.titulo}'





















































