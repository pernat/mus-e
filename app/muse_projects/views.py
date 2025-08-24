from django.http import HttpResponse
from django.template import loader
from .models import Project, ProjectSetting


def projects(request):
    # result = any_http_request.delay(metric_name="Atlassian Vulnerabilities")

    template = loader.get_template("muse_projects/projects.html")
    app_list = ProjectSetting.objects.all()
    print(app_list)
    if app_list.count() == 0:
        context = {
            "app_list_count": 0,
            "vulnerabilities": 0,
        }
    else:
        context = {
            "project_list": app_list,
            "project_list_count": len(app_list),
            
        }
    return HttpResponse(template.render(context, request))
