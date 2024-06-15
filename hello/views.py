from django.http import HttpResponse

def home(request):
    return HttpResponse("""<h1>My first App Django</h1><br />
                        Carlos Eduardo Laquine<br />
                        Cloud Computing & Site Reliability Engineering""")