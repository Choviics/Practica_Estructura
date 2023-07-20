# Python3 program to find the
# length of the longest substring
# without repeating characters
def longestUniqueSubsttr(str):
	
	n = len(str)
	
	# Result
	res = 0

	for i in range(n):
		
		# Note : Default values in
		# visited are false
		visited = [0] * 256

		for j in range(i, n):

			# If current character is visited
			# Break the loop
			if (visited[ord(str[j])] == True):
				break

			# Else update the result if
			# this window is larger, and mark
			# current character as visited.
			else:
				res = max(res, j - i + 1)
				visited[ord(str[j])] = True
			
		# Remove the first character of previous
		# window
		visited[ord(str[i])] = False
	
	return res

# Driver code
str = input("write a sentence: ")
print("The input is ", str)

len = longestUniqueSubsttr(str)
print("The length of the longest "
	"non-repeating character substring is ", len)
