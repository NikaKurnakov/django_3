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
	return Commendation.objects.create(text="Хвалю!", created="2018-10-01", schoolkid=schoolkid[0], teacher=teacher[0], subject=subject[0])
