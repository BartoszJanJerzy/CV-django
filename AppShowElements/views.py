from django.shortcuts import render
from .models import Kurs, Project
from .graphs.job_exp_graph import JobExperienceGraph
from .graphs.tasks_graph import TasksGraph
from .graphs.data_types_graph import DataTypesGraph
from .graphs.skills_graph import SkillsGraph



# Create your views here.
def ShowElements(request):
    kurs = Kurs.objects.all()
    project = Project.objects.all()

    graph_maker = JobExperienceGraph()
    experience_graph = graph_maker.get_graph()

    graph_maker = TasksGraph()
    task_graph = graph_maker.get_graph()

    graph_maker = DataTypesGraph()
    data_types_graph = graph_maker.get_graph()

    graph_maker = SkillsGraph()
    skills_graph = graph_maker.get_graph()

    context = {
        'kurs':kurs,
        'project':project,
        'exp_graph':experience_graph,
        'task_graph':task_graph,
        'data_types_graph':data_types_graph,
        'skills_graph':skills_graph
    }

    return render(request, 'index.html', context)



