import pandas
import numpy 
import math

def preprocessing(usertr):
    
    usertr['LTE_speed'] = usertr.index
    usertr['UMTS_speed'] = usertr.index
    usertr['UMTS_full'] = usertr.index
    usertr['UMTS_lim'] = usertr.index
    usertr['UMTS_no'] = usertr.index
    usertr['LTE_full'] = usertr.index
    usertr['LTE_lim'] = usertr.index
    usertr['LTE_no'] = usertr.index
    
    usertr.LTE_speed=usertr.Cumulative_YoutubeSess_LTE_DL_Volume/usertr.Cumulative_YoutubeSess_LTE_DL_Time
    usertr.UMTS_speed=usertr.Cumulative_YoutubeSess_UMTS_DL_Volume/usertr.Cumulative_YoutubeSess_UMTS_DL_Time
    usertr.UMTS_full=usertr.Cumulative_Full_Service_Time_UMTS/(usertr.Cumulative_Full_Service_Time_UMTS+usertr.Cumulative_Lim_Service_Time_UMTS+usertr.Cumulative_No_Service_Time_UMTS)
    usertr.UMTS_lim=usertr.Cumulative_Lim_Service_Time_UMTS/(usertr.Cumulative_Full_Service_Time_UMTS+usertr.Cumulative_Lim_Service_Time_UMTS+usertr.Cumulative_No_Service_Time_UMTS)
    usertr.UMTS_no=usertr.Cumulative_No_Service_Time_UMTS/(usertr.Cumulative_Full_Service_Time_UMTS+usertr.Cumulative_Lim_Service_Time_UMTS+usertr.Cumulative_No_Service_Time_UMTS)
    usertr.LTE_full=usertr.Cumulative_Full_Service_Time_LTE/(usertr.Cumulative_Full_Service_Time_LTE+usertr.Cumulative_Lim_Service_Time_LTE+usertr.Cumulative_No_Service_Time_LTE)
    usertr.LTE_lim=usertr.Cumulative_Lim_Service_Time_LTE/(usertr.Cumulative_Full_Service_Time_LTE+usertr.Cumulative_Lim_Service_Time_LTE+usertr.Cumulative_No_Service_Time_LTE)
    usertr.LTE_no=usertr.Cumulative_No_Service_Time_LTE/(usertr.Cumulative_Full_Service_Time_LTE+usertr.Cumulative_Lim_Service_Time_LTE+usertr.Cumulative_No_Service_Time_LTE)
    
   # usertr = usertr.drop(["User_Id","Max_RSRQ","Cumulative_Full_Service_Time_UMTS","Cumulative_Lim_Service_Time_UMTS","Cumulative_No_Service_Time_UMTS","Cumulative_Full_Service_Time_LTE","Cumulative_Lim_Service_Time_LTE","Cumulative_No_Service_Time_LTE"], axis=1)
    
    return usertr