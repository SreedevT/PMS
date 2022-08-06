from .models import Prescription

class PrescriptionForm:
    class Meta:
        model = Prescription
        fields = ('medicine')
