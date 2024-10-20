# redSocialMusica
        # Definir en qué consistirá mi página Web:

SocialSound es una aplicación basada en una red social para amantes de la música. La plataforma permite que los usuarios hacer login en su cuenta privada; puedan añadir su propia material; o descubrir y compartir distintos discos y canciones. Un usuario puede seguir a otros usuarios y ver las publicaciones de canciones y discos que sube o comparte en su feed. 

El usuario tiene un perfil personalizable que el resto de usuarios podrá ver.

Los usuarios pueden interactuar con otros usuarios por medio de likes, comentarios en publicaciones o mensajes directos. Además, los usuarios pueden guardar distintas canciones y añadirlas a playlists personalizadas.

        #  debe especificarse en que consiste cada modelo, cada atributo y cada parámetro usado. Y el esquema de modelo entidad-relación.


1. Modelo Usuario
Descripción: Representa a los usuarios de la plataforma.
Atributos:
nombre_usuario: CharField (máx. 100 caracteres) - Nombre único del usuario.
password: CharField (máx. 100 caracteres) - Contraseña del usuario (almacenada de forma encriptada).
bio: TextField (opcional) - Biografía del usuario.
ciudad: CharField (máx. 150 caracteres) - Ciudad del usuario.
foto_perfil: ImageField (opcional) - Imagen de perfil del usuario.
fecha_nac: DateField - Fecha de nacimiento del usuario.

2. Modelo Seguidores
Descripción: Representa la relación de seguimiento entre los usuarios.
Atributos:
seguidor: ForeignKey a Usuario - Usuario que sigue a otro.
seguido: ForeignKey a Usuario - Usuario que es seguido.
fecha_inicio: DateTimeField - Fecha en que se inició el seguimiento.

3. Modelo Album
Descripción: Representa un álbum musical.
Atributos:
titulo: CharField (máx. 200 caracteres) - Título del álbum.
artista: CharField (máx. 200 caracteres) - Artista del álbum.
usuario: ForeignKey a Usuario - Usuario que crea el álbum.
fecha_lanzamiento: DateField - Fecha de lanzamiento del álbum.
portada: ImageField (opcional) - Portada del álbum.
descripcion: TextField (opcional) - Descripción del álbum.
reposts: ManyToManyField a Usuario (opcional) - Usuarios que han compartido el álbum.

4. Modelo DetalleAlbum
Descripción: Contiene información adicional sobre un álbum.
Atributos:
album: OneToOneField a Album - Álbum asociado.
productor: CharField (máx. 200 caracteres) - Productor del álbum.
estudio_grabacion: CharField (máx. 200 caracteres, opcional) - Estudio donde se grabó el álbum.
numero_pistas: PositiveIntegerField - Número de pistas en el álbum.
sello_discografico: CharField (máx. 100 caracteres, opcional) - Sello discográfico del álbum.
5. Modelo EstadisticasAlbum

Descripción: Contiene estadísticas de un álbum.
Atributos:
album: OneToOneField a Album - Álbum asociado.
reproducciones: PositiveIntegerField (valor por defecto 0) - Número de reproducciones del álbum.
likes: PositiveIntegerField (valor por defecto 0) - Número de "me gusta" del álbum.
comentarios: PositiveIntegerField (valor por defecto 0) - Número de comentarios en el álbum.

6. Modelo Cancion
Descripción: Representa una canción musical.
Atributos:
etiqueta: CharField (máx. 50 caracteres) - Categoría de la canción (ej. rock, pop).
titulo: CharField (máx. 200 caracteres) - Título de la canción.
artista: CharField (máx. 100 caracteres) - Artista de la canción.
archivo_audio: FileField - Archivo de audio de la canción.
portada: ImageField (opcional) - Portada de la canción.
fecha_subida: DateTimeField (valor por defecto: hora actual) - Fecha en que se subió la canción.
usuario: ForeignKey a Usuario - Usuario que subió la canción.
album: ForeignKey a Album (opcional) - Álbum al que pertenece la canción.
likes: ManyToManyField a Usuario (opcional) - Usuarios que le han dado "me gusta" a la canción.
reposts: ManyToManyField a Usuario (opcional) - Usuarios que han compartido la canción.

7. Modelo DetalleCancion
Descripción: Contiene información adicional sobre una canción.
Atributos:
cancion: OneToOneField a Cancion - Canción asociada.
letra: TextField (opcional) - Letra de la canción.
creditos: TextField (opcional) - Créditos de la canción.
duracion: DurationField - Duración de la canción.
idioma: CharField (máx. 50 caracteres, opcional) - Idioma de la canción.

8. Modelo Playlist
Descripción: Representa una lista de reproducción de canciones.
Atributos:
nombre: CharField (máx. 100 caracteres) - Nombre de la lista de reproducción.
descripcion: TextField (máx. 255 caracteres) - Descripción de la lista de reproducción.
fecha_creacion: DateTimeField (valor por defecto: hora actual) - Fecha de creación de la lista de reproducción.
usuario: ForeignKey a Usuario - Usuario que creó la lista de reproducción.
canciones: ManyToManyField a Cancion (a través de CancionPlaylist) - Canciones en la lista de reproducción.
publica: BooleanField (valor por defecto: True) - Indica si la lista de reproducción es pública.

9. Modelo CancionPlaylist
Descripción: Tabla intermedia que relaciona Playlist y Cancion.
Atributos:
cancion: ForeignKey a Cancion - Canción en la lista de reproducción.
playlist: ForeignKey a Playlist - Lista de reproducción que contiene la canción.
orden: PositiveIntegerField (valor por defecto: 0) - Orden de la canción en la lista de reproducción.
fecha_agregada: DateTimeField (valor por defecto: hora actual) - Fecha en que se agregó la canción a la lista de reproducción.

