init:
	uv sync

lint:
	uv run ruff check .
	uv run mypy .

test:
	uv run pytest -q --disable-warnings

ci: lint test