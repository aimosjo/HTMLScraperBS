# testing script to check on outputs of calls of functions

import url2HTML
import url2domain
import HTML2filterstring
import filterstring2commastring
import commastring2listofatt

att = HTML2filterstring.filterHTML("www.worldpopulationreview.com.html",tag='td').split(',')
print(filterstring2commastring.commastring(att))

# att2 = HTML2filterstring.filterHTML("www.univsearch.com.html", cssid = 'tabbed').split('\n')
#print(filterstring2commastring.commastring(att2))

commastring2listofatt.commaatt(filterstring2commastring.commastring(att), 9)

# commastring2listofatt.commaatt(filterstring2commastring.commastring(att2), 3)