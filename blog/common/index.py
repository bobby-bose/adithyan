# core/listing/common/index.py
import logging
import datetime
import string
import random

logger = logging.getLogger('django')
today = datetime.datetime.today().date()


def generate_random_code(type_=None):
    number = random.randint(100001, 999999)
    result = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + str(number)
    if str(type_) == "S":
        result = "S" + str(result)
    elif str(type_) == "T":
        result = "T" + str(result)
    elif str(type_) == "P":
        result = "P" + str(result)
    else:
        result = "O" + str(result)
    return result


class AllStatusTypes():
    USER_SCOPES = [("1", "Owner"), ("2", "Super Admin"), ("3", "Admin"),
                   ("4", "staff"), ("5", "External"), ("6", "Other")]

    STATUS = [("DONE", "Done"), ("ACCEPTED", "Accepted"), ("COMPLETED", "Completed"),
              ("VERIFIED", "Verified"), ("ISSUED", "Issued"),
              ("IN_PROGRESS", "In progress"), ("OTHER", "Other"), ("SUBMITTED", "Submitted"),
              ("PENDING", "Pending"), ("CANCELLED", "Cancelled"),
              ("REJECTED", "Rejected"), ("DELETED", "Deleted"), ("HOLD", "Hold")]

    CREDENTIALS = [("PRIVATE", "Private"), ("PUBLIC", "Public"), ("SHARED", "Shared"), ]

    DESIGNATION = [("DIRECTOR", "Director"), ("HOD", "Head of the Department"),
                   ("MANAGER", "Manager"), ("TRAINEE", "Trainee"),
                   ("STAFF", "Staff"), ("OTHER_STAFF", "Other Staff"),
                   ("CUSTOMER", "Customer"), ("SUPPLIER", "Supplier"),
                   ("AGENT", "Agent"), ("EXTERNAL", "Third party")]

    JOB_TYPES = [("FULL_TIME", "Full time"), ("PERMANENT", "Permanent"), ("CONTRACT", "Contract"),
                 ("TRAINEE", "Trainee"), ("OTHER", "Other")]
    MODULES = [("project", "Project"), ("tasks", "Tasks"),
               ("subtasks", "SubTasks"), ("userwallet", "UserWallet")]

    WALLET_MODULES = (("EMPLOYEE", "EMPLOYEE"), ("PROJECT", "PROJECT"),
                      ("TASK", "TASK"), ("SUBTASK", "SUBTASK"),
                      ("DEPOSIT", "DEPOSIT"), ("WITHDRAW", "WITHDRAW"))

    GENDER = [("MAlE", "Male"), ("FEMALE", "Female"), ("OTHER", "Other"), ]
    LEADS = [("PENDING", "Pending"), ("IN_PROGRESS", "In progress"),
             ("REJECTED", "Rejected"), ("OTHER", "Other"), ]

    FAMILY_TYPE = [("BACHELOR", "Bachelor"), ("MARRIED", "Married")]
    ASSET_TYPES = [("P", "Physical"), ("D", "Digital"), ("I", "Intellectual"), ("O", "Other")]


# Model class for status text in tables
def status_info_text(self):
    res = {'class': None}
    if self.status in ("DONE", "COMPLETED", "ISSUED"):
        res['class'] = 'badge badge-success'
    elif self.status in ("HOLD", "IN_PROGRESS", "PENDING"):
        # res['class'] = 'text-warning'
        res['class'] = 'badge badge-warning'
    elif self.status in ("CANCELLED", "REJECTED"):
        res['class'] = 'badge badge-danger'
    return res
