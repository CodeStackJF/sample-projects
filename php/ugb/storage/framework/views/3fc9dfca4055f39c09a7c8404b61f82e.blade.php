---
name: pest-testing
description: "Use this skill for Pest PHP testing in Laravel projects only. Trigger whenever any test is being written, edited, fixed, or refactored — including fixing tests that broke after a code change, adding assertions, converting PHPUnit to Pest, adding datasets, and TDD workflows. Always activate when the user asks how to write something in Pest, mentions test files or directories (tests/Feature, tests/Unit, tests/Browser), or needs browser testing, smoke testing multiple pages for JS errors, architecture tests, or faster test runs with Test Impact Analysis. Covers: test()/it()/expect() syntax, datasets, mocking, browser testing (visit/click/fill), smoke testing, arch(), Livewire component tests, RefreshDatabase, Tia (--tia), sharding, and all Pest 5 features. Do not use for factories, seeders, migrations, controllers, models, or non-test PHP code."
license: MIT
metadata:
  author: laravel
---
@php
/** @var \Laravel\Boost\Install\GuidelineAssist $assist */
@endphp
# Pest Testing 5

## Documentation

Use ___SINGLE_BACKTICK___search-docs___SINGLE_BACKTICK___ for detailed Pest 5 patterns and documentation.

## Basic Usage

### Creating Tests

All tests must be written using Pest. Use ___SINGLE_BACKTICK___{{ $assist->artisanCommand('make:test --pest {name}') }}___SINGLE_BACKTICK___.

The ___SINGLE_BACKTICK___{name}___SINGLE_BACKTICK___ argument should include only the path and test name, but should not include the test suite.
- Incorrect: ___SINGLE_BACKTICK___{{ $assist->artisanCommand('make:test --pest Feature/SomeFeatureTest') }}___SINGLE_BACKTICK___ will generate ___SINGLE_BACKTICK___tests/Feature/Feature/SomeFeatureTest.php___SINGLE_BACKTICK___
- Correct: ___SINGLE_BACKTICK___{{ $assist->artisanCommand('make:test --pest SomeControllerTest') }}___SINGLE_BACKTICK___ will generate ___SINGLE_BACKTICK___tests/Feature/SomeControllerTest.php___SINGLE_BACKTICK___
- Incorrect: ___SINGLE_BACKTICK___{{ $assist->artisanCommand('make:test --pest --unit Unit/SomeServiceTest') }}___SINGLE_BACKTICK___ will generate ___SINGLE_BACKTICK___tests/Unit/Unit/SomeServiceTest.php___SINGLE_BACKTICK___
- Correct: ___SINGLE_BACKTICK___{{ $assist->artisanCommand('make:test --pest --unit SomeServiceTest') }}___SINGLE_BACKTICK___ will generate ___SINGLE_BACKTICK___tests/Unit/SomeServiceTest.php___SINGLE_BACKTICK___

### Test Organization

- Unit/Feature tests: ___SINGLE_BACKTICK___tests/Feature___SINGLE_BACKTICK___ and ___SINGLE_BACKTICK___tests/Unit___SINGLE_BACKTICK___ directories.
- Browser tests: ___SINGLE_BACKTICK___tests/Browser/___SINGLE_BACKTICK___ directory.
- Do NOT remove tests without approval - these are core application code.

### Basic Test Structure

Pest supports both ___SINGLE_BACKTICK___test()___SINGLE_BACKTICK___ and ___SINGLE_BACKTICK___it()___SINGLE_BACKTICK___ functions. Before writing new tests, check existing test files in the same directory to match the project's convention. Use ___SINGLE_BACKTICK___test()___SINGLE_BACKTICK___ if existing tests use ___SINGLE_BACKTICK___test()___SINGLE_BACKTICK___, or ___SINGLE_BACKTICK___it()___SINGLE_BACKTICK___ if they use ___SINGLE_BACKTICK___it()___SINGLE_BACKTICK___.

___BOOST_SNIPPET_0___

### Running Tests

- Run minimal tests with filter before finalizing: ___SINGLE_BACKTICK___{{ $assist->artisanCommand('test --compact --filter=testName') }}___SINGLE_BACKTICK___.
- Run all tests: ___SINGLE_BACKTICK___{{ $assist->artisanCommand('test --compact') }}___SINGLE_BACKTICK___.
- Run file: ___SINGLE_BACKTICK___{{ $assist->artisanCommand('test --compact tests/Feature/ExampleTest.php') }}___SINGLE_BACKTICK___.
- Run only tests affected by recent changes (Tia): ___SINGLE_BACKTICK___./vendor/bin/pest --parallel --tia___SINGLE_BACKTICK___.

## Assertions

