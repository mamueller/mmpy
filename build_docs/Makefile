# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
MODULESDIR    = ../src/mmpy
PUBDIR        = ../docs
INDEXF	      =	source/index.rst
INDEXFB	      =	$(INDEXF).bak
# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: api-doc
api-doc:
	if test -e $(INDEXF) ;then mv $(INDEXF) $(INDEXFB); fi
	rm -f source/*.rst
	sphinx-apidoc --module-first --separate -o $(SOURCEDIR)/ --ext-autodoc  $(MODULESDIR) # $(APIDOCIGNORE1) $(APIDOCIGNORE2)
	#rm source/ACGCA.rst source/modules.rst
	mv $(INDEXFB) $(INDEXF)

.PHONY: html
html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

.PHONY: publish 
publish:
	if test -d $(PUBDIR); then rm -rf $(PUBDIR)/* ;else mkdir $(PUBDIR);fi 
	@cp -r $(BUILDDIR)/html/* $(PUBDIR)
	@touch $(PUBDIR)/.nojekyll # tell github to serve plain html

.PHONY: show 
show: api-doc html publish	 
	firefox $(PUBDIR)/index.html	
