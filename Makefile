TAILWIND_VERSION = 4.3.1
TAILWIND_BIN = /tmp/tailwindcss-$(TAILWIND_VERSION)
TAILWIND_INPUT = src/interface/web/static/css/input.css
TAILWIND_OUTPUT = src/interface/web/static/css/styles.css

$(TAILWIND_BIN):
	curl -sL https://github.com/tailwindlabs/tailwindcss/releases/download/v$(TAILWIND_VERSION)/tailwindcss-linux-x64 -o $@ && chmod +x $@

.PHONY: css
css: $(TAILWIND_BIN)
	$(TAILWIND_BIN) --input $(TAILWIND_INPUT) --output $(TAILWIND_OUTPUT) --minify

.PHONY: css-watch
css-watch: $(TAILWIND_BIN)
	$(TAILWIND_BIN) --input $(TAILWIND_INPUT) --output $(TAILWIND_OUTPUT) --watch

HTMX_VERSION = 2.0.4
JS_DIR = src/interface/web/static/js

.PHONY: vendor-htmx
vendor-htmx:
	curl -sL https://unpkg.com/htmx.org@$(HTMX_VERSION)/dist/htmx.min.js -o $(JS_DIR)/htmx.min.js