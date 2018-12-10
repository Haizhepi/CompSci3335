from import_export import resources
from .models import Course, Section


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course