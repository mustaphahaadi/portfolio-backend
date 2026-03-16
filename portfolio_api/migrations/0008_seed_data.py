from django.db import migrations


def seed_data(apps, schema_editor):
    Profile = apps.get_model('portfolio_api', 'Profile')
    Project = apps.get_model('portfolio_api', 'Project')
    Tool = apps.get_model('portfolio_api', 'Tool')
    Experience = apps.get_model('portfolio_api', 'Experience')
    Education = apps.get_model('portfolio_api', 'Education')
    Service = apps.get_model('portfolio_api', 'Service')
    Testimonial = apps.get_model('portfolio_api', 'Testimonial')
    Certification = apps.get_model('portfolio_api', 'Certification')

    # Skip if data already exists
    if Profile.objects.exists():
        return

    # --- Profile ---
    Profile.objects.create(
        name="Mustapha Haadi Bugnaba",
        roles=["DevOps Engineer", "Cloud Architect", "Infrastructure Specialist"],
        bio=(
            "I architect and automate cloud infrastructure, build robust CI/CD pipelines, "
            "and orchestrate containers at scale. Passionate about reliability, scalability, "
            "and the art of keeping systems running smoothly. AWS, Docker, Kubernetes, "
            "Terraform — I speak fluent infrastructure."
        ),
    )

    # --- Projects ---
    Project.objects.bulk_create([
        Project(
            number="01",
            title="Blockchain-Based Medical Records System (EmersBlock)",
            description=(
                "A blockchain-based system for secure and efficient medical record management. "
                "This is my final year project at KsTU. I'm currently working on it."
            ),
            icon="fas fa-hospital",
        ),
        Project(
            number="02",
            title="School Management System",
            description=(
                "A comprehensive platform for managing school operations, including student "
                "enrollment, attendance, and grading. It is for basic school management."
            ),
            icon="fas fa-briefcase",
        ),
        Project(
            number="03",
            title="SaaS Cybersecurity Platform (CyberRest)",
            description=(
                "A SaaS platform for cybersecurity solutions, including threat detection, "
                "vulnerability assessment, and incident response."
            ),
            icon="fas fa-shield-alt",
        ),
    ])

    # --- Tools ---
    Tool.objects.bulk_create([
        Tool(name="Docker",         icon="fab fa-docker",       version="24.0.7", status="expert"),
        Tool(name="Kubernetes",     icon="fas fa-dharmachakra", version="1.29",   status="proficient"),
        Tool(name="AWS",            icon="fab fa-aws",          version="cli-2.x",status="expert"),
        Tool(name="Terraform",      icon="fas fa-cubes",        version="1.7.x",  status="proficient"),
        Tool(name="Linux",          icon="fab fa-linux",        version="6.x",    status="expert"),
        Tool(name="Git",            icon="fab fa-git-alt",      version="2.43",   status="expert"),
        Tool(name="Python",         icon="fab fa-python",       version="3.12",   status="expert"),
        Tool(name="JavaScript",     icon="fab fa-js",           version="ES2024", status="proficient"),
        Tool(name="React",          icon="fab fa-react",        version="18.x",   status="proficient"),
        Tool(name="GitHub Actions", icon="fab fa-github",       version="v4",     status="proficient"),
        Tool(name="Jenkins",        icon="fas fa-cogs",         version="2.4x",   status="proficient"),
        Tool(name="Node.js",        icon="fab fa-node",         version="20.x",   status="proficient"),
    ])

    # --- Experience ---
    Experience.objects.bulk_create([
        Experience(
            company="ReStart Digital / Kumasi",
            position="Co-Founder & CEO",
            year="2024-Present",
            description=(
                "A startup building innovative software solutions, making technical decisions, "
                "and driving innovation in software solutions"
            ),
            icon="fas fa-users-cog",
        ),
        Experience(
            company="Khoders World - KsTU / Campus Club",
            position="Former President & Tutor",
            year="2022-Present",
            description=(
                "Mentoring beginner programmers, making technical decisions, and driving "
                "innovation in software solutions."
            ),
            icon="fas fa-laptop-code",
        ),
        Experience(
            company="IRID, KsTU",
            position="Research Associate",
            year="May - Oct, 2025",
            description=(
                "Led front-end development for multiple projects, implemented modern JavaScript "
                "frameworks, and optimized web performance."
            ),
            icon="fas fa-chart-line",
        ),
        Experience(
            company="Code Masters / London",
            position="Full Stack Developer",
            year="2019-2020",
            description=(
                "Designed and developed full-stack applications, implemented REST APIs, "
                "and managed database systems."
            ),
            icon="fas fa-layer-group",
        ),
    ])

    # --- Education ---
    Education.objects.bulk_create([
        Education(
            year="2021 – 2025",
            institution="Kumasi Technical University",
            description=(
                "Bachelor's degree in Computer Technology with a focus on software engineering "
                "and web development."
            ),
            location="Kumasi, Ghana",
        ),
        Education(
            year="2017 – 2020",
            institution="Ghanaian-German Snr High",
            description="A pure general science with biology, chemistry, physics and elective maths.",
            location="Tepa, Ghana",
        ),
    ])

    # --- Services ---
    Service.objects.bulk_create([
        Service(
            icon="fas fa-cloud",
            title="Cloud Infrastructure",
            description=(
                "Designing and managing cloud infrastructure on AWS and GCP. Implementing IaC "
                "with Terraform and CloudFormation for reproducible, scalable environments."
            ),
        ),
        Service(
            icon="fab fa-docker",
            title="Container Orchestration",
            description=(
                "Building and orchestrating containerized applications with Docker and Kubernetes. "
                "Implementing service meshes, auto-scaling, and zero-downtime deployments."
            ),
        ),
        Service(
            icon="fas fa-code-branch",
            title="CI/CD Pipeline Engineering",
            description=(
                "Architecting end-to-end CI/CD pipelines with Jenkins, GitHub Actions, and "
                "GitLab CI. Automating testing, building, and deployment workflows for rapid delivery."
            ),
        ),
    ])

    # --- Testimonials ---
    Testimonial.objects.bulk_create([
        Testimonial(
            name="Prof. Smart A. Sarpong",
            position="Director, IRID-KsTU",
            text=(
                "Haadi is one of the very best young guys that worked with me at IRID. "
                "He doesn't talk much but always ready to learn"
            ),
            avatar="https://randomuser.me/api/portraits/men/1.jpg",
        ),
        Testimonial(
            name="Hope Nelson Decardi",
            position="Co-Founder ReStartDigital",
            text=(
                "Haadi is a cool guy. Though he is not technically good than me. But the rare "
                "thing about him is that he is always ready to learn and improve himself. He is "
                "a great team player and always brings positive energy to the team."
            ),
            avatar="https://randomuser.me/api/portraits/men/2.jpg",
        ),
        Testimonial(
            name="Madam Diana Owusu",
            position="Register, IRID-KsTU",
            text=(
                "Haadi is a dedicated and hardworking individual. He always strives to deliver "
                "the best results and is not afraid to take on challenges."
            ),
            avatar="https://randomuser.me/api/portraits/men/3.jpg",
        ),
    ])

    # --- Certifications ---
    Certification.objects.bulk_create([
        Certification(
            name="AWS Certified Solutions Architect – Associate",
            organization="Amazon Web Services",
            issue_date="Jun 2023",
            expiration_date="Jun 2026",
            credential_id="AWS-12345678",
            credential_url="https://aws.amazon.com/certification/",
            icon="fab fa-aws",
        ),
        Certification(
            name="Certified Kubernetes Administrator (CKA)",
            organization="Linux Foundation",
            issue_date="Sep 2024",
            expiration_date="Sep 2027",
            credential_id="LF-98765432",
            credential_url="https://training.linuxfoundation.org/",
            icon="fas fa-dharmachakra",
        ),
    ])


