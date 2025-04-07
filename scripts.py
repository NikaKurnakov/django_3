#Функция по исправлению оценок у определенного ребенка
def fix_marks(schoolkid_name):
    schoolkid = get_object_or_404(Schoolkid, full_name__icontains=schoolkid_name)
    updated_count = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)
    return updated_count

#Функция по создания комментария с похвалой от определенного учителя, предмета ребенку
def create_commendation(schoolkid_name, subject, teacher):
	schoolkid = get_object_or_404(Schoolkid, full_name__contains=schoolkid_name)                                                                   
	subject = get_object_or_404(Subject, title__contains=subject)                                                                            
	teacher = get_object_or_404(Teacher, full_name__contains=teacher)                                                                                    
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
def delete_chastisement(schoolkid_name):
        schoolkid = get_object_or_404(Schoolkid, full_name__contains=schoolkid_name)
        chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
        deleted_chastisement = chastisement.delete()
        return deleted_chastisement
