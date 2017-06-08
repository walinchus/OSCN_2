# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
import scraperwiki
import lxml.html
import mechanize


br = mechanize.Browser()
br.set_handle_robots( False )
br.open("http://www.oscn.net/dockets/Search.aspx")
for f in br.forms():
    print f

'''formcount=0
for frm in br.forms():  
if str(frm.attrs["id"])=="sblock":
    break
    formcount=formcount+1
br.select_form(nr=formcount)'''
br.select_form('form')
br.form[ 'db' ] = 'garfield'

#Get the search results

br.submit()
    
    
    
    
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
