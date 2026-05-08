SAGE = sage
PACKAGE = simple_sagemath_package

all: install ptest

install:
	$(SAGE) -pip install --upgrade -e .

logs:
	mkdir -p logs
test: logs
	$(SAGE) -t --force-lib --log=logs/test.log $(PACKAGE) demos
testlong: logs
	$(SAGE) -t --force-lib --long --log=logs/testlong.log $(PACKAGE) demos
ptest: logs
	$(SAGE) -tp --force-lib --log=logs/ptest.log $(PACKAGE) demos
ptestlong: logs
	$(SAGE) -tp --force-lib --long --log=logs/ptestlong.log $(PACKAGE) demos

coverage:
	$(SAGE) -coverage $(PACKAGE)/*

doc:install
	cd docs && $(SAGE) -sh -c "make clean && make html"
doc-pdf:install
	cd docs && $(SAGE) -sh -c "make latexpdf"

dist:
	$(SAGE) -python -m build
check: dist
	VERSION=`cat VERSION`; $(SAGE) -sh -c "twine check dist/$(PACKAGE)-$$VERSION.tar.gz"
upload: dist
	VERSION=`cat VERSION`; $(SAGE) -sh -c "twine upload dist/$(PACKAGE)-$$VERSION.tar.gz --repository $(PACKAGE)"

clean: clean-doc
clean-doc:
	cd docs && $(SAGE) -sh -c "make clean"

.PHONY: all install develop logs test coverage clean clean-doc doc doc-pdf dist upload
