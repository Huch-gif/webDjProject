from django.http import HttpResponse


def home(request):
    """
    Главная страница
    """
    return HttpResponse("<h1>Главная страница</h1><p>Добро пожаловать на сайт!</p>")


def data(request):
    """
    Страница /data/
    """
    return HttpResponse("""
        <h1>Содержимое страницы data</h1>
        <p>Это страница с данными.</p>
    """)


def test(request):
    """
    Страница /test/
    """
    return HttpResponse("""
        <h1>Содержимое страницы test</h1>
        <p>Это тестовая страница.</p>
    """)