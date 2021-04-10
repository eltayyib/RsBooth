from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from django_countries.fields import CountryField

# from ckeditor.fields import RichTextField


# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("super_list", kwargs={"pk": self.pk})


class Employer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default="")
    company_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    goal = models.TextField(max_length=200)
    vision = models.TextField(max_length=200)
    about_us = models.TextField(max_length=200)
    logo = models.ImageField(upload_to="featured_image", blank=True)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    Status_CHOICES = (
        ("single", "SINGLE"),
        ("married", "MARRIED"),
        ("other", "OTHER"),
    )

    worktype_CHOICES = (
        ("full time", "FULL TIME"),
        ("part time", "PARTIME"),
        ("remote", "REMOTE"),
        ("contract", "CONTRACT"),
        ("internship", "INTERNShIP"),
    )

    Gender_CHOICES = (
        ("male", "MALE"),
        ("female", "FEMALE"),
        ("both", "BOTH"),
    )

    COUNTRIES = (
        ("GB", "United Kingdom"),
        ("AF", "Afghanistan"),
        ("AX", "Aland Islands"),
        ("AL", "Albania"),
        ("DZ", "Algeria"),
        ("AS", "American Samoa"),
        ("AD", "Andorra"),
        ("AO", "Angola"),
        ("AI", "Anguilla"),
        ("AQ", "Antarctica"),
        ("AG", "Antigua and Barbuda"),
        ("AR", "Argentina"),
        ("AM", "Armenia"),
        ("AW", "Aruba"),
        ("AU", "Australia"),
        ("AT", "Austria"),
        ("AZ", "Azerbaijan"),
        ("BS", "Bahamas"),
        ("BH", "Bahrain"),
        ("BD", "Bangladesh"),
        ("BB", "Barbados"),
        ("BY", "Belarus"),
        ("BE", "Belgium"),
        ("BZ", "Belize"),
        ("BJ", "Benin"),
        ("BM", "Bermuda"),
        ("BT", "Bhutan"),
        ("BO", "Bolivia"),
        ("BA", "Bosnia and Herzegovina"),
        ("BW", "Botswana"),
        ("BV", "Bouvet Island"),
        ("BR", "Brazil"),
        ("IO", "British Indian Ocean Territory"),
        ("BN", "Brunei Darussalam"),
        ("BG", "Bulgaria"),
        ("BF", "Burkina Faso"),
        ("BI", "Burundi"),
        ("KH", "Cambodia"),
        ("CM", "Cameroon"),
        ("CA", "Canada"),
        ("CV", "Cape Verde"),
        ("KY", "Cayman Islands"),
        ("CF", "Central African Republic"),
        ("TD", "Chad"),
        ("CL", "Chile"),
        ("CN", "China"),
        ("CX", "Christmas Island"),
        ("CC", "Cocos (Keeling) Islands"),
        ("CO", "Colombia"),
        ("KM", "Comoros"),
        ("CG", "Congo"),
        ("CD", "Congo, The Democratic Republic of the"),
        ("CK", "Cook Islands"),
        ("CR", "Costa Rica"),
        ("CI", "Cote d'Ivoire"),
        ("HR", "Croatia"),
        ("CU", "Cuba"),
        ("CY", "Cyprus"),
        ("CZ", "Czech Republic"),
        ("DK", "Denmark"),
        ("DJ", "Djibouti"),
        ("DM", "Dominica"),
        ("DO", "Dominican Republic"),
        ("EC", "Ecuador"),
        ("EG", "Egypt"),
        ("SV", "El Salvador"),
        ("GQ", "Equatorial Guinea"),
        ("ER", "Eritrea"),
        ("EE", "Estonia"),
        ("ET", "Ethiopia"),
        ("FK", "Falkland Islands (Malvinas)"),
        ("FO", "Faroe Islands"),
        ("FJ", "Fiji"),
        ("FI", "Finland"),
        ("FR", "France"),
        ("GF", "French Guiana"),
        ("PF", "French Polynesia"),
        ("TF", "French Southern Territories"),
        ("GA", "Gabon"),
        ("GM", "Gambia"),
        ("GE", "Georgia"),
        ("DE", "Germany"),
        ("GH", "Ghana"),
        ("GI", "Gibraltar"),
        ("GR", "Greece"),
        ("GL", "Greenland"),
        ("GD", "Grenada"),
        ("GP", "Guadeloupe"),
        ("GU", "Guam"),
        ("GT", "Guatemala"),
        ("GG", "Guernsey"),
        ("GN", "Guinea"),
        ("GW", "Guinea-Bissau"),
        ("GY", "Guyana"),
        ("HT", "Haiti"),
        ("HM", "Heard Island and McDonald Islands"),
        ("VA", "Holy See (Vatican City State)"),
        ("HN", "Honduras"),
        ("HK", "Hong Kong"),
        ("HU", "Hungary"),
        ("IS", "Iceland"),
        ("IN", "India"),
        ("ID", "Indonesia"),
        ("IR", "Iran, Islamic Republic of"),
        ("IQ", "Iraq"),
        ("IE", "Ireland"),
        ("IM", "Isle of Man"),
        ("IL", "Israel"),
        ("IT", "Italy"),
        ("JM", "Jamaica"),
        ("JP", "Japan"),
        ("JE", "Jersey"),
        ("JO", "Jordan"),
        ("KZ", "Kazakhstan"),
        ("KE", "Kenya"),
        ("KI", "Kiribati"),
        ("KP", "Korea, Democratic People's Republic of"),
        ("KR", "Korea, Republic of"),
        ("KW", "Kuwait"),
        ("KG", "Kyrgyzstan"),
        ("LA", "Lao People's Democratic Republic"),
        ("LV", "Latvia"),
        ("LB", "Lebanon"),
        ("LS", "Lesotho"),
        ("LR", "Liberia"),
        ("LY", "Libyan Arab Jamahiriya"),
        ("LI", "Liechtenstein"),
        ("LT", "Lithuania"),
        ("LU", "Luxembourg"),
        ("MO", "Macao"),
        ("MK", "Macedonia, The Former Yugoslav Republic of"),
        ("MG", "Madagascar"),
        ("MW", "Malawi"),
        ("MY", "Malaysia"),
        ("MV", "Maldives"),
        ("ML", "Mali"),
        ("MT", "Malta"),
        ("MH", "Marshall Islands"),
        ("MQ", "Martinique"),
        ("MR", "Mauritania"),
        ("MU", "Mauritius"),
        ("YT", "Mayotte"),
        ("MX", "Mexico"),
        ("FM", "Micronesia, Federated States of"),
        ("MD", "Moldova"),
        ("MC", "Monaco"),
        ("MN", "Mongolia"),
        ("ME", "Montenegro"),
        ("MS", "Montserrat"),
        ("MA", "Morocco"),
        ("MZ", "Mozambique"),
        ("MM", "Myanmar"),
        ("NA", "Namibia"),
        ("NR", "Nauru"),
        ("NP", "Nepal"),
        ("NL", "Netherlands"),
        ("AN", "Netherlands Antilles"),
        ("NC", "New Caledonia"),
        ("NZ", "New Zealand"),
        ("NI", "Nicaragua"),
        ("NE", "Niger"),
        ("NG", "Nigeria"),
        ("NU", "Niue"),
        ("NF", "Norfolk Island"),
        ("MP", "Northern Mariana Islands"),
        ("NO", "Norway"),
        ("OM", "Oman"),
        ("PK", "Pakistan"),
        ("PW", "Palau"),
        ("PS", "Palestinian Territory, Occupied"),
        ("PA", "Panama"),
        ("PG", "Papua New Guinea"),
        ("PY", "Paraguay"),
        ("PE", "Peru"),
        ("PH", "Philippines"),
        ("PN", "Pitcairn"),
        ("PL", "Poland"),
        ("PT", "Portugal"),
        ("PR", "Puerto Rico"),
        ("QA", "Qatar"),
        ("RE", "Reunion"),
        ("RO", "Romania"),
        ("RU", "Russian Federation"),
        ("RW", "Rwanda"),
        ("BL", "Saint Barthelemy"),
        ("SH", "Saint Helena"),
        ("KN", "Saint Kitts and Nevis"),
        ("LC", "Saint Lucia"),
        ("MF", "Saint Martin"),
        ("PM", "Saint Pierre and Miquelon"),
        ("VC", "Saint Vincent and the Grenadines"),
        ("WS", "Samoa"),
        ("SM", "San Marino"),
        ("ST", "Sao Tome and Principe"),
        ("SA", "Saudi Arabia"),
        ("SN", "Senegal"),
        ("RS", "Serbia"),
        ("SC", "Seychelles"),
        ("SL", "Sierra Leone"),
        ("SG", "Singapore"),
        ("SK", "Slovakia"),
        ("SI", "Slovenia"),
        ("SB", "Solomon Islands"),
        ("SO", "Somalia"),
        ("ZA", "South Africa"),
        ("GS", "South Georgia and the South Sandwich Islands"),
        ("ES", "Spain"),
        ("LK", "Sri Lanka"),
        ("SD", "Sudan"),
        ("SR", "Suriname"),
        ("SJ", "Svalbard and Jan Mayen"),
        ("SZ", "Swaziland"),
        ("SE", "Sweden"),
        ("CH", "Switzerland"),
        ("SY", "Syrian Arab Republic"),
        ("TW", "Taiwan, Province of China"),
        ("TJ", "Tajikistan"),
        ("TZ", "Tanzania, United Republic of"),
        ("TH", "Thailand"),
        ("TL", "Timor-Leste"),
        ("TG", "Togo"),
        ("TK", "Tokelau"),
        ("TO", "Tonga"),
        ("TT", "Trinidad and Tobago"),
        ("TN", "Tunisia"),
        ("TR", "Turkey"),
        ("TM", "Turkmenistan"),
        ("TC", "Turks and Caicos Islands"),
        ("TV", "Tuvalu"),
        ("UG", "Uganda"),
        ("UA", "Ukraine"),
        ("AE", "United Arab Emirates"),
        ("US", "United States"),
        ("UM", "United States Minor Outlying Islands"),
        ("UY", "Uruguay"),
        ("UZ", "Uzbekistan"),
        ("VU", "Vanuatu"),
        ("VE", "Venezuela"),
        ("VN", "Viet Nam"),
        ("VG", "Virgin Islands, British"),
        ("VI", "Virgin Islands, U.S."),
        ("WF", "Wallis and Futuna"),
        ("EH", "Western Sahara"),
        ("YE", "Yemen"),
        ("ZM", "Zambia"),
        ("ZW", "Zimbabwe"),
    )

    # PERSONAL INFOMATION
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="employee"
    )
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=Gender_CHOICES, default="")
    status = models.CharField(max_length=100, choices=Status_CHOICES, default="")
    age = models.PositiveBigIntegerField(blank="True", null="True")
    nationality = models.CharField(max_length=100, choices=COUNTRIES, default="")
    # EDUCATIONAL BACKGROUND
    highest_qualifications = models.CharField(max_length=100, default="")
    institute_Names = models.CharField(max_length=100, default="")
    graduted_years = models.CharField(max_length=100, default="")
    grades = models.CharField(max_length=100, default="")
    # WORK EXPERIENCE
    job_title = models.CharField(max_length=100, default="")
    compnay_name = models.CharField(max_length=100, default="")
    monthly_salary = models.CharField(max_length=100, default="")
    work_type = models.CharField(max_length=100, choices=worktype_CHOICES, default="")
    start_date = models.CharField(max_length=100, default="")
    end_date = models.CharField(max_length=100, default="")
    job_responsibility = models.TextField(default="")
    career_objective = models.TextField(default="")
    cv = models.FileField(upload_to="featured_file", blank=True, default="")
    picture = models.ImageField(upload_to="featured_image", blank=True, default="")

    def __str__(self):
        return self.firstname


