# from datetime import datetime
# from events.models import Organiser, Student, StudentMaster, StudentBatch, AcademicKey
# from .models import  CdFossLanguages, Payee
# from .models import UserFossAccess, CdFossLanguages, Payee
# from training.models import Participant
GENDER_CHOICES = (
		('', '--- Gender ---'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', "Don't wish to disclose")
    )

PAY_FOR_CHOICES = (
	('S', 'Self'),
	('C', 'College'),
	('U', 'University'),
	('T', 'Corporate')
	)

PURPOSE = 'CdContent'

SIZE_CHOICES = (
    ('xs','XS'),
    ('s', 'S'),
    ('m','M'),
    ('l','L'),
    ('xl','XL'),
)  
ITEM_CHOICES = (
    ('tshirt','T-Shirt'),
) 
CURRENCY = (
    ('inr','INR'),
    ('usd','USD'),
) 
COUNTRY = (
	('India','India'),
	('USA','USA'),


	)


# def is_valid_subscription(expiry_date):
#     today = datetime.today().date()
#     return expiry_date >= today

# def is_organiser_insti_subscribed(user):
#     try:
#         academic_id = Organiser.objects.get(user=user).academic_id
#         expiry_date = AcademicKey.objects.filter(academic_id=academic_id).order_by('-expiry_date').first().expiry_date
#         if expiry_date:
#             return is_valid_subscription(expiry_date), expiry_date
#         return False, 'unsubscribed'
#     except Exception as e:
#         return False, 'unsubscribed'

# def is_student_insti_subscribed(user):
#     try:
#         student = Student.objects.get(user=user)
#         sm = StudentMaster.objects.get(student=student)
#         academic_id = StudentBatch.objects.get(id=sm.batch_id).academic_id
#         expiry_date = AcademicKey.objects.filter(academic_id=academic_id).order_by('-expiry_date').first().expiry_date
#         if expiry_date:
#             return is_valid_subscription(expiry_date), expiry_date
#         return False, 'unsubscribed'
#     except Exception as e:
#         return False, 'unsubscribed'

    
# def is_user_subscribed(user,foss,lang):
#     today = datetime.today().date()
#     # access = UserFossAccess.objects.filter(user=user, foss=foss, lang=lang).order_by('-subscription__expiry').first()
#     access = True
#     if access:
#         expiry = access.subscription.expiry
#         if  expiry >= today():
#             return True, expiry
#         else:
#             return False, expiry
#     return False, 'unsubscribed'

# def has_cdcontent_access(user,foss,lang):
#     today = datetime.today().today()
#     access = CdFossLanguages.objects.filter(user=user, foss=foss, lang=lang).order_by('-payment__expiry').first()
#     expiry = access.payment.expiry
#     if expiry >= today:
#         return True, expiry
#     return False, expiry

# def has_ilw_access(user, foss, lang):
#     today = datetime.today().today()
#     participant = Participant.objects.filter(event__foss=foss,foss_language_id=lang.id).exists()
#     return True, None