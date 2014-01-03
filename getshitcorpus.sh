echo "select body from post" | psql -A gijs | grep -v '^$' > shit.corpus

