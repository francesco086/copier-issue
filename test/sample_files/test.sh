mkdocs new .
mkdocs build

if [ ! -f site/index.html ]; then
  echo "Expected file site/index.html was not found. mkdocs seems to be broken!"
  exit 1
else
  echo "Expected file site/index.html exists. mkdocs seems to work properly!"
  exit 0
fi