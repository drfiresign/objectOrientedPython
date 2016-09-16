# Template list goes here:
templates = []
templates.sort()
url = "https://www.squarespace.com/websites/templates/"

f = open('templates.csv', 'w')
for template in templates:
    f.write("@{},[{}]({}{})\n".format(template.lower(), template.title(), url,
                                      template.lower()))

f.close()
