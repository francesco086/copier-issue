MKDOCS_INSTALLED_VERSION=$(pip list | grep 'mkdocs-material ' | sed 's;mkdocs-material *;;')

echo "${MKDOCS_INSTALLED_VERSION} latest"
