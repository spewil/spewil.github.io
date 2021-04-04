mkdir adjusted
for f in *.JPG
do convert $f -normalize -modulate 100,130,100 adjusted/$f.jpg
done
