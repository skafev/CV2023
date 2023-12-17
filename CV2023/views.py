import html

from django.shortcuts import render
from CV2023.data import CVinfo


def data():
    cv_data = CVinfo()
    return {
        'title_CV': cv_data.title_cv,
        'Name': cv_data.name,
        'Profession': cv_data.proffesion,
        'Bio': cv_data.bio,
        'Country': cv_data.country,
        'Contact': cv_data.social_media,
        'Birthday': cv_data.birthday,
        'Skills': cv_data.skills,
        'Hobbies': cv_data.hobbies,
        'Certificates': cv_data.certificates,
        'Education':cv_data.education,
        'Work': cv_data.work_experience,
        'Projects': cv_data.projects,
    }

def index(request):
    return render(request, 'cv.html', data())
