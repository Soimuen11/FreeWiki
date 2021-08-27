# The Free Wiki Project

## Access github pages from here

[click on this link](https://soimuen11.github.io/FreeWiki/)

## to-dos

1. write mini tuto how to get jekyll + gh-pages up and running
2. separate content into pages instead of sections

## tuto

+ on github:
	1. create a new repo without a readme

+ on your local machine:
	1. Install ruby
	2. Gem install bundler jekyll
	3. jekyll new $project-name OR cd into the repo you cloned from github
	4. run "bundler init"
	5. go to https://rubygems.org/ 
		+ search for a theme
		+ look for LINKS section and click on HOMEPAGE
		+ this will redirect you to the github repo
		+ copy the content of the _layouts folder from that repo
		+ modify your pages layout accordingly
	7. add name of your theme to \_config.yml & Gemfile
	8. run: "bundler install"
	9. run: "bundler exec jekyll serve" to check if your site works locally

+ For the midnight theme, which is the one this wiki uses:
	- [repo link](https://github.com/pages-themes/midnight)
	- [ruby gems link](https://rubygems.org/gems/jekyll-theme-midnight)
