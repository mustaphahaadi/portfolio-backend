from django.db import migrations


def backfill_seed_data(apps, schema_editor):
    Profile = apps.get_model('portfolio_api', 'Profile')
    Project = apps.get_model('portfolio_api', 'Project')
    Tool = apps.get_model('portfolio_api', 'Tool')
    Experience = apps.get_model('portfolio_api', 'Experience')
    Education = apps.get_model('portfolio_api', 'Education')
    Service = apps.get_model('portfolio_api', 'Service')
    Testimonial = apps.get_model('portfolio_api', 'Testimonial')
    Certification = apps.get_model('portfolio_api', 'Certification')

    # Profile
    Profile.objects.get_or_create(
        name="Mustapha Haadi Bugnaba",
        defaults={
            "roles": ["DevOps Engineer", "Cloud Engineer", "Software Engineer", "CI/CD Specialist"],
            "bio": (
                "I architect and automate cloud infrastructure, build robust CI/CD pipelines, "
                "and orchestrate containers at scale. Passionate about reliability, scalability, "
                "and the art of keeping systems running smoothly. AWS, Docker, Kubernetes, "
                "Terraform — I speak fluent infrastructure."
            ),
        },
    )

    # Projects
    Project.objects.get_or_create(
        number="01",
        defaults={
            "title": "Blockchain-Based Medical Records System (EmersBlock)",
            "description": (
                "A blockchain-based system for secure and efficient medical record management. "
                "This is my final year project at KsTU. I'm currently working on it."
            ),
            "icon": "fas fa-hospital",
        },
    )
    Project.objects.get_or_create(
        number="02",
        defaults={
            "title": "School Management System",
            "description": (
                "A comprehensive platform for managing school operations, including student "
                "enrollment, attendance, and grading. It is for basic school management."
            ),
            "icon": "fas fa-briefcase",
        },
    )
    Project.objects.get_or_create(
        number="03",
        defaults={
            "title": "SaaS Cybersecurity Platform (CyberRest)",
            "description": (
                "A SaaS platform for cybersecurity solutions, including threat detection, "
                "vulnerability assessment, and incident response."
            ),
            "icon": "fas fa-shield-alt",
        },
    )

    # Tools
    tool_rows = [
        ("Docker", "fab fa-docker", "24.0.7", "expert"),
        ("Kubernetes", "fas fa-dharmachakra", "1.29", "proficient"),
        ("AWS", "fab fa-aws", "cli-2.x", "expert"),
        ("Terraform", "fas fa-cubes", "1.7.x", "proficient"),
        ("Linux", "fab fa-linux", "6.x", "expert"),
        ("Git", "fab fa-git-alt", "2.43", "expert"),
        ("Python", "fab fa-python", "3.12", "expert"),
        ("JavaScript", "fab fa-js", "ES2024", "proficient"),
        ("React", "fab fa-react", "18.x", "proficient"),
        ("GitHub Actions", "fab fa-github", "v4", "proficient"),
        ("Jenkins", "fas fa-cogs", "2.4x", "proficient"),
        ("Node.js", "fab fa-node", "20.x", "proficient"),
    ]
    for name, icon, version, status in tool_rows:
        Tool.objects.get_or_create(
            name=name,
            defaults={"icon": icon, "version": version, "status": status},
        )

    # Experience
    Experience.objects.get_or_create(
        company="ReStart Digital / Kumasi",
        position="Co-Founder & CEO",
        defaults={
            "year": "2024-Present",
            "description": (
                "A startup building innovative software solutions, making technical decisions, "
                "and driving innovation in software solutions"
            ),
            "icon": "fas fa-users-cog",
        },
    )
    Experience.objects.get_or_create(
        company="Khoders World - KsTU / Campus Club",
        position="Former President & Tutor",
        defaults={
            "year": "2022-Present",
            "description": (
                "Mentoring beginner programmers, making technical decisions, and driving "
                "innovation in software solutions."
            ),
            "icon": "fas fa-laptop-code",
        },
    )
    Experience.objects.get_or_create(
        company="IRID, KsTU",
        position="Research Associate",
        defaults={
            "year": "May - Oct, 2025",
            "description": (
                "Led front-end development for multiple projects, implemented modern JavaScript "
                "frameworks, and optimized web performance."
            ),
            "icon": "fas fa-chart-line",
        },
    )
    Experience.objects.get_or_create(
        company="Code Masters / London",
        position="Full Stack Developer",
        defaults={
            "year": "2019-2020",
            "description": (
                "Designed and developed full-stack applications, implemented REST APIs, "
                "and managed database systems."
            ),
            "icon": "fas fa-layer-group",
        },
    )

    # Education
    Education.objects.get_or_create(
        institution="Kumasi Technical University",
        year="2021 – 2025",
        defaults={
            "description": (
                "Bachelor's degree in Computer Technology with a focus on software engineering "
                "and web development."
            ),
            "location": "Kumasi, Ghana",
        },
    )
    Education.objects.get_or_create(
        institution="Ghanaian-German Snr High",
        year="2017 – 2020",
        defaults={
            "description": "A pure general science with biology, chemistry, physics and elective maths.",
            "location": "Tepa, Ghana",
        },
    )

    # Services
    Service.objects.get_or_create(
        title="Cloud Infrastructure",
        defaults={
            "icon": "fas fa-cloud",
            "description": (
                "Designing and managing cloud infrastructure on AWS and GCP. Implementing IaC "
                "with Terraform and CloudFormation for reproducible, scalable environments."
            ),
        },
    )
    Service.objects.get_or_create(
        title="Container Orchestration",
        defaults={
            "icon": "fab fa-docker",
            "description": (
                "Building and orchestrating containerized applications with Docker and Kubernetes. "
                "Implementing service meshes, auto-scaling, and zero-downtime deployments."
            ),
        },
    )
    Service.objects.get_or_create(
        title="CI/CD Pipeline Engineering",
        defaults={
            "icon": "fas fa-code-branch",
            "description": (
                "Architecting end-to-end CI/CD pipelines with Jenkins, GitHub Actions, and "
                "GitLab CI. Automating testing, building, and deployment workflows for rapid delivery."
            ),
        },
    )

    # Testimonials
    Testimonial.objects.get_or_create(
        name="Prof. Smart A. Sarpong",
        position="Director, IRID-KsTU",
        defaults={
            "text": (
                "Haadi is one of the very best young guys that worked with me at IRID. "
                "He doesn't talk much but always ready to learn"
            ),
            "avatar": "https://randomuser.me/api/portraits/men/1.jpg",
        },
    )
    Testimonial.objects.get_or_create(
        name="Hope Nelson Decardi",
        position="Co-Founder ReStartDigital",
        defaults={
            "text": (
                "Haadi is a cool guy. Though he is not technically good than me. But the rare "
                "thing about him is that he is always ready to learn and improve himself. He is "
                "a great team player and always brings positive energy to the team."
            ),
            "avatar": "https://randomuser.me/api/portraits/men/2.jpg",
        },
    )
    Testimonial.objects.get_or_create(
        name="Madam Diana Owusu",
        position="Register, IRID-KsTU",
        defaults={
            "text": (
                "Haadi is a dedicated and hardworking individual. He always strives to deliver "
                "the best results and is not afraid to take on challenges."
            ),
            "avatar": "https://randomuser.me/api/portraits/men/3.jpg",
        },
    )

    # Certifications
    Certification.objects.get_or_create(
        credential_id="AWS-12345678",
        defaults={
            "name": "AWS Certified Solutions Architect – Associate",
            "organization": "Amazon Web Services",
            "issue_date": "Jun 2023",
            "expiration_date": "Jun 2026",
            "credential_url": "https://aws.amazon.com/certification/",
            "icon": "fab fa-aws",
        },
    )
    Certification.objects.get_or_create(
        credential_id="LF-98765432",
        defaults={
            "name": "Certified Kubernetes Administrator (CKA)",
            "organization": "Linux Foundation",
            "issue_date": "Sep 2024",
            "expiration_date": "Sep 2027",
            "credential_url": "https://training.linuxfoundation.org/",
            "icon": "fas fa-dharmachakra",
        },
    )


def noop_reverse(apps, schema_editor):
    # Keep reverse as no-op to avoid deleting user-modified production content.
    return


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api', '0008_seed_data'),
    ]

    operations = [
        migrations.RunPython(backfill_seed_data, reverse_code=noop_reverse),
    ]
