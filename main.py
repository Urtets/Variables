number_Of_Completed_HWs = 12
spent_Hours = 1.5
course_Name = "Python"
time_On_One_Task = spent_Hours / number_Of_Completed_HWs
text = "Курс: " + course_Name + ", всего задач:" + str(number_Of_Completed_HWs)
text = text + ", затрачено часов: " + str(spent_Hours)
text = text + ", среднее время выполнения " + str(time_On_One_Task) + " часа."
print(text)
