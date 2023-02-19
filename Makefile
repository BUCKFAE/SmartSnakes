doc:
	@echo "Deleting old documentation"
	rm -rf docs/build
	rm -rf docs/source/_autosummary

	@echo "Generating documentation"
	@cd docs && make html
