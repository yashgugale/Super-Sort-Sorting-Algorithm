#Input list
L = [2,7,4,19,45,16,9,13,8,69,55,11,23,98,14,5,1,3]	

#Merging function
def merge(M,N):
    merging_list = []   		#create empty list to merge the lists M and N

    if not M:   				#if M is empty list,
        m = 0   				#set m = 0
    else:
        m = len(M)  			#otherwise, set m = len(M)
    if not N:   				#if N is empty list,
        n = 0   				#set n = 0
    else:
        n = len(N)  			#otherwise, set n = len(N)

    (i, j) = (0,0)  			#set to indexes i and j as 0

    while i+j < m+n:
        if i == m:      		#if list M is empty, append entire list N to merging_list
            merging_list.append(N[j])
            j = j+1
        elif j == n:    		#if list N is empty, append entire list M to merging_list
            merging_list.append(M[i])
            i = i+1
        elif M[i] <= N[j]:  		#head of M is smaller, append element from M
            merging_list.append(M[i])
            i = i+1
        elif M[i] > N[j]:   		#head of N is smaller, append element from N
            merging_list.append(N[j])
            j = j+1
            
    return(merging_list)    		#return the merged list

#Sorting function
def supersort(L, left, right):
    if len(L) < 1:  			#if list is empty, return 0
        return()
		
    Forward_sorted_list = []  	#list for storing left to right traversals
    Backward_sorted_list = []  	#list for storing right to left traversals

#FORWARD SELECTION:
    #traversing from left to right
    current_highest = L[0]  					#set the first element as the current number
    Forward_sorted_list.append(current_highest)   		#add current element to the list Forward_sorted_list
    for i in range(left+1, right):  				#traverse all elements from left to right
        if L[i] >= current_highest: 				#if the number is greater than or equal to current_highest, 
            current_highest = L[i]  				#set that number as the current_highest  
            Forward_sorted_list.append(current_highest) 	#add it to the list Forward_sorted_list

    #The following step is done to reduce the elements in L as removing an element from a list while working on it is not recommended.
    for number in Forward_sorted_list:      			#now for all numbers in Forward_sorted_list,  
        if number in L: 					#if they are in L,
            L.remove(number)					#remove them from L so we have reduced the list L

	
#BACKWARD SELECTION:
    if len(L) > 1:  			#it is possible that after left traversal, the list L becomes empty
					#thus, in that case we need to check again, if number present, only then proceed for right traversal
        #traversing from right to left
        current_highest = L[-1] 				#set the last element as current_highest
        Backward_sorted_list.append(current_highest)   		#add current_highest to the list Backward_sorted_list
        for i in range(-2, -(len(L)+1), -1):    		#for all numbers starting from second last, till the index -(len(L)+1), go backwards
            if L[i] >= current_highest: 			#if the number is greater than or equal to current_highest,
                current_highest = L[i]  			#set that number as the current_highest
                Backward_sorted_list.append(current_highest)   	#add it to list Backward_sorted_list
	
	#The following step is done to reduce the elements in L as removing an element from a list while working on it is not recommended.
        for number in Backward_sorted_list:    			#now for all numbers in Backward_sorted_list, 
            if number in L: 					#if they are in L,
                L.remove(number)				#remove them from L so we have reduced the list L

    intermediate_sorted_1 = merge(Forward_sorted_list, Backward_sorted_list)  #store merged Forward_sorted_list and Backward_sorted_list in intermediate_sorted_1

    mid = len(L)//2     					#find the mid of the list L after left and right traversals
    Left_sublist = L[ : mid]  					#create left sublist
    Right_sublist = L[mid : ]  					#create right sublist
    Mid_list1 = supersort(Left_sublist, 0, len(Left_sublist))   #apply supersort on left sublist
    Mid_list2 = supersort(Right_sublist, 0, len(Right_sublist))	#apply supersort on right sublist

    intermediate_sorted_2 = merge(Mid_list1, Mid_list2)    	#merge left and right sorted sublist

    #Display the intermediate states of the lists to trace the algorithm (commented):
	
    #print("\nThe list L is: ", L)
    #print("The list forward sorted list is: ", Forward_sorted_list)
    #print("The list backward sorted is: ", Backward_sorted_list)
    #print("The intermediate merged list from forward and backward sorted list is: ", intermediate_sorted_1)
    #print("The intermediate merged list from merging left and right sublist is: ", intermediate_sorted_2)
    return(merge(intermediate_sorted_1, intermediate_sorted_2))

print("\n\nThe input list is:  ", L)
#Call to the sorting function
sorted_list = supersort(L, 0, len(L))	
print("\nThe sorted list is: ", sorted_list)













