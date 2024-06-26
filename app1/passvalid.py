
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class Passvalid:
    def __init__(self, min_length=1) :
        self.min_length=min_length
    def validate(self, password, user =None):
        sp="[!@#$%^&*()_+|}<{?]"
        if not any (char.isdigit() for char in password):
            raise ValidationError(_('Paswword Must contain at least %(_min_length)d digit') % {'min_length':self.min_length})
        if not any (char.isalpha() for char in password):
            raise ValidationError(_('Paswword Must contain at least %(_min_length)d letter') % {'min_length':self.min_length})
        if not any (char in sp for char in password):
            raise ValidationError(_('Paswword Must contain at least %(_min_length)d Special Character') % {'min_length':self.min_length})
    
    def get_help_text(self):
        return("Password should contain\n -Atleast one Digit\n-Atleast one letter\n-Atleast one Special")