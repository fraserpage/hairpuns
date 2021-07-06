from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class Hairpun: 
  def __init__(self, name, description, exists, streetview_link):
    self.name = name
    self.description = description
    self.exists = exists
    self.streetview_link = streetview_link

hairpuns = [
  Hairpun('Hairsay',"It's a good one",True,'https://www.google.com/maps/place/Hairsay/@43.6592451,-79.4141305,3a,37.5y,245.38h,92.89t/data=!3m6!1e1!3m4!1snwhTTXDehlKAk-pJQfVXeA!2e0!7i16384!8i8192!4m9!1m2!2m1!1shairsay!3m5!1s0x882b34f27ffbcd6b:0x85ac5dc1c48b1439!8m2!3d43.6591939!4d-79.414261!15sCgdoYWlyc2F5IgOIAQGSAQxiZWF1dHlfc2Fsb24'),
  Hairpun('Hair Today, Gone Tomorrow','I just thought of this pun and of course it exists. Does it still count if it is a hair removal service??',True,'https://www.google.com/maps/place/Hair+Today+Gone+Tomorrow/@43.8495569,-79.0490415,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipMl5UbHHinnukQUJ8qaoajv4XD_BBW-rlfyazQ!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipMl5UbHHinnukQUJ8qaoajv4XD_BBW-rlfyazQ%3Dw152-h86-k-no!7i4032!8i2269!4m9!1m2!2m1!1sHair+Today,+Gone+Tomorrow!3m5!1s0x89d4dfef9e40e74f:0xa4dedde605aaba7a!8m2!3d43.8495281!4d-79.0487577!15sChlIYWlyIFRvZGF5LCBHb25lIFRvbW9ycm93kgEhZWxlY3Ryb2x5c2lzX2hhaXJfcmVtb3ZhbF9zZXJ2aWNl'),
  Hairpun('Hair-ye, Hair-ye','Sadly I could find no real salon with this wonderful pun name',False, '')
]

def hairpuns_index(request):
  return render(request, 'hairpuns/index.html',{'hairpuns': hairpuns})