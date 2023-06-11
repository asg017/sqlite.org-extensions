import sqlite3
import unittest

EXTENSIONS = [
    "compress",
    "sqlar",
    "zipfile",
    "vfslog",
    "dbdump",
    "anycollseq",
    "amatch",
    "appendvfs",
    "base64",
    "base85",
    "basexx",
    "blobio",
    "btreeinfo",
    "cksumvfs",
    "closure",
    "completion",
    "csv",
    "decimal",
    "eval",
    "explain",
    "fileio",
    "fossildelta",
    "fuzzer",
    "ieee754",
    "memstat",
    "memvfs",
    "nextchar",
    "noop",
    "percentile",
    "prefixes",
    "qpvtab",
    "regexp",
    "remember",
    "rot13",
    "rtree",
    "series",
    "sha1",
    "shathree",
    "showauth",
    "spellfix",
    "stmt",
    "templatevtab",
    "totype",
    "uint",
    "unionvtab",
    "urifuncs",
    "uuid",
    "vfsstat",
    "vtablog",
    "vtshim",
    "wholenumber",
    "zorder",
]


def connect(ext):
    db = sqlite3.connect(":memory:")

    db.execute("create table base_functions as select name from pragma_function_list")
    db.execute("create table base_collations as select name from pragma_collation_list")
    db.execute("create table base_modules as select name from pragma_module_list")

    db.enable_load_extension(True)
    db.load_extension(ext)

    db.execute(
        "create temp table loaded_functions as select name from pragma_function_list where name not in (select name from base_functions) order by name"
    )
    db.execute(
        "create temp table loaded_modules as select name from pragma_module_list where name not in (select name from base_modules) order by name"
    )
    db.execute(
        "create temp table loaded_collations as select name from pragma_collation_list where name not in (select name from base_collations) order by name"
    )

    db.row_factory = sqlite3.Row
    return db


def loaded_funcs(db):
    return list(
        map(lambda a: a[0], db.execute("select name from loaded_functions").fetchall())
    )


def loaded_modules(db):
    return list(
        map(lambda a: a[0], db.execute("select name from loaded_modules").fetchall())
    )


def loaded_collations(db):
    return list(
        map(lambda a: a[0], db.execute("select name from loaded_collations").fetchall())
    )


