from django.shortcuts import render


def index(request):
    name = 'Gold nugget'
    value = 1000.00

    context = {'locations': locations}

    return render(request, 'index.html', context)


class Location:
    def __init__(self, name, predators, num_restaurants, img_url):
        self.name = name
        self.predators= predators
        self.num_restaurants = num_restaurants
        self.img_url = img_url

locations = [
    Location("Fool's Falls, CO", 'Flash Floods', 0,
             'http://courseware.codeschool.com/try_django/images/fools-falls.jpg'),
    Location("Curly's Creek, NM", 'Rattle Snakes', 2,
             'http://courseware.codeschool.com/try_django/images/curlys-creek.jpg'),
    Location("The Delicate Arch, UT", 'Angry Chicken', 5,
             'http://courseware.codeschool.com/try_django/images/delicate-arch.jpg')
]