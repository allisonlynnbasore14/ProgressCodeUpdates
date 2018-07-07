
def wrapStringInHTML(program, body):
    import datetime
    from webbrowser import open_new_tab

    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = program + '.html'
    f = open(filename,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>%s</p></body>
    </html>"""

    whole = wrapper % (program, now, body)
    f.write(whole)
    f.close()

    open_new_tab(filename)

def uploadToGit():
	from git import Repo

	repo_dir = 'mathematics'
	repo = Repo(repo_dir)
	file_list = [
	    'numerical_analysis/regression_analysis/simple_regression_analysis.py',
	    'numerical_analysis/regression_analysis/simple_regression_analysis.png'
	]
	commit_message = 'Add simple regression analysis'
	repo.index.add(file_list)
	repo.index.commit(commit_message)
	origin = repo.remote('origin')
	origin.push()


text = 'TESTING TESTING' # webPageToText(url)

# compile dictionary into string and wrap with HTML
outstring = ""
for s in text:
    outstring += str(s)
    outstring += "<br />"
wrapStringInHTML("UpdatedCodes", outstring)