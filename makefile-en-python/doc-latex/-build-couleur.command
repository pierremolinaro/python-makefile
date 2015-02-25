#!/bin/sh
set -x
DIR=`dirname $0` &&
cd $DIR &&
rm -f bdd-couleur.pdf &&
#--- First pass
/usr/texbin/pdflatex --file-line-error --shell-escape '\newcommand\afficherDetailSchema{false}\input{livre-bdd.tex}' &&
touch ref.idx &&
#touch ref.lof &&
#touch ref.lot &&
#touch ref.prgm-spice &&
touch ref.toc &&
iteration=0 &&
while [ `cmp -s ref.idx livre-bdd.idx ; echo $?` -ne 0 ] \
    || [ `cmp -s ref.toc livre-bdd.toc ; echo $?` -ne 0 ] \
#   || [ `cmp -s ref.lot livre-bdd.lot ; echo $?` -ne 0 ] \
#   || [ `cmp -s ref.prgm-spice livre-bdd.prgm-spice ; echo $?` -ne 0 ] \
#   || [ `cmp -s ref.lof livre-bdd.lof ; echo $?` -ne 0 ]
do
  cp livre-bdd.idx ref.idx &&
#  cp livre-bdd.lof ref.lof &&
#  cp livre-bdd.lot ref.lot &&
#  cp livre-bdd.prgm-spice ref.prgm-spice &&
  cp livre-bdd.toc ref.toc &&
  /usr/texbin/makeindex -s $DIR/fichiers-inclus/style-indexes.ist livre-bdd.idx &&
  /usr/texbin/pdflatex --file-line-error --shell-escape '\newcommand\afficherDetailSchema{false}\input{livre-bdd.tex}' &&
  iteration=$((iteration+=1))
done &&
cp livre-bdd.pdf livre-bdd-couleur.pdf &&
echo "---------------- SUCCES $iteration iterations"
