# fridgelin

fridgelin turns leftover ingredients into a pretend restaurant experience:
dish names, prices, menus, reviews and drink pairings. It is a lighthearted
Python package with no declared runtime dependencies.

> Integration status: this documentation is based on the team skeleton at
> `69666f8a59c55ec8520c7c466913237a578c359e` and Spark's review contribution.
> The review implementation is included in this sequence. The complete menu,
> drink, CLI, two-version CI and official PyPI release still require team
> integration and verification. Intended outputs below are not release evidence.

## Installation

The intended public package page is [fridgelin on PyPI](https://pypi.org/project/fridgelin/).
An official release must be published and checked before this command is a
verified installation path:

```bash
pip install fridgelin
```

Until then, use the [source setup instructions](docs/development.md).
The package declares Python 3.10 or newer.

## A review example

```python
from fridgelin import review

print(review("Ketchup-Glazed Rice", 3, seed=7))
```

```text
Ketchup-Glazed Rice did exactly what it said it would do, no more, no less. I finished it, which proves nothing.
-- Percival Crumb, 3/5
```

See the [API reference](docs/usage.md) for every public function, argument
rules, examples and the intended CLI. It marks functions and outputs that
still depend on team integration.

The team still needs a complete example program calling all public functions;
its planned path is `examples/example.py`.

## Development

The [development guide](docs/development.md) explains the virtual environment,
dependencies, tests, build commands, publication procedure and collaboration
workflow. Review code requires no secrets or database setup.

## Build and test status

Build/test CI is pending in the checked baseline. The intended workflow is
`.github/workflows/build.yaml`, using Python 3.12 and 3.14. Once it exists and
has been verified, place this live badge at the top of the README:

```markdown
![build and test](https://github.com/software-students-fall2026/python-package-exercise-milkfrog/actions/workflows/build.yaml/badge.svg)
```

The contribution event logger is separate from build/test CI.

## Team

Team milkfrog:

- [Kevin Han](https://github.com/kevinhan923)
- [Tony Dong](https://github.com/tongdong016)
- [Spark Fan](https://github.com/SparkFan-ui)
- [Yutong Xiao](https://github.com/yx3295-star)

## License

GPL-3.0-or-later. See [LICENSE](LICENSE).