class CreateJob(models.Model):

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, default="", related_name="createjob"
    )
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    no_of_vacancy = models.CharField(max_length=100, default="")
    company_logo = models.ImageField(upload_to="featured_image", blank=True)
    category = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=100, default="")
    job_type = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=500, default="")
    address = models.CharField(max_length=100)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("home")


class Application(models.Model):
    job_id = models.ForeignKey(
        CreateJob, related_name="application", on_delete=models.CASCADE
    )
    employer_id = models.CharField(
        max_length=100
    )
    employee_id = models.ForeignKey(
        CustomUser, related_name="application", on_delete=models.CASCADE
    )
    date_applied = models.DateTimeField(default=timezone.now)
    openings_position = models.DateTimeField

    def __str__(self):
        return self.job_title


class Location(models.Model):
    job_by_location    = models.CharField(max_length=200)

    def __str__(self):
        return self.job_by_location 
   
    def get_absolute_url(self):
        return reverse("super_list", kwargs={"pk": self.pk})


class Contact(models.Model):
    name = models.CharField(max_length = 128)
    email = models.CharField(max_length = 264, unique = True)
    phone_number = models.CharField(max_length = 128)
    message = models.TextField()


    def __str__(self):
        return self.name 

    
    def get_absolute_url(self):

        return reverse('contact',)