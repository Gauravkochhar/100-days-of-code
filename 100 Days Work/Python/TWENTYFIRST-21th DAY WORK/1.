# The first line of input contains the original string. The next line contains the substring.
# Output the integer number indicating the total number of occurrences of the substring in the original string.

#input Sample:
#    ABCDCDC
#    CDC

#output Sample:
#    2



def count_substring(string, sub_string):
    index=0
    count=0
    substring_length=len(sub_string)
    for i in range(len(string)):
        if(string[i:i+substring_length]==sub_string):
            index=i
            count=count+1
    return count
if __name__=="_main__":
    string=list(input().lower())
    substring=list(input().lower())
    count=count_substring(string,substring)
    print(count)
    
