def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if sub_string in string[i:i+len(sub_string)]:
            count=count+1
    return count
