import requests

url = 'http://localhost:8080/api'
#son = {"city_development_index":0.92,"experience":14.0,"training_hours":66.0,"city_city_1":0.0,"city_city_10":0.0,"city_city_100":0.0,"city_city_101":0.0,"city_city_102":0.0,"city_city_103":0.0,"city_city_104":0.0,"city_city_105":0.0,"city_city_106":0.0,"city_city_107":0.0,"city_city_109":0.0,"city_city_11":0.0,"city_city_111":0.0,"city_city_114":0.0,"city_city_115":0.0,"city_city_116":0.0,"city_city_117":0.0,"city_city_118":0.0,"city_city_12":0.0,"city_city_120":0.0,"city_city_121":0.0,"city_city_123":0.0,"city_city_126":0.0,"city_city_127":0.0,"city_city_128":0.0,"city_city_129":0.0,"city_city_13":0.0,"city_city_131":0.0,"city_city_133":0.0,"city_city_134":0.0,"city_city_136":0.0,"city_city_138":0.0,"city_city_139":0.0,"city_city_14":0.0,"city_city_140":0.0,"city_city_141":0.0,"city_city_142":0.0,"city_city_143":0.0,"city_city_144":0.0,"city_city_145":0.0,"city_city_146":0.0,"city_city_149":0.0,"city_city_150":0.0,"city_city_152":0.0,"city_city_155":0.0,"city_city_157":0.0,"city_city_158":0.0,"city_city_159":0.0,"city_city_16":0.0,"city_city_160":1.0,"city_city_162":0.0,"city_city_165":0.0,"city_city_166":0.0,"city_city_167":0.0,"city_city_171":0.0,"city_city_173":0.0,"city_city_175":0.0,"city_city_176":0.0,"city_city_179":0.0,"city_city_18":0.0,"city_city_180":0.0,"city_city_19":0.0,"city_city_2":0.0,"city_city_20":0.0,"city_city_21":0.0,"city_city_23":0.0,"city_city_24":0.0,"city_city_25":0.0,"city_city_26":0.0,"city_city_27":0.0,"city_city_28":0.0,"city_city_30":0.0,"city_city_31":0.0,"city_city_33":0.0,"city_city_36":0.0,"city_city_37":0.0,"city_city_39":0.0,"city_city_40":0.0,"city_city_41":0.0,"city_city_42":0.0,"city_city_43":0.0,"city_city_44":0.0,"city_city_45":0.0,"city_city_46":0.0,"city_city_48":0.0,"city_city_50":0.0,"city_city_53":0.0,"city_city_54":0.0,"city_city_55":0.0,"city_city_57":0.0,"city_city_59":0.0,"city_city_61":0.0,"city_city_62":0.0,"city_city_64":0.0,"city_city_65":0.0,"city_city_67":0.0,"city_city_69":0.0,"city_city_7":0.0,"city_city_70":0.0,"city_city_71":0.0,"city_city_72":0.0,"city_city_73":0.0,"city_city_74":0.0,"city_city_75":0.0,"city_city_76":0.0,"city_city_77":0.0,"city_city_78":0.0,"city_city_79":0.0,"city_city_8":0.0,"city_city_80":0.0,"city_city_81":0.0,"city_city_82":0.0,"city_city_83":0.0,"city_city_84":0.0,"city_city_89":0.0,"city_city_9":0.0,"city_city_90":0.0,"city_city_91":0.0,"city_city_93":0.0,"city_city_94":0.0,"city_city_97":0.0,"city_city_98":0.0,"city_city_99":0.0,"gender_Female":1.0,"gender_Male":0.0,"gender_Other":0.0,"relevent_experience_Has relevent experience":1.0,"relevent_experience_No relevent experience":0.0,"enrolled_university_Full time course":0.0,"enrolled_university_Part time course":0.0,"enrolled_university_no_enrollment":1.0,"education_level_Graduate":1.0,"education_level_High School":0.0,"education_level_Masters":0.0,"education_level_None":0.0,"education_level_Phd":0.0,"education_level_Primary School":0.0,"major_discipline_Arts":0.0,"major_discipline_Business Degree":0.0,"major_discipline_Humanities":0.0,"major_discipline_No Major":0.0,"major_discipline_Other":0.0,"major_discipline_STEM":1.0,"company_size_10\\/49":0.0,"company_size_100-500":1.0,"company_size_1000-4999":0.0,"company_size_10000+":0.0,"company_size_50-99":0.0,"company_size_500-999":0.0,"company_size_5000-9999":0.0,"company_size_<10":0.0,"company_size_Zero":0.0,"company_type_Early Stage Startup":0.0,"company_type_Funded Startup":1.0,"company_type_NGO":0.0,"company_type_None":0.0,"company_type_Other":0.0,"company_type_Public Sector":0.0,"company_type_Pvt Ltd":0.0,"last_new_job_1":1.0,"last_new_job_2":0.0,"last_new_job_3":0.0,"last_new_job_4":0.0,"last_new_job_>4":0.0,"last_new_job_None":0.0,"last_new_job_never":0.0}
lists = [  0.689,   3.   , 172.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   1.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   1.   ,   0.   ,   1.   ,   0.   ,   0.   ,   1.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   1.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   1.   ,   0.   ,   0.   ,   1.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         1.   ,   0.   ,   1.   ,   0.   ,   0.   ,   0.   ,   0.   ,
         0.   ]
data = {'arr':lists}
r = requests.post(url,json=data)
print(r.json())