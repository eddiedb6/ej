rm ../htdocs/php/generated/*.php -rf
rm ../htdocs/css/generated/*.css -rf
rm ../htdocs/js/generated/*.js -rf
rm ../pdb/generated/*.mysql -rf
rm ../pdb/generated/*.sh -rf

find .. -name "*~" | xargs rm -rf
find .. -name "*.pyc" | xargs rm -rf
