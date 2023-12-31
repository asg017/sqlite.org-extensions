# `sqlite.org-extensions`

The [official SQLite source code repository](https://sqlite.org/src/doc/trunk/README.md) has dozens of SQLite extensions for various real-world, debugging, and testing purposes. They are just plain C files that you normally have to compile yourself.

So `sqlite.org-extensions` aims to provide pre-compiled and re-distributed version of most of this extensions, so you don't have to worry about building it yourself.

This project is still early, not complete yet. The extensions are provided "as-is" with the exact same source code as listed in the official repository. While the SQLite codebase is in the public domain, consider this specific repository MIT + Apache 2.0 licensed.

| Extension    | Source                                                                                | Description |
| ------------ | ------------------------------------------------------------------------------------- | ----------- |
| anycollseq   | [`ext/misc/anycollseq.c`](https://sqlite.org/src/file?name=ext/misc/anycollseq.c)     |             |
| fts5         | [`ext/fts5`](https://sqlite.org/src/dir?ci=trunk&name=ext/fts5)                       |             |
| amatch       | [`ext/misc/amatch.c`](https://sqlite.org/src/file?name=ext/misc/amatch.c)             |             |
| appendvfs    | [`ext/misc/appendvfs.c`](https://sqlite.org/src/file?name=ext/misc/appendvfs.c)       |             |
| base64       | [`ext/misc/base64.c`](https://sqlite.org/src/file?name=ext/misc/base64.c)             |             |
| base85       | [`ext/misc/base85.c`](https://sqlite.org/src/file?name=ext/misc/base85.c)             |             |
| basexx       | [`ext/misc/basexx.c`](https://sqlite.org/src/file?name=ext/misc/basexx.c)             |             |
| blobio       | [`ext/misc/blobio.c`](https://sqlite.org/src/file?name=ext/misc/blobio.c)             |             |
| btreeinfo    | [`ext/misc/btreeinfo.c`](https://sqlite.org/src/file?name=ext/misc/btreeinfo.c)       |             |
| cksumvfs     | [`ext/misc/cksumvfs.c`](https://sqlite.org/src/file?name=ext/misc/cksumvfs.c)         |             |
| closure      | [`ext/misc/closure.c`](https://sqlite.org/src/file?name=ext/misc/closure.c)           |             |
| completion   | [`ext/misc/completion.c`](https://sqlite.org/src/file?name=ext/misc/completion.c)     |             |
| csv          | [`ext/misc/csv.c`](https://sqlite.org/src/file?name=ext/misc/csv.c)                   |             |
| decimal      | [`ext/misc/decimal.c`](https://sqlite.org/src/file?name=ext/misc/decimal.c)           |             |
| eval         | [`ext/misc/eval.c`](https://sqlite.org/src/file?name=ext/misc/eval.c)                 |             |
| explain      | [`ext/misc/explain.c`](https://sqlite.org/src/file?name=ext/misc/explain.c)           |             |
| fileio       | [`ext/misc/fileio.c`](https://sqlite.org/src/file?name=ext/misc/fileio.c)             |             |
| fossildelta  | [`ext/misc/fossildelta.c`](https://sqlite.org/src/file?name=ext/misc/fossildelta.c)   |             |
| fuzzer       | [`ext/misc/fuzzer.c`](https://sqlite.org/src/file?name=ext/misc/fuzzer.c)             |             |
| ieee754      | [`ext/misc/ieee754.c`](https://sqlite.org/src/file?name=ext/misc/ieee754.c)           |             |
| memstat      | [`ext/misc/memstat.c`](https://sqlite.org/src/file?name=ext/misc/memstat.c)           |             |
| memvfs       | [`ext/misc/memvfs.c`](https://sqlite.org/src/file?name=ext/misc/memvfs.c)             |             |
| nextchar     | [`ext/misc/nextchar.c`](https://sqlite.org/src/file?name=ext/misc/nextchar.c)         |             |
| noop         | [`ext/misc/noop.c`](https://sqlite.org/src/file?name=ext/misc/noop.c)                 |             |
| percentile   | [`ext/misc/percentile.c`](https://sqlite.org/src/file?name=ext/misc/percentile.c)     |             |
| prefixes     | [`ext/misc/prefixes.c`](https://sqlite.org/src/file?name=ext/misc/prefixes.c)         |             |
| qpvtab       | [`ext/misc/qpvtab.c`](https://sqlite.org/src/file?name=ext/misc/qpvtab.c)             |             |
| regexp       | [`ext/misc/regexp.c`](https://sqlite.org/src/file?name=ext/misc/regexp.c)             |             |
| remember     | [`ext/misc/remember.c`](https://sqlite.org/src/file?name=ext/misc/remember.c)         |             |
| rot13        | [`ext/misc/rot13.c`](https://sqlite.org/src/file?name=ext/misc/rot13.c)               |             |
| series       | [`ext/misc/series.c`](https://sqlite.org/src/file?name=ext/misc/series.c)             |             |
| sha1         | [`ext/misc/sha1.c`](https://sqlite.org/src/file?name=ext/misc/sha1.c)                 |             |
| shathree     | [`ext/misc/shathree.c`](https://sqlite.org/src/file?name=ext/misc/shathree.c)         |             |
| showauth     | [`ext/misc/showauth.c`](https://sqlite.org/src/file?name=ext/misc/showauth.c)         |             |
| spellfix     | [`ext/misc/spellfix.c`](https://sqlite.org/src/file?name=ext/misc/spellfix.c)         |             |
| stmt         | [`ext/misc/stmt.c`](https://sqlite.org/src/file?name=ext/misc/stmt.c)                 |             |
| templatevtab | [`ext/misc/templatevtab.c`](https://sqlite.org/src/file?name=ext/misc/templatevtab.c) |             |
| totype       | [`ext/misc/totype.c`](https://sqlite.org/src/file?name=ext/misc/totype.c)             |             |
| uint         | [`ext/misc/uint.c`](https://sqlite.org/src/file?name=ext/misc/uint.c)                 |             |
| unionvtab    | [`ext/misc/unionvtab.c`](https://sqlite.org/src/file?name=ext/misc/unionvtab.c)       |             |
| urifuncs     | [`ext/misc/urifuncs.c`](https://sqlite.org/src/file?name=ext/misc/urifuncs.c)         |             |
| uuid         | [`ext/misc/uuid.c`](https://sqlite.org/src/file?name=ext/misc/uuid.c)                 |             |
| vfsstat      | [`ext/misc/vfsstat.c`](https://sqlite.org/src/file?name=ext/misc/vfsstat.c)           |             |
| vtablog      | [`ext/misc/vtablog.c`](https://sqlite.org/src/file?name=ext/misc/vtablog.c)           |             |
| vtshim       | [`ext/misc/vtshim.c`](https://sqlite.org/src/file?name=ext/misc/vtshim.c)             |             |
| wholenumber  | [`ext/misc/wholenumber.c`](https://sqlite.org/src/file?name=ext/misc/wholenumber.c)   |             |
| zorder       | [`ext/misc/zorder.c`](https://sqlite.org/src/file?name=ext/misc/zorder.c)             |             |
