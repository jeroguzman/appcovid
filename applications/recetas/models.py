from django.db import models
from django.conf import settings
# import qrcode
# from io import BytesIO
# from django.core.files import File
# from PIL import Image, ImageDraw
from applications.users.models import Paciente

# Create your models here.
class Receta(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    contenido = models.TextField()
    # qr_code = models.ImageField(upload_to="static/img/recetas/qr", blank=True)

    # def save(self, *args, **kwargs):
    #     qrcode_img = qrcode.make(
    #         self.id, 
    #         self.doctor, 
    #         self.paciente, 
    #         self.fecha, 
    #         self.contenido
    #     )
    #     canvas = Image.new('RGB', (290, 290), 'white')
    #     draw = ImageDraw.Draw(canvas)
    #     canvas.paste(qrcode_img)
    #     fname = f'qr_code-{self.id}.png'
    #     buffer = BytesIO()
    #     canvas.save(buffer, 'PNG')
    #     self.qr_code.save(fname, File(buffer), save=False)
    #     canvas.close()
    #     super().save(*args, **kwargs)
