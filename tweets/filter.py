from django.contrib import admin

class MuskFilter(admin.SimpleListFilter):
    title = "Filter by Elon Musk"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return (
            ("elonmusk", "Elon Musk"),
            ("other", "Other"),
        )

    def queryset(self, request, queryset):
        if self.value() == "elonmusk":
            return queryset.filter(payload__contains="Elon Musk")
        elif self.value() == "other":
            return queryset.exclude(payload__contains="Elon Musk")