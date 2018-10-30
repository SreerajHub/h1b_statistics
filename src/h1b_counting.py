#!/usr/bin/python

import csv
import os
csv.field_size_limit(100000000)

#Function to check for certified applications and create list of jobs and states of emoployment

def generate_list(input_file):
    #print(input_file.fieldnames)

    status=[s for s in input_file.fieldnames if "STATUS" in s]  # To account for nomenclature differences between 2016/2015 data and 2014 data
    job=[s for s in input_file.fieldnames if "SOC_NAME" in s]   # To account for nomenclature differences between 2016/2015 data and 2014 data

    jobs_list=[]                                        # Create a list to add occupations of certified applications
    state_list=[]                                       # Create a list to add states of employment for certified applications
    certified_count=0                                   # initialize counter that keeps  count of certified applications
    for row in input_file:
        if row[status[0]]=='CERTIFIED':                 # If status is certified add SOC NAME and Worksite State
            jobs_list.append(row[job[0]])
            if "WORKSITE_STATE" in input_file.fieldnames:
                state_list.append(row["WORKSITE_STATE"])            # nomenclature for 2015/16

            else:
                state_list.append(row["LCA_CASE_WORKLOC1_STATE"])   # old nomenclature used in 2014

            certified_count+=1
    return(jobs_list,state_list,certified_count)

def sort_data(data_list):

#sort data based on frequency of job/state, and for tied frequencies, arrange alphabetically
    counter={}
    for item in data_list:                          # for each job/state in input list
        if item in counter:                         #If job/state is already in dictionary, increment count
            counter[item]+= 1
        else:
            counter[item]= 1                        # else, mark as first count of job/state
    temp = sorted(counter.items(), key=lambda k: (-k[1], k[0]))         #sort by frequency and alphabetically for ties
    top_list=[]
    for key,value in temp:
        top_list.append(key)                                            # list with job/state names in sorted order

    return(top_list,counter)

if __name__=='__main__':

    # Check Directories and read input csv file

    if os.path.exists("./input/h1b_input.csv"):
        input_file = csv.DictReader(open("./input/h1b_input.csv", encoding="utf8"), delimiter=';')
    else:
        print("File Not Found: ./input/h1b_input.csv")


    jobs_list,state_list,certified_count = generate_list(input_file)        # A list of certified jobs/states listed under header SOC NAME and WORKSITE STATE

    top_jobs, jobs_counter = sort_data(jobs_list)                           # sorted list of jobs and frequencies of each job
    top_states, states_counter = sort_data(state_list)                      # same for states

    directory = './output'                                                   # check for output directory, create if required
    if not os.path.exists(directory):
        os.makedirs(directory)

    result_file1='./output/top_10_occupations.txt'                          # Writes result as suggested in problem statement
    result1 = open(result_file1, 'w')
    result1.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for i in range(min(10,len(top_jobs))):
        result1.write(str(top_jobs[i]) + ";" + str(jobs_counter[top_jobs[i]]) + ";" + str(round(jobs_counter[top_jobs[i]] * 100 / certified_count, 1)) + "%\n")
                                                                            # delimiter = ';' and row separation by \n
    result_file2='./output/top_10_states.txt'
    result2 = open(result_file2, 'w')
    result2.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for i in range(min(10,len(top_states))):
        result2.write(str(top_states[i]) + ";" + str(states_counter[top_states[i]]) + ";" + str(
            round(states_counter[top_states[i]] * 100 / certified_count, 1)) + "%\n")