def reverse_seed_data(apps, schema_editor):
    # Only reverses if these exact records were created by this migration.
    # Safe to run — won't touch any records added after the migration.
    Profile = apps.get_model('portfolio_api', 'Profile')
    Project = apps.get_model('portfolio_api', 'Project')
    Tool = apps.get_model('portfolio_api', 'Tool')
    Experience = apps.get_model('portfolio_api', 'Experience')
    Education = apps.get_model('portfolio_api', 'Education')
    Service = apps.get_model('portfolio_api', 'Service')
    Testimonial = apps.get_model('portfolio_api', 'Testimonial')
    Certification = apps.get_model('portfolio_api', 'Certification')

    Profile.objects.filter(name="Mustapha Haadi Bugnaba").delete()
    Project.objects.filter(number__in=["01", "02", "03"]).delete()
    Tool.objects.filter(name__in=[
        "Docker", "Kubernetes", "AWS", "Terraform", "Linux", "Git",
        "Python", "JavaScript", "React", "GitHub Actions", "Jenkins", "Node.js",
    ]).delete()
    Experience.objects.filter(company__in=[
        "ReStart Digital / Kumasi",
        "Khoders World - KsTU / Campus Club",
        "IRID, KsTU",
        "Code Masters / London",
    ]).delete()
    Education.objects.filter(institution__in=[
        "Kumasi Technical University",
        "Ghanaian-German Snr High",
    ]).delete()
    Service.objects.filter(title__in=[
        "Cloud Infrastructure",
        "Container Orchestration",
        "CI/CD Pipeline Engineering",
    ]).delete()
    Testimonial.objects.filter(name__in=[
        "Prof. Smart A. Sarpong",
        "Hope Nelson Decardi",
        "Madam Diana Owusu",
    ]).delete()
    Certification.objects.filter(credential_id__in=["AWS-12345678", "LF-98765432"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api', '0007_certification'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_code=reverse_seed_data),
    ]
