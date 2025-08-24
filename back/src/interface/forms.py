from django import forms
from .models import Portofolio

class PortofolioForm(forms.ModelForm):
    class Meta:
        model = Portofolio
        fields = ["nom", "email", "sujet", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        common_attrs = {
            "class": "w-full bg-white/5 border border-white/10 rounded-lg px-3 sm:px-4 py-2 sm:py-3 placeholder-gray-400 focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/20 transition-all duration-300 text-xs sm:text-base",
        }
        self.fields["nom"].widget.attrs.update(
            {**common_attrs, "placeholder": "Votre nom"}
        )
        self.fields["email"].widget.attrs.update(
            {**common_attrs, "placeholder": "votre@email.com"}
        )
        self.fields["sujet"].widget.attrs.update(
            {**common_attrs, "placeholder": "Sujet de votre message"}
        )
        self.fields["message"].widget.attrs.update(
            {**common_attrs, "placeholder": "Votre message...", "rows": 5}
        )