Use specific assertions (___SINGLE_BACKTICK___assertSuccessful()___SINGLE_BACKTICK___, ___SINGLE_BACKTICK___assertNotFound()___SINGLE_BACKTICK___) instead of ___SINGLE_BACKTICK___assertStatus()___SINGLE_BACKTICK___:

___BOOST_SNIPPET_1___

| Use | Instead of |
|-----|------------|
| ___SINGLE_BACKTICK___assertSuccessful()___SINGLE_BACKTICK___ | ___SINGLE_BACKTICK___assertStatus(200)___SINGLE_BACKTICK___ |
| ___SINGLE_BACKTICK___assertNotFound()___SINGLE_BACKTICK___ | ___SINGLE_BACKTICK___assertStatus(404)___SINGLE_BACKTICK___ |
| ___SINGLE_BACKTICK___assertForbidden()___SINGLE_BACKTICK___ | ___SINGLE_BACKTICK___assertStatus(403)___SINGLE_BACKTICK___ |

## Mocking

Import mock function before use: ___SINGLE_BACKTICK___use function Pest\Laravel\mock;___SINGLE_BACKTICK___

## Datasets

Use datasets for repetitive tests (validation rules, etc.):

___BOOST_SNIPPET_2___

## Pest 5 Features

| Feature | Purpose |
|---------|---------|
| Tia (Test Impact Analysis) | Rerun only tests affected by recent changes |
| Time-Balanced Sharding | Split tests across CI shards by execution time |
| New Validation Expectations | ___SINGLE_BACKTICK___toBeEmail()___SINGLE_BACKTICK___, ___SINGLE_BACKTICK___toBeUlid()___SINGLE_BACKTICK___, ___SINGLE_BACKTICK___toBeIpAddress()___SINGLE_BACKTICK___, and more |
| Browser Testing | Full integration tests in real browsers |
| Smoke Testing | Validate multiple pages quickly |
| Visual Regression | Compare screenshots for visual changes |
| Architecture Testing | Enforce code conventions |

### Tia (Test Impact Analysis)

Tia reruns only tests affected by recent changes and replays cached results for the rest, dramatically reducing suite duration:

___BOOST_SNIPPET_3___

- Replayed tests are not skipped — cached tests store everything they produced, including covered lines and branches.
- Detects Laravel, Symfony, Livewire, and Inertia automatically.

### New Validation Expectations

Pest 5 ships eight new validation matchers, all supporting ___SINGLE_BACKTICK___.not___SINGLE_BACKTICK___ negation:

___BOOST_SNIPPET_4___

### Time-Balanced Sharding

Distribute tests across CI shards by execution time rather than count:

___BOOST_SNIPPET_5___

Commit ___SINGLE_BACKTICK___tests/.pest/shards.json___SINGLE_BACKTICK___ to the repository so CI shards stay consistent.

### Browser Test Example

Browser tests run in real browsers for full integration testing:

- Browser tests live in ___SINGLE_BACKTICK___tests/Browser/___SINGLE_BACKTICK___.
- Use Laravel features like ___SINGLE_BACKTICK___Event::fake()___SINGLE_BACKTICK___, ___SINGLE_BACKTICK___assertAuthenticated()___SINGLE_BACKTICK___, and model factories.
- Use ___SINGLE_BACKTICK___RefreshDatabase___SINGLE_BACKTICK___ for clean state per test.
- Interact with page: click, type, scroll, select, submit, drag-and-drop, touch gestures.
- Test on multiple browsers (Chrome, Firefox, Safari) if requested.
- Test on different devices/viewports (iPhone 14 Pro, tablets) if requested.
- Switch color schemes (light/dark mode) when appropriate.
- Take screenshots or pause tests for debugging.

___BOOST_SNIPPET_6___

### Smoke Testing

Quickly validate multiple pages have no JavaScript errors:

___BOOST_SNIPPET_7___

### Visual Regression Testing

Capture and compare screenshots to detect visual changes.

### Architecture Testing

___BOOST_SNIPPET_8___

## Common Pitfalls

- Not importing ___SINGLE_BACKTICK___use function Pest\Laravel\mock;___SINGLE_BACKTICK___ before using mock
- Using ___SINGLE_BACKTICK___assertStatus(200)___SINGLE_BACKTICK___ instead of ___SINGLE_BACKTICK___assertSuccessful()___SINGLE_BACKTICK___
- Forgetting datasets for repetitive validation tests
- Deleting tests without approval
- Forgetting ___SINGLE_BACKTICK___assertNoJavaScriptErrors()___SINGLE_BACKTICK___ in browser tests
- Prefixing ___SINGLE_BACKTICK___Feature/___SINGLE_BACKTICK___ or ___SINGLE_BACKTICK___Unit/___SINGLE_BACKTICK___ in ___SINGLE_BACKTICK___{name}___SINGLE_BACKTICK___ when using ___SINGLE_BACKTICK___make:test___SINGLE_BACKTICK___
