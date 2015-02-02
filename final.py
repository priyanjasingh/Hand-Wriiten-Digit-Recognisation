import csv
import math
import operator
 
def Open_file( train_result_array=[] ,train_data_array = [], test_data_array=[]): 
    with open('./train.csv',"r") as train_file: # opening the training file
        train_rows = csv.reader(train_file, delimiter = ',')
        for row in train_rows: # reading row by row
            train_result_array.append(row[0]) # storing the correct answer in the result set corresponding to the given traing set
            train_data_array.append(row[1:]) # storing the rest of the training test case data in the train_array
    del train_data_array[0] # deleting the headers for pixel
    del train_result_array[0] # deleting the headers for pixel

    with open('./test.csv','r') as test_file: # opeing the testing file
        test_rows = csv.reader(test_file, delimiter = ',') 
        for row in test_rows: # reading row by row 
            test_data_array.append(row[0:]) # storing the test data in the test array
    del test_data_array[0]  # deleting headers         
             
def getMinimumDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += (int(instance1[x]) - int(instance2[x]))**2 #using euclidean formula getting the distance between the two instances 
    return math.sqrt(distance)
        
def getClosest(train_data_array, testInstance, k,train_result):
    distances = []
    length = len(testInstance)-1 #lenght of the test instance 
    for x in range(len(train_data_array)):
        dist = getMinimumDistance(testInstance, train_data_array[x], length) #getting distance between the test and training instances
        distances.append((train_result[x], dist))  # oush the actual reslt set and corresponding distance in the array
    distances.sort(key=operator.itemgetter(1)) # sort the distances array according to the distance values
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0]) # get the top 10 neighbours from the sorted list 
    return neighbors # return the neighbours 
 
def getVote(neighbors):
    classVotes = [0,0,0,0,0,0,0,0,0,0] # initializing the class votes to zero
    maximum=-1
    index=-1
    for x in range(10):
        response = int(neighbors[x][0]) 
	classVotes[response]+=1 # calculating the votes corrssponding to the reponse
        if (maximum<int(classVotes[response])): # finding the value with maximum votes 
            maximum= classVotes[response]
            index=response
    return index #returning the result
        
 
def main():
    # prepare data
    train_data_array=[]
    test_data_array=[]
    train_result =[]
    ans = []
    #Function to open training and test files
    Open_file(train_result, train_data_array, test_data_array)
    fo = open("output.csv", "w")
    
    # Selection of k nearest neighbours
    k = 20
    for x in range(len(test_data_array)):
	#neighbours contains the closest neighbours corresponding to a given test case
        neighbors = getClosest(train_data_array, test_data_array[x], k,train_result)
	#Now taking the majority vote form the closest neighbours
        result = int(getVote(neighbors))
        print result
	fo.write("" + str(result) + "\n") # writing to file	
	#Storing the answere of each test case in the array
        ans.append(result) 
    #print ans
    fo.close()
main()
