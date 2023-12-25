from django.shortcuts import render
from .services import get_all_rows

def photo_wall(request):
  photos = get_all_rows("sample")
  return render(request, 'photo_wall.html', {'photos': photos})