echo "select body from post" | psql -A gijs | grep -v '^$' > shit.corpus
egrep -v "^20.*/.*/.* .* <.*@\w+\.(com|nl)>(:)*$" shit.corpus > shit2.corpus 
mv shit2.corpus shit.corpus
egrep -v "^Op .* schreef .* <.*@\w+\.(com|nl)>( het volgende)*:" shit.corpus > shit2.corpus
mv shit2.corpus shit.corpus
egrep -v "^Op .* schreef .* <.*@\w+\.(com|nl)> het" shit.corpus > shit2.corpus 
mv shit2.corpus shit.corpus
egrep -v "^volgende:$" shit.corpus > shit2.corpus 
mv shit2.corpus shit.corpus
egrep -v "^Op .* schreef .* <.*@\w+\.(com|nl)>$" shit.corpus > shit2.corpus 
mv shit2.corpus shit.corpus
egrep -v "het volgende:$" shit.corpus > shit2.corpus
mv shit2.corpus shit.corpus
egrep -v "het volgende geschreven:$" shit.corpus > shit2.corpus
mv shit2.corpus shit.corpus
egrep -v ".*@.*\.(com|nl)>" shit.corpus > shit2.corpus
mv shit2.corpus shit.corpus
egrep -v "http" shit.corpus > shit2.corpus
mv shit2.corpus shit.corpus
