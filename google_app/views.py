from django.shortcuts import render, redirect
from django.http import JsonResponse
from .services import get_all_rows, create_row, update_row, delete_row

def photo_wall(request):
  """
  Renders a template that displays all photos from the Google Sheet.
  """
  photos = get_all_rows("sample")
  return render(request, 'photo_wall.html', {'photos': photos})

def photo_create(request):
  """
  Creates a new photo entry in the Google Sheet based on the request data.
  """
  if request.method == "POST":
    data = request.POST
    create_row("sample", data=data)
    return redirect("photo_wall")
  else:
    return render(request, 'photo_create.html')

def photo_update(request, row):
  """
  Updates an existing photo entry in the Google Sheet based on the request data and row number.
  """
  if request.method == "POST":
    data = request.POST
    update_row("sample", row=row, data=data)
    return redirect("photo_wall")
  else:
    photos = get_all_rows("sample")
    photo = photos[row - 2] # row - 2 because the first row is the header and the index starts from 0
    return render(request, 'photo_update.html', {'photo': photo, 'row': row})

def photo_delete(request, row):
  """
  Deletes an existing photo entry from the Google Sheet based on the row number.
  """
  if request.method == "POST":
    delete_row("sample", row=row)
    return redirect("photo_wall")
  else:
    photos = get_all_rows("sample")
    photo = photos[row - 2] # row - 2 because the first row is the header and the index starts from 0
    return render(request, 'photo_delete.html', {'photo': photo, 'row': row})

def photo_api(request):
  """
  Returns a JSON response with all photos from the Google Sheet.
  """
  photos = get_all_rows("sample")
  return JsonResponse(photos, safe=False)