# open the file - and read all of the lines.
changes_file = 'changes_python.log'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()
def readfile(changes_file):
	data = [line.strip() for line in open(changes_file, 'r')]
	return data

# print the number of lines read

# Opening the log file to star the "clean".
file = 'changes_python.log'
data = readfile(file)

print(len(data))
# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits
commits = get_commits(data)


if __name__ == '__main__':
    
    # Print the total number of lines in data.
    print len(data)
    
    # Print the number of commit objects the list contains. It should be 422.
    print len(commits)
    
    # Print to see 1st, 2nd and 3rd elements in commits list. 
    # Print only specific keys for 2nd and 3rd elements/dictionaries.
    print(commits[0])
    print(commits[1]["author"])
    print(commits[2]["date"])
	


# Export commits list in a csv format.
import csv
with open("changes.csv", "w") as cfile:
    header = ["revision", "date", "author", "number_of_lines"]
    mywriter = csv.DictWriter(cfile, fieldnames = header, delimiter=',', lineterminator='\n',)
    # Give a header to the file with set keys.
    mywriter.writeheader()
    # Iterate over the list and add each commit object as a row to the file.
    index = 0
    while index < len(commits):
        mywriter.writerow(commits[index])
        index = index + 1


#for index, commit in enumerate(commits):
     #print(commit.get_commit_comment())
	 

