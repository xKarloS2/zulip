# Reviewing Zulip server code

This document is a brief discussion of what we look for when reviewing
contributions to Zulip:

* The Travis CI build.  One can investigate 

* Technical design.  There are a lot of considerations here: security,
  migration paths/backwards compatibility, cost of new dependencies,
  interactions with features.

* User interface and visual design.  If frontend changes are involved,
  the reviewer will check out the code, play with the new UI, and
  verify it for both quality and consistency with the rest of the
  Zulip UI.  We highly encourage posting screenshots to save reviewers
  time in getting a feel for what the feature looks like -- you'll get
  a quicker response that way.

* Error handling.  The code should always check for invalid user
  input.  User-facing error messages should be clear and when possible
  be actionable (it should be obvious to the user what they need to do
  in order to correct the problem).

* Testing.  The tests should validate that the feature works
  correctly, and specifically test for common error conditions, bad
  user input, and potential bugs that are likely for the type of
  change being made.  Tests that exclude whole classes of potential
  bugs are preferred when possible (e.g. the common test suite between
  the frontend and backend markdown processors or the GetEventsTest
  test for buggy race condition handling).  If the feature involves
  frontend changes, there should be frontend tests.  See the [test
  writing][test-writing] documentation for more details.

* mypy annotations.  New functions should be annotated using [mypy]
  and existing annotations should be updated.  Use of `Any`, `ignore`,
  and unparameterized containser should be limited to cases where a
  more precise type cannot be specified.

* Clear function, argument, variable, and test names.  Every new piece
  of Zulip code will be read many times by other developers, and so
  it's important that variable names communicate clearly the purpose
  of each piece of the codebase.

* Duplicated code.  Code duplication is a huge source of bugs in large
  projects and makes the codebase difficult to understand, so we avoid
  significant code duplication wherever possible.  Sometimes avoiding
  code duplication involves some refactoring of existing code; if so,
  that should usually be done as its own series of commits (not
  squashed into other changes or left as a thing to do later).

* For refactorings, verify that the changes are complete.  Usually one
  can check that efficiently using `git grep`.

* Documentation updates.  If this changes how something works, does it
  update the documentation in a corresponding way?  If it's a new
  feature, is it documented and documented in the right place?

* Good comments.  It's often worth thinking about whether explanation
  in a commit message or pull request discussion should be included in
  a comment or other documentation.

* Coding style.  See the Zulip [code-style] documentation for details.
  Our goal is to have as much of this as possible verified via the
  linters and tests, but there's always going to be unusual forms of
  unusual Python/JavaScript style that we don't check for.

* Clear commit messages.  See the [Zulip version
  control][commit-messages] documentation for details on what we look
  for.

[code-style]: 
[commit-messages]:
[test-writing]:
[mypy]: 