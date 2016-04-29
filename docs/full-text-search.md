# Full-text search

Zulip supports full-text search. By default, it supports only
English.

TODO: More description.

## The default full-text search implementation

Zulip uses
[PostgreSQL built-in full-text search feature](http://www.postgresql.org/docs/current/static/textsearch.html).

TODO: More description.

## An optional full-text search implementation

Zulip also supports [PGroonga](http://pgroonga.github.io/). PGroonga
is a PostgreSQL extension that provides full-text search
feature. PostgreSQL built-in full-text search feature supports only
one language at a time. PGroonga supports all languages including
Japanese, Chinese and so on at a time.

### How to enable full-text search against all languages

This section describes how to enable full-text search feature based on
PGroonga.

You [install PGroonga](http://pgroonga.github.io/install/).

You enable PGroonga by `scripts/setup/enable-pgroonga`:

    /home/zulip/deployments/current/scripts/setup/enable-pgroonga

You set `True` to `USING_PGROONGA` in `/etc/zulip/settings.py`:

Before:

    # USING_PGROONGA = True

After:

    USING_PGROONGA = True

You restart Zulip:

    su zulip -c /home/zulip/deployments/current/scripts/restart-server

Now, you can use full-text search against all languages.

### How to disable full-text search against all languages

This section describes how to disable full-text search feature based
on PGroonga.

You set `False` to `USING_PGROONGA` in
`local_settings.py`. `USING_PGROONGA` is `False` by default. So you
just comment it out:

Before:

    USING_PGROONGA = True

After:

    # USING_PGROONGA = True

You restart Zulip:

    su zulip -c /home/zulip/deployments/current/scripts/restart-server

You enable PGroonga by `scripts/setup/disable-pgroonga`:

    /home/zulip/deployments/current/scripts/setup/disable-pgroonga

Now, full-text search feature based on PGroonga is disabled.
