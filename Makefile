PYTHON = python3

VENV      = venv
ACTIVATE := . $(VENV)/bin/activate

DOCKER = docker
TESTDB = cow-test-db

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