10. Modelo Like
Descripción: Representa los "me gusta" dados a las canciones.
Atributos:
usuario: ForeignKey a Usuario - Usuario que dio "me gusta".
cancion: ForeignKey a Cancion - Canción a la que se le dio "me gusta".
fecha_like: DateTimeField (valor por defecto: hora actual) - Fecha en que se dio "me gusta".

Tipos de Atributos:
CharField: Se usa para cadenas cortas (nombres, títulos).
TextField: Se usa para cadenas más largas (biografías, letras).
DateField: Se usa para fechas.
DateTimeField: Se usa para fechas y horas.
PositiveIntegerField: Se usa para números enteros positivos (número de pistas, likes).
DurationField: Se usa para representar duraciones de tiempo.
ImageField: Se usa para cargar imágenes.
FileField: Se usa para cargar archivos (audio).
BooleanField: Se usa para valores verdadero/falso.
ManyToManyField: Se usa para relaciones de muchos a muchos.


        # Esquema de Modelo Entidad-Relación (ERD):


Relación Usuario

Relación 1 a N con Seguidores: Un usuario puede seguir a muchos otros usuarios (relación "seguidor").
Relación 1 a N con Album: Un usuario puede crear muchos álbumes.
Relación 1 a N con Cancion: Un usuario puede subir muchas canciones.
Relación N a N con Cancion a través de Like: Un usuario puede dar "me gusta" a muchas canciones, y una canción puede tener "me gusta" de muchos usuarios.
Relación N a N con Album a través de reposts: Un usuario puede repostear muchos álbumes, y un álbum puede ser reposted por muchos usuarios.
Relación N a N con Cancion a través de reposts: Un usuario puede repostear muchas canciones, y una canción puede ser reposted por muchos usuarios.
Relación 1 a N con Playlist: Un usuario puede crear muchas listas de reproducción.
Relación N a N con Cancion a través de Guardado: Un usuario puede guardar muchas canciones, y una canción puede ser guardada por muchos usuarios.


Relación Seguidores

Relación N a 1 con Usuario (seguidor): Cada relación de seguimiento tiene un usuario que es el "seguidor".
Relación N a 1 con Usuario (seguido): Cada relación de seguimiento tiene un usuario que es "seguido".
Relación única entre los usuarios: Un usuario no puede seguir al mismo usuario más de una vez (garantizado por unique_together).


Relación Album

Relación 1 a 1 con DetalleAlbum: Cada álbum tiene detalles específicos relacionados con él.
Relación 1 a 1 con EstadisticasAlbum: Cada álbum tiene estadísticas específicas relacionadas con él.
Relación 1 a N con Cancion: Un álbum puede contener muchas canciones.
Relación N a N con Usuario a través de reposts: Un álbum puede ser reposted por muchos usuarios, y un usuario puede repostear muchos álbumes.

Relación DetalleAlbum

Relación 1 a 1 con Album: Cada detalle del álbum está vinculado a un álbum específico.
Relación EstadisticasAlbum
Relación 1 a 1 con Album: Cada estadística del álbum está vinculada a un álbum específico.
Relación Cancion
Relación N a 1 con Album: Cada canción pertenece a un álbum específico (opcional, ya que puede ser nulo).
Relación 1 a N con DetalleCancion: Cada canción puede tener detalles específicos relacionados con ella.
Relación N a N con Usuario a través de Like: Una canción puede ser "gustada" por muchos usuarios y un usuario puede gustar muchas canciones.
Relación N a N con Usuario a través de reposts: Una canción puede ser reposted por muchos usuarios y un usuario puede repostear muchas canciones.
Relación 1 a N con Comentario: Una canción puede tener muchos comentarios.


Relación DetalleCancion

Relación 1 a 1 con Cancion: Cada detalle de la canción está vinculado a una canción específica.


Relación Playlist

Relación 1 a N con Usuario: Una lista de reproducción pertenece a un usuario específico.
Relación N a N con Cancion a través de CancionPlaylist: Una lista de reproducción puede contener muchas canciones, y una canción puede estar en muchas listas de reproducción.


Relación CancionPlaylist

Relación N a 1 con Cancion: Cada entrada de la tabla intermedia se refiere a una canción específica.
Relación N a 1 con Playlist: Cada entrada de la tabla intermedia se refiere a una lista de reproducción específica.
Relación única (cancion, playlist): Una canción no puede aparecer más de una vez en la misma lista de reproducción.


Relación Like

Relación N a 1 con Usuario: Cada "me gusta" está asociado a un usuario específico.
Relación N a 1 con Cancion: Cada "me gusta" está asociado a una canción específica.
Relación única (usuario, cancion): Un usuario no puede dar "me gusta" a la misma canción más de una vez.


Relación Comentario

Relación N a 1 con Cancion: Cada comentario está asociado a una canción específica.
Relación N a 1 con Usuario: Cada comentario está asociado a un usuario específico.


Relación MensajePrivado

Relación N a 1 con Usuario (emisor): Cada mensaje privado tiene un emisor que es un usuario específico.
Relación N a 1 con Usuario (receptor): Cada mensaje privado tiene un receptor que es un usuario específico.


Relación Guardado

Relación N a 1 con Usuario: Cada canción guardada está asociada a un usuario específico.
Relación N a 1 con Cancion: Cada canción guardada está asociada a una canción específica.
Relación única (usuario, cancion): Un usuario no puede guardar la misma canción más de una vez.

