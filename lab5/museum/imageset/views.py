from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from .models import Image, Rectangle, UserToImage
from .forms import RectangleForm


def render_svg(image_width, image_height, rectangles):
    svg = f'<svg width="{image_width}" height="{image_height}" xmlns="http://www.w3.org/2000/svg">'

    for rect in rectangles:
        x, y, width, height, color = [rect.X, rect.Y, rect.width, rect.height, rect.color]
        svg += f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" />'

    svg += '</svg>'
    return svg


def imageset_render(request):
    images = Image.objects.all()

    for image in images:
        print(image.name)

    context = {
        'images': images,
    }

    return render(request, "imageset/imageset.html", context)


def image_render(request, pk):
    image = get_object_or_404(Image, pk=pk)
    rectangles = Rectangle.objects.filter(image=image)

    form = RectangleForm()

    svg_image = render_svg(image.width, image.height, rectangles)

    if request.method == 'POST':
        form = RectangleForm(request.POST)

        if form.is_valid():
            rectangle = form.save(commit=False)

            setattr(rectangle, "image", image)
            rectangle.save()

            return redirect('imageset:image_render', pk=pk)

    can_edit = False

    if request.user.is_authenticated:
        userToImage = UserToImage.objects.filter(image=image, user=request.user)
        can_edit = request.user.is_superuser or userToImage

    context = {
        'image': image,
        'rectangles': rectangles,
        'form': form,
        'can_edit': can_edit,
        'svg_image': svg_image,
    }

    return render(request, "imageset/image.html", context)


def delete_rectangle(request, pk):
    rectangle = get_object_or_404(Rectangle, pk=pk)
    rectangle.delete()

    return redirect('imageset:imageset_render')

def create_rectangle(request):
    context = {}

    return render(request, '')

