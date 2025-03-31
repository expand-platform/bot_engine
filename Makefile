test:
	poetry run pytest -s tests/

test-clean:
	poetry run pytest tests/

save:
	git add . && git commit

build:
	rm dist -r && poetry build

release:
	rm dist -r && poetry build && twine upload dist/*

publish:
	poetry publish --build --repository pypi

twine:
	twine upload dist/*

search: 
	poetry search bot-engine


# install-locally:
# 	pip install dist/bot_engine-0.1.0-py3-none-any.whl

