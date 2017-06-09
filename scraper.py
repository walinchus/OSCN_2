# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
import scraperwiki
import lxml.html
import mechanize

def scrape_table(root):
    #grab all table rows <tr> in table class="tblSearchResults"
    rows = root.cssselect("table.caseCourtTable tr")
    #create an ID number set at 0 - will add 1 every time we store a record (below)
    idno = 0
    #create a record to hold the data
    record = {}
    #for each row, loop through this
    for row in rows:
        #create a list of all cells <td> in that row
        table_cells = row.cssselect("td")
        if table_cells: 
        #if there is a cell, record the contents in our dataset, the first cell [0] in 'recipient' and so on
            record['Case Number'] = table_cells[0].text_content()
            record['Date Filed'] = table_cells[1].text_content()
            #this line adds 1 to the ID no. we set at 0 earlier
            #idno=idno+1
            #record['ID'] = idno 
            record['Caption'] = table_cells[2].text_content()
            record['Found Party'] = table_cells[3].text_content()
            table_cellsurls = table_cells[0].cssselect("a")
            #grab the href=" attribute of the first <a ... and store
            record['URL'] = table_cellsurls[0].attrib.get('href')
                # Print out the data we've gathered
            print record, '------------'
            # Save the record to the datastore - 'ID' is our unique key - 
            scraperwiki.sqlite.save(["Case Number"], record)



br = mechanize.Browser()
br.set_handle_robots( False )
br.open("http://www.oscn.net/dockets/Search.aspx")
for f in br.forms():
    print f

'''formcount=0
for frm in br.forms():  
    if frm.attrs[class] == "search-form":
        break
        formcount=formcount+1
        br.select_form(nr=formcount)
#br.select_form('form')
        br.form[ 'db' ] = ['garfield',]

#Get the search results

        br.submit()'''

br.select_form(nr=0)
print br.form
br['db'] = ['garfield']
print br
response = br.submit()
html = response.read()
print html
root = lxml.html.fromstring(html)
scrape_table(root)

    
    
    
    
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
