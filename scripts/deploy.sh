#!/bin/bash
# Publishing of the site


DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)'/..'
DIR_OUTPUT="$DIR/output"


# Compile Pelican site
touch "$DIR/content"  # prevent caching
pelican "$DIR/content" -o "$DIR_OUTPUT" -s "$DIR/config/production.py"


# Remove unnecessary stuff
rm -rf \
    "$DIR_OUTPUT/author" \
    "$DIR_OUTPUT/category" \
    "$DIR_OUTPUT/drafts" \
    "$DIR_OUTPUT/tag" \
    "$DIR_OUTPUT/feeds" \
    "$DIR_OUTPUT/tags.html" \
    "$DIR_OUTPUT/authors.html" \
    "$DIR_OUTPUT/categories.html"


# Configuring Git
if [ ! -z "$CI" ]; then
  git config user.name "$(git show --format="%cN" -s | tr -d '\n')"
  git config user.email "$(git show --format="%cE" -s | tr -d '\n')"
  git remote set-url origin "https://$GITHUB_TOKEN@github.com/honzajavorek/prazeni.honzajavorek.cz.git" > /dev/null 2>&1
fi


# Deploy to GitHub Pages
ghp-import -m 'Published :notebook_with_decorative_cover:' "$DIR_OUTPUT"
git push origin gh-pages -f > /dev/null 2>&1
