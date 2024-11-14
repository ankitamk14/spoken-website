from datetime import datetime, date
from events.models import Organiser, Student, StudentMaster, StudentBatch, AcademicKey
from .models import  CdFossLanguages, Payee, UserFossAccess, UserSubscription, PaymentTransaction
# from .models import UserFossAccess, CdFossLanguages, Payee
from training.models import Participant


def check_auth_external_roles(user, groups, foss, lang):
    # check if user has organiser role and belongs to paid college
    if hasattr(user, 'organiser'):
        print(f"\033[92m The  user is organiser \033[0m")
        if is_organiser_insti_subscribed(user):
            print(f"\033[92m organiser insti is subscribed \033[0m")
            return True
        else:
            print(f"\033[91m organiser insti is not subscribed \033[0m")
    
    # check if user has student role and belongs to paid college
    if hasattr(user, 'student'):
        print(f"\033[92m The  user is student \033[0m")
        if is_student_insti_subscribed(user):
            print(f"\033[92m student insti is subscribed \033[0m")
            return True
        else:
            print(f"\033[91m student insti is not subscribed \033[0m")
    
    
    is_authorized = is_user_subscribed(user)
    if is_authorized:
        print(f"\033[93m The user has taken complete subscription \033[0m")
        return True
    else:
        print(f"\033[91m The user has not taken a subscription \033[0m")
    
    is_authorized = is_foss_subscribed(user, foss, lang)
    if is_authorized:
        print(f"\033[93m The user has taken FOSS subscription : foss - {foss}, lang - {lang}\033[0m")
        return True
    else:
        print(f"\033[91m The user has not taken a FOSS subscription : foss - {foss}, lang - {lang}\033[0m")
    
    is_authorized = has_cdcontent_access(user, foss, lang)
    if is_authorized:
        print(f"\033[93m The user has paid for cdcontent : foss - {foss}, lang - {lang}  \033[0m")
        return True
    else:
        print(f"\033[91m The user has not paid for CDContent download : foss - {foss}, lang - {lang}\033[0m")
    
    is_authorized = has_ilw_access(user, foss, lang)
    if is_authorized:
        print(f"\033[92m The user has paid for ILW. foss - {foss}, lang - {lang} \033[0m")
        return True
    else:
        print(f"\033[91m The user has not paid for ILW. : foss - {foss}, lang - {lang}\033[0m")
    
    return False






def is_valid_subscription(expiry_date):
    today = datetime.today().date()
    return expiry_date >= today

def is_organiser_insti_subscribed(user):
    print(f"\033[93m chekcing for organiser.... \033[0m")
    try:
        academic_id = Organiser.objects.get(user=user).academic_id
        print(f"\033[93m academic_id : {academic_id} \033[0m")
        ak = AcademicKey.objects.filter(academic_id=academic_id).order_by('-expiry_date').first()
        print(f"\033[93m ak : {ak} \033[0m")

        return ak and ak.expiry_date >= date.today()
    except Exception as e:
        print(f"\033[91m execption : {e} \033[0m")
        return False

def is_student_insti_subscribed(user):
    try:
        academic_id = StudentMaster.objects.select_related('student','batch').get(student__user=user).batch.academic_id
        # academic_id = Student.objects.select_related('studentmaster__batch').get(user=user).studentmaster.batch.academic_id
        print(f"\033[93m  academic_id : {academic_id}\033[0m")
        ak = AcademicKey.objects.filter(academic_id=academic_id).order_by('-expiry_date').first()
        print(f"\033[93m  ak : {ak}\033[0m")
        print(f"\033[93m academic_id: {academic_id}  \033[0m")
        return ak and ak.expiry_date >= date.today()
    except Exception as e:
        print(f"\033[91m exception from is_student_insti_subscribed : {e} \033[0m")
        return False
     
def is_user_subscribed(user):
    print(f"\033[93m checking for user subscription...... \033[0m")
    subscription = UserSubscription.objects.filter(user=user,usersubscriptiontransactions__status='S').order_by('-expiry').first()
    return subscription and subscription.expiry >= date.today()


def is_foss_subscribed(user,foss,lang):
    print(f"\033[93m foss: {type(foss)} lang: {type(lang)} \033[0m")
    access = UserFossAccess.objects.filter(user=user, foss=foss,subscription__fosssubscriptiontransactions__status='S').order_by('-subscription__expiry').first()
    return access and access.subscription.expiry >= date.today()
   
def has_cdcontent_access(user,foss,lang):
    # access = CdFossLanguages.objects.filter(payment__user=user, foss=foss, lang__name=lang).order_by('-payment__expiry').first()
    payee_ids = list(CdFossLanguages.objects.filter(payment__user=user, foss=foss, lang__name=lang).values_list('payment_id', flat=True))
    print(f"\033[93mpayee_ids : {payee_ids}  \033[0m")
    access = PaymentTransaction.objects.filter(status='S', paymentdetail_id__in=payee_ids).exists()
    print(f"\033[93maccess : {access}  \033[0m")
    return access


def has_ilw_access(user, foss, lang):
    print(f"\033[93m foss: {foss}, lang: {lang}, user: {user} \033[0m")
    participant = Participant.objects.filter(event__foss=foss,user=user,payment_status__status=1).exists()
    if participant:
        print(f"\033[92m Participant Exists \033[0m")
    else:
        print(f"\033[91m Participant do not exists \033[0m")
    return participant