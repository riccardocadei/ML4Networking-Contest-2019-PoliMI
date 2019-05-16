import pandas
import numpy 
import math

def newfeatures(usertr):
    
    usertr['LTE_speed'] = usertr.index
    usertr['UMTS_speed'] = usertr.index
    usertr['UMTS_full'] = usertr.index
    usertr['UMTS_lim'] = usertr.index
    usertr['UMTS_no'] = usertr.index
    usertr['LTE_full'] = usertr.index
    usertr['LTE_lim'] = usertr.index
    usertr['LTE_no'] = usertr.index
    usertr['LTE_tot'] = usertr.index
    usertr['UMTS_tot'] = usertr.index
    usertr['p1'] = usertr.index
    usertr['p2'] = usertr.index
    usertr['YT'] = usertr.index
    
    usertr.LTE_speed=usertr.Cumulative_YoutubeSess_LTE_DL_Volume/usertr.Cumulative_YoutubeSess_LTE_DL_Time
    usertr.UMTS_speed=usertr.Cumulative_YoutubeSess_UMTS_DL_Volume/usertr.Cumulative_YoutubeSess_UMTS_DL_Time
    
    usertr.LTE_tot=(usertr.Cumulative_Full_Service_Time_LTE+usertr.Cumulative_Lim_Service_Time_LTE+usertr.Cumulative_No_Service_Time_LTE)
    usertr.UMTS_tot=(usertr.Cumulative_Full_Service_Time_UMTS+usertr.Cumulative_Lim_Service_Time_UMTS+usertr.Cumulative_No_Service_Time_UMTS)
    usertr.UMTS_full=usertr.Cumulative_Full_Service_Time_UMTS/(usertr.Cumulative_Full_Service_Time_UMTS+usertr.Cumulative_Lim_Service_Time_UMTS+usertr.Cumulative_No_Service_Time_UMTS)
    usertr.UMTS_lim=usertr.Cumulative_Lim_Service_Time_UMTS/(usertr.Cumulative_Full_Service_Time_UMTS+usertr.Cumulative_Lim_Service_Time_UMTS+usertr.Cumulative_No_Service_Time_UMTS)
    usertr.UMTS_no=usertr.Cumulative_No_Service_Time_UMTS/(usertr.Cumulative_Full_Service_Time_UMTS+usertr.Cumulative_Lim_Service_Time_UMTS+usertr.Cumulative_No_Service_Time_UMTS)
    usertr.LTE_full=usertr.Cumulative_Full_Service_Time_LTE/(usertr.Cumulative_Full_Service_Time_LTE+usertr.Cumulative_Lim_Service_Time_LTE+usertr.Cumulative_No_Service_Time_LTE)
    usertr.LTE_lim=usertr.Cumulative_Lim_Service_Time_LTE/(usertr.Cumulative_Full_Service_Time_LTE+usertr.Cumulative_Lim_Service_Time_LTE+usertr.Cumulative_No_Service_Time_LTE)
    usertr.LTE_no=usertr.Cumulative_No_Service_Time_LTE/(usertr.Cumulative_Full_Service_Time_LTE+usertr.Cumulative_Lim_Service_Time_LTE+usertr.Cumulative_No_Service_Time_LTE)
    
    usertr.p1=(usertr.LTE_full+usertr.UMTS_full)/(usertr.LTE_tot+usertr.UMTS_tot)
    usertr.p2=(usertr.Cumulative_YoutubeSess_LTE_DL_Volume+usertr.Cumulative_YoutubeSess_UMTS_DL_Volume)/(usertr.Cumulative_YoutubeSess_LTE_DL_Time+usertr.Cumulative_YoutubeSess_UMTS_DL_Time)
  
    usertr.Max_RSRQ=10.0**(usertr.Max_RSRQ)
    usertr.Max_SNR=10.0**(usertr.Max_SNR)
    usertr.YT=(usertr.Cumulative_YoutubeSess_LTE_DL_Time+usertr.Cumulative_YoutubeSess_UMTS_DL_Time)/(usertr.LTE_tot+usertr.UMTS_tot)
    
    a=usertr.LTE_speed.median()
    b=usertr.UMTS_speed.median()

    for i in range(usertr.shape[0]):
        if math.isnan(usertr.LTE_speed[i]):
            usertr.LTE_speed[i]=a
        if math.isnan(usertr.UMTS_speed[i]):
             usertr.UMTS_speed[i]=b
    
    return usertr