






############### TASK 1 ###########
import pandas as pd
import re
file_path = 'C:\\Users\\abhosage\\PycharmProjects\\Python_Pandas\\Assignment\\mbox 1 (2).txt '        # path of input file
with open(file_path,'r') as file:
    data = file.read()

email = re.findall('From:(\s.+)', data)
result = re.findall('X-DSPAM-Result:(\s.+)',data)
date_time = re.findall('X-DSPAM-Processed:(\s.+)',data)
confidence = re.findall('X-DSPAM-Confidence:(\s.+)',data)
probablity = re.findall('X-DSPAM-Probability:(\s.+)',data)

dataframe = pd.DataFrame({'email_id': email,
                          'result': result,
                          'date_time': date_time,
                          'confidance': confidence,
                          'prob': probablity})

dataframe.to_csv('sample_1.csv',index=False, header=['email_id','result','date_time','confidance','prob'])

print(dataframe.to_string())




################## TASK 2 #########

# import pandas as pd
# file_1 = ''        #path of first filr
# file_2 = ''        # path of second file
#
# df1 = pd.read_csv(file_1)
# df2 = pd.read_csv(file_2)
#
# # print(df1.to_string())
# # print(df2.to_string())
# # print(df1['email_id'].dtype)
# # print(df2['email_id'].dtype)
# new_df = pd.merge(df1,df2, on='email_id',how='outer')
# new_df.fillna(0000)
# print(new_df.to_string())
# new_df.to_excel('new_dataframe.xlsx')




############ TASK 3 #############
# import pandas as pd
# import matplotlib.pyplot as plt
# file_path = 'new_dataframe.xlsx'         #path of file
# sheet_name = 'Sheet1'        #Sheet name
# data = pd.read_excel(file_path,sheet_name)
# newdata = data.fillna(0000)
# print(newdata.to_string())
# plt.plot(newdata['Age'], newdata['confidance'])
# plt.grid(True)
# plt.show()