# Full-text search

Zulip supports full-text search. By default, it supports only
English.

TODO: More description.

## The default full-text search implementation

Zulip uses
[PostgreSQL built-in full-text search feature](http://www.postgresql.org/docs/current/static/textsearch.html).

TODO: More description.

## How to enable full-text search against all languages

Zulip also supports [PGroonga](http://pgroonga.github.io/). PGroonga
is a PostgreSQL extension that provides full-text search
feature. PGroonga supports all languages including Japanese, Chinese
and so on.

This section describes how to enable full-text search feature based on
PGroonga.

First, you [install PGroonga](http://pgroonga.github.io/install/).

Then, you grant `USAGE` privilege on `pgroonga` schema to `zulip`
user:

    GRANT USAGE ON SCHEMA pgroonga TO zulip;

See also:
[GRANT USAGE ON SCHEMA pgroonga](http://pgroonga.github.io/reference/grant-usage-on-schema-pgroonga.html)

Then, you set `True` to `USING_PGROONGA` in `local_settings.py`.

Before:

    # USING_PGROONGA = True

After:

    USING_PGROONGA = True

TODO: Describe how to enable PGroonga on installed Zulip.

Now, you can use full-text search against all languages.
