from django.db import models

class Smaagam(models.Model):
    smaagam_id = models.AutoField(primary_key=True)
    smaagam_name = models.CharField(max_length=30)

    def __str__(self):
        return self.smaagam_name

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=30)

    def __str__(self):
        return self.artist_name

class Kirtan(models.Model):
    kirtan_id = models.AutoField(primary_key=True)
    smaagam = models.ForeignKey(Smaagam, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    duration = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.artist.artist_name + ' From '+self.smaagam.smaagam_name

