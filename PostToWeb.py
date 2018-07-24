
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

    #open_new_tab(filename)

def uploadToGit():
    # curl -i https://api.github.com -u valid_username:valid_password
	from git import Repo

	repo_dir = ''
	repo = Repo(repo_dir)
    #assert not repo.bare
	file_list = [
	    'docs/index.html',
        'PostToWeb.py'
	]
	commit_message = 'Updated Codes To Web Daily'
	repo.index.add(file_list)
	repo.index.commit(commit_message)
	origin = repo.remote('origin')
	origin.push()


#text = 'Yellow Cats' # webPageToText(url)

# compile dictionary into string and wrap with HTML
#outstring = ""
#for s in text:
 #   outstring += str(s)
  #  outstring += "<br />"
#wrapStringInHTML("docs/index", outstring)
#uploadToGit()
