# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Initial project setup.
- Basic UI with anime entry form.
- Functionality to add new anime entries to a CSV file.

### Changed

- Updated UI styling and layout.
- Improved input validation for anime entries.

## [1.0.0] - 2024-04-11

### Added

- Implemented genre filtering in the UI.
- Added pagination for better navigation of anime entries.
- Export functionality to save anime entries to a CSV file.

### Changed

- Updated styling to match a cyberpunk-inspired theme.

## [1.1.0] - 22024-04-11

### Added

- Confirmation dialogs for critical actions (delete, export, etc.).
- Custom fonts and icons for a more aesthetic UI.

### Changed

- Updated styling for a more modern look.
- Enhanced entry form with additional fields (synopsis, platform, language).

## [1.2.0] - 2024-04-11

### Added

- Implemented sorting functionality for anime entries.
- Cyberpunk-inspired UI color scheme.

### Changed

- Improved performance and responsiveness of the app.
- Fixed minor UI bugs.

## [1.3.0] - 2024-04-11

### Added

- Genre filter dropdown in the UI for filtering anime entries by genre.
- Enhanced entry addition logic to ensure new entries are added to the next available row.

### Changed

- Fixed display issues with the genre filter and other UI elements.
- Improved error handling for better user experience.

## [1.4.0] - 2024-04-12
### Added
- Pagination support for the anime list table to enhance user navigation through large datasets.

### Changed
- Updated the `populate_table` function to handle page-based data slicing.

### Fixed
- Minor UI adjustments for better alignment of pagination controls.

## [1.5.0] - 2024-04-12
### Added
**Release Highlights:**
- Added tagging functionality to the Anime Series Tracker. Users can now add and filter anime entries based on custom tags, enhancing the organizational capabilities of the app.

### Changed
**Bug Fixes:**
- Addressed minor UI responsiveness issues.
- Fixed a bug where filters were not resetting correctly.

**Known Issues:**
- None reported.

## [1.6.0] - 2024-04-14

### Added
- **Settings Dialog**: Introduced a new Settings Dialog that allows users to customize their application settings, including themes and items per page. This enhancement aims to provide users with a more personalized and controlled experience.
- Preparation for further dialog enhancements, including an Advanced Search Dialog and a Help Dialog, to improve user interactivity and access to information.

### Changed
- Modularized codebase to improve maintainability and separation of concerns, ensuring a clearer organization by dividing code into UI components, dialogs, and data management modules.
- Enhanced data management logic to handle CSV file interactions more efficiently, reducing potential errors and increasing performance.

### Fixed
- Addressed an issue where filtered table entries were not correctly displayed at the top of the table. Now, filtered results appear as expected, enhancing usability.
- Resolved various minor bugs and performance issues to ensure a smoother user experience.


We recommend all users to update to this latest version to enjoy the new features and improvements.