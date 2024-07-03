# Contributing

We are excited for you to start contributing to the application! Here are some guidelines:

- [Question or Problem](#have-a-question-or-problem)
- [Find A Bug?](#find-a-bug)
- [Coding guidelines](#coding-guidelines)
- [Development Setup](#development-setup)
- [Philosophy](#philosophy)

## Have a Question or Problem?

**TL;DR: Message slack, don't be scared to ask for help**

If you have any questions or problems, you can message the slack
channel directly. Whenever it is appropriate, we like to share
messages with the entire team to ensure everyone is on the same page.

**Do NOT be scared to ask for help!**
If you have already tried to answer the question yourself, but 
did not find an answer, don't hesitate to ask anyone else that 
you deem fit! We are all here to support each other and **WILL NOT** 
look down upon a request for help. 

## Find A Bug?

If you find a bug in the code, whenever possible, mention it to the team first.
Otherwise, you can submit a Pull Request with a fix.

## Development Setup

We use [Rye](https://rye.astral.sh/guide/) to manage dependencies, if you do not know it, it's great! [Check it out](
  https://rye.astral.sh/guide/installation/
)!

After you install it, you just have to run:

```bash
rye sync --all-features
```

You can then run scripts using rye run python script.py. 


### Commonly used rye scripts

```bash
# run linter (ruff)
rye run lint

# run formatter (ruff)
rye run format

# run dev server
rye run dev

# run test coverage
rye run test 
# OR for html report
rye run test-ui
```

## Coding guidelines

### Commit messages

Your commit message should be as descriptive as possible, as
it leads to more readable histories.

We have a format that we require in order to make a commit, which is described below.

```
<type of commit>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

For example:

```
chore(dependencies): bump @random-pkg/pkg-name from 1.10.0 to 1.11.0
```

The type and subject are **mandatory**, the rest, including the scope, are optional. 

Keep the message as concise and informative as you can. 

### Type 

When specifying a type, choose from these options:

- **build**: Changes that affect the build system or external dependencies.
- **chore**: Updating tasks etc; no production code change.
- **ci**: Changes to our CI configuration. 
- **docs**: Documentation only changes.
- **feat**: A new feature.
- **fix**: A bug fix.
- **perf**: A code change that regards / improves performance.
- **refactor**: A code change that neither fixes a bug nor adds a feature.
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc).
- **test**: Adding missing tests or correcting existing tests.

### Scope

The optional scope should be the names of the project directories it is affecting. 

If adding more than one scope, separate them by commons, e.g.`lib,tests`

At times it is not completely necessary to add a scope, one example would be a commit message like:
`style: add missing semicolons`, for a commit that affected multiple directories. 

### Subject 

The subject contains a concise summary / description of the change, keep it short and sweet.

## Philosophy

**TL;DR**: "Try" to write "clean code" when it is possible, but don't fear complexity.

Yes, a readable codebase is quite nice, so we encourage you to write that way whenever possible.
Though, don't just write it because it's "clean", write it so we can all extend upon it together, 
because that's when we can deliver the most value.

While writing clean code is important, don't let yourself fear complexity. Remember that first comes
meeting needs, and we are here to deliver value. Our top priority is the satisfaction of users and
the team. 

We encourage you to:

- Listen to your gut.
- Prioritize a net positive outcome on users and the team with all your contributions.
- Form responsible opinions / approaches and share them

Here's a nice [blog post](https://engineering.ramp.com/what-matters-suffers) by Pablo, a [Ramp](https://ramp.com) engineer, that we mostly agree with
