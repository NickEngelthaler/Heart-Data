# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:31:36 2022

@author: Nick Engelthaler
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""Data frame"""

df = pd.read_csv("heart.csv")

def getHeartAttack():
    
    val_counts = df["attack"].value_counts()
    no_heart_attack = (val_counts[0] / df.shape[0])
    heart_attack = (val_counts[1] / df.shape[0])
    percent_notation = "{:,.2f}%".format(no_heart_attack*100)
    print("\nThe percent of no heart attacks in the data: " + percent_notation)
    percent_notation = "{:,.2f}%".format(heart_attack*100)
    print("The percent of heart attacks in the data: " + percent_notation)
   
    # create pie chart
    labels = 'Heart Attack', 'No Heart Attack'
    sizes = [heart_attack, no_heart_attack]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
    ax1.set_title('Heart Attack Ratio in Data')
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig('HeartAttack.png')
    #plt.clf()
    
def getGender():
    #val_counts = df["sex"].value_counts()
    
    f_hattack = df[(df["sex"]==1) & (df["attack"]==1)].shape[0]
    m_hattack = df[(df["sex"]==0) & (df["attack"]==1)].shape[0]
    t_hattack  = f_hattack + m_hattack
                                                            
    Male_Heart_Attacks = (m_hattack / t_hattack)
    Female_Heart_Attacks = (f_hattack / t_hattack)
    
    #Male_Heart_Attacks = (val_counts[0] / df.shape[0])
    #Female_Heart_Attacks = (val_counts[1] / df.shape[0])
    percent_notation = "{:,.2f}%".format(Male_Heart_Attacks*100)
    print("\nMale Heart Attacks: " + percent_notation)
    percent_notation = "{:,.2f}%".format(Female_Heart_Attacks*100)
    print("Female Heart Attacks: " + percent_notation)
    
    
    
    # create pie chart
    labels = 'Male', 'Female'
    sizes = [Male_Heart_Attacks, Female_Heart_Attacks]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
    ax1.set_title('Heart Attack Ratio between Male & Female')
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig('getGender.png')
    #plt.clf()
#fun 3 chestpain

def getChestPain():
    
    val_t = df [( df["cp"]==0) & (df["attack"] == 1)].shape[0]
    denom_t = df[(df["cp"] ==0)].shape[0]
    prob_t = np.round ( (val_t / denom_t), 4)
    
    val_at = df [( df["cp"]==1) & (df["attack"] == 1)].shape[0]
    denom_at = df[(df["cp"] ==1)].shape[0]
    prob_at = np.round ( (val_at / denom_at), 4)
    
    val_ap = df [( df["cp"]==2) & (df["attack"] == 1)].shape[0]
    denom_ap = df[(df["cp"] ==2)].shape[0]
    prob_ap = np.round ( (val_at / denom_at), 4)
    
    val_asm = df [( df["cp"]==3) & (df["attack"] == 1)].shape[0]
    denom_asm = df[(df["cp"] ==3)].shape[0]
    prob_asm = np.round ( (val_asm / denom_asm), 4)
    
    vals = [prob_t, prob_at, prob_ap, prob_asm]
    labels = ["Typicial", "Atypical", "Any Pains", "Asymptomatic"]
    
    
    print("Chest Pain Type:")
    print("\t Chest Pain Type 0 - Typical")
    print("\t Chest Pain Type 1 - Atypical")
    print("\t Chest Pain Type 2 - Any Pains")
    print("\t Chest Pain Type 3 - Asymptomatic")

    
    for val, label in zip(vals, labels):
        print(f"Chest Pain Type - {label} -  has this prob. of heart attack", f'{val*100:.2f}''%')
        
    plt.figure()
    plt.bar(labels, vals, color = 'red')
    plt.xlabel('pain type')
    plt.ylabel('freguency per pain type')
    plt.title('Frequency of Pain Reported')
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig("chestpain.png")
    
def getBloodSugar():
    
    val_hfbs = df [( df["fbs"]==1) & (df["attack"] == 1)].shape[0]
    denom_hfbs = df[(df["fbs"] ==1)].shape[0]
    prob_hfbs = np.round ( (val_hfbs / denom_hfbs), 4)
    
    val_rfbs = df[(df["fbs"]==0) & (df["attack"] == 1)].shape[0]
    denom_rfbs = df[(df["fbs"] ==0)].shape[0]
    prob_rfbs = np.round ( (val_rfbs / denom_rfbs), 4)
    
    vals= [prob_hfbs, prob_rfbs]
    labels = ["High", "Regular"]
    for val, label in zip(vals, labels):
        print(f"Blood Sugar Level - {label} - has this prob. of heart attack", f'{val*100:.2f}''%')
    
    plt.figure(figsize = (10,5))
    plt.bar(labels, vals, color = "green")
    plt.xlabel("Blood Sugar")
    plt.ylabel("Prob. of heart attack per Blood Sugar Level")
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig("BloodSugar.png")

def getEKG():
    
    val_n = df [( df["restecg"]==0) & (df["attack"] == 1)].shape[0]
    denom_n = df[(df["restecg"] ==0)].shape[0]
    prob_n = np.round ( (val_n / denom_n), 4)
    
    val_stt = df[(df["restecg"]==1) & (df["attack"] == 1)].shape[0]
    denom_stt = df[(df["restecg"] ==1)].shape[0]
    prob_stt = np.round ( (val_stt / denom_stt), 4)
    
    val_lv = df[(df["restecg"]==2) & (df["attack"] == 1)].shape[0]
    denom_lv = df[(df["restecg"] ==2)].shape[0]
    prob_lv = np.round ( (val_lv / denom_lv), 4)
    
    vals= [prob_n, prob_stt, prob_lv]
    labels = ["Normal", "Abnormal with ST-T Wave", "Abnormal Left Ventricular"]
    for val, label in zip(vals, labels):
        print(f"EKG Type - {label} has this prob. of heart attack", f'{val*100:.2f}''%')
    
    plt.figure(figsize = (10,5))
    plt.bar(labels, vals, color = "red")
    plt.xlabel("EKG Type")
    plt.ylabel("Prob. of heart attack per EKG type")
    fig1 = plt.gcf()
    plt.show()
    fig1.savefig("EKG.png")

def getExercise():
    
   val_r = df [( df["exng"]==1) & (df["attack"] == 1)].shape[0]
   denom_r = df[(df["exng"] ==1)].shape[0]
   prob_r = np.round ( (val_r / denom_r), 4)
   
   val_nr = df[(df["exng"]==0) & (df["attack"] == 1)].shape[0]
   denom_nr = df[(df["exng"] ==0)].shape[0]
   prob_nr = np.round ( (val_nr / denom_nr), 4)
   
   vals= [prob_r, prob_nr]
   labels = ["Yes", "No"]
   for val, label in zip(vals, labels):
       print(f"People who have exercised - {label} - has this prob. of heart attack", f'{val*100:.2f}''%')
   
   plt.figure(figsize = (10,5))
   plt.bar(labels, vals, color = "purple")
   plt.xlabel("Exercise")
   plt.ylabel("Percent heart attack")
   fig1 = plt.gcf()
   plt.show()
   fig1.savefig("Exercise.png")
