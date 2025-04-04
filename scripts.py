#Функция по исправлению оценок у определенного ребенка
def fix_marks(schoolkid_name):
	schoolkid = Schoolkid.objects.get_or_404(full_name__contains=schoolkid_name)
	marks= Mark.objects.filter(schoolkid__full_name__icontains=schoolkid_name, points_range=["2","3"])
	mark_fix = [mark_fix.save() for mark_fix in marks if setattr(mark_fix, 'points', "5")]
	return mark_fix

#Функция по создания комментария с похвалой от определенного учителя, предмета ребенку
def create_commendation(schoolkid_name, subject, teacher):
	schoolkid = Schoolkid.objects.get_or_404(full_name__contains=schoolkid_name)                                                                   
	subject = Subject.objects.get_or_404(title__contains=subject)                                                                            
	teacher = Teacher.objects.get_or_404(full_name__contains=teacher)                                                                                    
	last_lesson = Lesson.objects.filter(
            subject=subject,
            teacher=teacher,
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter
        ).order_by('-date').first()
        
        if not last_lesson:
            raise Lesson.DoesNotExist("Не найден подходящий урок")
		
        commendation = Commendation.objects.create(
            text="Хвалю!",
            created=last_lesson.date,
            schoolkid=schoolkid,
            teacher=teacher,
            subject=subject
        )
        return commendation
	
#Функция по удалению плохих отметок
def delete_bad_marks(schoolkid_name):
        schoolkid = Schoolkid.objects.get_or_404(full_name__contains=schoolkid_name)
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        deleted_count = bad_marks.delete()[0]
        return deleted_count
