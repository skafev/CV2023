class CVinfo:
    '''Class for holding CV information.'''
    def __init__(self):
        '''Constructor for the class.'''
        self.title_cv = "Stanislav Kafev CV"
        self.name = "Stanislav Kafev"
        self.proffesion = "Software Engineer"
        self.bio = CVinfo._get_bio()
        self.country = "Sofia, Bulgaria"
        self.social_media = CVinfo._get_social_media()
        self.birthday = '05 Aug 1991'
        self.skills = CVinfo._get_skills_percentage()
        self.hobbies = CVinfo._get_hobbies()
        self.certificates = CVinfo._get_certificates()
        self.education = CVinfo._get_education()
        self.work_experience = CVinfo._get_work_experience()
        self.projects = CVinfo._get_projects()


    @staticmethod
    def _get_bio():
        msg = """
            Working in the IT industry with already 3y of experience and counting.
            Throughout my career I have honed my skills in Python, Django and Linux.
            In my journey, I am eager to push myself to understand where my limits are 
            and also to learn new stuff so i can expand my knowledge.
        """
        return msg

    @staticmethod
    def _get_social_media():
        return {
            'github': 'https://github.com/skafev',
            'linkedin': 'https://www.linkedin.com/in/stanislav-kafev/',
            'email': 'mailto:skafev@gmal.com',
            'phone':' tel:0883435666'
        }

    @staticmethod
    def _get_skills_percentage():
        return {
            'HTML/CSS' : '60',
            'Bash, Kornshell': '70',
            'Linux/Solaris': '60',
            'Twinscan': '40',
            'Django': '70',
            'MySQL': '60',
            'C++': '40',
            'Python': '80'
        }

    @staticmethod
    def _get_hobbies():
        return [
            'Computer Gaming',
            'Playing Football',
            'Playing Basketball',
            'Crossfit',
            'Supporting animal charity organizations'
        ]

    @staticmethod
    def _get_certificates():
        return [
            'Python OOP, Python Web',
            'Full Django path SoftUni',
            'MNKnowledge course',
            'Linux systems  administration',
            'Compromising platforms',
            'Complete Python Deep-Dive udemy course',
            'C++ internal Strypes course',
            'ASML internal courses',
            'DevOps internal Strypes academy'
        ]

    @staticmethod
    def _get_education():
        return {
            'Dimitar A. Tsenov Academy of Economics - Statistics and Econometry': '2011 - 2015'
        }

    @staticmethod
    def _get_work_experience():
        return {
            'Strypes': 'June 2022 - Present',
            'Bulgarian customs inspector': '2019- June 2022'
        }

    @staticmethod
    def _get_projects():
        return [
            'Currently the ones that are in my github repo'
        ]
