# !!! Replace the content of this file with your own !!!
# This script will run in a container of your Docker image.
# This script must return (by means of an `echo` command)
# the tags that should be used when pushing the docker image.
# You can return multiple tags by using a space as a separator.
# Examples:
#
# - echo "latest"                     ---> 1 tag: latest
#
# - echo "latest funny"               ---> 2 tags: latest and funny
#
# - NUMPY_VERSION="$(python -c 'import pydantic; print(pydantic.__version__)')"
#   "echo "latest ${NUMPY_VERSION}".  ---> 2 tags: latest and the installed version of numpy

echo "latest"
