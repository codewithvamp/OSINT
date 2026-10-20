# CodeWithVamp OSINT Toolkit

**A community-maintained directory of public intelligence resources for learners, defenders and authorized investigators.**

> **Publicly discoverable ≠ authorized access.** This directory is educational, not permission to monitor people, bypass access controls, or access exposed devices.

[Browse all tools](docs/DIRECTORY.md) · [Responsible use](RESPONSIBLE_USE.md) · [Contribute](CONTRIBUTING.md) · [JSON](data/tools.json) · [CSV](data/tools.csv)

## At a glance
- **106 catalog entries** across **15 categories** (including tools listed in multiple relevant categories).
- Tool descriptions, official/project URLs and indicative access requirements.
- Machine-readable JSON and CSV, suitable for a future searchable website.
- Python standard-library validation and GitHub Actions checks.

## Categories

- **Flight Tracking & Aviation** — 7 entries
- **Satellite Positions & Earth Imagery** — 9 entries
- **Maritime & Vessel Tracking** — 6 entries
- **Public Webcams & Traffic Cameras** — 6 entries
- **Roads, Maps & Mobility** — 6 entries
- **Weather, Disasters & Environment** — 11 entries
- **Geolocation & Verification** — 7 entries
- **Web Archives & Search** — 7 entries
- **Domains, Dns & Certificates** — 8 entries
- **Internet Exposure & Cyber Intelligence** — 9 entries
- **Code, Packages & Developer Footprint** — 7 entries
- **Images, Video & Metadata** — 6 entries
- **Usernames, Social & People Search** — 5 entries
- **Email, Organizations & Breach Awareness** — 6 entries
- **Osint Workflows & Learning** — 6 entries

## Getting started

1. Open [the directory](docs/DIRECTORY.md) and choose an investigation category.
2. Read the **access** label; check current provider terms, account requirements and rate limits.
3. Validate timestamps, coverage and provenance independently.
4. Follow [responsible-use guidance](RESPONSIBLE_USE.md).

## Data structure

Each `data/tools.json` record has `id`, `name`, `description`, `access`, `category`, `url`, and `responsible_use`. Labels are descriptive snapshots, **not guarantees of current availability or pricing**.

## Validate the catalog

```bash
python scripts/validate.py
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md). Prefer official provider/project pages, evidence-based descriptions and minimal data collection.

## Disclaimer

Satellite tracking is not live satellite video; ADS-B/AIS coverage can be delayed or incomplete; an indexed camera or internet service is not permission to access it. No live availability verification was performed for every entry in this initial import.

## License

Repository text and original curation: [CC BY 4.0](LICENSE). Third-party trademarks, logos, screenshots, datasets, and linked tools remain subject to their owners’ terms.

**CodeWithVamp — Stay curious… stay protected.**
