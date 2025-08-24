from django.conf import settings
# from jcp_h_apps.models import App


def app_version_context(request):
    return {"app_version": settings.APP_VERSION}


# def global_menu_context(request):
#     apps = App.objects.all().exclude(app_short_name__icontains="Atlassian API")
#     app_urls = {}
#     for app in apps:
#         app_urls[app.app_name] = app.id
#     data = {
#         "0": {
#             "name": "Home",
#             "url": "/",
#             "child": "",
#             "icon": "<i class='ti ti-yin-yang'></i>",
#         },
#         "1": {
#             "name": "Analytics",
#             "url": "/analytics",
#             "child": {"name": app_urls},
#             "icon": "<i class='ti ti-radar'></i>",
#         },
#         "2": {
#             "name": "Projects",
#             "url": "/projects",
#             "child": "",
#             "icon": "<i class='ti ti-folder-code'></i>",
#         },
#         "3": {
#             "name": "Dependency's",
#             "url": "/dependencys",
#             "child": "",
#             "icon": "<i class='ti ti-smoking'></i>",
#         },
#         "4": {
#             "name": "Customizations",
#             "url": "/customizations",
#             "child": "",
#             "icon": "<i class='ti ti-rectangular-prism-plus'></i>",
#         },
#         "5": {
#             "name": "SCM List",
#             "url": "/scm",
#             "child": "",
#             "icon": "<i class='ti ti-brand-bitbucket'></i>",
#         },
#     }
#     return {"menu_context": data}
