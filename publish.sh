#!/bin/bash

# Check if version parameter is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <version>"
  exit 1
fi

VERSION=$1

# Update the version in galaxy.yml
if [[ "$(uname)" == "Darwin" ]]; then
  sed -i '' "s/^version:.*/version: $VERSION/" galaxy.yml
else
  sed -i "s/^version:.*/version: $VERSION/" galaxy.yml
fi

git add galaxy.yml
git commit -m "Update the version to $VERSION"
git push

# Build the collection
ansible-galaxy collection build

# Find the built tarball
TARBALL=$(ls -t *.tar.gz | head -n 1)

ansible-galaxy collection publish "$TARBALL"

# Tag the version in git and push the tag
git tag $VERSION
git push --tags

echo "Collection version $VERSION published to Ansible Galaxy and tagged in git."

rm -f $TARBALL
