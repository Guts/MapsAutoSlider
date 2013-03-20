from modules import *

png = r'C:\Documents and Settings\Utilisateur\Bureau\img\densidad_mallas_pob_2007.png'
jpeg = r'C:\Documents and Settings\Utilisateur\Mes documents\Mes images\Illustrations Metadator\PourPortail\metadator_export_excel.jpg'

f = open(jpeg, 'rb')
tags = EXIF.process_file(f, details = False, stop_tag='ExifImageLength')

print tags.get('EXIF ExifImageWidth')
print tags.get('EXIF ExifImageLength')