from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from .models import About


def about_me(request):
    about_obj = None

    # If an About model exists, try to get the first record
    if About:
        try:
            about_obj = About.objects.first()
        except Exception:
            about_obj = None

    # If no model/record, provide a simple default object for the template
    if not about_obj:
        class _About:
            title = "About Matt"
            content = (
                "<p>Matt is a professional software developer with a passion for building reliable, "
                "user-centered web applications. He specializes in Python and Django for backend "
                "development, and uses modern frontend tools (HTML, CSS, JavaScript, and React) to "
                "deliver polished user experiences.</p>"
                "<p>With experience working on projects from small startups to larger products, Matt "
                "focuses on clean architecture, automated testing, and continuous delivery. He enjoys "
                "mentoring junior developers and contributing to open source.</p>"
                "<p>Key skills: Python, Django, REST APIs, SQL, Git, Docker, CI/CD, and responsive UI.</p>"
                "<p>Contact: matt@example.com</p>"
            )
            updated_on = timezone.now()
        about_obj = _About()

    return render(request, 'about/about.html', {"about": about_obj})