from django.db import models
# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre")
    subtitle =models.CharField(max_length=200, verbose_name="Apellido")
    content = models.TextField(verbose_name="Contenido")
    
    image = models.ImageField(verbose_name="Imagen", upload_to = "services")
    url1 = models.URLField(verbose_name="Twitter", max_length=200, null=True, blank=True)
    url2 = models.URLField(verbose_name="Facebook", max_length=200, null=True, blank=True)
    url3 = models.URLField(verbose_name="Instagram", max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated =models.DateTimeField(auto_now =True, verbose_name="Fecha de actualización")
    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personales"
        ordering = ["-created"]
        
    def __str__(self):
        return self.title
            