class TestExts(unittest.TestCase):
    def test_anycollseq(self):
        db = connect("./dist/anycollseq")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_amatch(self):
        db = connect("./dist/amatch")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["approximate_match"])
        self.assertEqual(loaded_collations(db), [])

    def test_appendvfs(self):
        db = connect("./dist/appendvfs")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_base64(self):
        db = connect("./dist/base64")
        self.assertEqual(loaded_funcs(db), ["base64"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_base85(self):
        db = connect("./dist/base85")
        self.assertEqual(loaded_funcs(db), ["base85", "is_base85"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_basexx(self):
        db = connect("./dist/basexx")
        self.assertEqual(loaded_funcs(db), ["base64", "base85", "is_base85"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_blobio(self):
        db = connect("./dist/blobio")
        self.assertEqual(loaded_funcs(db), ["readblob", "writeblob"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_btreeinfo(self):
        db = connect("./dist/btreeinfo")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["sqlite_btreeinfo"])
        self.assertEqual(loaded_collations(db), [])

    def test_cksumvfs(self):
        db = connect("./dist/cksumvfs")
        self.assertEqual(loaded_funcs(db), ["verify_checksum"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_closure(self):
        db = connect("./dist/closure")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["transitive_closure"])
        self.assertEqual(loaded_collations(db), [])

    def test_completion(self):
        db = connect("./dist/completion")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["completion"])
        self.assertEqual(loaded_collations(db), [])

    def test_csv(self):
        db = connect("./dist/csv")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["csv"])
        self.assertEqual(loaded_collations(db), [])

    def test_decimal(self):
        db = connect("./dist/decimal")
        self.assertEqual(
            loaded_funcs(db),
            [
                "decimal",
                "decimal_add",
                "decimal_cmp",
                "decimal_mul",
                "decimal_sub",
                "decimal_sum",
            ],
        )
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), ["decimal"])

    def test_eval(self):
        db = connect("./dist/eval")
        self.assertEqual(loaded_funcs(db), ["eval", "eval"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_explain(self):
        db = connect("./dist/explain")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["explain"])
        self.assertEqual(loaded_collations(db), [])

    def test_fileio(self):
        db = connect("./dist/fileio")
        self.assertEqual(loaded_funcs(db), ["lsmode", "readfile", "writefile"])
        self.assertEqual(loaded_modules(db), ["fsdir"])
        self.assertEqual(loaded_collations(db), [])

    def test_fossildelta(self):
        db = connect("./dist/fossildelta")
        self.assertEqual(
            loaded_funcs(db), ["delta_apply", "delta_create", "delta_output_size"]
        )
        self.assertEqual(loaded_modules(db), ["delta_parse"])
        self.assertEqual(loaded_collations(db), [])

    def test_fuzzer(self):
        db = connect("./dist/fuzzer")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["fuzzer"])
        self.assertEqual(loaded_collations(db), [])

    def test_ieee754(self):
        db = connect("./dist/ieee754")
        self.assertEqual(
            loaded_funcs(db),
            [
                "ieee754",
                "ieee754",
                "ieee754_exponent",
                "ieee754_from_blob",
                "ieee754_mantissa",
                "ieee754_to_blob",
            ],
        )
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_memstat(self):
        db = connect("./dist/memstat")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["sqlite_memstat"])
        self.assertEqual(loaded_collations(db), [])

    def test_memvfs(self):
        db = connect("./dist/memvfs")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_nextchar(self):
        db = connect("./dist/nextchar")
        self.assertEqual(loaded_funcs(db), ["next_char", "next_char", "next_char"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_noop(self):
        db = connect("./dist/noop")
        self.assertEqual(loaded_funcs(db), ["noop", "noop_do", "noop_i", "noop_nd"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_percentile(self):
        db = connect("./dist/percentile")
        self.assertEqual(loaded_funcs(db), ["percentile"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_prefixes(self):
        db = connect("./dist/prefixes")
        self.assertEqual(loaded_funcs(db), ["prefix_length"])
        self.assertEqual(loaded_modules(db), ["prefixes"])
        self.assertEqual(loaded_collations(db), [])

    def test_qpvtab(self):
        db = connect("./dist/qpvtab")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["qpvtab"])
        self.assertEqual(loaded_collations(db), [])

    def test_regexp(self):
        db = connect("./dist/regexp")
        self.assertEqual(loaded_funcs(db), ["regexp", "regexpi"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_remember(self):
        db = connect("./dist/remember")
        self.assertEqual(loaded_funcs(db), ["remember"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_rot13(self):
        db = connect("./dist/rot13")
        self.assertEqual(loaded_funcs(db), ["rot13"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), ["rot13"])

    def test_rtree(self):
        db = connect("./dist/rtree")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_series(self):
        db = connect("./dist/series")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["generate_series"])
        self.assertEqual(loaded_collations(db), [])

    def test_sha1(self):
        db = connect("./dist/sha1")
        self.assertEqual(loaded_funcs(db), ["sha1", "sha1_query"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_shathree(self):
        db = connect("./dist/shathree")
        self.assertEqual(loaded_funcs(db), ["sha3", "sha3", "sha3_query", "sha3_query"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_showauth(self):
        db = connect("./dist/showauth")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_spellfix(self):
        db = connect("./dist/spellfix")
        self.assertEqual(
            loaded_funcs(db),
            [
                "editdist3",
                "editdist3",
                "editdist3",
                "spellfix1_editdist",
                "spellfix1_phonehash",
                "spellfix1_scriptcode",
                "spellfix1_translit",
            ],
        )
        self.assertEqual(loaded_modules(db), ["spellfix1"])
        self.assertEqual(loaded_collations(db), [])

    def test_stmt(self):
        db = connect("./dist/stmt")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["sqlite_stmt"])
        self.assertEqual(loaded_collations(db), [])

    def test_templatevtab(self):
        db = connect("./dist/templatevtab")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["templatevtab"])
        self.assertEqual(loaded_collations(db), [])

    def test_totype(self):
        db = connect("./dist/totype")
        self.assertEqual(loaded_funcs(db), ["tointeger", "toreal"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_uint(self):
        db = connect("./dist/uint")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), ["uint"])

    def test_unionvtab(self):
        db = connect("./dist/unionvtab")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["swarmvtab", "unionvtab"])
        self.assertEqual(loaded_collations(db), [])

    def test_urifuncs(self):
        db = connect("./dist/urifuncs")
        self.assertEqual(
            loaded_funcs(db),
            [
                "sqlite3_db_filename",
                "sqlite3_filename_database",
                "sqlite3_filename_journal",
                "sqlite3_filename_wal",
                "sqlite3_uri_boolean",
                "sqlite3_uri_int64",
                "sqlite3_uri_key",
                "sqlite3_uri_parameter",
            ],
        )
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_uuid(self):
        db = connect("./dist/uuid")
        self.assertEqual(loaded_funcs(db), ["uuid", "uuid_blob", "uuid_str"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_vfsstat(self):
        db = connect("./dist/vfsstat")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["vfsstat"])
        self.assertEqual(loaded_collations(db), [])

    def test_vtablog(self):
        db = connect("./dist/vtablog")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["vtablog"])
        self.assertEqual(loaded_collations(db), [])

    def test_vtshim(self):
        db = connect("./dist/vtshim")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])

    def test_wholenumber(self):
        db = connect("./dist/wholenumber")
        self.assertEqual(loaded_funcs(db), [])
        self.assertEqual(loaded_modules(db), ["wholenumber"])
        self.assertEqual(loaded_collations(db), [])

    def test_zorder(self):
        db = connect("./dist/zorder")
        self.assertEqual(loaded_funcs(db), ["unzorder", "zorder"])
        self.assertEqual(loaded_modules(db), [])
        self.assertEqual(loaded_collations(db), [])


class TestCoverage(unittest.TestCase):
    def test_coverage(self):
        test_methods = [
            method for method in dir(TestExts) if method.startswith("test_")
        ]
        extensions_with_tests = set([x.replace("test_", "") for x in test_methods])
        for extension in EXTENSIONS:
            self.assertTrue(
                extension in extensions_with_tests,
                f"{extension} does not have corresponding test in TestExts",
            )


if __name__ == "__main__":
    unittest.main()
