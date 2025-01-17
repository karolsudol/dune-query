PYTHON = python3

VENV      = venv
ACTIVATE := . $(VENV)/bin/activate

DOCKER = docker
TESTDB = cow-test-db

INST := $(VENV)/.install
$(INST): requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE); pip install --upgrade pip
	$(ACTIVATE); pip install -r requirements.txt
	touch $@

.PHONY: install
install: $(INST)

.PHONY: clean
clean:
	rm -rf __pycache__ venv

.PHONY: fmt
fmt: install
	$(ACTIVATE); black ./

.PHONY: lint
lint: install
	$(ACTIVATE); pylint src/

.PHONY: types
types: install
	$(ACTIVATE); mypy src/ --strict

.PHONY: check
check: fmt lint types

.PHONY: test-unit
test-unit: install
	$(ACTIVATE); python -m pytest tests/unit

.PHONY: db
db:
	$(DOCKER) build -t $(TESTDB) -f Dockerfile.db .;

.PHONY: test-db
test-db: install db
	if ! $(DOCKER) container inspect $(TESTDB) >/dev/null 2>&1; then \
		$(DOCKER) run --rm -d -p 5432:5432 $(TESTDB) \
		`# sleep just long enough for the machine to recognize the establishing container.` \
		sleep 1s \
	fi
	$(ACTIVATE); python -m pytest tests/db
	$(ACTIVATE); python -m pytest tests/queries