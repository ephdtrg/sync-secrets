.PHONY: install

.DEFAULT: sync-secrets

sync-secrets:
	@echo ${BACKUP_DIR}
	mkdir -p build
	cp sync-secrets.py build/sync-secrets
	sed -i 's#BACKUP_ROOT =.*#BACKUP_ROOT = "${BACKUP_DIR}"#g' build/sync-secrets

install:
	cp build/sync-secrets ~/.local/bin/sync-secrets

clean:
	rm -rf build
