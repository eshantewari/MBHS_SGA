from django.contrib import admin

from .models import Category, Students, Candidate

class CandidateInline(admin.TabularInline):
	model = Candidate
	extra = 3

class CategoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['category_num','slug','category_text', 'grade_level']}),
	]
	inlines = [CandidateInline]
	list_display = ('category_num','slug','category_text', 'grade_level')
	list_filter = ['category_num']
	search_fields = ['category_text']

class StudentsAdmin(admin.ModelAdmin):
	fields = ['student_id','grade','password']
	list_display = ('student_id','grade','password')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Students, StudentsAdmin)

