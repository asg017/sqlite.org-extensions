ifndef CC
CC=gcc
endif

ifeq ($(shell uname -s),Darwin)
CONFIG_DARWIN=y
else ifeq ($(OS),Windows_NT)
CONFIG_WINDOWS=y
else
CONFIG_LINUX=y
endif

ifdef CONFIG_DARWIN
LOADABLE_EXTENSION=dylib
endif

ifdef CONFIG_LINUX
LOADABLE_EXTENSION=so
endif


ifdef CONFIG_WINDOWS
LOADABLE_EXTENSION=dll
endif

ifndef prefix
prefix=dist
endif

$(prefix):
	mkdir -p $(prefix)

TARGET_FTS5=$(prefix)/fts5.$(LOADABLE_EXTENSION)
fts5: $(TARGET_FTS5)

$(TARGET_FTS5): sqlite/fts5.c $(prefix)
	$(CC) \
		-fPIC -shared \
		-Isqlite \
		-O3 -Lsqlite/.libs \
		$< \
		-o $@

MISC_PATH=sqlite/ext/misc


MISC_NODEPS = anycollseq \
  amatch \
  appendvfs \
  base64 \
  base85 \
  basexx \
  blobio \
  btreeinfo \
  cksumvfs \
  closure \
  completion \
  csv \
  decimal \
  eval \
  explain \
  fileio \
  fossildelta \
  fuzzer \
  ieee754 \
  memstat \
  memvfs \
  nextchar \
  noop \
  percentile \
  prefixes \
  qpvtab \
  regexp \
  remember \
  rot13 \
  series \
  sha1 \
  shathree \
  showauth \
  spellfix \
  stmt \
  templatevtab \
  totype \
  uint \
  unionvtab \
  urifuncs \
  uuid \
  vfsstat \
  vtablog \
  vtshim \
  wholenumber \
  zorder

MISC_Z = compress sqlar zipfile vfslog dbdump
# MISC_TODO dbdump memtrace mmapwarm normalize scrub vfslog

EXTENSIONS_MISC: $(MISC_NODEPS) $(MISC_Z)

define MISC_NODEPS_template
$(prefix)/$(1).$(LOADABLE_EXTENSION): $(MISC_PATH)/$(1).c $(prefix)
	$(CC) \
		-fPIC -shared \
		-Isqlite \
		-Isqlite/src \
		-O3 \
		$(MISC_PATH)/$(1).c \
		-o $(prefix)/$(1).$(LOADABLE_EXTENSION)

$(prefix)/$(1).a: $(MISC_PATH)/$(1).c $(prefix)
	$(CC) -Isqlite -Isqlite/src -DSQLITE_CORE \
		-O3 -c  $(MISC_PATH)/$(1).c -o $(prefix)/$(1).o
	ar rcs $(prefix)/$(1).a $(prefix)/$(1).o

$(1)-loadable: $(prefix)/$(1).$(LOADABLE_EXTENSION)
$(1)-static: $(prefix)/$(1).a
endef
$(foreach prog,$(MISC_NODEPS),$(eval $(call MISC_NODEPS_template,$(prog))))

define MISC_Z_template
$(prefix)/$(1).$(LOADABLE_EXTENSION): $(MISC_PATH)/$(1).c $(prefix)
	$(CC) \
		-fPIC -shared \
		-Isqlite \
		-Isqlite/src \
		-O3 \
		-lz \
		$(MISC_PATH)/$(1).c \
		-o $(prefix)/$(1).$(LOADABLE_EXTENSION)

$(prefix)/$(1).a: $(MISC_PATH)/$(1).c $(prefix)
	$(CC) -Isqlite -Isqlite/src -DSQLITE_CORE -lz \
		-O3 -c  $(MISC_PATH)/$(1).c -o $(prefix)/$(1).o
	ar rcs $(prefix)/$(1).a $(prefix)/$(1).o

$(prefix)/$(1).h: include/$(1).h
	cp include/$(1).h $(prefix)/$(1).h

$(1)-loadable: $(prefix)/$(1).$(LOADABLE_EXTENSION)
$(1)-static: $(prefix)/$(1).a $(prefix)/$(1).h
endef

#-I/usr/local/opt/zlib/include \
#-L/usr/local/opt/zlib/lib \

$(foreach prog,$(MISC_Z),$(eval $(call MISC_Z_template,$(prog))))


publish-release:
	./scripts/publish_release.sh

all: $(EXTENSIONS_MISC) $(TARGET_FTS5)

clean:
	rm -rf dist/

.PHONY: all $(EXTENSIONS_MISC) clean publish-release
