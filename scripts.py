#Функция по исправлению оценок у определенного ребенка
def fix_marks(scoolkid):
	schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid)
	marks = Mark.objects.filter(schoolkid__full_name__icontains=schoolkid, points_range=["2","3"])
	for mark_fix in marks:
		mark_fix.points = "5"
		mark_fix.save()

#Функция по создания комментария с похвалой от определенного учителя, предмета ребенку
def create_commendation(schoolkid, subject, teacher):
	schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid)                                                                   
	subject = Subject.objects.filter(title__contains=subject)                                                                            
	teacher = Teacher.objects.filter(full_name__contains=teacher)                                                                                    
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
