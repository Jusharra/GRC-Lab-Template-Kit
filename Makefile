.PHONY: test lint package clean report
test:
	pytest -q
lint:
	flake8 src tests
package:
	./scripts/deploy.sh dev
report:
	./scripts/run_report.sh
clean:
	rm -rf .pytest_cache build dist .coverage *.zip
