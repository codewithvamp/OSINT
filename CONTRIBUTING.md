# Contributing

We welcome new OSINT resources and corrections.

## Submit a tool

1. Open an issue or pull request describing the resource and its legitimate investigative use.
2. Prefer an official homepage or source repository URL.
3. Add or update the entry in `data/tools.json`, including category, concise description and access requirements.
4. Regenerate `data/tools.csv` and `docs/DIRECTORY.md` to keep formats synchronized.
5. Run `python scripts/validate.py`.
6. Explain whether you personally verified the link and when; do not claim verification without checking.

## Quality rules

- No credentials, API keys, private personal data, exploits, or unlawfully obtained datasets.
- No instructions for accessing private cameras or evading authorization.
- No affiliate links, misleading pricing guarantees, or unsupported surveillance claims.
- State if account, API key, paid tier, or regional access may be required.
- Describe limitations and privacy concerns where relevant.
- Keep the tone neutral and descriptions factual.

## Reporting problems

Use an issue for dead links, inaccurate labels, duplicates, or changes in access conditions.
