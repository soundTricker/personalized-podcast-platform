# Flowbite React Full Documentation

# Getting started

## Introduction

# Flowbite React - UI Component Library

> Learn more about Flowbite React, a powerful UI component library that combines React components with Tailwind CSS to help you build modern web applications faster

[Flowbite React](https://github.com/themesberg/flowbite-react) is a comprehensive UI component library that brings together the power of React and the utility-first approach of Tailwind CSS. Built on top of the core Flowbite components, it provides a robust foundation for creating modern, responsive web applications.

## What is Flowbite React?

Flowbite React offers a collection of production-ready React components that are:

- **Fully Interactive**: Each component is built with React's component model and handles all necessary interactivity out of the box
- **Tailwind CSS Based**: Leverages Tailwind CSS utility classes for styling, providing complete customization flexibility
- **Accessible**: Follows web accessibility best practices to ensure your applications are usable by everyone
- **TypeScript Ready**: Comes with full TypeScript support for a better development experience
- **Open Source**: Free to use and modify under the MIT license

## Component Ecosystem

The library includes a growing collection of interactive elements such as:

- Navigation components (navbars, breadcrumbs, tabs)
- Data display elements (tables, cards, lists)
- Form components (inputs, selects, checkboxes)
- Feedback components (alerts, modals, toasts)
- Layout components (sidebars, accordions, footers)
- And many more

Each component is designed to be:

- **Modular**: Use only what you need
- **Customizable**: Easily adapt to your brand and design system
- **Responsive**: Works seamlessly across different screen sizes
- **Well-documented**: Comprehensive documentation with examples and API references

## Why Choose Flowbite React?

Flowbite React accelerates your development workflow by:

1. **Reducing Development Time**: Pre-built components mean less time writing boilerplate code
2. **Ensuring Consistency**: Standardized components maintain visual and behavioral consistency
3. **Providing Flexibility**: Extensive customization options through Tailwind CSS and theme configuration
4. **Supporting Modern Development**: Built with current best practices and modern tooling

## Next Steps

Ready to explore more? Check out:

- [Theme customization](https://flowbite-react.com/docs/customize/theme.md) to learn about styling components
- [Dark mode implementation](https://flowbite-react.com/docs/customize/dark-mode.md) for adding dark theme support
- [Contributing guide](https://flowbite-react.com/docs/getting-started/contributing.md) to get involved with the project

For installation and setup instructions, visit our [quickstart guide](https://flowbite-react.com/docs/getting-started/quickstart.md).


---

## Quickstart (updated)

# Quickstart - Flowbite React

> Learn how to get started with the free and open-source Flowbite React UI component library based on the utility classes from Tailwind CSS

Get started with Flowbite React by either creating a new project or adding it to an existing one using our CLI tools.

## Creating a new project

Use our project creation CLI to scaffold a new application with Flowbite React pre-configured:

```bash
npx create-flowbite-react@latest
```

## Adding to an existing project

For existing projects, use the Flowbite React CLI to set up and configure everything automatically:

```bash
npx flowbite-react@latest init
```

## Integration Guides

Looking to integrate Flowbite React with your favorite framework or tool? Check out our detailed integration guides below for step-by-step instructions on setting up Flowbite React with various technologies:

- [AdonisJS](https://flowbite-react.com/docs/guides/adonisjs.md)
- [Astro](https://flowbite-react.com/docs/guides/astro.md)
- [Blitz.js](https://flowbite-react.com/docs/guides/blitzjs.md)
- [Bun](https://flowbite-react.com/docs/guides/bun.md)
- [ESBuild](https://flowbite-react.com/docs/guides/esbuild.md)
- [Farm](https://flowbite-react.com/docs/guides/farm.md)
- [Gatsby](https://flowbite-react.com/docs/guides/gatsby.md)
- [Laravel](https://flowbite-react.com/docs/guides/laravel.md)
- [Meteor.js](https://flowbite-react.com/docs/guides/meteorjs.md)
- [Modern.js](https://flowbite-react.com/docs/guides/modernjs.md)
- [Next.js](https://flowbite-react.com/docs/guides/nextjs.md)
- [Parcel](https://flowbite-react.com/docs/guides/parcel.md)
- [React Router](https://flowbite-react.com/docs/guides/react-router.md)
- [React Server](https://flowbite-react.com/docs/guides/react-server.md)
- [RedwoodJS](https://flowbite-react.com/docs/guides/redwoodjs.md)
- [Remix](https://flowbite-react.com/docs/guides/remix.md)
- [Rsbuild](https://flowbite-react.com/docs/guides/rsbuild.md)
- [Rspack](https://flowbite-react.com/docs/guides/rspack.md)
- [TanStack Router](https://flowbite-react.com/docs/guides/tanstack-router.md)
- [TanStack Start](https://flowbite-react.com/docs/guides/tanstack-start.md)
- [Vike](https://flowbite-react.com/docs/guides/vike.md)
- [Vite](https://flowbite-react.com/docs/guides/vite.md)
- [Waku](https://flowbite-react.com/docs/guides/waku.md)
- [Webpack](https://flowbite-react.com/docs/guides/webpack.md)



---

## Compatibility (new)

# Tailwind CSS Compatibility - Flowbite React

> Learn about Flowbite React's compatibility with Tailwind CSS versions and how to easily migrate between Tailwind CSS v3 and v4

Flowbite React is designed to work seamlessly with both Tailwind CSS v3 and v4, automatically detecting which version you're using in your project.

## Version Compatibility

Flowbite React features automatic version detection that allows it to:

- **Work with Tailwind CSS v3**: Full compatibility with Tailwind CSS v3.x projects
- **Support Tailwind CSS v4**: Ready for the latest features in Tailwind CSS v4
- **Adapt automatically**: No manual configuration needed to specify which version you're using

This means you can use Flowbite React in both existing Tailwind CSS v3 projects and new Tailwind CSS v4 projects without worrying about compatibility issues.

## Migrating from Tailwind CSS v3 to v4

If you have an existing project using Flowbite React with Tailwind CSS v3 and want to upgrade to Tailwind CSS v4, the process is straightforward:

1. Run the official Tailwind CSS upgrade command:

```bash
npx @tailwindcss/upgrade
```

2. Follow any additional instructions provided by the upgrade tool

3. That's it! Flowbite React will automatically detect that you're now using Tailwind CSS v4 and adapt accordingly

If you encounter any issues with compatibility, please check our [GitHub repository](https://github.com/themesberg/flowbite-react) for the latest updates or to report problems.


---

## CLI (updated)

# CLI - Flowbite React

> Learn about the powerful CLI tools for managing and developing Flowbite React applications

## Overview

The Flowbite React CLI provides a comprehensive set of tools for:

- Creating new Flowbite React projects
- Setting up Flowbite React in existing projects
- Managing development workflows
- Handling class generation
- Configuring your development environment
- Patching Tailwind CSS configurations
- Providing help and documentation

## Installation & Setup

### 1. Create a New Project

To scaffold a new Flowbite React application:

```bash
npx create-flowbite-react@latest
```

The CLI will guide you through:

- Project directory name
- Template selection
- Git repository initialization

### 2. Add to Existing Project

To integrate Flowbite React into an existing project:

```bash
npx flowbite-react@latest init
```

This command performs several automated setup steps:

- Verifies Tailwind CSS installation
- Installs Flowbite React dependencies
- Configures Tailwind CSS
- Creates the `.flowbite-react` config directory
- Creates `config.json` and `.gitignore` files in the config directory
- Creates `.vscode/settings.json` and `.vscode/extensions.json` files
- Sets up bundler-specific plugins

## CLI Commands

### `flowbite-react build`

Generates the class list for your components. This command:

- Creates the `.flowbite-react` output directory if it doesn't exist
- Generates a comprehensive list of Tailwind classes used in your components
- Analyzes your project files to find component imports if no components are explicitly defined in your config
- Writes the generated class list to `.flowbite-react/class-list.json`
- This class list is used by the Tailwind plugin to ensure all component classes are included in your CSS

### `flowbite-react create`

Creates a new component with the proper structure and theming setup.

The `create` command uses the configuration options from `.flowbite-react/config.json` to determine:

1. **Where to create the component** (`path`):

   - Determines the directory where the component will be created
   - Default: `"src/components"`

2. **Language format** (`tsx`):

   - When `true`: Creates a TypeScript component (`.tsx`) with full type definitions
   - When `false`: Creates a JavaScript component (`.jsx`) without TypeScript syntax
   - Default: `true`

3. **React Server Components support** (`rsc`):
   - When `true`: Adds the `"use client";` directive at the top of the component file
   - When `false`: Omits the directive for client-only components
   - Default: `true`

The generated component includes:

- Proper theme structure with base styles
- Theme resolution with the Flowbite React theming system
- Component props with proper typing (in TypeScript mode)
- Forward ref implementation for DOM access
- Display name for better debugging

### `flowbite-react dev`

Starts the development mode which:

- Watches for component changes
- Automatically updates class lists
- Provides real-time class generation
- Monitors imported components

### `flowbite-react help`

Displays help information about available commands:

- Lists all available commands with descriptions
- Shows usage examples
- Provides guidance on command options
- Can be accessed with `flowbite-react help` or `flowbite-react --help`

### `flowbite-react init`

Initializes Flowbite React in your project. This command:

- Ensures Tailwind CSS is installed
- Creates the `.flowbite-react` config directory
- Creates `config.json` and `.gitignore` files in the config directory
- Creates `.vscode/settings.json` and `.vscode/extensions.json` files
- Detects and configures your bundler with the appropriate plugin
- Adds postinstall script to `package.json` (if no bundler detected)

### `flowbite-react install`

Installs Flowbite React in your project:

- Detects your package manager (npm, yarn, pnpm, bun, etc.)
- Installs the latest version of flowbite-react
- Skips installation if already installed

### `flowbite-react migrate`

Runs code transformations to help migrate your codebase:

- Transforms compound components to their simple form (e.g., `Accordion.Panel` to `AccordionPanel`)
- Automatically updates import statements and component usage

Example transformations:

```tsx
// Before
import { Accordion } from "flowbite-react";

<Accordion.Panel>...</Accordion.Panel>

// After
import { AccordionPanel } from "flowbite-react";

<AccordionPanel>...</AccordionPanel>
```

### `flowbite-react patch`

Patches Tailwind CSS to expose its version number for compatibility detection:

- Creates a JavaScript file that exports the Tailwind CSS version
- Necessary because package.json cannot be reliably read by all bundlers
- Makes the version accessible via `import version from "tailwindcss/version"`
- Enables Flowbite React to adapt its behavior based on the installed Tailwind version

### `flowbite-react register`

Registers the Flowbite React process for development:

- Runs the dev process in the background
- Manages process lifecycle
- Handles automatic class generation
- Creates and maintains process ID file

### `flowbite-react setup plugin`

Sets up the appropriate bundler plugin for your project:

- Detects your bundler configuration file
- Supports multiple bundlers (Bun, ESBuild, Parcel, Rsbuild, Rspack, Vite, Webpack, etc.)
- Adds the Flowbite React plugin to your bundler config
- Configures plugin settings automatically

### `flowbite-react setup tailwindcss`

Configures Tailwind CSS for use with Flowbite React:

- Sets up Tailwind CSS v3 or v4 configuration
- Adds necessary plugin configurations
- Updates content paths for component styles
- Configures class generation settings

### `flowbite-react setup vscode`

Sets up VSCode for optimal development:

- Configures Tailwind CSS IntelliSense
- Sets up file associations
- Adds recommended extensions
- Configures class attribute settings

## Configuration

### Bundler Integration

The CLI automatically detects and configures popular bundlers:

- Bun
- Farm
- Parcel
- Rolldown
- Rollup
- Rsbuild
- Rspack
- Turbopack
- Vite
- Webpack

Each bundler plugin automatically handles class generation by:

- Running the `flowbite-react dev` command during development
- Running the `flowbite-react build` command during production builds
- Watching for component changes and updating class lists in real-time
- Managing the class generation process lifecycle

This means you don't need to manually run these commands - the bundler plugin takes care of everything automatically.

### Configuration Options

The CLI creates a `.flowbite-react/config.json` file with several configuration options:

```json
{
  "$schema": "https://unpkg.com/flowbite-react/schema.json",
  "components": [],
  "dark": true,
  "path": "src/components",
  "prefix": "",
  "rsc": true,
  "tsx": true
}
```

#### `components`

List of component names to generate styles for. An empty array enables automatic detection.

#### `dark`

Whether to generate dark mode styles. Default is `true`.

#### `path`

Path where components will be created, relative to the project root. Default is `"src/components"`.

#### `prefix`

Optional prefix to apply to all Tailwind CSS classes.

#### `rsc`

Whether to include the `"use client"` directive for React Server Components. Default is `true`.

#### `tsx`

Whether to use TypeScript (.tsx) or JavaScript (.jsx) for component creation. Default is `true`.

### VSCode Integration

The CLI sets up VSCode for optimal development:

- Configures Tailwind CSS IntelliSense
- Sets up file associations
- Recommends essential extensions
- Configures class attribute settings

### Project Structure

The CLI creates and manages:

- `.flowbite-react/` directory for configuration
- Class list generation
- Bundler-specific configurations
- Git ignore rules

## Command Line Options

When creating new projects:

```bash
npx create-flowbite-react@latest <project-directory> [options]
```

Options:

| Name                    | Description                     |
| ----------------------- | ------------------------------- |
| `--template, -t <name>` | Specify your template           |
| `--git`                 | Initialize a new git repository |
| `--help, -h`            | Display available flags         |
| `--version, -v`         | Display CLI version             |

Example:

```bash
npx create-flowbite-react@latest my-app -t nextjs --git
```

## Project Templates

The CLI supports various framework templates. Each template comes with a complete guide and example implementation:

| \<name>           | Repository                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `adonisjs`        | [flowbite-react-template-adonisjs](https://github.com/themesberg/flowbite-react-template-adonisjs)                                 |
| `astro`           | [flowbite-react-template-astro](https://github.com/themesberg/flowbite-react-template-astro)                                       |
| `blitzjs`         | [flowbite-react-template-blitzjs](https://github.com/themesberg/flowbite-react-template-blitzjs)                                   |
| `bun`             | [flowbite-react-template-bun](https://github.com/themesberg/flowbite-react-template-bun)                                           |
| `esbuild`         | [flowbite-react-template-esbuild](https://github.com/themesberg/flowbite-react-template-esbuild)                                   |
| `farm`            | [flowbite-react-template-farm](https://github.com/themesberg/flowbite-react-template-farm)                                         |
| `gatsby`          | [flowbite-react-template-gatsby](https://github.com/themesberg/flowbite-react-template-gatsby)                                     |
| `laravel`         | [flowbite-react-template-laravel](https://github.com/themesberg/flowbite-react-template-laravel)                                   |
| `meteorjs`        | [flowbite-react-template-meteorjs](https://github.com/themesberg/flowbite-react-template-meteorjs)                                 |
| `modernjs`        | [flowbite-react-template-modernjs](https://github.com/themesberg/flowbite-react-template-modernjs)                                 |
| `nextjs`          | [flowbite-react-template-nextjs](https://github.com/themesberg/flowbite-react-template-nextjs)                                     |
| `parcel`          |                                                                                                                                    |
| ↳ `client`        | [flowbite-react-template-parcel-client](https://github.com/themesberg/flowbite-react-template-parcel-client)                       |
| ↳ `server-bun`    | [flowbite-react-template-parcel-server-bun](https://github.com/themesberg/flowbite-react-template-parcel-server-bun)               |
| ↳ `server-deno`   | [flowbite-react-template-parcel-server-deno](https://github.com/themesberg/flowbite-react-template-parcel-server-deno)             |
| ↳ `server`        | [flowbite-react-template-parcel-server](https://github.com/themesberg/flowbite-react-template-parcel-server)                       |
| `react-router`    |                                                                                                                                    |
| ↳ `framework`     | [flowbite-react-template-react-router-framework](https://github.com/themesberg/flowbite-react-template-react-router-framework)     |
| ↳ `data`          | [flowbite-react-template-react-router-data](https://github.com/themesberg/flowbite-react-template-react-router-data)               |
| ↳ `declarative`   | [flowbite-react-template-react-router-declarative](https://github.com/themesberg/flowbite-react-template-react-router-declarative) |
| `react-server`    | [flowbite-react-template-react-server](https://github.com/themesberg/flowbite-react-template-react-server)                         |
| `redwoodjs`       | [flowbite-react-template-redwoodjs](https://github.com/themesberg/flowbite-react-template-redwoodjs)                               |
| `remix`           | [flowbite-react-template-remix](https://github.com/themesberg/flowbite-react-template-remix)                                       |
| `rsbuild`         | [flowbite-react-template-rsbuild](https://github.com/themesberg/flowbite-react-template-rsbuild)                                   |
| `rspack`          | [flowbite-react-template-rspack](https://github.com/themesberg/flowbite-react-template-rspack)                                     |
| `tanstack-router` | [flowbite-react-template-tanstack-router](https://github.com/themesberg/flowbite-react-template-tanstack-router)                   |
| `tanstack-start`  | [flowbite-react-template-tanstack-start](https://github.com/themesberg/flowbite-react-template-tanstack-start)                     |
| `vike`            | [flowbite-react-template-vike](https://github.com/themesberg/flowbite-react-template-vike)                                         |
| `vite`            | [flowbite-react-template-vite](https://github.com/themesberg/flowbite-react-template-vite)                                         |
| `waku`            | [flowbite-react-template-waku](https://github.com/themesberg/flowbite-react-template-waku)                                         |
| `webpack`         | [flowbite-react-template-webpack](https://github.com/themesberg/flowbite-react-template-webpack)                                   |

You can use any of these templates with the `--template` or `-t` flag:

```bash
npx create-flowbite-react@latest my-app -t nextjs
```

## Development Workflow

The CLI enhances your development workflow by:

1. Watching for component changes
2. Automatically generating class lists
3. Updating configurations in real-time
4. Managing bundler integrations
5. Providing VSCode optimizations

For the best development experience, ensure you have the recommended VSCode extensions installed and your bundler is properly configured.


---

## Editor Setup

# Editor Setup - Flowbite React

> Learn how to configure Visual Studio Code with Tailwind CSS support, code formatting, and linting for Flowbite React development.

This comprehensive guide will help you set up your development environment with proper intellisense, formatting, and linting support for Flowbite React's custom `theme` prop and Tailwind CSS integration.

## VS Code Setup

Visual Studio Code is our recommended editor for Flowbite React development. Follow these sections to configure your environment properly.

### Tailwind Intellisense

Follow these steps to enable intelligent Tailwind CSS suggestions and autocompletion:

1. Install the official [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) extension from the VS Code marketplace.
2. Create a `.vscode` directory in your project root:

```bash
mkdir .vscode
```

3. Create a VS Code settings file:

```bash
touch .vscode/settings.json
```

4. Configure VS Code settings for Tailwind CSS support:

```json
{
  "files.associations": {
    "*.css": "tailwindcss"
  },
  "tailwindCSS.classAttributes": ["class", "className", "theme"],
  "tailwindCSS.experimental.classRegex": [
    ["twMerge\\(([^)]*)\\)", "[\"'`]([^\"'`]*).*?[\"'`]"],
    ["createTheme(?:<\\w+>)?\\s*\\(([^)]*)\\)", "{?\\s?[\\w].*:\\s*?[\"'`]([^\"'`]*).*?,?\\s?}?"]
  ]
}
```

### Prettier Setup

Ensure consistent code formatting with Prettier:

1. Install the required packages:

```bash
npm i -D prettier prettier-plugin-tailwindcss
```

2. Create a Prettier configuration file:

```bash
touch prettier.config.js
```

3. Configure Prettier with Tailwind CSS support:

```js
/** @type {import('prettier').Config} */
module.exports = {
  plugins: ["prettier-plugin-tailwindcss"],
  // tailwindcss
  tailwindAttributes: ["theme"],
  tailwindFunctions: ["twMerge", "createTheme"],
};
```

### ESLint Setup

Set up ESLint to ensure code quality and catch potential issues:

#### Legacy Configuration

1. Install the Tailwind CSS ESLint plugin:

```bash
npm i -D eslint-plugin-tailwindcss
```

2. Configure ESLint with Tailwind CSS support:

```js {6,10-13}
/** @type {import("eslint").Linter.Config} */
module.exports = {
  // ...
  extends: [
    // ...
    "plugin:tailwindcss/recommended",
  ],
  settings: {
    // ...
    tailwindcss: {
      callees: ["twMerge", "createTheme"],
      classRegex: "^(class(Name)|theme)?$",
    },
  },
};
```

#### Flat Configuration

Starting with ESLint v9, the flat config format is the default configuration method. Here's how to set up ESLint with Tailwind CSS support using the new flat config format:

1. Install ESLint Tailwind CSS plugin:

```bash
npm i -D eslint-plugin-tailwindcss
```

2. Configure ESLint with Tailwind CSS support using the flat config format:

```js {1,4,6-10}
import tailwindcss from "eslint-plugin-tailwindcss";

export default [
  ...tailwindcss.configs["flat/recommended"],
  {
    settings: {
      tailwindcss: {
        callees: ["twMerge", "createTheme"],
        classRegex: "^(class(Name)|theme)?$",
      },
    },
  },
];
```

## Automated Setup

For existing projects, you can quickly configure your editor using our CLI tool:

```bash
npx flowbite-react@latest setup vscode
```

This command will:

- Create the necessary `.vscode` directory
- Configure VS Code settings for Tailwind CSS
- Set up recommended extensions
- Configure Prettier and ESLint integrations

> **Note:** If you're starting a new project, you don't need to run this command separately. The `npx flowbite-react@latest init` command automatically includes all editor setup as part of its initialization process. Only use `setup vscode` when configuring an editor for an existing project.

## Next Steps

After completing this setup, your Visual Studio Code environment will be fully configured for Flowbite React development with:

- Intelligent Tailwind CSS suggestions
- Automatic code formatting
- Code quality checking
- Full support for the custom `theme` prop

For additional configuration options or troubleshooting, refer to our [GitHub repository](https://github.com/themesberg/flowbite-react) or join our community on Discord.


---

## AI Integration (new)

# AI and LLM Integration with Flowbite React

> Learn how to integrate Flowbite React with AI models, LLMs, and chatbots using our specialized documentation routes and markdown accessibility features

Flowbite React provides powerful, built-in support for AI and Large Language Model (LLM) integration through specialized routes that expose documentation in machine-readable formats. These features enable seamless integration with ChatGPT, Claude, and other AI assistants.

## Compliance

Flowbite React follows the [llms.txt standard](https://llmstxt.org/), a community-driven proposal initiated by Jeremy Howard that standardizes how websites provide LLM-friendly information.

Our implementation helps address the fundamental challenge that language models face: context windows are too small to process entire websites, and HTML content with navigation, ads, and JavaScript is difficult to convert to LLM-friendly formats.

By adopting this standard, Flowbite React ensures that AI assistants can efficiently access our documentation without struggling with complex HTML or excessive content.

## Machine-Readable Routes

### LLM-Optimized Endpoints

- **`https://flowbite-react.com/llms.txt`** - A concise version of the documentation specifically optimized for LLM consumption and context-efficient prompting
- **`https://flowbite-react.com/llms-full.txt`** - The complete documentation in a format suitable for comprehensive LLM processing when token limits aren't a concern

### Markdown API Access

All documentation pages can be accessed in pure markdown format by simply appending `.md` to their URLs. For example:

- `https://flowbite-react.com/docs/getting-started/introduction.md`
- `https://flowbite-react.com/docs/components/button.md`
- `https://flowbite-react.com/docs/customize/theme.md`

## Implementation Examples

Here's how you might leverage these features in your AI integration:

```ts
// Fetching LLM-optimized documentation for context-efficient prompting
const llmDocs = await fetch("https://flowbite-react.com/llms.txt").then((res) => res.text());

// Getting full documentation for comprehensive LLM processing
const fullDocs = await fetch("https://flowbite-react.com/llms-full.txt").then((res) => res.text());

// Accessing specific component documentation in markdown format
const buttonDocs = await fetch("https://flowbite-react.com/docs/components/button.md").then((res) => res.text());

// Using markdown documentation in a ChatGPT prompt
const chatGptPrompt = `Based on this Flowbite React Button component documentation:
${buttonDocs}

Generate a code example for a primary button with an icon.`;
```

These features make it easy to integrate Flowbite React's documentation with modern AI systems, creating powerful, intelligent tools to enhance developer experience and productivity.


---

## Server Components

# Server Components (RSC) - Flowbite React

> Learn how to use Flowbite React components inside React Server Components

React Server Components are a powerful feature that allows components to be rendered entirely on the server. When used with Flowbite React, they offer several benefits:

- 🚀 Reduced client-side JavaScript bundle size
- ⚡ Improved initial page load performance
- 🔄 Server-side data fetching

## Server vs Client Components

### Server Components (Default)

By default, all components in React are now server components. They don't need any special directive:

```jsx
import { Button } from "flowbite-react";

function ServerComponent() {
  // ✅ Works: Static button without interactions
  return <Button>Click Me</Button>;
}
```

### Client Components

To handle user interactions (like clicks or input), you need to mark your component as a client component using the `"use client"` directive:

```jsx
"use client";

import { Button } from "flowbite-react";

function ClientComponent() {
  // ✅ Works: Button with click handler
  return <Button onClick={() => console.log("clicked!")}>Interactive Button</Button>;
}
```

## Common Pitfalls

### ❌ Wrong: Event Handlers in Server Components

```jsx
// This will cause an error!
import { Button } from "flowbite-react";

function ServerComponent() {
  return <Button onClick={() => console.log("clicked!")}>This Won't Work</Button>;
}
```

### ✅ Correct: Event Handlers in Client Components

```jsx
"use client";

import { Button } from "flowbite-react";

function ClientComponent() {
  return <Button onClick={() => console.log("clicked!")}>This Works Fine</Button>;
}
```

## Important Notes

1. **Flowbite React Compatibility**

   - All Flowbite React components are server-component ready
   - They can be used in both server and client components

2. **Event Handlers**

   - User events (`onClick`, `onBlur`, etc.) require `"use client"`
   - The component containing these events must be a client component

3. **Props Limitations**
   - Only serializable data can be passed to server components
   - Functions, complex objects, and React nodes might not work as props in server components

## Best Practices

- Use server components by default for static content
- Switch to client components only when you need:
  - User interactions (event handlers)
  - Browser APIs
  - State management
  - Effects

This approach ensures optimal performance while maintaining full functionality.

## Support

💡 **Full Server Component Support**

Flowbite React is fully optimized for React Server Components:

- All components work out-of-the-box in server components
- Zero configuration needed for server-side rendering
- Automatic client/server boundary handling
- Optimized for performance in both environments

Just remember to add `"use client"` only when you need interactivity:

```jsx
"use client";

import { Button, Modal } from "flowbite-react";

function InteractiveWidget() {
  // ✅ Use client components when you need interactivity
  return <Button onClick={() => setIsOpen(true)}>Open Modal</Button>;
}
```


---

## License

# License - Flowbite React

> Learn more about the open-source licensing rights of the Flowbite React UI component library

## MIT License

Copyright &copy; 2024 Bergside Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<div className="h-[20vh]" />


---

## Contributing

# How to Contribute - Flowbite React

> Learn how you can start contributing to the open-source Flowbite React UI component library

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:

- Star the project
- Tweet about it
- Refer this project in your project's readme
- Mention the project at local meetups and tell your friends/colleagues

## Code of Conduct

This project has adopted the [Contributor Covenant](https://www.contributor-covenant.org/) as its Code of Conduct. Everyone is expected to adhere to these rules, so please read the [full text](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Thank you.

## I Have a Question

**If you want to ask a question, we assume that you have read the available [Documentation](https://flowbite-react.com/docs/getting-started/introduction.md).**

Before you ask a question, it is best to search for existing [Issues](https://github.com/themesberg/flowbite-react/issues) that might help you. We also have a [Discord server](https://discord.gg/flowbite-902911619032576090) where you can ask questions and get help from the community directly. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/themesberg/flowbite-react/issues/new).
- Follow the [Issue template](https://github.com/themesberg/flowbite-react/blob/main/.github/ISSUE_TEMPLATE/bug_report.md) and fill it out as completely as possible. Don't forget to:
  - Provide as much context as you can about what you're running into.
  - Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.

## I Want To Contribute

### Legal Notice

When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the [project license](https://github.com/themesberg/flowbite-react/blob/main/LICENSE).

### Reporting Bugs

#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://flowbite-react.com/docs/getting-started/introduction.md). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/themesberg/flowbite-react/issues?q=label%3A%22%3Abug%3A+bug%22).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?

#### How Do I Submit a Good Bug Report?

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/themesberg/flowbite-react/issues/new).
- Follow the [Issue template for bug reports](https://github.com/themesberg/flowbite-react/blob/main/.github/ISSUE_TEMPLATE/bug_report.md) to the best of your ability.

Don't forget to:

- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the _reproduction steps_ that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs info`. Bugs with the `needs info` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `confirmed`, as well as possibly other tags (such as `bug`, `help wanted`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for flowbite-react, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://flowbite-react.com/docs/getting-started/introduction.md) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/themesberg/flowbite-react/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/themesberg/flowbite-react/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Follow the [Issue template for feature requests](https://github.com/themesberg/flowbite-react/blob/main/.github/ISSUE_TEMPLATE/feature_request.md) to the best of your ability.

Don't forget to:

- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
- **Explain why this enhancement would be useful** to most flowbite-react users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

### Your First Code Contribution

#### Prerequisites

- You need to understand how to use a terminal, `Git`, `Node.js`, and `Bun`
- You should be able to write `Markdown` and `React TypeScript`
- You should be familiar with `Tailwind` `CSS`, `ESLint`, and `Prettier`
- You should understand what [vitest](https://vitest.dev/) is, and be able to write tests if your contribution changes the behavior of the library in some way
- You should strongly consider using [Visual Studio Code](https://code.visualstudio.com/) as your editor, as it has plugins for `Tailwind CSS`, `ESLint`, and `Prettier` which will automatically fix most style issues for you, and offer suggestions for how to fix the rest

#### Creating a Pull Request

1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Clone the fork and add a remote called `upstream`:

```bash
git clone https://github.com/<your username>/flowbite-react.git
cd flowbite-react
git remote add upstream https://github.com/themesberg/flowbite-react.git
```

3. Create a new branch named after your PR:

```bash
git checkout -b fix/accordion-alwaysopen
```

4. Install dependencies with [`bun`](https://bun.sh/):

```bash
bun install
```

5. Start a development server on your machine:

```bash
bun run dev
```

6. Make sure your changes work and don't break anything else:

```bash
bun run format && bun run lint:fix && bun run test && bun run build
```

7. Push to your forked repository

```bash
git push -u origin fix/accordion-alwaysopen
```

8. Go to [the repository](https://github.com/themesberg/flowbite-react) and [create a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

9. Fill out the Pull Request template, which will be available automatically

#### What Happens Next?

If you have followed the steps above, your Pull Request will be reviewed by a maintainer soon. If it passes review, it will be merged into the `main` branch and will be included in the next release. If not, you will receive feedback about what needs to be improved until it is ready to be merged.

Please note that you will be expected to update the [documentation](https://flowbite-react.com/docs/getting-started/introduction.md) and write appropriate unit tests if your contribution changes the behavior of the library in some way.

### Improving The Documentation

The [documentation at flowbite-react.com](https://flowbite-react.com/docs/getting-started/introduction.md) can all be found inside the `app` folder of this repository. It's written in [Next.js](https://nextjs.org/), and we use [Markdown](https://www.markdownguide.org/cheat-sheet/) for almost all of the content, so you don't need to even be able to write React TypeScript to make documentation changes!

## Styleguides

### Files

We use [Prettier](https://prettier.io/) to format all of our code. Please make sure to run `bun run format` before committing any changes. You can also use VS Code as your editor, and install the Prettier and Tailwind CSS IntelliSense plugins to automatically format your code each time you save.

Please refer to the code written already in the project to see how we format our code, what naming conventions we use, and so on. The more consistent your code is with the rest of the project, the easier it will be to review and merge your Pull Request.

### Branches &amp; Pull Requests

Please follow the same guidelines published by [commitizen](https://github.com/commitizen/cz-cli) when you name a branch that will be used for a Pull Request. The branch name should be prefixed with the most significant change that will be introduced in the Pull Request.

For example, if you are fixing a bug in the accordion component, the branch name should be something like, `fix/accordion-does-x-wrong`.

## Attribution

This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!


---

# Integration guides

## AdonisJS

# Use with AdonisJS - Flowbite React

> Learn how to install Flowbite React for your AdonisJS project and start developing modern full-stack web applications

This guide provides three ways to integrate Flowbite React with AdonisJS:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing AdonisJS project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new AdonisJS project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t adonisjs
```

This will:

- Create a new AdonisJS project
- Install and configure Tailwind CSS and Vite
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have an AdonisJS project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create AdonisJS Project

Create a new AdonisJS project with Inertia.js and React support:

```bash
npx create-adonisjs@latest -K=inertia --adapter=react
```

### 2. Set Up Tailwind CSS

1. Install Tailwind CSS and its Vite plugin:

```bash
npm install -D tailwindcss @tailwindcss/vite
```

2. Configure the Vite plugin in your `vite.config.ts`:

```js {2,7}
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [
    // ...
    tailwindcss(),
  ],
});
```

3. Add Tailwind CSS to your CSS file (`inertia/css/app.css`):

```css
@import "../frontend/node_modules/tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

### 4. Configure Dark Mode

Add the `ThemeModeScript` component to prevent dark mode flickering:

```tsx {3,16}
// inertia/app/ssr.tsx
import { createInertiaApp } from "@inertiajs/react";
import { ThemeModeScript } from "flowbite-react";
import ReactDOMServer from "react-dom/server";

export default function render(page: any) {
  return createInertiaApp({
    page,
    render: ReactDOMServer.renderToString,
    resolve: (name) => {
      const pages = import.meta.glob("../pages/**/*.tsx", { eager: true });
      return pages[`../pages/${name}.tsx`];
    },
    setup: ({ App, props }) => (
      <>
        <ThemeModeScript />
        <App {...props} />
      </>
    ),
  });
}
```

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// inertia/pages/home.tsx
import { Button } from "flowbite-react";

export default function Home() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-adonisjs)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-adonisjs)


---

## Astro

# Use with Astro - Flowbite React

> Learn how to install Flowbite React for your Astro project and start building modern websites with a lightning fast and content-focused web framework

This guide provides three ways to integrate Flowbite React with Astro:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Astro project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Astro project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t astro
```

This will:

- Create a new Astro project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have an Astro project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up dark mode support

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Astro Project

Create a new Astro project:

```bash
npx create-astro@latest
```

### 2. Add React Support

Install React support using the Astro CLI:

```bash
npx astro add react
```

**Note:** Make sure to answer `Yes` to all the questions.

### 3. Configure Tailwind CSS

Install Tailwind CSS using the Astro CLI:

```bash
npx astro add tailwind
```

**Note:** Make sure to answer `Yes` to all the questions.

### 4. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

### 5. Configure Dark Mode

To prevent dark mode flickering, add the `ThemeModeScript` component to your root layout:

```tsx
// src/layouts/index.astro
---
import { ThemeModeScript } from "flowbite-react";
---

<html lang="en">
  <head>
    <ThemeModeScript />
  </head>
  <body>
    <slot />
  </body>
</html>
```

Import and use the layout in your pages:

```tsx
// src/pages/index.astro
---
import RootLayout from "../layouts/index.astro";
---

<RootLayout>
  // Your content here
</RootLayout>
```

### 6. Component Hydration

By default, UI Framework components are not hydrated in the client. To make Flowbite React components interactive, add a `client:*` directive:

```tsx
<DarkThemeToggle client:load />
```

Available directives:

- `client:load`: Hydrates immediately on page load
- `client:idle`: Hydrates when the browser is idle
- `client:visible`: Hydrates when the component becomes visible

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/pages/index.astro
---
import { Button } from "flowbite-react";
import RootLayout from "../layouts/index.astro";
---

<RootLayout>
  <Button>Click me</Button>
</RootLayout>
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-astro)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-astro)


---

## Blitz.js (new)

# Use with Blitz.js - Flowbite React

> Learn how to install Flowbite React with Blitz.js

This guide provides three ways to integrate Flowbite React with Blitz.js:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Blitz.js project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Blitz.js project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t blitzjs
```

This will:

- Create a new Blitz.js project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Blitz.js project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Blitz.js project:

```bash
npm install -g blitz
blitz new blitzjs-project
cd blitzjs-project
```

### 2. Configure Tailwind CSS

Install Tailwind CSS and its dependencies:

```bash
npm install -D tailwindcss @tailwindcss/postcss postcss
```

Create a `postcss.config.mjs` file:

```bash
touch postcss.config.mjs
```

Add `@tailwindcss/postcss` to your `postcss.config.mjs` file:

```js
/** @type {import('postcss-load-config').Config} */
const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
export default config;
```

Update the css file `src/app/globals.css` to include Tailwind CSS:

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// app/pages/index.tsx
import { Button } from "flowbite-react";

function Home() {
  return (
    <div className="p-4">
      <h1 className="mb-4 text-2xl font-bold">Welcome to Blitz.js with Flowbite React</h1>
      <Button>Click me</Button>
    </div>
  );
}

export default Home;
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-blitzjs)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-blitzjs)


---

## Bun (new)

# Use with Bun - Flowbite React

> Learn how to install and set up Flowbite React in your Bun project and start building modern web applications with interactive components

This guide provides three ways to integrate Flowbite React with Bun:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Bun project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Bun project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t bun
```

This will:

- Create a new Bun project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure development and build scripts
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Bun project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary build configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Bun Project

Create a new Bun project with React and Tailwind CSS:

```bash
mkdir my-app && cd my-app
bun init
```

When prompted:

- Select "React" for the project template
- Select "TailwindCSS" for the React template

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Bun to include Flowbite React plugin
- Set up necessary build configurations

### 3. Configure Dark Mode

Add the `ThemeModeScript` component to prevent dark mode flickering:

```tsx
// src/main.tsx
import { ThemeModeScript } from "flowbite-react";
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ThemeModeScript />
    <App />
  </React.StrictMode>,
);
```

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/App.tsx
import { Button } from "flowbite-react";

export default function App() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-bun)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-bun)


---

## ESBuild (new)

# Use with ESBuild - Flowbite React

> Learn how to install Flowbite React with ESBuild

This guide provides three ways to integrate Flowbite React with ESBuild:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing ESBuild project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new ESBuild project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t esbuild
```

This will:

- Create a new ESBuild project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have an ESBuild project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new directory and initialize a new project:

```bash
mkdir esbuild-react-app
cd esbuild-react-app
npm init -y
```

Create `package.json` file:

```json {7,8}
{
  "name": "esbuild-react-app",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "node esbuild.dev.js",
    "build": "node esbuild.build.js"
  }
}
```

Install the required dependencies:

```bash
npm install react react-dom
npm install -D @types/react @types/react-dom esbuild typescript tailwindcss @tailwindcss/postcss
```

Create `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"]
}
```

Create `esbuild.dev.js`:

```ts
import { readFile } from "node:fs/promises";
import { createServer } from "node:http";
import tailwindcss from "@tailwindcss/postcss";
import * as esbuild from "esbuild";
import flowbiteReact from "flowbite-react/plugin/esbuild";
import postcss from "postcss";

const clients = new Set();

const cssPlugin = {
  name: "css",
  setup(build) {
    build.onLoad({ filter: /\.css$/ }, async (args) => {
      const css = await readFile(args.path, "utf8");
      const result = await postcss([tailwindcss]).process(css, {
        from: args.path,
        map: { inline: true },
      });

      return {
        contents: result.css,
        loader: "css",
      };
    });
  },
};

const buildOptions = {
  entryPoints: ["src/main.tsx"],
  bundle: true,
  outdir: "dist",
  sourcemap: true,
  format: "esm",
  loader: {
    ".tsx": "tsx",
    ".ts": "tsx",
    ".jsx": "jsx",
    ".js": "jsx",
  },
  plugins: [
    cssPlugin,
    flowbiteReact(),
    {
      name: "live-reload",
      setup(build) {
        build.onEnd(() => {
          clients.forEach((client) => client.write("data: update\n\n"));
        });
      },
    },
  ],
};

const ctx = await esbuild.context(buildOptions);
await ctx.watch();

// Initial build
await ctx.rebuild();

// Simple HTTP server
createServer(async (req, res) => {
  const { url } = req;

  if (url === "/esbuild") {
    return clients.add(
      res.writeHead(200, {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
      }),
    );
  }

  try {
    let path = url === "/" ? "/index.html" : url;
    const filePath = path.startsWith("/dist") ? path.slice(1) : `.${path}`;

    const content = await readFile(filePath);
    const ext = path.split(".").pop();

    const contentTypes = {
      html: "text/html",
      js: "text/javascript",
      css: "text/css",
      png: "image/png",
      jpg: "image/jpeg",
      jpeg: "image/jpeg",
      gif: "image/gif",
      svg: "image/svg+xml",
    };

    res.writeHead(200, {
      "Content-Type": contentTypes[ext] || "text/plain",
    });
    res.end(content);
  } catch (e) {
    res.writeHead(404);
    res.end("Not found");
  }
}).listen(3000);

console.log("Development server running on http://localhost:3000");
```

Create `esbuild.build.js`:

```ts
import { readFile } from "node:fs/promises";
import tailwindcss from "@tailwindcss/postcss";
import * as esbuild from "esbuild";
import flowbiteReact from "flowbite-react/plugin/esbuild";
import postcss from "postcss";

const cssPlugin = {
  name: "css",
  setup(build) {
    build.onLoad({ filter: /\.css$/ }, async (args) => {
      const css = await readFile(args.path, "utf8");
      const result = await postcss([tailwindcss]).process(css, {
        from: args.path,
      });

      return {
        contents: result.css,
        loader: "css",
      };
    });
  },
};

await esbuild.build({
  entryPoints: ["src/main.tsx"],
  bundle: true,
  minify: true,
  sourcemap: true,
  outdir: "dist",
  format: "esm",
  loader: {
    ".tsx": "tsx",
    ".ts": "tsx",
    ".jsx": "jsx",
    ".js": "jsx",
  },
  plugins: [cssPlugin, flowbiteReact()],
});
```

Create `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>esbuild React App</title>
    <link rel="stylesheet" href="/dist/main.css" />
    <script type="module" src="/dist/main.js"></script>
    <script>
      new EventSource("/esbuild").addEventListener("message", () => location.reload());
    </script>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
```

Create `src/main.tsx`:

```tsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

import "./index.css";

const root = document.getElementById("root");
if (!root) throw new Error("Root element not found");

createRoot(root).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
```

Create `src/App.tsx`:

```tsx
export default function App() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-50">
      <div className="w-full max-w-md rounded-lg bg-white p-8 shadow-lg">
        <h1 className="mb-4 text-3xl font-bold text-gray-900">esbuild + React + Tailwind</h1>
        <p className="text-gray-600">
          Welcome to your new project! This template is set up with esbuild for blazing-fast builds, React for UI
          components, and Tailwind CSS for styling.
        </p>
      </div>
    </div>
  );
}
```

Create `src/index.css`:

```css
@import "tailwindcss";
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/App.tsx
import { Button } from "flowbite-react";

export default function App() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-esbuild)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-esbuild)


---

## Farm (new)

# Use with Farm - Flowbite React

> Learn how to install Flowbite React with Farm

This guide provides three ways to integrate Flowbite React with Farm:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Farm project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Farm project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t farm
```

This will:

- Create a new Farm project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Farm project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Farm project:

```bash
npx create-farm@latest farm-project
cd farm-project
```

When prompted:

- Select "React"

Install PostCSS:

```bash
npm install @farmfe/js-plugin-postcss postcss
```

Add `@farmfe/js-plugin-postcss` to your `farm.config.ts` file:

```ts {2,5}
import { defineConfig } from "@farmfe/core";
import farmPluginPostcss from "@farmfe/js-plugin-postcss";

export default defineConfig({
  plugins: ["@farmfe/plugin-react", farmPluginPostcss()],
});
```

### 2. Configure Tailwind CSS

Install Tailwind CSS and its dependencies:

```bash
npm install -D tailwindcss @tailwindcss/postcss
```

Create a `postcss.config.mjs` file:

```bash
touch postcss.config.mjs
```

Add `@tailwindcss/postcss` to your `postcss.config.mjs` file:

```js
/** @type {import('postcss-load-config').Config} */
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

Update the css file `src/index.css` to include Tailwind CSS:

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/main.tsx
import { Button } from "flowbite-react";

export function Main() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-farm)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-farm)


---

## Gatsby

# Use with Gatsby - Flowbite React

> Learn how to install Flowbite React for your Gatsby project and start building websites with an open-source static site generator built on top of React and GraphQL

This guide provides three ways to integrate Flowbite React with Gatsby:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Gatsby project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Gatsby project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t gatsby
```

This will:

- Create a new Gatsby project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Gatsby project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations for dark mode

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Gatsby project with Tailwind CSS:

```bash
npm init gatsby
```

When prompted:

- Select `"Tailwind CSS"` to `"Would you like to install a styling system?"` question.

(Omit this when Gatsby CLI tailwind template is updated to v4.)

> **Note:** Install the correct version of Tailwind CSS, Gatsby CLI installs Tailwind CSS v4 by default but their template is configured for v3:

```bash
npm install -D tailwindcss@^3
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

### 3. Configure Dark Mode

In server side rendered applications like Gatsby, to avoid page flicker when dark mode is set, you need to configure the `ThemeModeScript` component:

1. Create `gatsby-ssr.js` file at the root folder of the project:

```js
// gatsby-ssr.js
export const onRenderBody = ({ setPreBodyComponents }) => {
  setPreBodyComponents([]);
};
```

2. Import `ThemeModeScript` and add it to `setPreBodyComponents` function:

```js {2,5}
// gatsby-ssr.js
import { ThemeModeScript } from "flowbite-react";

export const onRenderBody = ({ setPreBodyComponents }) => {
  setPreBodyComponents([ThemeModeScript]);
};
```

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/pages/index.tsx (or .jsx)
import { Button } from "flowbite-react";

export default function IndexPage() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-gatsby)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-gatsby)


---

## Laravel

# Use with Laravel - Flowbite React

> Learn how to install Flowbite React for your Laravel project using Inertia and start building modern websites with the most popular PHP framework in the world

This guide provides three ways to integrate Flowbite React with Laravel:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Laravel project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Laravel project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t laravel
```

This will:

- Create a new Laravel project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure Inertia.js and React
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Laravel project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Laravel Project

Create a new Laravel project with Inertia.js and React support:

```bash
laravel new flowbite-react-laravel --react
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```jsx
// resources/js/pages/welcome.tsx
import { Button } from "flowbite-react";

export default function Welcome() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-laravel)


---

## Meteor.js (new)

# Use with Meteor.js - Flowbite React

> Learn how to install Flowbite React with Meteor.js

This guide provides three ways to integrate Flowbite React with Meteor.js:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Meteor project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Meteor project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t meteorjs
```

This will:

- Create a new Meteor project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Meteor project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Meteor project:

For JavaScript:

```bash
meteor create meteor-project
cd meteor-project
```

For TypeScript:

```bash
meteor create meteor-project --typescript
cd meteor-project
```

### 2. Configure Tailwind CSS

Install Tailwind CSS and its peer dependencies:

```bash
npm install -D tailwindcss @tailwindcss/postcss postcss postcss-load-config
```

Create a `postcss.config.mjs` file:

```bash
touch postcss.config.mjs
```

Add `@tailwindcss/postcss` to your `postcss.config.mjs` file:

```js
/** @type {import('postcss-load-config').Config} */
const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
export default config;
```

Update the css file `client/main.css` to include Tailwind CSS:

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library. Create or update a component in your Meteor app:

```tsx
// imports/ui/App.tsx (or .jsx)
import { Button } from "flowbite-react";
import React from "react";

export const App = () => (
  <>
    <Button>Click me</Button>
  </>
);
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-meteorjs)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-meteorjs)


---

## Modern.js (new)

# Use with Modern.js - Flowbite React

> Learn how to install Flowbite React with Modern.js

This guide provides three ways to integrate Flowbite React with Modern.js:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Modern.js project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Modern.js project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t modernjs
```

This will:

- Create a new Modern.js project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Modern.js project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Modern.js project:

```bash
npx @modern-js/create@latest my-app
cd my-app
```

When prompted, select:

- "Web Application"
- "React"

### 2. Configure Tailwind CSS

Install Tailwind CSS and its dependencies:

```bash
npm install -D tailwindcss @tailwindcss/postcss
```

Update `modern.config.ts` to include Tailwind CSS:

```ts {2,14-20}
import { appTools, defineConfig } from "@modern-js/app-tools";
import tailwindcss from "@tailwindcss/postcss";

// https://modernjs.dev/en/configure/app/usage
export default defineConfig({
  runtime: {
    router: true,
  },
  plugins: [
    appTools({
      bundler: "rspack", // Set to 'webpack' to enable webpack
    }),
  ],
  tools: {
    postcss: {
      postcssOptions: {
        plugins: [tailwindcss],
      },
    },
  },
});
```

Update `src/routes/index.css` to include Tailwind CSS:

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Modern.js to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/routes/page.tsx
import { Button } from "flowbite-react";

export default function Index() {
  return (
    <div className="p-4">
      <Button>Click me</Button>
    </div>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-modernjs)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-modernjs)


---

## Next.js

# Use with Next.js - Flowbite React

> Learn how to install Flowbite React for your Next.js project and start developing with the most popular React-based framework built by Vercel

This guide provides three ways to integrate Flowbite React with Next.js:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Next.js project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Next.js project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t nextjs
```

This will:

- Create a new Next.js project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Next.js project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Next.js project:

When prompted:

- Would you like to use Tailwind CSS? » Yes

```bash
npx create-next-app@latest
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

### 3. Configure Dark Mode (Optional)

To avoid page flicker in dark mode before hydration, add the `ThemeModeScript` to your root layout:

For App Router:

```tsx
// app/layout.tsx
import { ThemeModeScript } from "flowbite-react";

export default function RootLayout({ children }) {
  return (
    <html suppressHydrationWarning>
      <head>
        <ThemeModeScript />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

For Pages Router:

```tsx
// pages/_document.tsx
import { ThemeModeScript } from "flowbite-react";

export default function Document() {
  return (
    <Html suppressHydrationWarning>
      <Head>
        <ThemeModeScript />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
```

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// app/page.tsx
import { Button } from "flowbite-react";

export default function Page() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

#### Official

- [Github](https://github.com/themesberg/flowbite-react-template-nextjs)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-nextjs)

#### Community

- [Kitchen Sink](https://github.com/tulupinc/flowbite-next-starter) - [Demo](https://flowbite-next-starter.vercel.app/)


---

## Parcel

# Use with Parcel - Flowbite React

> Learn how to install Flowbite React for your Parcel project and start developing modern web applications with interactive components

This guide provides three ways to integrate Flowbite React with Parcel:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Parcel project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Parcel project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t parcel
```

This will:

- Create a new Parcel project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Parcel project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

> **Note:** Make sure you have a `.parcelrc` file in your project root. This file is required for proper bundler/plugin detection to work with Flowbite React.

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project with React

Create a new Parcel project:

```bash
mkdir flowbite-react-parcel
cd flowbite-react-parcel
npm init -y
```

Install Parcel and React:

```bash
npm install react react-dom
npm install -D parcel @types/react @types/react-dom
```

Configure `package.json` file and update `scripts` with `start` and `build` steps:

```json {6,7}
{
  "name": "flowbite-react-parcel",
  "private": true,
  "version": "1.0.0",
  "scripts": {
    "start": "parcel src/index.html",
    "build": "parcel build src/index.html"
  }
}
```

Create a `.parcelrc` file:

```json
{
  "extends": ["@parcel/config-default"]
}
```

Create a `tsconfig.json` file in the root of your project:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"]
}
```

Create `src/index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Flowbite React Parcel</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="./index.tsx"></script>
  </body>
</html>
```

Create `src/index.tsx` file:

```tsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./app";

import "./index.css";

const root = createRoot(document.getElementById("root")!);
root.render(
  <StrictMode>
    <App />
  </StrictMode>,
);
```

Create `src/app.tsx` file:

```tsx
export default function App() {
  return <h1>Hello world!</h1>;
}
```

### 2. Configure Tailwind CSS

Install Tailwind CSS and PostCSS:

```bash
npm install -D tailwindcss @tailwindcss/postcss
```

Create `.postcssrc` file and enable the tailwindcss plugin:

```json
{
  "plugins": {
    "@tailwindcss/postcss": {}
  }
}
```

Create a `src/index.css` file and import Tailwind CSS:

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/app.tsx
import { Button } from "flowbite-react";

export default function App() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-parcel)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-parcel)


---

## React Router (new)

# Use with React Router - Flowbite React

> Learn how to install Flowbite React with React Router

React Router v7 can be used either as a framework or as a library. This guide covers both approaches and provides three ways to integrate Flowbite React with each mode:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing React Router project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new React Router project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t react-router
```

This will:

- Create a new React Router project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components and routes

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a React Router project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually, follow these steps:

### 1. Choose Your Mode

#### Framework Mode Setup:

See [React Router as a Framework](https://reactrouter.com/home#react-router-as-a-framework) for more information.

```bash
npx create-react-router@latest my-app
cd my-app
```

#### Library Mode Setup:

See [React Router as a Library](https://reactrouter.com/home#react-router-as-a-library) for more information.

```bash
npx create-vite@latest my-app
cd my-app
```

When prompted, select the "React" option.

Install React Router:

```bash
npm install react-router
```

Set up React Router by updating your `src/main.tsx` file to use the `BrowserRouter` component:

```tsx {3, 10-12}
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router";
import App from "./App";

import "./index.css";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
);
```

#### Configure Tailwind CSS with Vite (Library Mode)

Since the library mode doesn't include Tailwind CSS by default, you'll need to set it up manually:

1. Install Tailwind CSS and its Vite plugin:

```bash
npm install -D tailwindcss @tailwindcss/vite
```

2. Configure the Vite plugin in your `vite.config.ts`:

```ts {1,7}
import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
});
```

3. Add Tailwind CSS to your CSS file (`src/index.css`):

```css
@import "tailwindcss";
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

### Framework Mode Example

```tsx
// app/routes/home.tsx
import { Button } from "flowbite-react";

export default function Home() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

### Library Mode Example

```tsx
// src/App.tsx
import { Button } from "flowbite-react";

export default function App() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-react-router)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-react-router)


---

## React Server (new)

# Use with @lazarv/react-server - Flowbite React

> Learn how to install Flowbite React with @lazarv/react-server framework

This guide provides three ways to integrate Flowbite React with @lazarv/react-server:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing @lazarv/react-server project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new @lazarv/react-server project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t react-server
```

This will:

- Create a new @lazarv/react-server project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components with proper client/server component separation

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a @lazarv/react-server project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new @lazarv/react-server project:

```bash
npx @lazarv/create-react-server@latest
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

### 3. Configure Dark Mode (Optional)

To support dark mode in your application, add the `ThemeModeScript` to your root layout:

```tsx
// src/App.tsx
import { ThemeModeScript } from "flowbite-react";

export function App() {
  return (
    <html lang="en" className="h-screen" suppressHydrationWarning>
      <head>
        <ThemeModeScript />
      </head>
      {/* Rest of your app */}
    </html>
  );
}
```

## Try it out

Now that you have successfully installed Flowbite React, you can start using the components from the library:

```tsx
// src/App.tsx
import { Button } from "flowbite-react";

export default function App() {
  return (
    <html lang="en" className="h-screen" suppressHydrationWarning>
      <head></head>
      <body
        className="flex min-h-full w-full flex-col items-center justify-center dark:bg-zinc-900 dark:text-gray-400"
        suppressHydrationWarning
      >
        <Button>Click me</Button>
      </body>
    </html>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-react-server)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-react-server)


---

## RedwoodJS

# Use with RedwoodJS - Flowbite React

> Learn how to install Flowbite React for your RedwoodJS project and start developing modern full-stack web applications

This guide provides three ways to integrate Flowbite React with RedwoodJS:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing RedwoodJS project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new RedwoodJS project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t redwoodjs
```

This will:

- Create a new RedwoodJS project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure necessary project settings
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a RedwoodJS project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new RedwoodJS project:

```bash
yarn create redwood-app my-redwood-app
cd my-redwood-app
yarn install
```

Create a new homepage using the CLI:

```bash
yarn redwood generate page home /
```

### 2. Configure Tailwind CSS

Install Tailwind CSS using the RedwoodJS CLI:

```bash
yarn rw setup ui tailwindcss
```

This will automatically:

- Install Tailwind CSS and its dependencies
- Create and configure the necessary Tailwind configuration files
- Update your CSS files to include Tailwind directives

### 3. Install Flowbite React

Setup VSCode using Flowbite React CLI:

```bash
npx flowbite-react@latest setup vscode
```

Install Flowbite React in `web` directory:

```bash
cd web && npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// web/src/pages/HomePage/HomePage.tsx
import { Button } from "flowbite-react";

export default function HomePage() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-redwoodjs)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-redwoodjs)


---

## Remix

# Use with Remix - Flowbite React

> Learn how to install Flowbite React for your Remix project to leverage quicker page loads with a full-stack web framework built by Shopify

This guide provides three ways to integrate Flowbite React with Remix:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Remix project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Remix project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t remix
```

This will:

- Create a new Remix project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Remix project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations for dark mode

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Remix project:

```bash
npx create-remix@latest
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

### 3. Configure Dark Mode

In server-side rendered applications like Remix, to avoid page flicker (if `dark` mode is set) before Remix hydrates the content, the `ThemeModeScript` component must be rendered in the `<head>` tag.

`ThemeModeScript` renders a script tag that sets `dark` or removes `dark` from the `<html>` element before hydration occurs.

Import and render `ThemeModeScript` in `app/root.tsx` the `<head>` tag:

```tsx {1,8}
import { ThemeModeScript } from "flowbite-react";

export default function Layout() {
  return (
    <html lang="en">
      <head>
        {/* ... */}
        <ThemeModeScript />
      </head>
      <body>{/* ... */}</body>
    </html>
  );
}
```

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// app/routes/_index.tsx

import { Button } from "flowbite-react";

export default function Index() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-remix)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-remix)


---

## Rsbuild (new)

# Use with Rsbuild - Flowbite React

> Learn how to install Flowbite React with Rsbuild

This guide provides three ways to integrate Flowbite React with Rsbuild:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Rsbuild project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Rsbuild project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t rsbuild
```

This will:

- Create a new Rsbuild project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Rsbuild project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Rsbuild project:

```bash
npx create-rsbuild@latest
```

When prompted, select the "React" option.

### 2. Configure Tailwind CSS

Install Tailwind CSS and its dependencies:

```bash
npm install -D tailwindcss @tailwindcss/postcss
```

Create a `postcss.config.mjs` file:

```bash
touch postcss.config.mjs
```

Add `@tailwindcss/postcss` to your `postcss.config.mjs` file:

```js
/** @type {import('postcss-load-config').Config} */
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

Update the css file `src/App.css` to include Tailwind CSS:

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/App.tsx
import { Button } from "flowbite-react";

export function App() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-rsbuild)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-rsbuild)


---

## Rspack (new)

# Use with Rspack - Flowbite React

> Learn how to install Flowbite React with Rspack

This guide provides three ways to integrate Flowbite React with Rspack:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Rspack project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Rspack project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t rspack
```

This will:

- Create a new Rspack project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Rspack project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Rspack project:

```bash
npx create-rspack@latest
```

When prompted:

- Select the "React" template

### 2. Configure Tailwind CSS

Install Tailwind CSS and PostCSS:

```bash
npm install -D tailwindcss @tailwindcss/postcss postcss postcss-loader
```

Update the `rspack.config.ts` file to enable the postcss-loader:

```ts
export default defineConfig({
  // ...
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["postcss-loader"],
        type: "css",
      },
      // ...
    ],
  },
}
```

Create a `postcss.config.mjs` file:

```bash
touch postcss.config.mjs
```

Add `@tailwindcss/postcss` to your `postcss.config.mjs` file:

```js
/** @type {import('postcss-load-config').Config} */
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

Update the css file `src/index.css` to include Tailwind CSS:

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/App.tsx
import { Button } from "flowbite-react";

export function App() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-rspack)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-rspack)


---

## TanStack Router (new)

# Use with TanStack Router - Flowbite React

> Learn how to install Flowbite React with TanStack Router and start developing with the modern type-safe router for React applications

This guide provides three ways to integrate Flowbite React with TanStack Router:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing TanStack Router project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new TanStack Router project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t tanstack-router
```

This will:

- Create a new TanStack Router project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure example routes and components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a TanStack Router project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new TanStack Router project:

```bash
npx @tanstack/create-router@latest
```

### 2. Configure Tailwind CSS

1. Install Tailwind CSS and its Vite plugin:

```bash
npm install -D tailwindcss @tailwindcss/vite
```

2. Configure the Vite plugin in your `vite.config.ts`:

```ts {1,14}
import tailwindcss from "@tailwindcss/vite";
import { TanStackRouterVite } from "@tanstack/router-plugin/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    TanStackRouterVite({
      target: "react",
      autoCodeSplitting: true,
    }),
    react(),
    tailwindcss(),
  ],
});
```

3. Create a new CSS file (`src/index.css`):

```bash
touch src/index.css
```

4. Add Tailwind CSS to your CSS file (`src/index.css`):

```css
@import "tailwindcss";
```

5. Import the CSS file in your `src/main.tsx` file:

```tsx
import "./index.css";
```

6. Remove Tailwind CSS browser script from the `index.html` file, since we are using the Vite plugin (recommended):

```html
<script src="https://unpkg.com/@tailwindcss/browser@4"></script>
<style type="text/tailwindcss">
  html {
    color-scheme: light dark;
  }
  * {
    @apply border-gray-200 dark:border-gray-800;
  }
  body {
    @apply bg-gray-50 text-gray-950 dark:bg-gray-900 dark:text-gray-200;
  }
</style>
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now you can start using Flowbite React components in your routes:

```tsx
// src/routes/index.tsx
import { createFileRoute } from "@tanstack/react-router";
import { Button } from "flowbite-react";

export const Route = createFileRoute("/")({
  component: HomeComponent,
});

function HomeComponent() {
  return (
    <div className="p-2">
      <Button>Click me</Button>
    </div>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-tanstack-router)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-tanstack-router)


---

## TanStack Start (new)

# Use with TanStack Start - Flowbite React

> Learn how to install Flowbite React with TanStack Start and start developing with the modern type-safe framework for React applications

This guide provides three ways to integrate Flowbite React with TanStack Start:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing TanStack Start project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new TanStack Start project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t tanstack-start
```

This will:

- Create a new TanStack Start project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a TanStack Start project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new TanStack Start project:

```bash
npx degit https://github.com/tanstack/router/examples/react/start-basic start-basic
cd start-basic
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now you can start using Flowbite React components in your application:

```tsx
// app/routes/index.tsx
import { createFileRoute } from "@tanstack/react-router";
import { Button } from "flowbite-react";

export const Route = createFileRoute("/")({
  component: Home,
});

function Home() {
  return (
    <div className="p-2">
      <Button>Click me</Button>
    </div>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-tanstack-start)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-tanstack-start)


---

## Vike (new)

# Use with Vike - Flowbite React

> Learn how to install and set up Flowbite React with Vike (formerly Vite Plugin SSR), a versatile framework for building server-side rendered React applications

This guide provides three ways to integrate Flowbite React with Vike:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Vike project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Vike project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t vike
```

This will:

- Create a new Vike project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure necessary plugins
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Vike project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Vike project using the official template:

```bash
npx create-vike@latest --react --tailwindcss
```

### 2. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// pages/index/+Page.tsx
import { Button } from "flowbite-react";

export default function Page() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-vike)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-vike)


---

## Vite

# Use with Vite - Flowbite React

> Learn how to install Flowbite React for your Vite project and start developing modern web applications with interactive components

This guide provides three ways to integrate Flowbite React with Vite:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Vite project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Vite project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t vite
```

This will:

- Create a new Vite project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure necessary plugins
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Vite project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Vite project with React and TypeScript:

```bash
npx create-vite@latest my-app
cd my-app
```

When prompted, select the "React" option.

### 2. Configure Tailwind CSS

1. Install Tailwind CSS and its Vite plugin:

```bash
npm install -D tailwindcss @tailwindcss/vite
```

2. Configure the Vite plugin in your `vite.config.ts`:

```ts {1,7}
import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
});
```

3. Add Tailwind CSS to your CSS file (`src/index.css`):

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/App.tsx
import { Button } from "flowbite-react";

export default function App() {
  return <Button>Click me</Button>;
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-vite)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-vite)


---

## Waku (new)

# Use with Waku - Flowbite React

> Learn how to install Flowbite React with Waku

This guide provides three ways to integrate Flowbite React with Waku:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Waku project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Waku project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t waku
```

This will:

- Create a new Waku project
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Waku project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new Waku project:

```bash
npx create-waku@latest
```

### 2. Create Vite Config

Create a `vite.config.ts` file in the root of your project:

```ts
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [],
});
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Configure Vite to include Flowbite React plugin

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library. Remember that Waku uses React Server Components by default, so you'll need to add the 'use client' directive to use interactive components:

```tsx
// src/pages/index.tsx
import { Button } from "flowbite-react";

export default async function HomePage() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-waku)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-waku)


---

## Webpack (new)

# Use with Webpack - Flowbite React

> Learn how to install Flowbite React with Webpack

This guide provides three ways to integrate Flowbite React with Webpack:

1. [Quick Start](#quick-start): Create a new project with everything pre-configured
2. [Add to Existing Project](#add-to-existing-project): Add Flowbite React to an existing Webpack project
3. [Manual Setup](#manual-setup): Set up everything from scratch manually

<TextDivider>Quick Start (Recommended)</TextDivider>

## Quick Start

The fastest way to get started is using our project creation CLI, which sets up a new Webpack + React project with Flowbite React, Tailwind CSS, and all necessary configurations:

```bash
npx create-flowbite-react@latest -t webpack
```

This will:

- Create a new React project with Webpack
- Install and configure Tailwind CSS
- Set up Flowbite React with all required dependencies
- Configure dark mode support
- Set up example components

<TextDivider>Add to Existing Project</TextDivider>

## Add to Existing Project

If you already have a Webpack + React project and want to add Flowbite React, you can use our initialization CLI:

```bash
npx flowbite-react@latest init
```

This will automatically:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

<TextDivider>Manual Setup</TextDivider>

## Manual Setup

If you prefer to set everything up manually or need more control over the configuration, follow these steps:

### 1. Create Project

Create a new directory and initialize a new project:

```bash
mkdir webpack-project
cd webpack-project
npm init -y
```

Install necessary packages:

```bash
npm install react react-dom
npm install -D webpack webpack-cli webpack-dev-server @babel/core @babel/preset-react @babel/preset-env @babel/preset-typescript babel-loader typescript @types/react @types/react-dom postcss css-loader style-loader postcss-loader
```

Update your `package.json` to include these scripts:

```json
{
  "scripts": {
    "dev": "webpack serve --mode development --open",
    "build": "webpack --mode production",
    "start": "webpack serve --mode production"
  }
}
```

Create `tsconfig.json` file:

```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": false,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
```

Create `webpack.config.js` file:

```js
const path = require("path");
const { ProvidePlugin } = require("webpack");

module.exports = {
  entry: "./src/index.tsx",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx|js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env", "@babel/preset-react", "@babel/preset-typescript"],
          },
        },
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader", "postcss-loader"],
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js", ".jsx"],
  },
  devServer: {
    static: {
      directory: path.join(__dirname, "public"),
    },
    port: 3000,
  },
  plugins: [
    new ProvidePlugin({
      React: "react",
    }),
  ],
};
```

Create `public/index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Flowbite React + Webpack + TypeScript</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="/bundle.js"></script>
  </body>
</html>
```

Create `src/index.tsx` file:

```tsx
import React from "react";
import { createRoot } from "react-dom/client";
import { App } from "./App";

import "./styles.css";

const container = document.getElementById("root");
if (!container) throw new Error("Failed to find the root element");
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
```

Create `src/App.tsx` file:

```tsx
import React from "react";

export function App() {
  const [count, setCount] = React.useState(0);

  return (
    <div className="p-4">
      <h1 className="mb-4 text-2xl font-bold">Welcome to React + Webpack</h1>
      <p className="mb-4">This is a sample component to test your setup.</p>
      <div className="flex items-center gap-2">
        <button
          onClick={() => setCount(count + 1)}
          className="rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
        >
          Count: {count}
        </button>
      </div>
    </div>
  );
}
```

### 2. Configure Tailwind CSS

Install Tailwind CSS and its dependencies:

```bash
npm install -D tailwindcss @tailwindcss/postcss
```

Create a `postcss.config.mjs` file:

```bash
touch postcss.config.mjs
```

Add `@tailwindcss/postcss` to your `postcss.config.mjs` file:

```js
/** @type {import('postcss-load-config').Config} */
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
```

Create `src/styles.css` file:

```css
@import "tailwindcss";
```

### 3. Install Flowbite React

Install Flowbite React:

```bash
npx flowbite-react@latest init
```

This will:

- Install Flowbite React and its dependencies
- Configure Tailwind CSS to include Flowbite React plugin
- Set up necessary configurations

## Try it out

Now that you have successfully installed Flowbite React you can start using the components from the library:

```tsx
// src/App.tsx
export function App() {
  return (
    <>
      <Button>Click me</Button>
    </>
  );
}
```

<hr />

## Templates

- [Github](https://github.com/themesberg/flowbite-react-template-webpack)
- [StackBlitz](https://stackblitz.com/edit/flowbite-react-template-webpack)


---

# Customize

## Colors (new)

# Colors - Flowbite React

> Learn how to customize and override the default color system in Flowbite React, including base colors, semantic colors, and theme configuration for both Tailwind CSS v3 and v4

Flowbite React comes with a comprehensive color system that includes both base colors and semantic colors, along with additional theme configurations. This guide will show you how to use and customize these settings in your project.

## Default Theme Settings

### Background Images

These background images are used for various UI components:

```js
const backgroundImage = {
  "arrow-down-icon":
    "url('data:image/svg+xml,%3Csvg%20aria-hidden%3D%22true%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill%3D%22none%22%20viewBox%3D%220%200%2010%206%22%3E%3Cpath%20stroke%3D%22%236B7280%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%20stroke-width%3D%222%22%20d%3D%22m1%201%204%204%204-4%22%2F%3E%3C%2Fsvg%3E')",
  "check-icon":
    "url('data:image/svg+xml,%3Csvg%20aria-hidden%3D%27true%27%20xmlns%3D%27http://www.w3.org/2000/svg%27%20fill%3D%27none%27%20viewBox%3D%270%200%2016%2012%27%3E%3Cpath%20stroke%3D%27white%27%20stroke-linecap%3D%27round%27%20stroke-linejoin%3D%27round%27%20stroke-width%3D%273%27%20d%3D%27M1%205.917%205.724%2010.5%2015%201.5%27/%3E%3C/svg%3E')",
  "dash-icon":
    "url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill%3D%22none%22%20viewBox%3D%220%200%2016%2012%22%3E%3Cpath%20stroke%3D%22white%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%20stroke-width%3D%223%22%20d%3D%22M0.5%206h14%22%2F%3E%3C%2Fsvg%3E')",
  "dot-icon":
    "url('data:image/svg+xml,%3Csvg%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22white%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Ccircle%20cx%3D%228%22%20cy%3D%228%22%20r%3D%223%22%2F%3E%3C%2Fsvg%3E')",
};
```

### Box Shadows

Additional box shadow utilities:

```js
const boxShadow = {
  "sm-light": "0 2px 5px 0px rgba(255, 255, 255, 0.08)",
};
```

### Base Colors

The complete set of base colors with their full spectrum:

```js
const baseColors = {
  gray: {
    50: "#F9FAFB",
    100: "#F3F4F6",
    200: "#E5E7EB",
    300: "#D1D5DB",
    400: "#9CA3AF",
    500: "#6B7280",
    600: "#4B5563",
    700: "#374151",
    800: "#1F2937",
    900: "#111827",
  },
  red: {
    50: "#FDF2F2",
    100: "#FDE8E8",
    200: "#FBD5D5",
    300: "#F8B4B4",
    400: "#F98080",
    500: "#F05252",
    600: "#E02424",
    700: "#C81E1E",
    800: "#9B1C1C",
    900: "#771D1D",
  },
  orange: {
    50: "#FFF8F1",
    100: "#FEECDC",
    200: "#FCD9BD",
    300: "#FDBA8C",
    400: "#FF8A4C",
    500: "#FF5A1F",
    600: "#D03801",
    700: "#B43403",
    800: "#8A2C0D",
    900: "#771D1D",
  },
  yellow: {
    50: "#FDFDEA",
    100: "#FDF6B2",
    200: "#FCE96A",
    300: "#FACA15",
    400: "#E3A008",
    500: "#C27803",
    600: "#9F580A",
    700: "#8E4B10",
    800: "#723B13",
    900: "#633112",
  },
  green: {
    50: "#F3FAF7",
    100: "#DEF7EC",
    200: "#BCF0DA",
    300: "#84E1BC",
    400: "#31C48D",
    500: "#0E9F6E",
    600: "#057A55",
    700: "#046C4E",
    800: "#03543F",
    900: "#014737",
  },
  teal: {
    50: "#EDFAFA",
    100: "#D5F5F6",
    200: "#AFECEF",
    300: "#7EDCE2",
    400: "#16BDCA",
    500: "#0694A2",
    600: "#047481",
    700: "#036672",
    800: "#05505C",
    900: "#014451",
  },
  blue: {
    50: "#EBF5FF",
    100: "#E1EFFE",
    200: "#C3DDFD",
    300: "#A4CAFE",
    400: "#76A9FA",
    500: "#3F83F8",
    600: "#1C64F2",
    700: "#1A56DB",
    800: "#1E429F",
    900: "#233876",
  },
  indigo: {
    50: "#F0F5FF",
    100: "#E5EDFF",
    200: "#CDDBFE",
    300: "#B4C6FC",
    400: "#8DA2FB",
    500: "#6875F5",
    600: "#5850EC",
    700: "#5145CD",
    800: "#42389D",
    900: "#362F78",
  },
  purple: {
    50: "#F6F5FF",
    100: "#EDEBFE",
    200: "#DCD7FE",
    300: "#CABFFD",
    400: "#AC94FA",
    500: "#9061F9",
    600: "#7E3AF2",
    700: "#6C2BD9",
    800: "#5521B5",
    900: "#4A1D96",
  },
  pink: {
    50: "#FDF2F8",
    100: "#FCE8F3",
    200: "#FAD1E8",
    300: "#F8B4D9",
    400: "#F17EB8",
    500: "#E74694",
    600: "#D61F69",
    700: "#BF125D",
    800: "#99154B",
    900: "#751A3D",
  },
};
```

### Semantic Colors

The default semantic colors used throughout Flowbite React components:

```js
const semanticColors = {
  primary: {
    50: "#EBF5FF",
    100: "#E1EFFE",
    200: "#C3DDFD",
    300: "#A4CAFE",
    400: "#76A9FA",
    500: "#3F83F8",
    600: "#1C64F2",
    700: "#1A56DB",
    800: "#1E429F",
    900: "#233876",
  },
};
```

## Customizing Colors

### Tailwind CSS v3

For Tailwind CSS v3, you can customize colors by extending the theme in your `tailwind.config.js`:

```js
/** @type {import('tailwindcss').Config} */
export default {
  theme: {
    extend: {
      colors: {
        // Override primary colors
        primary: {
          50: "#f0f9ff",
          100: "#e0f2fe",
          200: "#bae6fd",
          300: "#7dd3fc",
          400: "#38bdf8",
          500: "#0ea5e9",
          600: "#0284c7",
          700: "#0369a1",
          800: "#075985",
          900: "#0c4a6e",
        },
      },
    },
  },
};
```

### Tailwind CSS v4

Tailwind CSS v4 introduces a new color system based on CSS variables. To customize colors define your color variables in the base layer:

```css
@import "tailwindcss";

@theme {
  --color-primary-50: #f0f9ff;
  --color-primary-100: #e0f2fe;
  --color-primary-200: #bae6fd;
  --color-primary-300: #7dd3fc;
  --color-primary-400: #38bdf8;
  --color-primary-500: #0ea5e9;
  --color-primary-600: #0284c7;
  --color-primary-700: #0369a1;
  --color-primary-800: #075985;
  --color-primary-900: #0c4a6e;
}
```


---

## Config (new)

# Configuration - Flowbite React

> Learn how to configure Flowbite React using the config.json file to control component styles, automatic class generation, and more

## Configuration File

The `.flowbite-react/config.json` file is a central configuration file that controls how Flowbite React generates and manages component styles. This guide explains its structure, features, and how it affects your application's behavior.

### Schema

The configuration file follows this JSON Schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "components": {
      "description": "List of component names to generate styles for. Empty array enables automatic detection.",
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "*"
          // ...rest of the components
        ]
      },
      "uniqueItems": true
    },
    "dark": {
      "description": "Whether to generate dark mode styles",
      "type": "boolean",
      "default": true
    },
    "path": {
      "description": "Path where components will be created, relative to the project root",
      "type": "string",
      "default": "src/components"
    },
    "prefix": {
      "description": "Optional prefix to apply to all Tailwind CSS classes",
      "type": "string"
    },
    "rsc": {
      "description": "Whether to include the 'use client' directive for React Server Components",
      "type": "boolean",
      "default": true
    },
    "tsx": {
      "description": "Whether to use TypeScript (.tsx) or JavaScript (.jsx) for component creation",
      "type": "boolean",
      "default": true
    }
  },
  "required": ["components", "dark", "path", "prefix", "rsc", "tsx"]
}
```

### Properties

#### `components`

- Type: `string[]`
- Default: `[]`
- Description: List of component names to generate Tailwind CSS classes for.
  - When empty (`[]`), enables automatic component detection
  - When populated, disables automatic detection and only generates styles for listed components
  - Use `"*"` to explicitly include all components (equivalent to listing every component)
  - When not using `"*"`, use valid component names (e.g., `Button`, `Card`, `Modal`). See the [schema](https://unpkg.com/flowbite-react/schema.json) for the full list of valid components.

#### `dark`

- Type: `boolean`
- Default: `true`
- Description: Whether to generate dark mode styles.

#### `path`

- Type: `string`
- Default: `"src/components"`
- Description: Path where components will be created, relative to the project root. Used by the CLI when creating new components.

#### `prefix`

- Type: `string`
- Default: `""`
- Description: Optional prefix to apply to all Tailwind CSS classes. Useful for avoiding class name conflicts.

For detailed instructions on configuring and using prefixes, see the [Prefix](https://flowbite-react.com/docs/customize/prefix.md) documentation.

#### `rsc`

- Type: `boolean`
- Default: `true`
- Description: Whether to include the 'use client' directive for React Server Components. When set to `true`, the "use client" directive will be added at the top of created component files.

#### `tsx`

- Type: `boolean`
- Default: `true`
- Description: Whether to use TypeScript (.tsx) or JavaScript (.jsx) for component creation. When set to `false`, components will be created with .jsx extension.

## Automatic Class Generation

The automatic class generation system works in two modes:

### 1. Automatic Mode (Default)

When `components` array is empty:

- Automatically scans your codebase for Flowbite React component imports
- Generates styles for all detected components and their dependencies
- Updates in real-time as you add/remove component imports
- Watches for file changes during development

Example config for automatic mode:

```json
{
  "$schema": "https://unpkg.com/flowbite-react/schema.json",
  "components": [],
  "path": "src/components",
  "prefix": "",
  "rsc": true,
  "tsx": true
}
```

### 2. Manual Mode

When `components` array contains component names:

- Disables automatic component detection
- Only generates styles for explicitly listed components
- Includes styles for component dependencies automatically
- Shows warning: "Components specified in config.json. Automatic class generation is disabled."

Example config for manual mode:

```json
{
  "$schema": "https://unpkg.com/flowbite-react/schema.json",
  "components": ["Button", "Card", "Modal"],
  "path": "src/components",
  "prefix": "",
  "rsc": true,
  "tsx": true
}
```

## Component Creation

The CLI uses the configuration file to determine how to create new components:

```bash
npx flowbite-react@latest create my-component
```

The component creation process is affected by these configuration options:

- `path`: Determines where the component will be created
- `rsc`: Determines whether to include the "use client" directive
- `tsx`: Determines whether to use TypeScript (.tsx) or JavaScript (.jsx)

For more information on creating custom components, see the [Custom Components](https://flowbite-react.com/docs/customize/custom-components.md) documentation.

## Build Process

The build process handles style generation differently based on your configuration:

### Development (`flowbite-react dev`)

1. Reads the `config.json` file
2. If `components` is empty:
   - Watches for component imports across your codebase
   - Updates class list in real-time as components are added/removed
   - Generates styles for all detected components
3. If `components` has entries:
   - Generates styles only for listed components
   - Does not watch for new component imports
   - Shows warning about disabled automatic generation

### Production (`flowbite-react build`)

1. Creates the `.flowbite-react` output directory if needed
2. Generates the final `class-list.json` containing:
   - All required Tailwind CSS classes
   - Classes for component dependencies
   - Prefixed classes if prefix is specified
3. Optimizes the class list by:
   - Removing duplicates
   - Sorting for consistency
   - Converting utilities to match your Tailwind version

## Component Dependencies

When generating styles, the system automatically includes dependencies:

- Each component may depend on other components
- Dependencies are defined in the `DEPENDENCY_LIST_MAP`
- When a component is included (either automatically or manually), all its dependencies are also included
- This ensures all necessary styles are available

## Best Practices

**1. Start with Automatic Mode**

- Leave `components` empty initially
- Let the system detect your usage
- Switch to manual mode if you need precise control

**2. Use Manual Mode When**

- You need to strictly control bundle size
- You want to ensure specific components are included
- You have complex dependency requirements

**3. Prefix Considerations**

- Use prefixes when integrating with other libraries
- Keep prefixes short but meaningful
- Consider your Tailwind version when choosing prefix format

**4. Component Creation Settings**

- Use `path` to organize components in your project structure
- Set `rsc` to `false` if you're not using React Server Components
- Set `tsx` to `false` if your project uses JavaScript instead of TypeScript


---

## Custom Components (new)

# Creating Custom Components - Flowbite React

> Learn how to create your own themeable components using the Flowbite React theming system

The Flowbite React theming system can be used to create your own themeable components. The system provides powerful utilities from `resolve-theme.ts` that handle theme resolution, merging, and inheritance.

## Using the CLI

The easiest way to create a new custom component is to use the Flowbite React CLI:

```bash
npx flowbite-react@latest create my-component
```

This will generate a new component with the proper structure and theming setup. The CLI uses the configuration from `.flowbite-react/config.json` to determine:

1. Where to create the component (`path`)
2. Whether to include the `"use client"` directive (`rsc`)
3. Whether to use TypeScript or JavaScript (`tsx`)

You can customize these options in your config file `.flowbite-react/config.json`:

```json
{
  "$schema": "https://unpkg.com/flowbite-react/schema.json",
  "components": [],
  "path": "src/components",
  "prefix": "",
  "rsc": true,
  "tsx": true
}
```

## Component Blueprint

Here's a minimal blueprint for creating Flowbite React components:

```tsx
"use client";

import { createTheme } from "flowbite-react/helpers/create-theme";
import { get } from "flowbite-react/helpers/get";
import { resolveProps } from "flowbite-react/helpers/resolve-props";
import { useResolveTheme } from "flowbite-react/helpers/resolve-theme";
import { twMerge } from "flowbite-react/helpers/tailwind-merge";
import { useThemeProvider } from "flowbite-react/theme/provider";
import type { ThemingProps } from "flowbite-react/types";
import { forwardRef, type ComponentProps } from "react";

// 1. Extend the FlowbiteTheme and FlowbiteProps interfaces
declare module "flowbite-react/types" {
  interface FlowbiteTheme {
    myComponent: MyComponentTheme;
  }

  interface FlowbiteProps {
    myComponent: Partial<WithoutThemingProps<MyComponentProps>>;
  }
}

// 2. Theme structure
export interface MyComponentTheme {
  base: string;
  color: MyComponentColors;
}

export interface MyComponentColors {
  info: string;
  success: string;
  error: string;
}

// 3. Default theme
export const myComponentTheme = createTheme<MyComponentTheme>({
  base: "flex items-center font-medium",
  color: {
    info: "text-blue-600",
    success: "text-green-600",
    error: "text-red-600",
  },
});

// 4. Props
export interface MyComponentProps extends ComponentProps<"div">, ThemingProps<MyComponentTheme> {
  color?: keyof MyComponentColors;
}

// 5. Component
export const MyComponent = forwardRef<HTMLDivElement, MyComponentProps>((props, ref) => {
  // Get theme from provider
  const provider = useThemeProvider();

  // Resolve theme with proper inheritance
  const theme = useResolveTheme(
    [myComponentTheme, provider.theme?.myComponent, props.theme],
    [get(provider.clearTheme, "myComponent"), props.clearTheme],
    [get(provider.applyTheme, "myComponent"), props.applyTheme],
  );

  // Resolve props with provider
  const { children, color = "info", className, ...restProps } = resolveProps(props, provider.props?.myComponent);

  return (
    <div ref={ref} className={twMerge(theme.base, theme.color[color], className)} {...restProps}>
      {children}
    </div>
  );
});

MyComponent.displayName = "MyComponent";
```

## Using the Component

```tsx
import { createTheme, ThemeProvider } from "flowbite-react";
import { MyComponent } from "./MyComponent";

// Custom theme
const theme = createTheme({
  myComponent: {
    base: "flex items-center gap-2 rounded-lg p-2",
    color: {
      info: "bg-blue-100 text-blue-800",
      success: "bg-green-100 text-green-800",
      error: "bg-red-100 text-red-800",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      {/* Basic usage */}
      <MyComponent>Default Component</MyComponent>

      {/* With color */}
      <MyComponent color="success">Success Component</MyComponent>

      {/* With theme override */}
      <MyComponent
        theme={{
          base: "flex items-center gap-4 rounded-full p-3",
          color: {
            info: "bg-purple-100 text-purple-800",
          },
        }}
      >
        Custom Theme
      </MyComponent>

      {/* With theme clearing */}
      <MyComponent clearTheme={{ color: true }}>Default Color Theme</MyComponent>

      {/* With theme application control */}
      <MyComponent
        theme={{
          base: "shadow-lg",
        }}
        applyTheme={{
          base: "merge", // Will merge with existing base styles
        }}
      >
        Merged Styles
      </MyComponent>
    </ThemeProvider>
  );
}
```

## Component Features

The component automatically supports:

- Global theme inheritance
- Component-level overrides
- Provider-level props
- Theme clearing and applying
- Type safety

## Understanding the Blueprint

Let's break down the key parts of the component blueprint:

### 1. Extend the FlowbiteTheme interface

```tsx
declare module "flowbite-react/types" {
  interface FlowbiteTheme {
    myComponent: MyComponentTheme;
  }
}
```

This is necessary to enable TypeScript type inference for your component's theme.

### 2. Theme Structure

```tsx
export interface MyComponentTheme {
  base: string;
  color: MyComponentColors;
}
```

This interface defines the structure of your component's theme. It should include all the customizable style aspects of your component.

### 3. Default Theme

```tsx
const myComponentTheme = createTheme<MyComponentTheme>({
  base: "flex items-center font-medium",
  color: {
    info: "text-blue-600",
    success: "text-green-600",
    error: "text-red-600",
  },
});
```

The default theme provides the base styling for your component when no custom theme is applied. Using `createTheme` ensures type safety and enables Tailwind CSS IntelliSense.

### 4. Props Interface

```tsx
export interface MyComponentProps extends ComponentProps<"div">, ThemingProps<MyComponentTheme> {
  color?: keyof MyComponentColors;
}
```

The props interface extends:

- `ComponentProps<"div">` - All standard HTML div props
- `ThemingProps<MyComponentTheme>` - Theme-related props (`theme`, `clearTheme`, `applyTheme`)
- Custom props specific to your component

### 5. Theme Resolution

```tsx
const theme = useResolveTheme(
  [myComponentTheme, provider.theme?.myComponent, props.theme],
  [get(provider.clearTheme, "myComponent"), props.clearTheme],
  [get(provider.applyTheme, "myComponent"), props.applyTheme],
);
```

The `useResolveTheme` hook handles the complex logic of:

- Merging themes from different sources
- Applying theme clearing
- Controlling how themes are merged or replaced

### 6. Props Resolution

```tsx
const { children, color = "info", className, ...restProps } = resolveProps(props, provider.props?.myComponent);
```

The `resolveProps` helper merges component-specific props with provider-level props, with component props taking precedence.

## Advanced Component Patterns

### Compound Components

For more complex components with multiple parts, you can create separate theme structures for each part:

```tsx
export interface CardTheme {
  root: {
    base: string;
    children: string;
  };
  img: {
    base: string;
    horizontal: string;
  };
  header: {
    base: string;
  };
  footer: {
    base: string;
  };
}
```

### State-Based Styling

For components with different states, include state variations in your theme:

```tsx
export interface ButtonTheme {
  base: string;
  color: Record<string, string>;
  disabled: string;
  loading: string;
}
```

### Responsive Components

For responsive components, include different size variations:

```tsx
export interface ModalTheme {
  base: string;
  show: {
    on: string;
    off: string;
  };
  sizes: {
    sm: string;
    md: string;
    lg: string;
    xl: string;
    "2xl": string;
    "3xl": string;
    "4xl": string;
    "5xl": string;
    "6xl": string;
    "7xl": string;
  };
}
```

## Best Practices

1. **Keep Theme Structures Flat**: Avoid deeply nested theme structures when possible
2. **Use Descriptive Names**: Name theme properties clearly to make customization intuitive
3. **Provide Sensible Defaults**: Default themes should work well without customization
4. **Document Theme Structure**: Include comments or documentation for complex theme properties
5. **Use Type Safety**: Always use TypeScript interfaces for theme structures
6. **Test with Different Themes**: Ensure your component works with various theme configurations

By following these patterns, you can create flexible, themeable components that integrate seamlessly with the Flowbite React theming system.


---

## Dark Mode

# Dark Mode - Flowbite React

> Learn how to implement and customize dark mode in your React application using Flowbite and Tailwind CSS. Includes step-by-step instructions for theme switching, SSR support, and framework-specific integrations.

## Overview

Flowbite React provides built-in dark mode functionality that seamlessly integrates with popular full-stack frameworks like Next.js, Remix, Astro, and Gatsby. The dark mode implementation fully supports server-side rendering (SSR) and offers an intuitive developer experience.

## Dark Mode Toggle

The easiest way to implement dark mode in your application is by using the `DarkThemeToggle` component. This component automatically handles theme detection and provides a user-friendly interface for switching between light and dark modes.

```jsx
import { DarkThemeToggle } from "flowbite-react";

export default function MyPage() {
  return (
    // ...
    <DarkThemeToggle />
  );
}
```

## Theme Mode Hook

For more granular control over theme management, Flowbite React provides the `useThemeMode` hook. This powerful hook handles:

- Theme state management
- Automatic theme detection
- Theme persistence in LocalStorage
- Cross-tab theme synchronization

### Hook API

```tsx
type ThemeMode = "light" | "dark" | "auto";

declare const useThemeMode: () => {
  mode: ThemeMode;
  computedMode: ThemeMode; // "light" | "dark"
  setMode: (mode: ThemeMode) => void;
  toggleMode: () => void;
  clearMode: () => void;
};
```

### Features

1. **Automatic Theme Persistence**: Your users' theme preferences are automatically saved in the browser's LocalStorage
2. **Cross-Tab Synchronization**: Theme changes are instantly synchronized across all open browser tabs
3. **No Additional Configuration**: All features work out of the box

## Disabling Dark Mode

To completely disable dark mode class generation in your Flowbite React application, you should use both of the following methods:

### 1. Using the ThemeConfig Component

First, disable dark mode at the application level by setting the `dark` prop to `false` in the `ThemeConfig` component:

```jsx
import { ThemeConfig } from "flowbite-react";

function App() {
  return (
    <>
      <ThemeConfig dark={false} />
      {/* Your application */}
    </>
  );
}
```

This approach prevents the dark mode toggle functionality from working in your application's runtime.

### 2. Using the Configuration File

Additionally, you must disable dark mode in your build configuration by setting the `dark` property to `false` in your `.flowbite-react/config.json` file:

```json {4}
{
  "$schema": "https://unpkg.com/flowbite-react/schema.json",
  "components": [],
  "dark": false,
  "path": "src/components",
  "prefix": "",
  "rsc": true,
  "tsx": true
}
```

This method prevents dark mode classes from being generated during the build process, which reduces your CSS bundle size.

> **Important**: For complete dark mode disabling, both methods should be used together. The ThemeConfig approach affects runtime behavior, while the config.json approach affects build-time class generation.

## Framework Integration

For detailed, framework-specific implementation instructions, refer to our comprehensive integration guides:

- [AdonisJS Dark Mode](https://flowbite-react.com/docs/guides/adonisjs#dark-mode.md)
- [Astro Dark Mode](https://flowbite-react.com/docs/guides/astro#dark-mode.md)
- [Gatsby Dark Mode](https://flowbite-react.com/docs/guides/gatsby#dark-mode.md)
- [Next.js Dark Mode](https://flowbite-react.com/docs/guides/nextjs#dark-mode.md)
- [Remix Dark Mode](https://flowbite-react.com/docs/guides/remix#dark-mode.md)


---

## Prefix (new)

# Prefix - Flowbite React

> Learn how you can change the Tailwind CSS classes prefix used by the components in Flowbite React

By following these steps, you can easily customize the Tailwind CSS prefix in your Flowbite React project, ensuring better compatibility with other CSS frameworks and avoiding class name conflicts.

## Setting the Prefix

### Flowbite React Configuration

To set a custom prefix for Flowbite React components, modify the `prefix` property in your `.flowbite-react/config.json` file:

```json {6}
{
  "$schema": "https://unpkg.com/flowbite-react/schema.json",
  "components": [],
  "dark": true,
  "path": "components",
  "prefix": "tw",
  "rsc": true,
  "tsx": true
}
```

### Tailwind CSS Configuration

You must also configure the prefix in your Tailwind CSS setup. The configuration syntax differs between Tailwind CSS versions:

#### Tailwind CSS v3

In Tailwind CSS v3, you can use any prefix including special characters:

```js
/** @type {import('tailwindcss').Config} */
export default {
  prefix: "tw-",
  // ... rest of your config
};
```

#### Tailwind CSS v4

In Tailwind CSS v4, the prefix cannot contain special characters (like hyphens). Use simple strings like `tw` instead of `tw-`:

```css
@import "tailwindcss" prefix(tw);
```

## Update Your React Application

Next, render the `ThemeConfig` component at the **root of your app** with the same `prefix` property:

```tsx {1,6}
import { ThemeConfig } from "flowbite-react";

export default function App() {
  return (
    <>
      <ThemeConfig prefix="tw" />
      {/* ... */}
    </>
  );
}
```

This configuration will ensure that all Flowbite React components use the specified prefix for their Tailwind CSS classes. The prefix will be automatically applied to all component classes.


---

## Theme (updated)

# Theme - Flowbite React

> Learn how to customize the appearance of Flowbite React components using the theming system

Flowbite React provides a flexible theming system that allows you to customize the appearance of components. The system is built on top of Tailwind CSS and supports multiple levels of customization.

## Component-Level Customization

The simplest way to customize a component is by using the `className` prop, which allows you to override or extend the default styles:

```tsx
import { Button } from "flowbite-react";

function App() {
  return <Button className="bg-red-500 hover:bg-red-600">Custom Button</Button>;
}
```

## Theme Provider

For application-wide customization, use the `ThemeProvider` component. The `createTheme` helper provides TypeScript and Tailwind CSS IntelliSense support:

```tsx
import { Button, createTheme, ThemeProvider } from "flowbite-react";

const customTheme = createTheme({
  button: {
    color: {
      primary: "bg-red-500 hover:bg-red-600",
      secondary: "bg-blue-500 hover:bg-blue-600",
    },
    size: {
      lg: "px-6 py-3 text-lg",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={customTheme}>
      <Button color="primary">Red Button</Button>
      <Button color="secondary" size="lg">
        Large Blue Button
      </Button>
    </ThemeProvider>
  );
}
```

## Theme Resolution and Inheritance

The theming system follows this resolution order:

1. Component-specific `clearTheme` prop
2. Component-specific `theme` prop
3. Nearest parent `ThemeProvider` theme
4. Default component theme

When using nested `ThemeProvider` components, the following rules apply:

Unless `root={true}` is specified:

- Child providers inherit and merge all theme values from their parent
- They only override the specific values they define
- Parent values for undefined properties are preserved

When `root={true}` is specified:

- The theme provider ignores all parent theme values
- No merging occurs with parent themes
- Only the specified theme and default theme values are used
- This affects all theme-related props (`theme`, `clearTheme`, `applyTheme`) and component props

## Nested Themes

```tsx
import { Button, createTheme, ThemeProvider } from "flowbite-react";

const mainTheme = createTheme({
  button: {
    color: {
      primary: "bg-blue-500 hover:bg-blue-600",
    },
    size: {
      lg: "px-6 py-3",
    },
  },
});

const sectionTheme = createTheme({
  button: {
    color: {
      primary: "bg-green-500 hover:bg-green-600",
      // size.lg from mainTheme is preserved
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={mainTheme}>
      <Button size="lg">Blue Large Button</Button>
      <ThemeProvider theme={sectionTheme}>
        {/* Inherits size.lg from mainTheme */}
        <Button size="lg">Green Large Button</Button>
      </ThemeProvider>
    </ThemeProvider>
  );
}
```

### Preventing Theme Inheritance

```tsx
import { Button, createTheme, ThemeProvider } from "flowbite-react";

const mainTheme = createTheme({
  button: {
    color: {
      primary: "bg-blue-500 hover:bg-blue-600",
    },
    size: {
      lg: "px-6 py-3",
    },
  },
});

const isolatedTheme = createTheme({
  button: {
    color: {
      primary: "bg-green-500 hover:bg-green-600",
    },
    // No size definitions
  },
});

function App() {
  return (
    <ThemeProvider theme={mainTheme}>
      <Button size="lg">Large Blue Button</Button>

      {/* root={true} prevents merging with mainTheme */}
      <ThemeProvider theme={isolatedTheme} root>
        <Button size="lg">
          {/* size="lg" will use default theme since isolatedTheme
              doesn't define sizes and parent theme is ignored */}
        </Button>
      </ThemeProvider>
    </ThemeProvider>
  );
}
```

### Theme Merging Strategy

The theme system uses the following merging strategy:

1. **Props Merging**: Component props from parent and child `ThemeProvider`s are deep merged
2. **Theme Merging**: Theme values are merged using [tailwind-merge](https://www.npmjs.com/package/tailwind-merge) for intelligent Tailwind CSS class handling
3. **Clear Theme Merging**: `clearTheme` values are deep merged between providers
4. **Apply Theme Merging**: `applyTheme` configurations are deep merged between providers

The use of `tailwind-merge` ensures:

- Automatic conflict resolution between Tailwind CSS classes
- Support for both Tailwind CSS v3 and v4 (automatically detected)
- Proper handling of complex class combinations
- Efficient merging without duplicate utilities

For example:

```tsx
import { Button, createTheme, ThemeProvider } from "flowbite-react";

const baseTheme = createTheme({
  button: {
    base: "rounded-lg shadow-md",
    color: {
      primary: "bg-blue-500 text-white",
    },
  },
});

const customTheme = createTheme({
  button: {
    base: "border-2",
    color: {
      primary: "bg-red-500",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={baseTheme}>
      {/* Merges themes: rounded-lg shadow-md border-2 */}
      <Button theme={customTheme.button}>Merged Styles</Button>

      {/* Replaces base completely: only border-2 remains */}
      <Button theme={customTheme.button} applyTheme={{ base: "replace" }}>
        Replaced Base Style
      </Button>

      {/* Replaces color completely: loses text-white */}
      <Button theme={customTheme.button} applyTheme={{ color: { primary: "replace" } }}>
        Replaced Color
      </Button>
    </ThemeProvider>
  );
}
```

## Theme Modification Tools

The combination of `theme`, `clearTheme`, and `applyTheme` props provides granular control over component styling. Here are examples showing different levels of customization:

### Component Level Control

```tsx
import { Card, createTheme } from "flowbite-react";

const cardTheme = createTheme({
  card: {
    root: {
      base: "rounded-xl bg-white shadow-md",
      children: "space-y-4 p-6",
    },
    img: {
      base: "rounded-t-xl",
      horizontal: "h-full w-full rounded-l-xl",
    },
  },
});

function App() {
  return (
    <>
      {/* Basic theme override */}
      <Card theme={cardTheme.card}>Basic Theme Override</Card>

      {/* Clear specific nested properties */}
      <Card
        theme={cardTheme.card}
        clearTheme={{
          root: { children: true }, // Clear only padding and spacing
          img: { horizontal: true }, // Clear horizontal image styles
        }}
      >
        Selective Clearing
      </Card>

      {/* Control how new styles are applied */}
      <Card
        theme={cardTheme.card}
        applyTheme={{
          root: { base: "replace" }, // Replace entire base styles
          img: { base: "merge" }, // Merge with existing image styles
        }}
      >
        Controlled Style Application
      </Card>

      {/* Combining all three props */}
      <Card theme={cardTheme.card} clearTheme={{ root: { children: true } }} applyTheme={{ img: { base: "replace" } }}>
        Complex Style Control
      </Card>
    </>
  );
}
```

### Nested Component Control

```tsx
import { createTheme, Navbar, NavbarCollapse, NavbarLink, ThemeProvider } from "flowbite-react";

const navTheme = createTheme({
  navbar: {
    root: {
      base: "bg-white shadow-lg",
    },
    collapse: {
      base: "w-full md:block md:w-auto",
      list: "mt-4 flex flex-col md:mt-0 md:flex-row md:space-x-8",
    },
    link: {
      base: "block px-3 py-2",
      active: {
        on: "text-blue-600",
        off: "text-gray-900",
      },
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={navTheme}>
      <Navbar>
        {/* Control collapse styles */}
        <NavbarCollapse
          clearTheme={{ list: true }} // Remove default list styles
          applyTheme={{ base: "replace" }} // Replace base styles
        >
          {/* Control individual link styles */}
          <NavbarLink
            href="#"
            active
            theme={{
              base: "font-medium",
              active: {
                on: "text-green-600", // Override active state
              },
            }}
            applyTheme={{
              active: { on: "merge" }, // Merge active state styles
            }}
          >
            Custom Link
          </NavbarLink>
        </NavbarCollapse>
      </Navbar>
    </ThemeProvider>
  );
}
```

### Form Components Control

```tsx
import { createTheme, Label, TextInput } from "flowbite-react";

const formTheme = createTheme({
  label: {
    root: {
      base: "text-sm font-medium",
      disabled: "opacity-50",
      colors: {
        default: "text-gray-900",
        error: "text-red-700",
      },
    },
  },
  textInput: {
    base: "block w-full",
    field: {
      base: "rounded-lg border",
      input: {
        base: "px-3 py-2",
        sizes: {
          sm: "text-sm",
          md: "text-base",
        },
        colors: {
          gray: "border-gray-300 bg-gray-50",
          error: "border-red-500 bg-red-50",
        },
      },
    },
  },
});

function App() {
  return (
    <form>
      {/* Label with error state */}
      <Label
        theme={formTheme.label}
        color="error"
        clearTheme={{
          root: { disabled: true }, // Remove disabled styles
        }}
      >
        Email
      </Label>

      {/* Input with custom styling */}
      <TextInput
        theme={formTheme.textInput}
        color="error"
        size="sm"
        applyTheme={{
          field: {
            input: {
              colors: { error: "replace" }, // Replace error styles
              sizes: { sm: "merge" }, // Merge size styles
            },
          },
        }}
      />

      {/* Combining multiple controls */}
      <TextInput
        theme={formTheme.textInput}
        clearTheme={{
          field: {
            input: { sizes: true }, // Remove all size variations
          },
        }}
        applyTheme={{
          base: "merge", // Merge base styles
          field: { base: "replace" }, // Replace field base styles
        }}
      />
    </form>
  );
}
```

These examples demonstrate how to:

- Use nested theme properties for precise control
- Clear specific style categories while preserving others
- Control how new styles are merged or replaced
- Combine multiple theme controls for complex customization
- Handle component-specific theme variations
- Manage state-dependent styles (active, disabled, etc.)

## Clearing Theme Values

The `clearTheme` prop allows you to selectively or completely remove theme values, reverting them to their default styles. When a theme value is cleared, it's set to an empty string.

### Basic Usage

```tsx
import { Button, createTheme, ThemeProvider } from "flowbite-react";

const theme = createTheme({
  button: {
    color: {
      primary: "bg-red-500 hover:bg-red-600",
    },
    base: "rounded-lg",
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Button>Red Rounded Button</Button>
      {/* Clear specific theme property */}
      <Button clearTheme={{ color: true }}>Default Color, Still Rounded</Button>
      {/* Clear all button theme values */}
      <Button clearTheme>Completely Default Button</Button>
    </ThemeProvider>
  );
}
```

### Selective Clearing

You can clear specific nested properties while keeping others:

```tsx
import { Card, createTheme, ThemeProvider } from "flowbite-react";

const theme = createTheme({
  card: {
    root: {
      base: "rounded-xl shadow-lg",
      children: "space-y-4 p-6",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Card>Regular Card</Card>
      <Card clearTheme={{ root: { children: true } }}>
        {/* Keeps rounded-xl and shadow-lg, but clears padding and spacing */}
      </Card>
    </ThemeProvider>
  );
}
```

## Applying Theme Values

The `applyTheme` prop provides fine-grained control over how theme values are merged. It supports two modes:

- `"merge"` (default): Combines the new theme values with existing ones
- `"replace"`: Completely replaces existing theme values

### Merging vs Replacing

```tsx
import { Button, createTheme, ThemeProvider } from "flowbite-react";

const baseTheme = createTheme({
  button: {
    base: "rounded-lg shadow-md",
    color: {
      primary: "bg-blue-500 text-white",
    },
  },
});

const customTheme = createTheme({
  button: {
    base: "border-2",
    color: {
      primary: "bg-red-500",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={baseTheme}>
      {/* Merges themes: rounded-lg shadow-md border-2 */}
      <Button theme={customTheme.button}>Merged Styles</Button>

      {/* Replaces base completely: only border-2 remains */}
      <Button theme={customTheme.button} applyTheme={{ base: "replace" }}>
        Replaced Base Style
      </Button>

      {/* Replaces color completely: loses text-white */}
      <Button theme={customTheme.button} applyTheme={{ color: { primary: "replace" } }}>
        Replaced Color
      </Button>
    </ThemeProvider>
  );
}
```

### Inheritance Control

The `applyTheme` prop is particularly useful when working with nested components:

```tsx
import { createTheme, Navbar, NavbarCollapse, NavbarLink, ThemeProvider } from "flowbite-react";

const theme = createTheme({
  navbar: {
    root: {
      base: "bg-white shadow-lg",
    },
    collapse: {
      base: "w-full md:block md:w-auto",
      list: "mt-4 flex flex-col md:mt-0 md:flex-row md:space-x-8",
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Navbar>
        <NavbarCollapse
          applyTheme={{
            list: "replace", // Replace entire list styles
          }}
        >
          <NavbarLink href="#">Custom Layout</NavbarLink>
        </NavbarCollapse>
      </Navbar>
    </ThemeProvider>
  );
}
```

### Theme Resolution Order

When both `clearTheme` and `applyTheme` are used, the resolution follows this order:

1. Apply `clearTheme` to remove specified values
2. Apply component-specific `theme` prop
3. Apply `applyTheme` rules to control how new values are merged
4. Inherit from parent `ThemeProvider` (unless `root={true}`)
5. Fall back to default component theme

This system provides complete control over theme inheritance and application while maintaining a predictable behavior.

## Provider-Level Props

The `ThemeProvider` component accepts a `props` prop that allows you to set default props for all components within its scope. These props are merged with any component-specific props, with component props taking precedence:

```tsx
import { Button, ThemeProvider } from "flowbite-react";

function App() {
  return (
    <ThemeProvider
      props={{
        // Set default props for all buttons
        button: {
          color: "success",
          size: "lg",
        },
      }}
    >
      {/* Will be large and green */}
      <Button>Inherits Provider Props</Button>

      {/* Will be large and red (color prop overrides provider) */}
      <Button color="error">Overrides Color Prop</Button>

      {/* Nested providers merge props by default */}
      <ThemeProvider
        props={{
          button: {
            size: "sm", // Override size while keeping color from parent
          },
        }}
      >
        {/* Will be small and green */}
        <Button>Inherits Merged Props</Button>
      </ThemeProvider>

      {/* root={true} prevents props inheritance */}
      <ThemeProvider
        root
        props={{
          button: {
            size: "sm",
          },
        }}
      >
        {/* Will be small with default color */}
        <Button>Independent Props</Button>
      </ThemeProvider>
    </ThemeProvider>
  );
}
```

Props are resolved in the following order:

1. Component-specific props
2. Nearest parent `ThemeProvider` props
3. Default component props

Like themes, provider props are deep merged between parent and child providers unless `root={true}` is specified.

## Component-Specific Theme

You can also apply a custom theme to a specific component instance using the `theme` prop:

```tsx
import { Button, createTheme } from "flowbite-react";

const buttonTheme = createTheme({
  button: {
    color: {
      custom: "bg-purple-500 text-white hover:bg-purple-600",
    },
  },
}).button;

function App() {
  return (
    <Button theme={buttonTheme} color="custom">
      Purple Button
    </Button>
  );
}
```

## Type Safety and IntelliSense

The `createTheme` helper ensures type safety and enables Tailwind CSS IntelliSense in your IDE:

```tsx
import { createTheme } from "flowbite-react";

// Full theme customization
const theme = createTheme({
  button: {
    color: {
      primary: "bg-blue-500 hover:bg-blue-600", // ✓ Tailwind CSS IntelliSense
      custom: 123, // ✗ Type error: expected string
    },
  },
});

// Single component theme
const buttonTheme = createTheme({
  button: {
    size: {
      xl: "px-8 py-4 text-xl", // ✓ Tailwind CSS IntelliSense
    },
  },
}).button;
```

This helps catch errors early and provides better development experience with auto-completion for Tailwind CSS classes.

For information on how to create your own themeable components that work with this system, see the [Creating Custom Components](https://flowbite-react.com/docs/customize/custom-components.md) guide.


---

# Components

## Accordion

# React Accordion - Flowbite

> Use the accordion component and its options to expand and collapse the content inside each panel based on state reactivity from React and Tailwind CSS

The accordion component from Flowbite React can be used to toggle the visibility of the content of each accordion panel tab by expanding the collapsing the trigger element based on multiple examples and styles.

The reactivity and state is handled by React and the components is built using the Tailwind CSS framework meaning that you can easily customize the styles and colors of the accordion.

To use the accordion component, you need to import the `<Accordion>` component from `flowbite-react`:

```jsx
import { Accordion } from "flowbite-react";
```

## Default accordion

Use this example of the `<Accordion>` component and the `<AccordionPanel>` and `<AccordionTitle>` subcomponents to create an accordion with multiple panels.

```tsx
// index.tsx

import { Accordion, AccordionContent, AccordionPanel, AccordionTitle } from "flowbite-react";

export function Component() {
  return (
    <Accordion>
      <AccordionPanel>
        <AccordionTitle>What is Flowbite?</AccordionTitle>
        <AccordionContent>
          <p className="mb-2 text-gray-500 dark:text-gray-400">
            Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons,
            dropdowns, modals, navbars, and more.
          </p>
          <p className="text-gray-500 dark:text-gray-400">
            Check out this guide to learn how to&nbsp;
            <a
              href="https://flowbite.com/docs/getting-started/introduction/"
              className="text-cyan-600 hover:underline dark:text-cyan-500"
            >
              get started&nbsp;
            </a>
            and start developing websites even faster with components on top of Tailwind CSS.
          </p>
        </AccordionContent>
      </AccordionPanel>
      <AccordionPanel>
        <AccordionTitle>Is there a Figma file available?</AccordionTitle>
        <AccordionContent>
          <p className="mb-2 text-gray-500 dark:text-gray-400">
            Flowbite is first conceptualized and designed using the Figma software so everything you see in the library
            has a design equivalent in our Figma file.
          </p>
          <p className="text-gray-500 dark:text-gray-400">
            Check out the
            <a href="https://flowbite.com/figma/" className="text-cyan-600 hover:underline dark:text-cyan-500">
              Figma design system
            </a>
            based on the utility classes from Tailwind CSS and components from Flowbite.
          </p>
        </AccordionContent>
      </AccordionPanel>
      <AccordionPanel>
        <AccordionTitle>What are the differences between Flowbite and Tailwind UI?</AccordionTitle>
        <AccordionContent>
          <p className="mb-2 text-gray-500 dark:text-gray-400">
            The main difference is that the core components from Flowbite are open source under the MIT license, whereas
            Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone
            components, whereas Tailwind UI offers sections of pages.
          </p>
          <p className="mb-2 text-gray-500 dark:text-gray-400">
            However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no
            technical reason stopping you from using the best of two worlds.
          </p>
          <p className="mb-2 text-gray-500 dark:text-gray-400">Learn more about these technologies:</p>
          <ul className="list-disc pl-5 text-gray-500 dark:text-gray-400">
            <li>
              <a href="https://flowbite.com/pro/" className="text-cyan-600 hover:underline dark:text-cyan-500">
                Flowbite Pro
              </a>
            </li>
            <li>
              <a
                href="https://tailwindui.com/"
                rel="nofollow"
                className="text-cyan-600 hover:underline dark:text-cyan-500"
              >
                Tailwind UI
              </a>
            </li>
          </ul>
        </AccordionContent>
      </AccordionPanel>
    </Accordion>
  );
}
```

## Collapse all

Use this example to automatically collapse all of the accordion panels by passing the `collapseAll` prop to the `<Accordion>` component.

```tsx
// index.tsx

import { Accordion, AccordionContent, AccordionPanel, AccordionTitle } from "flowbite-react";

export function Component() {
  return (
    <Accordion collapseAll>
      <AccordionPanel>
        <AccordionTitle>What is Flowbite?</AccordionTitle>
        <AccordionContent>
          <p className="mb-2 text-gray-500 dark:text-gray-400">
            Flowbite is an open-source library of interactive components built on top of Tailwind CSS including buttons,
            dropdowns, modals, navbars, and more.
          </p>
          <p className="text-gray-500 dark:text-gray-400">
            Check out this guide to learn how to&nbsp;
            <a
              href="https://flowbite.com/docs/getting-started/introduction/"
              className="text-cyan-600 hover:underline dark:text-cyan-500"
            >
              get started&nbsp;
            </a>
            and start developing websites even faster with components on top of Tailwind CSS.
          </p>
        </AccordionContent>
      </AccordionPanel>
      <AccordionPanel>
        <AccordionTitle>Is there a Figma file available?</AccordionTitle>
        <AccordionContent>
          <p className="mb-2 text-gray-500 dark:text-gray-400">
            Flowbite is first conceptualized and designed using the Figma software so everything you see in the library
            has a design equivalent in our Figma file.
          </p>
          <p className="text-gray-500 dark:text-gray-400">
            Check out the
            <a href="https://flowbite.com/figma/" className="text-cyan-600 hover:underline dark:text-cyan-500">
              Figma design system
            </a>
            based on the utility classes from Tailwind CSS and components from Flowbite.
          </p>
        </AccordionContent>
      </AccordionPanel>
      <AccordionPanel>
        <AccordionTitle>What are the differences between Flowbite and Tailwind UI?</AccordionTitle>
        <AccordionContent>
          <p className="mb-2 text-gray-500 dark:text-gray-400">
            The main difference is that the core components from Flowbite are open source under the MIT license, whereas
            Tailwind UI is a paid product. Another difference is that Flowbite relies on smaller and standalone
            components, whereas Tailwind UI offers sections of pages.
          </p>
          <p className="mb-2 text-gray-500 dark:text-gray-400">
            However, we actually recommend using both Flowbite, Flowbite Pro, and even Tailwind UI as there is no
            technical reason stopping you from using the best of two worlds.
          </p>
          <p className="mb-2 text-gray-500 dark:text-gray-400">Learn more about these technologies:</p>
          <ul className="list-disc pl-5 text-gray-500 dark:text-gray-400">
            <li>
              <a href="https://flowbite.com/pro/" className="text-cyan-600 hover:underline dark:text-cyan-500">
                Flowbite Pro
              </a>
            </li>
            <li>
              <a
                href="https://tailwindui.com/"
                rel="nofollow"
                className="text-cyan-600 hover:underline dark:text-cyan-500"
              >
                Tailwind UI
              </a>
            </li>
          </ul>
        </AccordionContent>
      </AccordionPanel>
    </Accordion>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "divide-y divide-gray-200 border-gray-200 dark:divide-gray-700 dark:border-gray-700",
    "flush": {
      "off": "rounded-lg border",
      "on": "border-b"
    }
  },
  "content": {
    "base": "p-5 first:rounded-t-lg last:rounded-b-lg dark:bg-gray-900"
  },
  "title": {
    "arrow": {
      "base": "h-6 w-6 shrink-0",
      "open": {
        "off": "",
        "on": "rotate-180"
      }
    },
    "base": "flex w-full items-center justify-between p-5 text-left font-medium text-gray-500 first:rounded-t-lg last:rounded-b-lg dark:text-gray-400",
    "flush": {
      "off": "hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 dark:hover:bg-gray-800 dark:focus:ring-gray-800",
      "on": "bg-transparent dark:bg-transparent"
    },
    "heading": "",
    "open": {
      "off": "",
      "on": "bg-gray-100 text-gray-900 dark:bg-gray-800 dark:text-white"
    }
  }
}
```

## References

- [Flowbite Accordion](https://flowbite.com/docs/components/accordion/)


---

## Alert

# React Alert - Flowbite

> Get started with the alert component to show contextual information to the user such as when validating forms or showing errors based on React and Tailwind CSS

The alert component can be used to show a contextual text to the user such as a success or error message after form validation inside an alert box where you can choose from multiple colors, sizes, and styles.

The examples below are styled with Tailwind CSS and the reactivity is handled by React and you can also add any type of content inside the alert box.

To start using the alert box you need to import the `<Alert>` component from the `flowbite-react` package:

```jsx
import { Alert } from "flowbite-react";
```

## Default alert

The default alert component is a simple alert box with a text inside it and you can use the `color` prop to change the color of the alert box and the `title` prop to add a title to the alert box.

Inside of the `<Alert>` component you can add any type of content such as text, images, or other components as they will be considered children of the alert box.

```tsx
// index.tsx

import { Alert } from "flowbite-react";

export function Component() {
  return (
    <Alert color="info">
      <span className="font-medium">Info alert!</span> Change a few things up and try submitting again.
    </Alert>
  );
}
```

## Alert with icon

Use the `icon` prop to add an icon to the alert box and you can use any icon from the [React Icons](https://react-icons.github.io/react-icons/) library.

```tsx
// index.tsx

"use client";

import { Alert } from "flowbite-react";
import { HiInformationCircle } from "react-icons/hi";

export function Component() {
  return (
    <Alert color="failure" icon={HiInformationCircle}>
      <span className="font-medium">Info alert!</span> Change a few things up and try submitting again.
    </Alert>
  );
}
```

## Dismissible alert

You can use the `onDismiss` prop on the `<Alert>` component to add a dismiss button to the alert box by adding a function inside of it that will be called when the user clicks on the dismiss button.

```tsx
// index.tsx

"use client";

import { Alert } from "flowbite-react";

export function Component() {
  return (
    <Alert color="success" onDismiss={() => alert('Alert dismissed!')}>
      <span className="font-medium">Info alert!</span> Change a few things up and try submitting again.
    </Alert>
  );
}
```

## Rounded alert

To make the alert box rounded you can use the `rounded` prop on the `<Alert>` component.

```tsx
// index.tsx

import { Alert } from "flowbite-react";

export function Component() {
  return (
    <Alert color="warning" rounded>
      <span className="font-medium">Info alert!</span> Change a few things up and try submitting again.
    </Alert>
  );
}
```

## Border accent

Add a border accent to the alert box by applying the `withBorderAccent` prop on the `<Alert>` component.

```tsx
// index.tsx

import { Alert } from "flowbite-react";

export function Component() {
  return (
    <Alert color="warning" withBorderAccent>
      <span>
        <span className="font-medium">Info alert!</span> Change a few things up and try submitting again.
      </span>
    </Alert>
  );
}
```

## Additional content

Add additional content by using the `additionalContent` prop and add any type of content inside of it.

```tsx
// index.tsx

"use client";

import { Alert } from "flowbite-react";
import { HiEye, HiInformationCircle } from "react-icons/hi";

export function Component() {
  return (
    <Alert additionalContent={<ExampleAdditionalContent />} color="warning" icon={HiInformationCircle}>
      <span className="font-medium">Info alert!</span> Change a few things up and try submitting again.
    </Alert>
  );
}

function ExampleAdditionalContent() {
  return (
    <>
      <div className="mb-4 mt-2 text-sm text-cyan-700 dark:text-cyan-800">
        More info about this info alert goes here. This example text is going to run a bit longer so that you can see
        how spacing within an alert works with this kind of content.
      </div>
      <div className="flex">
        <button
          type="button"
          className="mr-2 inline-flex items-center rounded-lg bg-cyan-700 px-3 py-1.5 text-center text-xs font-medium text-white hover:bg-cyan-800 focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-800 dark:hover:bg-cyan-900"
        >
          <HiEye className="-ml-0.5 mr-2 h-4 w-4" />
          View more
        </button>
        <button
          type="button"
          className="rounded-lg border border-cyan-700 bg-transparent px-3 py-1.5 text-center text-xs font-medium text-cyan-700 hover:bg-cyan-800 hover:text-white focus:ring-4 focus:ring-cyan-300 dark:border-cyan-800 dark:text-cyan-800 dark:hover:text-white"
        >
          Dismiss
        </button>
      </div>
    </>
  );
}
```

## All options

This is an example with all of the available options and props for the alert component.

```tsx
// index.tsx

"use client";

import { Alert } from "flowbite-react";
import { HiEye, HiInformationCircle } from "react-icons/hi";

export function Component() {
  return (
    <Alert
      additionalContent={<ExampleAdditionalContent />}
      color="success"
      icon={HiInformationCircle}
      onDismiss={() => alert('Alert dismissed!')}
      rounded
    >
      <span className="font-medium">Info alert!</span> Change a few things up and try submitting again.
    </Alert>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "flex flex-col gap-2 p-4 text-sm",
  "borderAccent": "border-t-4",
  "closeButton": {
    "base": "-m-1.5 ml-auto inline-flex h-8 w-8 rounded-lg p-1.5 focus:ring-2",
    "icon": "h-5 w-5",
    "color": {
      "info": "bg-cyan-100 text-cyan-500 hover:bg-cyan-200 focus:ring-cyan-400 dark:bg-cyan-200 dark:text-cyan-600 dark:hover:bg-cyan-300",
      "gray": "bg-gray-100 text-gray-500 hover:bg-gray-200 focus:ring-gray-400 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-800 dark:hover:text-white",
      "failure": "bg-red-100 text-red-500 hover:bg-red-200 focus:ring-red-400 dark:bg-red-200 dark:text-red-600 dark:hover:bg-red-300",
      "success": "bg-green-100 text-green-500 hover:bg-green-200 focus:ring-green-400 dark:bg-green-200 dark:text-green-600 dark:hover:bg-green-300",
      "warning": "bg-yellow-100 text-yellow-500 hover:bg-yellow-200 focus:ring-yellow-400 dark:bg-yellow-200 dark:text-yellow-600 dark:hover:bg-yellow-300",
      "red": "bg-red-100 text-red-500 hover:bg-red-200 focus:ring-red-400 dark:bg-red-200 dark:text-red-600 dark:hover:bg-red-300",
      "green": "bg-green-100 text-green-500 hover:bg-green-200 focus:ring-green-400 dark:bg-green-200 dark:text-green-600 dark:hover:bg-green-300",
      "yellow": "bg-yellow-100 text-yellow-500 hover:bg-yellow-200 focus:ring-yellow-400 dark:bg-yellow-200 dark:text-yellow-600 dark:hover:bg-yellow-300",
      "blue": "bg-blue-100 text-blue-500 hover:bg-blue-200 focus:ring-blue-400 dark:bg-blue-200 dark:text-blue-600 dark:hover:bg-blue-300",
      "cyan": "bg-cyan-100 text-cyan-500 hover:bg-cyan-200 focus:ring-cyan-400 dark:bg-cyan-200 dark:text-cyan-600 dark:hover:bg-cyan-300",
      "pink": "bg-pink-100 text-pink-500 hover:bg-pink-200 focus:ring-pink-400 dark:bg-pink-200 dark:text-pink-600 dark:hover:bg-pink-300",
      "lime": "bg-lime-100 text-lime-500 hover:bg-lime-200 focus:ring-lime-400 dark:bg-lime-200 dark:text-lime-600 dark:hover:bg-lime-300",
      "dark": "bg-gray-100 text-gray-500 hover:bg-gray-200 focus:ring-gray-400 dark:bg-gray-200 dark:text-gray-600 dark:hover:bg-gray-300",
      "indigo": "bg-indigo-100 text-indigo-500 hover:bg-indigo-200 focus:ring-indigo-400 dark:bg-indigo-200 dark:text-indigo-600 dark:hover:bg-indigo-300",
      "purple": "bg-purple-100 text-purple-500 hover:bg-purple-200 focus:ring-purple-400 dark:bg-purple-200 dark:text-purple-600 dark:hover:bg-purple-300",
      "teal": "bg-teal-100 text-teal-500 hover:bg-teal-200 focus:ring-teal-400 dark:bg-teal-200 dark:text-teal-600 dark:hover:bg-teal-300",
      "light": "bg-gray-50 text-gray-500 hover:bg-gray-100 focus:ring-gray-200 dark:bg-gray-600 dark:text-gray-200 dark:hover:bg-gray-700 dark:hover:text-white"
    }
  },
  "color": {
    "info": "border-cyan-500 bg-cyan-100 text-cyan-700 dark:bg-cyan-200 dark:text-cyan-800",
    "gray": "border-gray-500 bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-gray-300",
    "failure": "border-red-500 bg-red-100 text-red-700 dark:bg-red-200 dark:text-red-800",
    "success": "border-green-500 bg-green-100 text-green-700 dark:bg-green-200 dark:text-green-800",
    "warning": "border-yellow-500 bg-yellow-100 text-yellow-700 dark:bg-yellow-200 dark:text-yellow-800",
    "red": "border-red-500 bg-red-100 text-red-700 dark:bg-red-200 dark:text-red-800",
    "green": "border-green-500 bg-green-100 text-green-700 dark:bg-green-200 dark:text-green-800",
    "yellow": "border-yellow-500 bg-yellow-100 text-yellow-700 dark:bg-yellow-200 dark:text-yellow-800",
    "blue": "border-blue-500 bg-blue-100 text-blue-700 dark:bg-blue-200 dark:text-blue-800",
    "cyan": "border-cyan-500 bg-cyan-100 text-cyan-700 dark:bg-cyan-200 dark:text-cyan-800",
    "pink": "border-pink-500 bg-pink-100 text-pink-700 dark:bg-pink-200 dark:text-pink-800",
    "lime": "border-lime-500 bg-lime-100 text-lime-700 dark:bg-lime-200 dark:text-lime-800",
    "dark": "border-gray-600 bg-gray-800 text-gray-200 dark:bg-gray-900 dark:text-gray-300",
    "indigo": "border-indigo-500 bg-indigo-100 text-indigo-700 dark:bg-indigo-200 dark:text-indigo-800",
    "purple": "border-purple-500 bg-purple-100 text-purple-700 dark:bg-purple-200 dark:text-purple-800",
    "teal": "border-teal-500 bg-teal-100 text-teal-700 dark:bg-teal-200 dark:text-teal-800",
    "light": "border-gray-400 bg-gray-50 text-gray-600 dark:bg-gray-500 dark:text-gray-200"
  },
  "icon": "mr-3 inline h-5 w-5 shrink-0",
  "rounded": "rounded-lg",
  "wrapper": "flex items-center"
}
```

## References

- [Flowbite Alerts](https://flowbite.com/docs/components/alerts/)


---

## Avatar

# React Avatar - Flowbite

> Use the avatar component to show user profile images and placeholders in different sizes, colors and shapes based on React and Tailwind CSS

The avatar component from Flowbite React can be used to show a visual representation of a user or team account for your application based on multiple examples, colors, sizes and shapes.

All of the example are built as React components and you can access custom props and methods to customize the component and you can also use Tailwind CSS classes to style the component.

To start using the avatar component you need to import it from the `flowbite-react` package:

```jsx
import { Avatar } from "flowbite-react";
```

## Default avatar

Here's a default example of the `<Avatar>` component where you can use the `img` prop to pass the image URL, the `alt` prop to pass a description of the image for accessibility and the `rounded` prop to make the avatar rounded.

```tsx
// index.tsx

import { Avatar } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Avatar img="/images/people/profile-picture-5.jpg" alt="avatar of Jese" rounded />
      <Avatar img="/images/people/profile-picture-5.jpg" />
    </div>
  );
}
```

## Avatar with border

Use the `bordered` prop to add a border style to the avatar.

```tsx
// index.tsx

import { Avatar } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Avatar img="/images/people/profile-picture-5.jpg" rounded bordered />
      <Avatar img="/images/people/profile-picture-5.jpg" bordered />
    </div>
  );
}
```

## Avatar placeholder

If the user doesn't have an image you can use the `placeholder` prop to show a placeholder image and you can still pass the `rounded` prop to make the avatar rounded and other options.

```tsx
// index.tsx

import { Avatar } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Avatar />
      <Avatar rounded />
    </div>
  );
}
```

## Placeholder initials

Alternatively to the placeholder image you can use the `placeholderInitials` prop to show the user initials.

```tsx
// index.tsx

import { Avatar } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Avatar placeholderInitials="RR" />
      <Avatar placeholderInitials="RR" rounded />
    </div>
  );
}
```

## Dot indicator

You can use the `status` prop to show a dot indicator on the avatar and you can use the `statusPosition` prop to change the position of the dot indicator.

This is useful to show the user status like online, offline, busy, away, and more.

```tsx
// index.tsx

import { Avatar } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Avatar img="/images/people/profile-picture-5.jpg" status="online" />
      <Avatar img="/images/people/profile-picture-5.jpg" rounded status="busy" statusPosition="top-right" />
      <Avatar img="/images/people/profile-picture-5.jpg" status="offline" statusPosition="bottom-left" />
      <Avatar img="/images/people/profile-picture-5.jpg" rounded status="away" statusPosition="bottom-right" />
    </div>
  );
}
```

## Stacked layout

Stack multiple avatars together by using the `<AvatarGroup>` component and by passing the `stacked` prop to the child components of the group.

The `<AvatarGroupCounter>` component can be used to show the total number of avatars in the group by passing the `total` prop and a link to the `href` prop to view all users.

```tsx
// index.tsx

import { Avatar, AvatarGroup, AvatarGroupCounter } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <AvatarGroup>
        <Avatar img="/images/people/profile-picture-1.jpg" rounded stacked />
        <Avatar img="/images/people/profile-picture-2.jpg" rounded stacked />
        <Avatar img="/images/people/profile-picture-3.jpg" rounded stacked />
        <Avatar img="/images/people/profile-picture-4.jpg" rounded stacked />
        <Avatar img="/images/people/profile-picture-5.jpg" rounded stacked />
      </AvatarGroup>
      <AvatarGroup>
        <Avatar img="/images/people/profile-picture-1.jpg" rounded stacked />
        <Avatar img="/images/people/profile-picture-2.jpg" rounded stacked />
        <Avatar img="/images/people/profile-picture-3.jpg" rounded stacked />
        <Avatar img="/images/people/profile-picture-4.jpg" rounded stacked />
        <Avatar.Counter total={99} href="#" />
      </AvatarGroup>
    </div>
  );
}
```

## Avatar with text

Use this example to show an avatar with text (ie. user name, email, etc) by passing the custom markup inside the `<Avatar>` component. This is useful for admin dashboard interfaces while the user is logged in.

```tsx
// index.tsx

import { Avatar } from "flowbite-react";

export function Component() {
  return (
    <Avatar img="/images/people/profile-picture-5.jpg" rounded>
      <div className="space-y-1 font-medium dark:text-white">
        <div>Jese Leos</div>
        <div className="text-sm text-gray-500 dark:text-gray-400">Joined in August 2014</div>
      </div>
    </Avatar>
  );
}
```

## Avatar dropdown

Use the `<Dropdown>` component to show a dropdown menu when clicking on the avatar component. This example is often used to show the user settings, account settings, and more.

```tsx
// index.tsx

import { Avatar, Dropdown, DropdownDivider, DropdownHeader, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <Dropdown
      label={<Avatar alt="User settings" img="/images/people/profile-picture-5.jpg" rounded />}
      arrowIcon={false}
      inline
    >
      <DropdownHeader>
        <span className="block text-sm">Bonnie Green</span>
        <span className="block truncate text-sm font-medium">name@flowbite.com</span>
      </DropdownHeader>
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownDivider />
      <DropdownItem>Sign out</DropdownItem>
    </Dropdown>
  );
}
```

## Colors

If you want to change the default color of the avatar component you can pass the `color` prop. Colors that you can choose from are gray, light, purple, success, pink, and more.

```tsx
// index.tsx

import { Avatar } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-col gap-3">
      <div className="flex flex-wrap gap-2">
        <Avatar img="/images/people/profile-picture-5.jpg" rounded bordered color="gray" />
        <Avatar img="/images/people/profile-picture-5.jpg" rounded bordered color="light" />
        <Avatar img="/images/people/profile-picture-5.jpg" rounded bordered color="purple" />
        <Avatar img="/images/people/profile-picture-5.jpg" rounded bordered color="success" />
        <Avatar img="/images/people/profile-picture-5.jpg" rounded bordered color="pink" />
      </div>
      <div className="flex flex-wrap gap-2">
        <Avatar img="/images/people/profile-picture-5.jpg" bordered color="gray" />
        <Avatar img="/images/people/profile-picture-5.jpg" bordered color="light" />
        <Avatar img="/images/people/profile-picture-5.jpg" bordered color="purple" />
        <Avatar img="/images/people/profile-picture-5.jpg" bordered color="success" />
        <Avatar img="/images/people/profile-picture-5.jpg" bordered color="pink" />
      </div>
    </div>
  );
}
```

## Sizes

Change the default size of the avatar component by passing the `size` prop. Sizes that you can choose from are xs, sm, md, lg, and xl.

```tsx
// index.tsx

import { Avatar } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <Avatar img="/images/people/profile-picture-5.jpg" size="xs" />
      <Avatar img="/images/people/profile-picture-5.jpg" size="sm" />
      <Avatar img="/images/people/profile-picture-5.jpg" size="md" />
      <Avatar img="/images/people/profile-picture-5.jpg" size="lg" />
      <Avatar img="/images/people/profile-picture-5.jpg" size="xl" />
    </div>
  );
}
```

## Override image element

You can override the default image element by passing the `img` prop to the `<Avatar>` component. This is useful if you want to use a different image element like `<Image>` from Next.js.

```tsx
// index.tsx

"use client";

import { Avatar } from "flowbite-react";
import Image from "next/image";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Avatar
        img={(props) => (
          <Image
            alt=""
            height="48"
            referrerPolicy="no-referrer"
            src="/images/people/profile-picture-5.jpg"
            width="48"
            {...props}
          />
        )}
      />
      <Avatar
        img={(props) => (
          <picture>
            <source media="(min-width: 900px)" srcSet="/images/people/profile-picture-3.jpg" />
            <source media="(min-width: 480px)" srcSet="/images/people/profile-picture-4.jpg" />
            <Image alt="" height="48" src="/images/people/profile-picture-5.jpg" width="48" {...props} />
          </picture>
        )}
      />
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "flex items-center justify-center space-x-4 rounded",
    "inner": "relative",
    "bordered": "p-1 ring-2",
    "rounded": "rounded-full",
    "color": {
      "dark": "ring-gray-800 dark:ring-gray-800",
      "failure": "ring-red-500 dark:ring-red-700",
      "gray": "ring-gray-500 dark:ring-gray-400",
      "info": "ring-cyan-400 dark:ring-cyan-800",
      "light": "ring-gray-300 dark:ring-gray-500",
      "purple": "ring-purple-500 dark:ring-purple-600",
      "success": "ring-green-500 dark:ring-green-500",
      "warning": "ring-yellow-300 dark:ring-yellow-500",
      "pink": "ring-pink-500 dark:ring-pink-500"
    },
    "img": {
      "base": "rounded",
      "off": "relative overflow-hidden bg-gray-100 dark:bg-gray-600",
      "on": "",
      "placeholder": "absolute -bottom-1 h-auto w-auto text-gray-400"
    },
    "size": {
      "xs": "h-6 w-6",
      "sm": "h-8 w-8",
      "md": "h-10 w-10",
      "lg": "h-20 w-20",
      "xl": "h-36 w-36"
    },
    "stacked": "ring-2 ring-gray-300 dark:ring-gray-500",
    "statusPosition": {
      "bottom-left": "-bottom-1 -left-1",
      "bottom-center": "-bottom-1",
      "bottom-right": "-bottom-1 -right-1",
      "top-left": "-left-1 -top-1",
      "top-center": "-top-1",
      "top-right": "-right-1 -top-1",
      "center-right": "-right-1",
      "center": "",
      "center-left": "-left-1"
    },
    "status": {
      "away": "bg-yellow-400",
      "base": "absolute h-3.5 w-3.5 rounded-full border-2 border-white dark:border-gray-800",
      "busy": "bg-red-400",
      "offline": "bg-gray-400",
      "online": "bg-green-400"
    },
    "initials": {
      "text": "font-medium text-gray-600 dark:text-gray-300",
      "base": "relative inline-flex items-center justify-center overflow-hidden bg-gray-100 dark:bg-gray-600"
    }
  },
  "group": {
    "base": "flex -space-x-4"
  },
  "groupCounter": {
    "base": "relative flex h-10 w-10 items-center justify-center rounded-full bg-gray-700 text-xs font-medium text-white ring-2 ring-gray-300 hover:bg-gray-600 dark:ring-gray-500"
  }
}
```

## References

- [Flowbite Avatar](https://flowbite.com/docs/components/avatar/)


---

## Badge

# React Badge - Flowbite

> Get started with the badge component to add labels or counters inside paragraphs, buttons, and inputs based on multiple colors and sizes from React and Tailwind CSS

The badge component can be used to show text, labels, and counters inside a small box or circle element which can be placed inside paragraphs, buttons, dropdowns, menu items, and more.

You can choose from multiple examples of badges based on the color, size, and icon and even use it as a link component by leveraging the properties from React and classes from Tailwind CSS.

To start using the badge component you need to import it from `flowbite-react`:

```jsx
import { Badge } from "flowbite-react";
```

## Default badges

Here's a list of default `<Badge>` component examples where you can use the `color` property to change the color of the badge based on contextual colors such as info, gray, success, and more.

```tsx
// index.tsx

import { Badge } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Badge color="info">Default</Badge>
      <Badge color="gray">Dark</Badge>
      <Badge color="failure">Failure</Badge>
      <Badge color="success">Success</Badge>
      <Badge color="warning">Warning</Badge>
      <Badge color="indigo">Indigo</Badge>
      <Badge color="purple">Purple</Badge>
      <Badge color="pink">Pink</Badge>
    </div>
  );
}
```

## Badge as link

Use the badge as a link component by wrapping it with an anchor element.

```tsx
// index.tsx

import { Badge } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <a href="#">
        <Badge>Default</Badge>
      </a>
      <a href="#">
        <Badge size="sm">Default</Badge>
      </a>
    </div>
  );
}
```

## Badge with icon

Add an icon to the badge by using the `icon` property and pass the icon component as a value. This can be used to show the status of a task or a notification often used for admin dashboards and user feeds.

```tsx
// index.tsx

"use client";

import { Badge } from "flowbite-react";
import { HiCheck, HiClock } from "react-icons/hi";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Badge icon={HiCheck}>2 minutes ago</Badge>
      <Badge color="gray" icon={HiClock}>
        3 days ago
      </Badge>
    </div>
  );
}
```

## Badge with icon only

An alternative style for the badge component is by only showing an icon without any text. You can do this by removing the children from the component and only using the `icon` property.

```tsx
// index.tsx

"use client";

import { Badge } from "flowbite-react";
import { HiCheck, HiClock } from "react-icons/hi";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Badge icon={HiCheck} />
      <Badge color="gray" icon={HiCheck} />
      <Badge size="sm" icon={HiCheck} />
      <Badge color="gray" size="sm" icon={HiCheck} />
    </div>
  );
}
```

## Sizes

Update the size of the badge component by using the `size` property and passing the size as a value.

You can choose from `xs` and `sm` sizes.

```tsx
// index.tsx

import { Badge } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Badge color="info" size="sm">
        Default
      </Badge>
      <Badge color="gray" size="sm">
        Dark
      </Badge>
      <Badge color="failure" size="sm">
        Failure
      </Badge>
      <Badge color="success" size="sm">
        Success
      </Badge>
      <Badge color="warning" size="sm">
        Warning
      </Badge>
      <Badge color="indigo" size="sm">
        Indigo
      </Badge>
      <Badge color="purple" size="sm">
        Purple
      </Badge>
      <Badge color="pink" size="sm">
        Pink
      </Badge>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "flex h-fit items-center gap-1 font-semibold",
    "color": {
      "info": "bg-cyan-100 text-cyan-800 hover:bg-cyan-200 dark:bg-cyan-200 dark:text-cyan-800 dark:hover:bg-cyan-300",
      "gray": "bg-gray-100 text-gray-800 hover:bg-gray-200 dark:bg-gray-700 dark:text-gray-300 dark:hover:bg-gray-600",
      "failure": "bg-red-100 text-red-800 hover:bg-red-200 dark:bg-red-200 dark:text-red-900 dark:hover:bg-red-300",
      "success": "bg-green-100 text-green-800 hover:bg-green-200 dark:bg-green-200 dark:text-green-900 dark:hover:bg-green-300",
      "warning": "bg-yellow-100 text-yellow-800 hover:bg-yellow-200 dark:bg-yellow-200 dark:text-yellow-900 dark:hover:bg-yellow-300",
      "indigo": "bg-indigo-100 text-indigo-800 hover:bg-indigo-200 dark:bg-indigo-200 dark:text-indigo-900 dark:hover:bg-indigo-300",
      "purple": "bg-purple-100 text-purple-800 hover:bg-purple-200 dark:bg-purple-200 dark:text-purple-900 dark:hover:bg-purple-300",
      "pink": "bg-pink-100 text-pink-800 hover:bg-pink-200 dark:bg-pink-200 dark:text-pink-900 dark:hover:bg-pink-300",
      "blue": "bg-blue-100 text-blue-800 hover:bg-blue-200 dark:bg-blue-200 dark:text-blue-900 dark:hover:bg-blue-300",
      "cyan": "bg-cyan-100 text-cyan-800 hover:bg-cyan-200 dark:bg-cyan-200 dark:text-cyan-900 dark:hover:bg-cyan-300",
      "dark": "bg-gray-600 text-gray-100 hover:bg-gray-500 dark:bg-gray-900 dark:text-gray-200 dark:hover:bg-gray-700",
      "light": "bg-gray-200 text-gray-800 hover:bg-gray-300 dark:bg-gray-400 dark:text-gray-900 dark:hover:bg-gray-500",
      "green": "bg-green-100 text-green-800 hover:bg-green-200 dark:bg-green-200 dark:text-green-900 dark:hover:bg-green-300",
      "lime": "bg-lime-100 text-lime-800 hover:bg-lime-200 dark:bg-lime-200 dark:text-lime-900 dark:hover:bg-lime-300",
      "red": "bg-red-100 text-red-800 hover:bg-red-200 dark:bg-red-200 dark:text-red-900 dark:hover:bg-red-300",
      "teal": "bg-teal-100 text-teal-800 hover:bg-teal-200 dark:bg-teal-200 dark:text-teal-900 dark:hover:bg-teal-300",
      "yellow": "bg-yellow-100 text-yellow-800 hover:bg-yellow-200 dark:bg-yellow-200 dark:text-yellow-900 dark:hover:bg-yellow-300"
    },
    "size": {
      "xs": "p-1 text-xs",
      "sm": "p-1.5 text-sm"
    }
  },
  "icon": {
    "off": "rounded px-2 py-0.5",
    "on": "rounded-full p-1.5",
    "size": {
      "xs": "h-3 w-3",
      "sm": "h-3.5 w-3.5"
    }
  }
}
```

## References

- [Flowbite Badge](https://flowbite.com/docs/components/badge/)


---

## Banner

# React Sticky Banner - Flowbite

> Use the banner component to show marketing messages and CTA buttons at the top or bottom side of your website based on the utility classes from Tailwind CSS

Get started with the sticky banner component coded with Tailwind CSS and Flowbite to show marketing, informational and CTA messages to your website visitors fixed to the top or bottom part of the page as the user scroll down the main content area.

Explore the following examples based on various styles, sizes, and positionings to leverage the sticky banner component and increase marketing conversions with a responsive element supporting dark mode.

To start using the banner component you need to import it from `flowbite-react`:

```jsx
import { Banner } from "flowbite-react";
```

## Default sticky banner

Use this free example to show a text message for announcement with a CTA link, an icon element and a close button to dismiss the banner.

```tsx
// index.tsx

import { Banner, BannerCollapseButton } from "flowbite-react";
import { HiX } from "react-icons/hi";
import { MdAnnouncement } from "react-icons/md";

export function Component() {
  return (
    <Banner>
      <div className="flex w-full justify-between border-b border-gray-200 bg-gray-50 p-4 dark:border-gray-600 dark:bg-gray-700">
        <div className="mx-auto flex items-center">
          <p className="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">
            <MdAnnouncement className="mr-4 h-4 w-4" />
            <span className="[&_p]:inline">
              New brand identity has been launched for the&nbsp;
              <a
                href="https://flowbite.com"
                className="inline font-medium text-cyan-600 underline decoration-solid underline-offset-2 hover:no-underline dark:text-cyan-500"
              >
                Flowbite Library
              </a>
            </span>
          </p>
        </div>
        <BannerCollapseButton color="gray" className="border-0 bg-transparent text-gray-500 dark:text-gray-400">
          <HiX className="h-4 w-4" />
        </BannerCollapseButton>
      </div>
    </Banner>
  );
}
```

## Bottom banner position

This example can be used to position the sticky banner to the bottom side of the page instead of the top side.

```tsx
// index.tsx

import { Banner, BannerCollapseButton } from "flowbite-react";
import { HiArrowRight, HiX } from "react-icons/hi";
import { MdPercent } from "react-icons/md";

export function Component() {
  return (
    <Banner>
      <div className="flex w-full justify-between border-t border-gray-200 bg-gray-50 p-4 dark:border-gray-600 dark:bg-gray-700">
        <div className="mx-auto flex items-center">
          <p className="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">
            <span className="mr-3 inline-flex h-6 w-6 items-center justify-center rounded-full bg-gray-200 p-1 dark:bg-gray-600">
              <MdPercent className="h-4 w-4" />
            </span>
            <span className="[&_p]:inline">
              Get 5% commision per sale&nbsp;
              <a
                href="https://flowbite.com"
                className="ml-0 flex items-center text-sm font-medium text-cyan-600 hover:underline md:ml-1 md:inline-flex dark:text-cyan-500"
              >
                Become a partner
                <HiArrowRight className="ml-2" />
              </a>
            </span>
          </p>
        </div>
        <BannerCollapseButton color="gray" className="border-0 bg-transparent text-gray-500 dark:text-gray-400">
          <HiX className="h-4 w-4" />
        </BannerCollapseButton>
      </div>
    </Banner>
  );
}
```

## Marketing CTA banner

Use this free example to show a text message for announcement with a CTA link, an icon element and a close button to dismiss the banner. Set a different width by using the `max-w-{*}` utility classes from Tailwind CSS.

```tsx
// index.tsx

import { Banner, BannerCollapseButton, Button } from "flowbite-react";
import { HiX } from "react-icons/hi";

export function Component() {
  return (
    <Banner>
      <div className="flex w-[calc(100%-2rem)] flex-col justify-between rounded-lg border border-gray-100 bg-white p-4 shadow-sm md:flex-row lg:max-w-7xl dark:border-gray-600 dark:bg-gray-700">
        <div className="mb-3 mr-4 flex flex-col items-start md:mb-0 md:flex-row md:items-center">
          <a
            href="https://flowbite.com/"
            className="mb-2 flex items-center border-gray-200 md:mb-0 md:mr-4 md:border-r md:pr-4 dark:border-gray-600"
          >
            <img src="https://flowbite.com/docs/images/logo.svg" className="mr-2 h-6" alt="Flowbite Logo" />
            <span className="self-center whitespace-nowrap text-lg font-semibold md:pr-6 dark:text-white">
              Flowbite
            </span>
          </a>
          <p className="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">
            Build websites even faster with components on top of Tailwind CSS
          </p>
        </div>
        <div className="flex shrink-0 items-center">
          <Button href="#">Sign up</Button>
          <BannerCollapseButton color="gray" className="border-0 bg-transparent text-gray-500 dark:text-gray-400">
            <HiX className="h-4 w-4" />
          </BannerCollapseButton>
        </div>
      </div>
    </Banner>
  );
}
```

## Newsletter sign-up banner

This example can be used to encourage your website visitors to sign up to your email newsletter by showing an inline form inside the sticky banner on the top side of your page.

```tsx
// index.tsx

import { Banner, BannerCollapseButton, Button, Label, TextInput } from "flowbite-react";
import { HiX } from "react-icons/hi";

export function Component() {
  return (
    <Banner>
      <div className="flex w-full items-center justify-between border-b border-gray-200 bg-gray-50 p-4 dark:border-gray-600 dark:bg-gray-700">
        <div className="mx-auto flex w-full shrink-0 items-center sm:w-auto">
          <form action="#" className="flex w-full flex-col items-center md:flex-row md:gap-x-3">
            <Label
              htmlFor="email"
              className="mb-2 mr-auto shrink-0 text-sm font-medium text-gray-500 md:m-0 md:mb-0 dark:text-gray-400"
            >
              Sign up for our newsletter
            </Label>
            <TextInput id="email" placeholder="Enter your email" required type="email" />
            <Button type="submit">Subscribe</Button>
          </form>
        </div>
        <BannerCollapseButton color="gray" className="border-0 bg-transparent text-gray-500 dark:text-gray-400">
          <HiX className="h-4 w-4" />
        </BannerCollapseButton>
      </div>
    </Banner>
  );
}
```

## Informational banner

This example can be used to share important information with your website visitors by showing a heading and a paragraph inside the sticky banner and two CTA buttons with links.

```tsx
// index.tsx

import { Banner, BannerCollapseButton } from "flowbite-react";
import { FaBookOpen } from "react-icons/fa";
import { HiArrowRight, HiX } from "react-icons/hi";

export function Component() {
  return (
    <Banner>
      <div className="flex w-full flex-col justify-between border-b border-gray-200 bg-gray-50 p-4 md:flex-row dark:border-gray-600 dark:bg-gray-700">
        <div className="mb-4 md:mb-0 md:mr-4">
          <h2 className="mb-1 text-base font-semibold text-gray-900 dark:text-white">Integration is the key</h2>
          <p className="flex items-center text-sm font-normal text-gray-500 dark:text-gray-400">
            You can integrate Flowbite with many tools to make your work even more efficient and lightning fast based on
            Tailwind CSS.
          </p>
        </div>
        <div className="flex shrink-0 items-center">
          <a
            href="#"
            className="mr-3 inline-flex items-center justify-center rounded-lg border border-gray-200 bg-white px-3 py-2 text-xs font-medium text-gray-900 hover:bg-gray-100 hover:text-cyan-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700"
          >
            <FaBookOpen className="mr-2 h-4 w-4" />
            Learn more
          </a>
          <a
            href="#"
            className="mr-2 inline-flex items-center justify-center rounded-lg bg-cyan-700 px-3 py-2 text-xs font-medium text-white hover:bg-cyan-800 focus:outline-none focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"
          >
            Get started
            <HiArrowRight className="ml-2 h-4 w-4" />
          </a>
          <BannerCollapseButton color="gray" className="border-0 bg-transparent text-gray-500 dark:text-gray-400">
            <HiX className="h-4 w-4" />
          </BannerCollapseButton>
        </div>
      </div>
    </Banner>
  );
}
```

## Theme

**This component is a work in progress, and currently doesn't have a theme.** It may in future updates.

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

## References

- [Flowbite Banner](https://flowbite.com/docs/components/banner/)


---

## Breadcrumb

# React Breadcrumb - Flowbite

> Get started with the breadcrumb component to show the current page location based on the URL structure using React and Tailwind CSS

The breadcrumb component can be used to indicate the current page's location within a navigational hierarchy and you can choose from multiple examples, colors, and sizes built with React and based on the utility classes from Tailwind CSS.

To start using the breadcrumb component you need to import it from `flowbite-react`:

```jsx
import { Breadcrumb } from "flowbite-react";
```

## Default breadcrumb

Use the `<Breadcrumb>` component and the child `<BreadcrumbItem>` components to create and indicate a series of page structure and URLs to help the user navigate through the website.

You can use the `href` prop from React to make the breadcrumb items clickable and the `icon` prop to add an icon to the breadcrumb item such as for the homepage.

```tsx
// index.tsx

"use client";

import { Breadcrumb, BreadcrumbItem } from "flowbite-react";
import { HiHome } from "react-icons/hi";

export function Component() {
  return (
    <Breadcrumb aria-label="Default breadcrumb example">
      <BreadcrumbItem href="#" icon={HiHome}>
        Home
      </BreadcrumbItem>
      <BreadcrumbItem href="#">Projects</BreadcrumbItem>
      <BreadcrumbItem>Flowbite React</BreadcrumbItem>
    </Breadcrumb>
  );
}
```

## Background color

You can add a solid background style to the breadcrumb component by adding the `bg-gray-50` class to the component from Tailwind CSS.

```tsx
// index.tsx

"use client";

import { Breadcrumb, BreadcrumbItem } from "flowbite-react";
import { HiHome } from "react-icons/hi";

export function Component() {
  return (
    <Breadcrumb aria-label="Solid background breadcrumb example" className="bg-gray-50 px-5 py-3 dark:bg-gray-800">
      <BreadcrumbItem href="#" icon={HiHome}>
        Home
      </BreadcrumbItem>
      <BreadcrumbItem href="#">Projects</BreadcrumbItem>
      <BreadcrumbItem>Flowbite React</BreadcrumbItem>
    </Breadcrumb>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "",
    "list": "flex items-center"
  },
  "item": {
    "base": "group flex items-center",
    "chevron": "mx-1 h-4 w-4 text-gray-400 group-first:hidden md:mx-2",
    "href": {
      "off": "flex items-center text-sm font-medium text-gray-500 dark:text-gray-400",
      "on": "flex items-center text-sm font-medium text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
    },
    "icon": "mr-2 h-4 w-4"
  }
}
```

## References

- [Flowbite Breadcrumbs](https://flowbite.com/docs/components/breadcrumb/)


---

## Button

# React Button - Flowbite

> Enable user interaction with the button component to perform actions on your website as links, for payment, form submission, social buttons and more based on React and Tailwind CSS

The button component is a common UI component found on the web that allows users to trigger certain actions on your website such as submitting a form, navigating to a new page, or downloading a file.

The examples from the Flowbite React library allows you to customise the buttons with different colors, sizes, icons, and more. All examples are built with React and Tailwind CSS.

In order to start using the button component you need to import it from Flowbite React:

```jsx
import { Button } from "flowbite-react";
```

## Default buttons

Use this example to create a default button by using the `<Button>` component from React and by adding the `color` property you can change the color of the button.

```tsx
// index.tsx

import { Button } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button>Default</Button>
      <Button color="alternative">Alternative</Button>
      <Button color="dark">Dark</Button>
      <Button color="light">Light</Button>
      <Button color="green">Green</Button>
      <Button color="red">Red</Button>
      <Button color="yellow">Yellow</Button>
      <Button color="purple">Purple</Button>
    </div>
  );
}
```

## Button pills

Add the `pill` property to the `<Button>` component to create a button with rounded corners.

```tsx
// index.tsx

import { Button } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button pill>Default</Button>
      <Button color="alternative" pill>
        Alternative
      </Button>
      <Button color="dark" pill>
        Dark
      </Button>
      <Button color="light" pill>
        Light
      </Button>
      <Button color="green" pill>
        Green
      </Button>
      <Button color="red" pill>
        Red
      </Button>
      <Button color="yellow" pill>
        Yellow
      </Button>
      <Button color="purple" pill>
        Purple
      </Button>
    </div>
  );
}
```

## Gradient monochrome

These beautifully colored buttons built with the gradient color utility classes from Tailwind CSS can be used as a creative alternative to the default button styles.

```tsx
// index.tsx

import { Button } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button className="bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 text-white hover:bg-gradient-to-br focus:ring-blue-300 dark:focus:ring-blue-800">
        Blue
      </Button>
      <Button className="bg-gradient-to-r from-green-400 via-green-500 to-green-600 text-white hover:bg-gradient-to-br focus:ring-green-300 dark:focus:ring-green-800">
        Green
      </Button>
      <Button className="bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 text-white hover:bg-gradient-to-br focus:ring-cyan-300 dark:focus:ring-cyan-800">
        Cyan
      </Button>
      <Button className="bg-gradient-to-r from-teal-400 via-teal-500 to-teal-600 text-white hover:bg-gradient-to-br focus:ring-teal-300 dark:focus:ring-teal-800">
        Teal
      </Button>
      <Button className="bg-gradient-to-r from-lime-200 via-lime-400 to-lime-500 text-gray-900 hover:bg-gradient-to-br focus:ring-lime-300 dark:focus:ring-lime-800">
        Lime
      </Button>
      <Button className="bg-gradient-to-r from-red-400 via-red-500 to-red-600 text-white hover:bg-gradient-to-br focus:ring-red-300 dark:focus:ring-red-800">
        Red
      </Button>
      <Button className="bg-gradient-to-r from-pink-400 via-pink-500 to-pink-600 text-white hover:bg-gradient-to-br focus:ring-pink-300 dark:focus:ring-pink-800">
        Pink
      </Button>
      <Button className="bg-gradient-to-r from-purple-500 via-purple-600 to-purple-700 text-white hover:bg-gradient-to-br focus:ring-purple-300 dark:focus:ring-purple-800">
        Purple
      </Button>
    </div>
  );
}
```

## Gradient duotone

These buttons use a style that includes two contrasted colors creating an impressive mesh gradient effect.

```tsx
// index.tsx

import { Button } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button className="bg-gradient-to-br from-purple-600 to-blue-500 text-white hover:bg-gradient-to-bl focus:ring-blue-300 dark:focus:ring-blue-800">
        Purple to Blue
      </Button>
      <Button className="bg-gradient-to-r from-cyan-500 to-blue-500 text-white hover:bg-gradient-to-bl focus:ring-cyan-300 dark:focus:ring-cyan-800">
        Cyan to Blue
      </Button>
      <Button className="bg-gradient-to-br from-green-400 to-blue-600 text-white hover:bg-gradient-to-bl focus:ring-green-200 dark:focus:ring-green-800">
        Green to Blue
      </Button>
      <Button className="bg-gradient-to-r from-purple-500 to-pink-500 text-white hover:bg-gradient-to-l focus:ring-purple-200 dark:focus:ring-purple-800">
        Purple to Pink
      </Button>
      <Button className="bg-gradient-to-br from-pink-500 to-orange-400 text-white hover:bg-gradient-to-bl focus:ring-pink-200 dark:focus:ring-pink-800">
        Pink to Orange
      </Button>
      <Button className="bg-gradient-to-r from-teal-200 to-lime-200 text-gray-900 hover:bg-gradient-to-l hover:from-teal-200 hover:to-lime-200 focus:ring-lime-200 dark:focus:ring-teal-700">
        Teal to Lime
      </Button>
      <Button className="bg-gradient-to-r from-red-200 via-red-300 to-yellow-200 text-gray-900 hover:bg-gradient-to-bl focus:ring-red-100 dark:focus:ring-red-400">
        Red to Yellow
      </Button>
    </div>
  );
}
```

## Outline buttons

Use the `outline` property to create an outline button with transparent background and colored border.

```tsx
// index.tsx

import { Button } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button outline>Default</Button>
      <Button color="dark" outline>
        Dark
      </Button>
      <Button color="green" outline>
        Green
      </Button>
      <Button color="red" outline>
        Red
      </Button>
      <Button color="yellow" outline>
        Yellow
      </Button>
      <Button color="purple" outline>
        Purple
      </Button>
    </div>
  );
}
```

## Button sizes

You can update the size of the button by adding the `size` property to the `<Button>` component.

Choose from `xs`, `sm`, `md`, `lg`, and `xl` as the value.

```tsx
// index.tsx

import { Button } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap items-start gap-2">
      <Button size="xs">Extra small</Button>
      <Button size="sm">Small</Button>
      <Button size="md">Base</Button>
      <Button size="lg">Large</Button>
      <Button size="xl">Extra large</Button>
    </div>
  );
}
```

## Buttons with icon

You can add icons to the buttons by adding it inside the `<Button>` component near the text.

```tsx
// index.tsx

import { Button } from "flowbite-react";
import { HiOutlineArrowRight, HiShoppingCart } from "react-icons/hi";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button>
        <HiShoppingCart className="mr-2 h-5 w-5" />
        Buy now
      </Button>
      <Button>
        Choose plan
        <HiOutlineArrowRight className="ml-2 h-5 w-5" />
      </Button>
    </div>
  );
}
```

## Button with label

This example can be used to show a notification count or helper text inside a button using the [Badge](https://flowbite-react.com/docs/components/badge.md) component.

```tsx
// index.tsx

import { Badge, Button } from "flowbite-react";

export function Component() {
  return (
    <Button>
      Messages
      <Badge className="ms-2 rounded-full px-1.5">2</Badge>
    </Button>
  );
}
```

## Button with only icons

Create a button with only icons by adding the `iconOnly` property to the `<Button>` component. These are useful when you want to show buttons in a small space and for things like pagination.

```tsx
// index.tsx

import { Button } from "flowbite-react";
import { HiOutlineArrowRight } from "react-icons/hi";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button>
        <HiOutlineArrowRight className="h-6 w-6" />
      </Button>
      <Button pill>
        <HiOutlineArrowRight className="h-6 w-6" />
      </Button>
      <Button outline>
        <HiOutlineArrowRight className="h-6 w-6" />
      </Button>
      <Button outline pill>
        <HiOutlineArrowRight className="h-6 w-6" />
      </Button>
    </div>
  );
}
```

## Button with loading state

Use the following [Spinner](https://flowbite-react.com/docs/components/spinner.md) component to indicate a loader animation inside buttons:

```tsx
// index.tsx

import { Button, Spinner } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap items-start gap-2">
      <Button>
        <Spinner size="sm" aria-label="Info spinner example" className="me-3" light />
        Loading...
      </Button>
      <Button color="alternative">
        <Spinner size="sm" aria-label="Info spinner example" className="me-3" light />
        Loading...
      </Button>
    </div>
  );
}
```

## Disabled buttons

You can disable the button by adding the `disabled` property to the `<Button>` component.

```tsx
// index.tsx

import { Button } from "flowbite-react";

export function Component() {
  return <Button disabled>Disabled button</Button>;
}
```

## Override Button base component

The `as` prop provides you the ability to transform the `<Button />` component into another component or HTML element. This prop accepts a string representing an HTML tag or a functional React component.

```tsx
// index.tsx

import { Button } from "flowbite-react";
import Link from "next/link";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Button as="span" className="cursor-pointer">
        Span Button
      </Button>
      <Button as={Link} href="#">
        Next Link Button
      </Button>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "relative flex items-center justify-center rounded-lg text-center font-medium focus:outline-none focus:ring-4",
  "disabled": "pointer-events-none opacity-50",
  "fullSized": "w-full",
  "grouped": "rounded-none border-l-0 first:rounded-s-lg first:border-l last:rounded-e-lg focus:ring-2",
  "pill": "rounded-full",
  "size": {
    "xs": "h-8 px-3 text-xs",
    "sm": "h-9 px-3 text-sm",
    "md": "h-10 px-5 text-sm",
    "lg": "h-12 px-5 text-base",
    "xl": "h-[52px] px-6 text-base"
  },
  "color": {
    "default": "bg-primary-700 text-white hover:bg-primary-800 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800",
    "alternative": "border border-gray-200 bg-white text-gray-900 hover:bg-gray-100 hover:text-primary-700 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700",
    "blue": "bg-blue-700 text-white hover:bg-blue-800 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
    "cyan": "bg-cyan-700 text-white hover:bg-cyan-800 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800",
    "dark": "bg-gray-800 text-white hover:bg-gray-900 focus:ring-gray-300 dark:bg-gray-800 dark:hover:bg-gray-700 dark:focus:ring-gray-700",
    "gray": "bg-gray-700 text-white hover:bg-gray-800 focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800",
    "green": "bg-green-700 text-white hover:bg-green-800 focus:ring-green-300 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800",
    "indigo": "bg-indigo-700 text-white hover:bg-indigo-800 focus:ring-indigo-300 dark:bg-indigo-600 dark:hover:bg-indigo-700 dark:focus:ring-indigo-800",
    "light": "border border-gray-300 bg-white text-gray-900 hover:bg-gray-100 focus:ring-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-white dark:hover:border-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-700",
    "lime": "bg-lime-700 text-white hover:bg-lime-800 focus:ring-lime-300 dark:bg-lime-600 dark:hover:bg-lime-700 dark:focus:ring-lime-800",
    "pink": "bg-pink-700 text-white hover:bg-pink-800 focus:ring-pink-300 dark:bg-pink-600 dark:hover:bg-pink-700 dark:focus:ring-pink-800",
    "purple": "bg-purple-700 text-white hover:bg-purple-800 focus:ring-purple-300 dark:bg-purple-600 dark:hover:bg-purple-700 dark:focus:ring-purple-800",
    "red": "bg-red-700 text-white hover:bg-red-800 focus:ring-red-300 dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800",
    "teal": "bg-teal-700 text-white hover:bg-teal-800 focus:ring-teal-300 dark:bg-teal-600 dark:hover:bg-teal-700 dark:focus:ring-teal-800",
    "yellow": "bg-yellow-400 text-white hover:bg-yellow-500 focus:ring-yellow-300 dark:bg-yellow-600 dark:hover:bg-yellow-400 dark:focus:ring-yellow-900"
  },
  "outlineColor": {
    "default": "border border-primary-700 text-primary-700 hover:border-primary-800 hover:bg-primary-800 hover:text-white focus:ring-primary-300 dark:border-primary-600 dark:text-primary-500 dark:hover:border-primary-700 dark:hover:bg-primary-700 dark:hover:text-white dark:focus:ring-primary-800",
    "blue": "border border-blue-700 text-blue-700 hover:border-blue-800 hover:bg-blue-800 hover:text-white focus:ring-blue-300 dark:border-blue-500 dark:text-blue-500 dark:hover:border-blue-700 dark:hover:bg-blue-700 dark:hover:text-white dark:focus:ring-blue-800",
    "cyan": "border border-cyan-700 text-cyan-700 hover:border-cyan-800 hover:bg-cyan-800 hover:text-white focus:ring-cyan-300 dark:border-cyan-500 dark:text-cyan-500 dark:hover:border-cyan-700 dark:hover:bg-cyan-700 dark:hover:text-white dark:focus:ring-cyan-800",
    "dark": "border border-gray-800 text-gray-800 hover:border-gray-900 hover:bg-gray-900 hover:text-white focus:ring-gray-300 dark:border-gray-600 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-800",
    "gray": "border border-gray-700 text-gray-700 hover:border-gray-800 hover:bg-gray-800 hover:text-white focus:ring-gray-300 dark:border-gray-600 dark:text-gray-400 dark:hover:border-gray-700 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-800",
    "green": "border border-green-700 text-green-700 hover:border-green-800 hover:bg-green-800 hover:text-white focus:ring-green-300 dark:border-green-600 dark:text-green-500 dark:hover:border-green-700 dark:hover:bg-green-700 dark:hover:text-white dark:focus:ring-green-800",
    "indigo": "border border-indigo-700 text-indigo-700 hover:border-indigo-800 hover:bg-indigo-800 hover:text-white focus:ring-indigo-300 dark:border-indigo-600 dark:text-indigo-400 dark:hover:border-indigo-700 dark:hover:bg-indigo-700 dark:hover:text-white dark:focus:ring-indigo-800",
    "lime": "border border-lime-700 text-lime-700 hover:border-lime-800 hover:bg-lime-800 hover:text-white focus:ring-lime-300 dark:border-lime-600 dark:text-lime-500 dark:hover:border-lime-700 dark:hover:bg-lime-700 dark:hover:text-white dark:focus:ring-lime-800",
    "pink": "border border-pink-700 text-pink-700 hover:border-pink-800 hover:bg-pink-800 hover:text-white focus:ring-pink-300 dark:border-pink-600 dark:text-pink-500 dark:hover:border-pink-700 dark:hover:bg-pink-700 dark:hover:text-white dark:focus:ring-pink-800",
    "purple": "border border-purple-700 text-purple-700 hover:border-purple-800 hover:bg-purple-800 hover:text-white focus:ring-purple-300 dark:border-purple-600 dark:text-purple-400 dark:hover:border-purple-700 dark:hover:bg-purple-700 dark:hover:text-white dark:focus:ring-purple-800",
    "red": "border border-red-700 text-red-700 hover:border-red-800 hover:bg-red-800 hover:text-white focus:ring-red-300 dark:border-red-600 dark:text-red-500 dark:hover:border-red-700 dark:hover:bg-red-700 dark:hover:text-white dark:focus:ring-red-800",
    "teal": "border border-teal-700 text-teal-700 hover:border-teal-800 hover:bg-teal-800 hover:text-white focus:ring-teal-300 dark:border-teal-600 dark:text-teal-400 dark:hover:border-teal-700 dark:hover:bg-teal-700 dark:hover:text-white dark:focus:ring-teal-800",
    "yellow": "border border-yellow-400 text-yellow-400 hover:border-yellow-500 hover:bg-yellow-500 hover:text-white focus:ring-yellow-300 dark:border-yellow-300 dark:text-yellow-300 dark:hover:border-yellow-400 dark:hover:bg-yellow-400 dark:hover:text-white dark:focus:ring-yellow-900"
  }
}
```

## References

- [Flowbite Buttons](https://flowbite.com/docs/components/buttons/)


---

## Button group

# React Button Group - Flowbite

> Button groups allow you to stack together multiple buttons in a single line horizontally based on multiple styles and sizes using React and Tailwind CSS

The button group component from Flowbite React can be used to stack multiple button elements and group them visually together. It can often be used to create a navigation menu or a toolbar.

Choose from multiple examples and you can update properties such as the color, size, and appearance using the props from React and utility classes from Tailwind CSS.

To start using the component you need to import it from the Flowbite React library:

```jsx
import { Button } from "flowbite-react";
```

## Default button group

Use this example of the `<ButtonGroup>` component by adding the `Button` component as a child element and stack them together. You can also use the `color` prop to change the color of the buttons.

```tsx
// index.tsx

import { Button, ButtonGroup } from "flowbite-react";

export function Component() {
  return (
    <ButtonGroup>
      <Button color="alternative">Profile</Button>
      <Button color="alternative">Settings</Button>
      <Button color="alternative">Messages</Button>
    </ButtonGroup>
  );
}
```

## Button group with icons

Import one of the icons from the `react-icons` library and add it as a child element to the `<Button>` component to create multiple buttons with icons grouped together.

```tsx
// index.tsx

import { Button, ButtonGroup } from "flowbite-react";
import { HiAdjustments, HiCloudDownload, HiUserCircle } from "react-icons/hi";

export function Component() {
  return (
    <ButtonGroup>
      <Button color="alternative">
        <HiUserCircle className="me-2 h-4 w-4" />
        Profile
      </Button>
      <Button color="alternative">
        <HiAdjustments className="me-2 h-4 w-4" />
        Settings
      </Button>
      <Button color="alternative">
        <HiCloudDownload className="me-2 h-4 w-4" />
        Messages
      </Button>
    </ButtonGroup>
  );
}
```

## Outline button group

By passing the outline prop to the `<ButtonGroup>` component you can create a button group with outline buttons with no background and solid borders.

```tsx
// index.tsx

import { Button, ButtonGroup } from "flowbite-react";

export function Component() {
  return (
    <ButtonGroup outline>
      <Button>Profile</Button>
      <Button>Settings</Button>
      <Button>Messages</Button>
    </ButtonGroup>
  );
}
```

## Outline button group with icons

Here's an example on how you can use both the outline and icon props together.

```tsx
// index.tsx

import { Button, ButtonGroup } from "flowbite-react";
import { HiAdjustments, HiCloudDownload, HiUserCircle } from "react-icons/hi";

export function Component() {
  return (
    <ButtonGroup outline>
      <Button>
        <HiUserCircle className="me-2 h-4 w-4" />
        Profile
      </Button>
      <Button>
        <HiAdjustments className="me-2 h-4 w-4" />
        Settings
      </Button>
      <Button>
        <HiCloudDownload className="me-3 h-4 w-4" />
        Messages
      </Button>
    </ButtonGroup>
  );
}
```

## Color options

Use the `color` prop to change the color of the buttons.

```tsx
// index.tsx

import { Button, ButtonGroup } from "flowbite-react";

export function Component() {
  return (
    <ButtonGroup>
      <Button color="cyan">Profile</Button>
      <Button color="cyan">Settings</Button>
      <Button color="cyan">Messages</Button>
    </ButtonGroup>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "inline-flex rounded-md shadow-sm"
}
```

## References

- [Flowbite Button Group](https://flowbite.com/docs/components/button-group/)


---

## Card

# React Card - Flowbite

> Get started with the card component to show content in a box such as titles, descriptions, and images based on multiple styles and sizes built with React

The card component can be used to show a wide variety of content such as previews of blog posts, user profiles, pricing plans, and more. Choose from one of the many examples built with React and the utility classes from Tailwind CSS.

To start using the card component you will need to import it from `flowbite-react`:

```jsx
import { Card } from "flowbite-react";
```

## Default card

Use this example to show a simple card component with a title and description and apply the `href` tag to the `<Card>` component to set a hyperlink to the card.

```tsx
// index.tsx

import { Card } from "flowbite-react";

export function Component() {
  return (
    <Card href="#" className="max-w-sm">
      <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
        Noteworthy technology acquisitions 2021
      </h5>
      <p className="font-normal text-gray-700 dark:text-gray-400">
        Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
      </p>
    </Card>
  );
}
```

## Card with CTA button

By also importing the `<Button>` component you can add it inside the card to show a call to action button.

```tsx
// index.tsx

import { Button, Card } from "flowbite-react";

export function Component() {
  return (
    <Card className="max-w-sm">
      <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
        Noteworthy technology acquisitions 2021
      </h5>
      <p className="font-normal text-gray-700 dark:text-gray-400">
        Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
      </p>
      <Button>
        Read more
        <svg className="-mr-1 ml-2 h-4 w-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <path
            fillRule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clipRule="evenodd"
          />
        </svg>
      </Button>
    </Card>
  );
}
```

## Card with image

Add an image to the card by using the `imgSrc` prop and set the `imgAlt` prop to add an alt text to the image.

```tsx
// index.tsx

import { Card } from "flowbite-react";

export function Component() {
  return (
    <Card
      className="max-w-sm"
      imgAlt="Meaningful alt text for an image that is not purely decorative"
      imgSrc="/images/blog/image-1.jpg"
    >
      <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
        Noteworthy technology acquisitions 2021
      </h5>
      <p className="font-normal text-gray-700 dark:text-gray-400">
        Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
      </p>
    </Card>
  );
}
```

## Card with custom image render function

Specify your own render function for the image component for the card by using the `renderImage` prop. This is especially useful when
using the component with NextJS or Gatsby.

```tsx
// index.tsx

"use client";

import { Card } from "flowbite-react";
import Image from "next/image";

export function Component() {
  return (
    <Card
      className="max-w-sm"
      renderImage={() => <Image width={500} height={500} src="/images/blog/image-1.jpg" alt="image 1" />}
    >
      <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
        Noteworthy technology acquisitions 2021
      </h5>
      <p className="font-normal text-gray-700 dark:text-gray-400">
        Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
      </p>
    </Card>
  );
}
```

## Horizontal card

Use the `horizontal` prop to show the card in a horizontal layout.

```tsx
// index.tsx

import { Card } from "flowbite-react";

export function Component() {
  return (
    <Card className="max-w-sm" imgSrc="/images/blog/image-4.jpg" horizontal>
      <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
        Noteworthy technology acquisitions 2021
      </h5>
      <p className="font-normal text-gray-700 dark:text-gray-400">
        Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
      </p>
    </Card>
  );
}
```

## User profile card

Use this example to show a user card with a profile picture, name, job title, buttons and a dropdown menu.

```tsx
// index.tsx

import { Card, Dropdown, DropdownItem } from "flowbite-react";
import Image from "next/image";

export function Component() {
  return (
    <Card className="max-w-sm">
      <div className="flex justify-end px-4 pt-4">
        <Dropdown inline label="">
          <DropdownItem>
            <a
              href="#"
              className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white"
            >
              Edit
            </a>
          </DropdownItem>
          <DropdownItem>
            <a
              href="#"
              className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white"
            >
              Export Data
            </a>
          </DropdownItem>
          <DropdownItem>
            <a
              href="#"
              className="block px-4 py-2 text-sm text-red-600 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white"
            >
              Delete
            </a>
          </DropdownItem>
        </Dropdown>
      </div>
      <div className="flex flex-col items-center pb-10">
        <Image
          alt="Bonnie image"
          height="96"
          src="/images/people/profile-picture-3.jpg"
          width="96"
          className="mb-3 rounded-full shadow-lg"
        />
        <h5 className="mb-1 text-xl font-medium text-gray-900 dark:text-white">Bonnie Green</h5>
        <span className="text-sm text-gray-500 dark:text-gray-400">Visual Designer</span>
        <div className="mt-4 flex space-x-3 lg:mt-6">
          <a
            href="#"
            className="inline-flex items-center rounded-lg bg-cyan-700 px-4 py-2 text-center text-sm font-medium text-white hover:bg-cyan-800 focus:outline-none focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"
          >
            Add friend
          </a>
          <a
            href="#"
            className="inline-flex items-center rounded-lg border border-gray-300 bg-white px-4 py-2 text-center text-sm font-medium text-gray-900 hover:bg-gray-100 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:border-gray-600 dark:bg-gray-800 dark:text-white dark:hover:border-gray-700 dark:hover:bg-gray-700 dark:focus:ring-gray-700"
          >
            Message
          </a>
        </div>
      </div>
    </Card>
  );
}
```

## Card with form

You can also add form elements inside of the card component such as for sign up or login forms.

```tsx
// index.tsx

import { Button, Card, Checkbox, Label, TextInput } from "flowbite-react";

export function Component() {
  return (
    <Card className="max-w-sm">
      <form className="flex flex-col gap-4">
        <div>
          <div className="mb-2 block">
            <Label htmlFor="email1">Your email</Label>
          </div>
          <TextInput id="email1" type="email" placeholder="name@flowbite.com" required />
        </div>
        <div>
          <div className="mb-2 block">
            <Label htmlFor="password1">Your password</Label>
          </div>
          <TextInput id="password1" type="password" required />
        </div>
        <div className="flex items-center gap-2">
          <Checkbox id="remember" />
          <Label htmlFor="remember">Remember me</Label>
        </div>
        <Button type="submit">Submit</Button>
      </form>
    </Card>
  );
}
```

## E-commerce card

Use this example to show a product card with an image (product preview), title, price, rating stars and buttons built for E-commerce websites.

```tsx
// index.tsx

import { Card } from "flowbite-react";

export function Component() {
  return (
    <Card
      className="max-w-sm"
      imgAlt="Apple Watch Series 7 in colors pink, silver, and black"
      imgSrc="/images/products/apple-watch.png"
    >
      <a href="#">
        <h5 className="text-xl font-semibold tracking-tight text-gray-900 dark:text-white">
          Apple Watch Series 7 GPS, Aluminium Case, Starlight Sport
        </h5>
      </a>
      <div className="mb-5 mt-2.5 flex items-center">
        <svg
          className="h-5 w-5 text-yellow-300"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
        <svg
          className="h-5 w-5 text-yellow-300"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
        <svg
          className="h-5 w-5 text-yellow-300"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
        <svg
          className="h-5 w-5 text-yellow-300"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
        <svg
          className="h-5 w-5 text-yellow-300"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
        </svg>
        <span className="ml-3 mr-2 rounded bg-cyan-100 px-2.5 py-0.5 text-xs font-semibold text-cyan-800 dark:bg-cyan-200 dark:text-cyan-800">
          5.0
        </span>
      </div>
      <div className="flex items-center justify-between">
        <span className="text-3xl font-bold text-gray-900 dark:text-white">$599</span>
        <a
          href="#"
          className="rounded-lg bg-cyan-700 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-cyan-800 focus:outline-none focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"
        >
          Add to cart
        </a>
      </div>
    </Card>
  );
}
```

## CTA card

Use this component to display a call to action card for mobile applications where you feature download buttons for App Store and Google Play.

```tsx
// index.tsx

import { Card } from "flowbite-react";

export function Component() {
  return (
    <Card className="max-w-sm">
      <h5 className="mb-2 text-3xl font-bold text-gray-900 dark:text-white">Work fast from anywhere</h5>
      <p className="mb-5 text-base text-gray-500 sm:text-lg dark:text-gray-400">
        Stay up to date and move work forward with Flowbite on iOS & Android. Download the app today.
      </p>
      <div className="items-center justify-center space-y-4 sm:flex sm:space-x-4 sm:space-y-0">
        <a
          href="#"
          className="inline-flex w-full items-center justify-center rounded-lg bg-gray-800 px-4 py-2.5 text-white hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-300 sm:w-auto dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700"
        >
          <svg
            className="mr-3 h-7 w-7"
            aria-hidden="true"
            focusable="false"
            data-prefix="fab"
            data-icon="apple"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 384 512"
          >
            <path
              fill="currentColor"
              d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-65.2-30.7-61.7-90-61.7-91.9zm-56.6-164.2c27.3-32.4 24.8-61.9 24-72.5-24.1 1.4-52 16.4-67.9 34.9-17.5 19.8-27.8 44.3-25.6 71.9 26.1 2 49.9-11.4 69.5-34.3z"
            />
          </svg>
          <div className="text-left">
            <div className="mb-1 text-xs">Download on the</div>
            <div className="-mt-1 font-sans text-sm font-semibold">Mac App Store</div>
          </div>
        </a>
        <a
          href="#"
          className="inline-flex w-full items-center justify-center rounded-lg bg-gray-800 px-4 py-2.5 text-white hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-300 sm:w-auto dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700"
        >
          <svg
            className="mr-3 h-7 w-7"
            aria-hidden="true"
            focusable="false"
            data-prefix="fab"
            data-icon="google-play"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              fill="currentColor"
              d="M325.3 234.3L104.6 13l280.8 161.2-60.1 60.1zM47 0C34 6.8 25.3 19.2 25.3 35.3v441.3c0 16.1 8.7 28.5 21.7 35.3l256.6-256L47 0zm425.2 225.6l-58.9-34.1-65.7 64.5 65.7 64.5 60.1-34.1c18-14.3 18-46.5-1.2-60.8zM104.6 499l280.8-161.2-60.1-60.1L104.6 499z"
            />
          </svg>
          <div className="text-left">
            <div className="mb-1 text-xs">Get in on</div>
            <div className="-mt-1 font-sans text-sm font-semibold">Google Play</div>
          </div>
        </a>
      </div>
    </Card>
  );
}
```

## Card with list

Use this component to display a card with a list of items such as your latest customers or latest orders that include an image, descriptive text and a link to view more.

```tsx
// index.tsx

import { Card } from "flowbite-react";
import Image from "next/image";

export function Component() {
  return (
    <Card className="max-w-sm">
      <div className="mb-4 flex items-center justify-between">
        <h5 className="text-xl font-bold leading-none text-gray-900 dark:text-white">Latest Customers</h5>
        <a href="#" className="text-sm font-medium text-cyan-600 hover:underline dark:text-cyan-500">
          View all
        </a>
      </div>
      <div className="flow-root">
        <ul className="divide-y divide-gray-200 dark:divide-gray-700">
          <li className="py-3 sm:py-4">
            <div className="flex items-center space-x-4">
              <div className="shrink-0">
                <Image
                  alt="Neil image"
                  height="32"
                  src="/images/people/profile-picture-1.jpg"
                  width="32"
                  className="rounded-full"
                />
              </div>
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Neil Sims</p>
                <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@windster.com</p>
              </div>
              <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">$320</div>
            </div>
          </li>
          <li className="py-3 sm:py-4">
            <div className="flex items-center space-x-4">
              <div className="shrink-0">
                <Image
                  alt="Bonnie image"
                  height="32"
                  src="/images/people/profile-picture-3.jpg"
                  width="32"
                  className="rounded-full"
                />
              </div>
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Bonnie Green</p>
                <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@windster.com</p>
              </div>
              <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                $3467
              </div>
            </div>
          </li>
          <li className="py-3 sm:py-4">
            <div className="flex items-center space-x-4">
              <div className="shrink-0">
                <Image
                  alt="Michael image"
                  height="32"
                  src="/images/people/profile-picture-2.jpg"
                  width="32"
                  className="rounded-full"
                />
              </div>
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Michael Gough</p>
                <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@windster.com</p>
              </div>
              <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">$67</div>
            </div>
          </li>
          <li className="py-3 sm:py-4">
            <div className="flex items-center space-x-4">
              <div className="shrink-0">
                <Image
                  alt="Lana image"
                  height="32"
                  src="/images/people/profile-picture-4.jpg"
                  width="32"
                  className="rounded-full"
                />
              </div>
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Lana Byrd</p>
                <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@windster.com</p>
              </div>
              <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">$367</div>
            </div>
          </li>
          <li className="pb-0 pt-3 sm:pt-4">
            <div className="flex items-center space-x-4">
              <div className="shrink-0">
                <Image
                  alt="Thomas image"
                  height="32"
                  src="/images/people/profile-picture-5.jpg"
                  width="32"
                  className="rounded-full"
                />
              </div>
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Thomes Lean</p>
                <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@windster.com</p>
              </div>
              <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">
                $2367
              </div>
            </div>
          </li>
        </ul>
      </div>
    </Card>
  );
}
```

## Pricing card

Use the pricing card component to show the pricing of your product or service.

```tsx
// index.tsx

import { Card } from "flowbite-react";

export function Component() {
  return (
    <Card className="max-w-sm">
      <h5 className="mb-4 text-xl font-medium text-gray-500 dark:text-gray-400">Standard plan</h5>
      <div className="flex items-baseline text-gray-900 dark:text-white">
        <span className="text-3xl font-semibold">$</span>
        <span className="text-5xl font-extrabold tracking-tight">49</span>
        <span className="ml-1 text-xl font-normal text-gray-500 dark:text-gray-400">/month</span>
      </div>
      <ul className="my-7 space-y-5">
        <li className="flex space-x-3">
          <svg
            className="h-5 w-5 shrink-0 text-cyan-600 dark:text-cyan-500"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
          <span className="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">2 team members</span>
        </li>
        <li className="flex space-x-3">
          <svg
            className="h-5 w-5 shrink-0 text-cyan-600 dark:text-cyan-500"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
          <span className="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">
            20GB Cloud storage
          </span>
        </li>
        <li className="flex space-x-3">
          <svg
            className="h-5 w-5 shrink-0 text-cyan-600 dark:text-cyan-500"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
          <span className="text-base font-normal leading-tight text-gray-500 dark:text-gray-400">Integration help</span>
        </li>
        <li className="flex space-x-3 line-through decoration-gray-500">
          <svg
            className="h-5 w-5 shrink-0 text-gray-400 dark:text-gray-500"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
          <span className="text-base font-normal leading-tight text-gray-500">Sketch Files</span>
        </li>
        <li className="flex space-x-3 line-through decoration-gray-500">
          <svg
            className="h-5 w-5 shrink-0 text-gray-400 dark:text-gray-500"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
          <span className="text-base font-normal leading-tight text-gray-500">API Access</span>
        </li>
        <li className="flex space-x-3 line-through decoration-gray-500">
          <svg
            className="h-5 w-5 shrink-0 text-gray-400 dark:text-gray-500"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
          <span className="text-base font-normal leading-tight text-gray-500">Complete documentation</span>
        </li>
        <li className="flex space-x-3 line-through decoration-gray-500">
          <svg
            className="h-5 w-5 shrink-0 text-gray-400 dark:text-gray-500"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
          <span className="text-base font-normal leading-tight text-gray-500">24×7 phone & email support</span>
        </li>
      </ul>
      <button
        type="button"
        className="inline-flex w-full justify-center rounded-lg bg-cyan-600 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-cyan-700 focus:outline-none focus:ring-4 focus:ring-cyan-200 dark:focus:ring-cyan-900"
      >
        Choose plan
      </button>
    </Card>
  );
}
```

## Crypto card (web3)

This component can be used for crypto and web3 related projects where you can choose which wallet you want to connect with (ie. Metamask, Coinbase).

```tsx
// index.tsx

import { Card } from "flowbite-react";

export function Component() {
  return (
    <Card className="max-w-sm">
      <h5 className="mb-3 text-base font-semibold text-gray-900 lg:text-xl dark:text-white">Connect wallet</h5>
      <p className="text-sm font-normal text-gray-500 dark:text-gray-400">
        Connect with one of our available wallet providers or create a new one.
      </p>
      <ul className="my-4 space-y-3">
        <li>
          <a
            href="#"
            className="group flex items-center rounded-lg bg-gray-50 p-3 text-base font-bold text-gray-900 hover:bg-gray-100 hover:shadow dark:bg-gray-600 dark:text-white dark:hover:bg-gray-500"
          >
            <svg className="h-4" viewBox="0 0 40 38" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M39.0728 0L21.9092 12.6999L25.1009 5.21543L39.0728 0Z" fill="#E17726" />
              <path d="M0.966797 0.0151367L14.9013 5.21656L17.932 12.7992L0.966797 0.0151367Z" fill="#E27625" />
              <path
                d="M32.1656 27.0093L39.7516 27.1537L37.1004 36.1603L27.8438 33.6116L32.1656 27.0093Z"
                fill="#E27625"
              />
              <path
                d="M7.83409 27.0093L12.1399 33.6116L2.89876 36.1604L0.263672 27.1537L7.83409 27.0093Z"
                fill="#E27625"
              />
              <path
                d="M17.5203 10.8677L17.8304 20.8807L8.55371 20.4587L11.1924 16.4778L11.2258 16.4394L17.5203 10.8677Z"
                fill="#E27625"
              />
              <path
                d="M22.3831 10.7559L28.7737 16.4397L28.8067 16.4778L31.4455 20.4586L22.1709 20.8806L22.3831 10.7559Z"
                fill="#E27625"
              />
              <path d="M12.4115 27.0381L17.4768 30.9848L11.5928 33.8257L12.4115 27.0381Z" fill="#E27625" />
              <path d="M27.5893 27.0376L28.391 33.8258L22.5234 30.9847L27.5893 27.0376Z" fill="#E27625" />
              <path
                d="M22.6523 30.6128L28.6066 33.4959L23.0679 36.1282L23.1255 34.3884L22.6523 30.6128Z"
                fill="#D5BFB2"
              />
              <path
                d="M17.3458 30.6143L16.8913 34.3601L16.9286 36.1263L11.377 33.4961L17.3458 30.6143Z"
                fill="#D5BFB2"
              />
              <path d="M15.6263 22.1875L17.1822 25.4575L11.8848 23.9057L15.6263 22.1875Z" fill="#233447" />
              <path d="M24.3739 22.1875L28.133 23.9053L22.8184 25.4567L24.3739 22.1875Z" fill="#233447" />
              <path d="M12.8169 27.0049L11.9606 34.0423L7.37109 27.1587L12.8169 27.0049Z" fill="#CC6228" />
              <path d="M27.1836 27.0049L32.6296 27.1587L28.0228 34.0425L27.1836 27.0049Z" fill="#CC6228" />
              <path
                d="M31.5799 20.0605L27.6165 24.0998L24.5608 22.7034L23.0978 25.779L22.1387 20.4901L31.5799 20.0605Z"
                fill="#CC6228"
              />
              <path
                d="M8.41797 20.0605L17.8608 20.4902L16.9017 25.779L15.4384 22.7038L12.3988 24.0999L8.41797 20.0605Z"
                fill="#CC6228"
              />
              <path d="M8.15039 19.2314L12.6345 23.7816L12.7899 28.2736L8.15039 19.2314Z" fill="#E27525" />
              <path d="M31.8538 19.2236L27.2061 28.2819L27.381 23.7819L31.8538 19.2236Z" fill="#E27525" />
              <path
                d="M17.6412 19.5088L17.8217 20.6447L18.2676 23.4745L17.9809 32.166L16.6254 25.1841L16.625 25.1119L17.6412 19.5088Z"
                fill="#E27525"
              />
              <path
                d="M22.3562 19.4932L23.3751 25.1119L23.3747 25.1841L22.0158 32.1835L21.962 30.4328L21.75 23.4231L22.3562 19.4932Z"
                fill="#E27525"
              />
              <path
                d="M27.7797 23.6011L27.628 27.5039L22.8977 31.1894L21.9414 30.5138L23.0133 24.9926L27.7797 23.6011Z"
                fill="#F5841F"
              />
              <path
                d="M12.2373 23.6011L16.9873 24.9926L18.0591 30.5137L17.1029 31.1893L12.3723 27.5035L12.2373 23.6011Z"
                fill="#F5841F"
              />
              <path
                d="M10.4717 32.6338L16.5236 35.5013L16.4979 34.2768L17.0043 33.8323H22.994L23.5187 34.2753L23.48 35.4989L29.4935 32.641L26.5673 35.0591L23.0289 37.4894H16.9558L13.4197 35.0492L10.4717 32.6338Z"
                fill="#C0AC9D"
              />
              <path
                d="M22.2191 30.231L23.0748 30.8354L23.5763 34.8361L22.8506 34.2234H17.1513L16.4395 34.8485L16.9244 30.8357L17.7804 30.231H22.2191Z"
                fill="#161616"
              />
              <path
                d="M37.9395 0.351562L39.9998 6.53242L38.7131 12.7819L39.6293 13.4887L38.3895 14.4346L39.3213 15.1542L38.0875 16.2779L38.8449 16.8264L36.8347 19.1742L28.5894 16.7735L28.5179 16.7352L22.5762 11.723L37.9395 0.351562Z"
                fill="#763E1A"
              />
              <path
                d="M2.06031 0.351562L17.4237 11.723L11.4819 16.7352L11.4105 16.7735L3.16512 19.1742L1.15488 16.8264L1.91176 16.2783L0.678517 15.1542L1.60852 14.4354L0.350209 13.4868L1.30098 12.7795L0 6.53265L2.06031 0.351562Z"
                fill="#763E1A"
              />
              <path
                d="M28.1861 16.2485L36.9226 18.7921L39.7609 27.5398L32.2728 27.5398L27.1133 27.6049L30.8655 20.2912L28.1861 16.2485Z"
                fill="#F5841F"
              />
              <path
                d="M11.8139 16.2485L9.13399 20.2912L12.8867 27.6049L7.72971 27.5398H0.254883L3.07728 18.7922L11.8139 16.2485Z"
                fill="#F5841F"
              />
              <path
                d="M25.5283 5.17383L23.0847 11.7736L22.5661 20.6894L22.3677 23.4839L22.352 30.6225H17.6471L17.6318 23.4973L17.4327 20.6869L16.9139 11.7736L14.4707 5.17383H25.5283Z"
                fill="#F5841F"
              />
            </svg>
            <span className="ml-3 flex-1 whitespace-nowrap">MetaMask</span>
            <span className="ml-3 inline-flex items-center justify-center rounded bg-gray-200 px-2 py-0.5 text-xs font-medium text-gray-500 dark:bg-gray-700 dark:text-gray-400">
              Popular
            </span>
          </a>
        </li>
        <li>
          <a
            href="#"
            className="group flex items-center rounded-lg bg-gray-50 p-3 text-base font-bold text-gray-900 hover:bg-gray-100 hover:shadow dark:bg-gray-600 dark:text-white dark:hover:bg-gray-500"
          >
            <svg className="h-5" viewBox="0 0 292 292" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M145.7 291.66C226.146 291.66 291.36 226.446 291.36 146C291.36 65.5541 226.146 0.339844 145.7 0.339844C65.2542 0.339844 0.0400391 65.5541 0.0400391 146C0.0400391 226.446 65.2542 291.66 145.7 291.66Z"
                fill="#3259A5"
              />
              <path
                d="M195.94 155.5C191.49 179.08 170.8 196.91 145.93 196.91C117.81 196.91 95.0204 174.12 95.0204 146C95.0204 117.88 117.81 95.0897 145.93 95.0897C170.8 95.0897 191.49 112.93 195.94 136.5H247.31C242.52 84.7197 198.96 44.1797 145.93 44.1797C89.6904 44.1797 44.1104 89.7697 44.1104 146C44.1104 202.24 89.7004 247.82 145.93 247.82C198.96 247.82 242.52 207.28 247.31 155.5H195.94Z"
                fill="white"
              />
            </svg>
            <span className="ml-3 flex-1 whitespace-nowrap">Coinbase Wallet</span>
          </a>
        </li>
        <li>
          <a
            href="#"
            className="group flex items-center rounded-lg bg-gray-50 p-3 text-base font-bold text-gray-900 hover:bg-gray-100 hover:shadow dark:bg-gray-600 dark:text-white dark:hover:bg-gray-500"
          >
            <svg
              className="h-5"
              viewBox="0 0 75.591 75.591"
              xmlns="http://www.w3.org/2000/svg"
              xmlnsXlink="http://www.w3.org/1999/xlink"
            >
              <linearGradient
                id="a"
                gradientTransform="matrix(0 -54.944 -54.944 0 23.62 79.474)"
                gradientUnits="userSpaceOnUse"
                x2="1"
              >
                <stop offset="0" stopColor="#ff1b2d" />
                <stop offset=".3" stopColor="#ff1b2d" />
                <stop offset=".614" stopColor="#ff1b2d" />
                <stop offset="1" stopColor="#a70014" />
              </linearGradient>
              <linearGradient
                id="b"
                gradientTransform="matrix(0 -48.595 -48.595 0 37.854 76.235)"
                gradientUnits="userSpaceOnUse"
                x2="1"
              >
                <stop offset="0" stopColor="#9c0000" />
                <stop offset=".7" stopColor="#ff4b4b" />
                <stop offset="1" stopColor="#ff4b4b" />
              </linearGradient>
              <g transform="matrix(1.3333 0 0 -1.3333 0 107.2)">
                <path
                  d="m28.346 80.398c-15.655 0-28.346-12.691-28.346-28.346 0-15.202 11.968-27.609 26.996-28.313.44848-.02115.89766-.03314 1.3504-.03314 7.2574 0 13.876 2.7289 18.891 7.2137-3.3227-2.2036-7.2074-3.4715-11.359-3.4715-6.7504 0-12.796 3.3488-16.862 8.6297-3.1344 3.6999-5.1645 9.1691-5.3028 15.307v1.3349c.13821 6.1377 2.1683 11.608 5.302 15.307 4.0666 5.2809 10.112 8.6297 16.862 8.6297 4.1526 0 8.038-1.2679 11.361-3.4729-4.9904 4.4643-11.569 7.1876-18.786 7.2144-.03596 0-.07122.0014-.10718.0014z"
                  fill="url(#a)"
                />
                <path
                  d="m19.016 68.025c2.6013 3.0709 5.9607 4.9227 9.631 4.9227 8.2524 0 14.941-9.356 14.941-20.897s-6.6891-20.897-14.941-20.897c-3.6703 0-7.0297 1.851-9.6303 4.922 4.0659-5.2809 10.111-8.6297 16.862-8.6297 4.1519 0 8.0366 1.2679 11.359 3.4715 5.802 5.1906 9.4554 12.735 9.4554 21.133 0 8.397-3.6527 15.941-9.4533 21.131-3.3234 2.205-7.2088 3.4729-11.361 3.4729-6.7504 0-12.796-3.3488-16.862-8.6297"
                  fill="url(#b)"
                />
              </g>
            </svg>
            <span className="ml-3 flex-1 whitespace-nowrap">Opera Wallet</span>
          </a>
        </li>
        <li>
          <a
            href="#"
            className="group flex items-center rounded-lg bg-gray-50 p-3 text-base font-bold text-gray-900 hover:bg-gray-100 hover:shadow dark:bg-gray-600 dark:text-white dark:hover:bg-gray-500"
          >
            <svg
              className="h-5"
              viewBox="0 0 512 512"
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              xmlnsXlink="http://www.w3.org/1999/xlink"
            >
              <defs>
                <radialGradient cx="0%" cy="50%" fx="0%" fy="50%" r="100%" id="radialGradient-1">
                  <stop stopColor="#5D9DF6" offset="0%" />
                  <stop stopColor="#006FFF" offset="100%" />
                </radialGradient>
              </defs>
              <g id="Page-1" stroke="none" strokeWidth="1" fill="none" fillRule="evenodd">
                <g id="logo">
                  <rect id="base" fill="url(#radialGradient-1)" x="0" y="0" width="512" height="512" rx="256" />
                  <path
                    d="M169.209772,184.531136 C217.142772,137.600733 294.857519,137.600733 342.790517,184.531136 L348.559331,190.179285 C350.955981,192.525805 350.955981,196.330266 348.559331,198.676787 L328.82537,217.99798 C327.627045,219.171241 325.684176,219.171241 324.485851,217.99798 L316.547278,210.225455 C283.10802,177.485633 228.89227,177.485633 195.453011,210.225455 L186.951456,218.549188 C185.75313,219.722448 183.810261,219.722448 182.611937,218.549188 L162.877976,199.227995 C160.481326,196.881474 160.481326,193.077013 162.877976,190.730493 L169.209772,184.531136 Z M383.602212,224.489406 L401.165475,241.685365 C403.562113,244.031874 403.562127,247.836312 401.165506,250.182837 L321.971538,327.721548 C319.574905,330.068086 315.689168,330.068112 313.292501,327.721609 C313.292491,327.721599 313.29248,327.721588 313.29247,327.721578 L257.08541,272.690097 C256.486248,272.103467 255.514813,272.103467 254.915651,272.690097 C254.915647,272.690101 254.915644,272.690105 254.91564,272.690108 L198.709777,327.721548 C196.313151,330.068092 192.427413,330.068131 190.030739,327.721634 C190.030725,327.72162 190.03071,327.721606 190.030695,327.721591 L110.834524,250.181849 C108.437875,247.835329 108.437875,244.030868 110.834524,241.684348 L128.397819,224.488418 C130.794468,222.141898 134.680206,222.141898 137.076856,224.488418 L193.284734,279.520668 C193.883897,280.107298 194.85533,280.107298 195.454493,279.520668 C195.454502,279.520659 195.45451,279.520651 195.454519,279.520644 L251.65958,224.488418 C254.056175,222.141844 257.941913,222.141756 260.338618,224.488222 C260.338651,224.488255 260.338684,224.488288 260.338717,224.488321 L316.546521,279.520644 C317.145683,280.107273 318.117118,280.107273 318.71628,279.520644 L374.923175,224.489406 C377.319825,222.142885 381.205562,222.142885 383.602212,224.489406 Z"
                    id="WalletConnect"
                    fill="#FFFFFF"
                    fillRule="nonzero"
                  />
                </g>
              </g>
            </svg>
            <span className="ml-3 flex-1 whitespace-nowrap">WalletConnect</span>
          </a>
        </li>
        <li>
          <a
            href="#"
            className="group flex items-center rounded-lg bg-gray-50 p-3 text-base font-bold text-gray-900 hover:bg-gray-100 hover:shadow dark:bg-gray-600 dark:text-white dark:hover:bg-gray-500"
          >
            <svg className="h-4" viewBox="0 0 96 96" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M72.0998 0.600098H48.3998H24.5998H0.799805V24.4001V48.2001V49.7001V71.8001V71.9001V95.5001H24.5998V72.0001V71.9001V49.8001V48.3001V24.5001H48.3998H72.1998H95.9998V0.700104H72.0998V0.600098Z"
                fill="#617BFF"
              />
              <path
                d="M48.5 71.8002H72.1V95.6002H73C79.1 95.6002 84.9 93.2002 89.2 88.9002C93.5 84.6002 95.9 78.8002 95.9 72.7002V48.2002H48.5V71.8002Z"
                fill="#617BFF"
              />
            </svg>
            <span className="ml-3 flex-1 whitespace-nowrap">Fortmatic</span>
          </a>
        </li>
      </ul>
      <div>
        <a
          href="#"
          className="inline-flex items-center text-xs font-normal text-gray-500 hover:underline dark:text-gray-400"
        >
          <svg
            className="mr-2 h-3 w-3"
            aria-hidden="true"
            focusable="false"
            data-prefix="far"
            data-icon="question-circle"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              fill="currentColor"
              d="M256 8C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm0 448c-110.532 0-200-89.431-200-200 0-110.495 89.472-200 200-200 110.491 0 200 89.471 200 200 0 110.53-89.431 200-200 200zm107.244-255.2c0 67.052-72.421 68.084-72.421 92.863V300c0 6.627-5.373 12-12 12h-45.647c-6.627 0-12-5.373-12-12v-8.659c0-35.745 27.1-50.034 47.579-61.516 17.561-9.845 28.324-16.541 28.324-29.579 0-17.246-21.999-28.693-39.784-28.693-23.189 0-33.894 10.977-48.942 29.969-4.057 5.12-11.46 6.071-16.666 2.124l-27.824-21.098c-5.107-3.872-6.251-11.066-2.644-16.363C184.846 131.491 214.94 112 261.794 112c49.071 0 101.45 38.304 101.45 88.8zM298 368c0 23.159-18.841 42-42 42s-42-18.841-42-42 18.841-42 42-42 42 18.841 42 42z"
            />
          </svg>
          Why do I need to connect with my wallet?
        </a>
      </div>
    </Card>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "flex rounded-lg border border-gray-200 bg-white shadow-md dark:border-gray-700 dark:bg-gray-800",
    "children": "flex h-full flex-col justify-center gap-4 p-6",
    "horizontal": {
      "off": "flex-col",
      "on": "flex-col md:max-w-xl md:flex-row"
    },
    "href": "hover:bg-gray-100 dark:hover:bg-gray-700"
  },
  "img": {
    "base": "",
    "horizontal": {
      "off": "rounded-t-lg",
      "on": "h-96 w-full rounded-t-lg object-cover md:h-auto md:w-48 md:rounded-none md:rounded-l-lg"
    }
  }
}
```

## References

- [Flowbite Card](https://flowbite.com/docs/components/card/)


---

## Carousel

# React Carousel - Flowbite

> Get started with the carousel component to showcase images and content and slide through them using custom controls, intervals, and indicators with React and Tailwind CSS

Use the responsive carousel component to allow users to slide through multiple items and navigate between them using the control buttons and indicators.

Choose from multiple examples and options to update the intervals, make the carousel static and set custom control button and indicator by configuring React and the utility classes from Tailwind CSS.

To start using the carousel component you first need to import it from Flowbite React:

```jsx
import { Carousel } from "flowbite-react";
```

## Default carousel

Use this example by adding a series of images inside of the `<Carousel>` component.

```tsx
// index.tsx

import { Carousel } from "flowbite-react";

export function Component() {
  return (
    <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel>
        <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-4.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-5.svg" alt="..." />
      </Carousel>
    </div>
  );
}
```

## Static carousel

Pass the `slide` prop to the carousel component to make it static and disable the automatic sliding functionality. This does not disable the control or indicator buttons.

```tsx
// index.tsx

import { Carousel } from "flowbite-react";

export function Component() {
  return (
    <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel slide={false}>
        <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-4.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-5.svg" alt="..." />
      </Carousel>
    </div>
  );
}
```

## Sliding interval

Use the `slideInterval` prop to set the interval between slides in milliseconds. The default value is `3000`.

```tsx
// index.tsx

import { Carousel } from "flowbite-react";

export function Component() {
  return (
    <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel slideInterval={5000}>
        <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-4.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-5.svg" alt="..." />
      </Carousel>
    </div>
  );
}
```

## Custom controls

Use the `leftControl` and `rightControl` props to set custom control buttons.

```tsx
// index.tsx

import { Carousel } from "flowbite-react";

export function Component() {
  return (
    <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel leftControl="left" rightControl="right">
        <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-4.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-5.svg" alt="..." />
      </Carousel>
    </div>
  );
}
```

## Indicators

Add custom indicators or disable them by passing the `indicators` prop to the `<Carousel>` component.

```tsx
// index.tsx

import { Carousel } from "flowbite-react";

export function Component() {
  return (
    <div className="grid h-56 grid-cols-2 gap-4 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel>
        <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-4.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-5.svg" alt="..." />
      </Carousel>
      <Carousel indicators={false}>
        <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-4.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-5.svg" alt="..." />
      </Carousel>
    </div>
  );
}
```

## Pause On Hover

To conditionally pause the carousel on mouse hover (desktop), or touch and hold (mobile), you can use the `pauseOnHover` property on the `<Carousel>` component. Default value is `false`.

```tsx
// index.tsx

import { Carousel } from "flowbite-react";

export function Component() {
  return (
    <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel pauseOnHover>
        <img src="https://flowbite.com/docs/images/carousel/carousel-1.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-2.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-3.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-4.svg" alt="..." />
        <img src="https://flowbite.com/docs/images/carousel/carousel-5.svg" alt="..." />
      </Carousel>
    </div>
  );
}
```

## Slider content

Instead of images you can also use any type of markup and content inside the carousel such as simple text.

```tsx
// index.tsx

import { Carousel } from "flowbite-react";

export function Component() {
  return (
    <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel>
        <div className="flex h-full items-center justify-center bg-gray-400 dark:bg-gray-700 dark:text-white">
          Slide 1
        </div>
        <div className="flex h-full items-center justify-center bg-gray-400 dark:bg-gray-700 dark:text-white">
          Slide 2
        </div>
        <div className="flex h-full items-center justify-center bg-gray-400 dark:bg-gray-700 dark:text-white">
          Slide 3
        </div>
      </Carousel>
    </div>
  );
}
```

## Handle `onSlideChanged` event

To hook events to slide changed you can use `onSlideChange` property.

```tsx
// index.tsx

"use client";

import { Carousel } from "flowbite-react";

export function Component() {
  return (
    <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
      <Carousel onSlideChange={(index) => console.log("onSlideChange()", index)}>
        <div className="flex h-full items-center justify-center bg-gray-400 dark:bg-gray-700 dark:text-white">
          Slide 1
        </div>
        <div className="flex h-full items-center justify-center bg-gray-400 dark:bg-gray-700 dark:text-white">
          Slide 2
        </div>
        <div className="flex h-full items-center justify-center bg-gray-400 dark:bg-gray-700 dark:text-white">
          Slide 3
        </div>
      </Carousel>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "relative h-full w-full",
    "leftControl": "absolute left-0 top-0 flex h-full items-center justify-center px-4 focus:outline-none",
    "rightControl": "absolute right-0 top-0 flex h-full items-center justify-center px-4 focus:outline-none"
  },
  "indicators": {
    "active": {
      "off": "bg-white/50 hover:bg-white dark:bg-gray-800/50 dark:hover:bg-gray-800",
      "on": "bg-white dark:bg-gray-800"
    },
    "base": "h-3 w-3 rounded-full",
    "wrapper": "absolute bottom-5 left-1/2 flex -translate-x-1/2 space-x-3"
  },
  "item": {
    "base": "absolute left-1/2 top-1/2 block w-full -translate-x-1/2 -translate-y-1/2",
    "wrapper": {
      "off": "w-full shrink-0 transform cursor-default snap-center",
      "on": "w-full shrink-0 transform cursor-grab snap-center"
    }
  },
  "control": {
    "base": "inline-flex h-8 w-8 items-center justify-center rounded-full bg-white/30 group-hover:bg-white/50 group-focus:outline-none group-focus:ring-4 group-focus:ring-white sm:h-10 sm:w-10 dark:bg-gray-800/30 dark:group-hover:bg-gray-800/60 dark:group-focus:ring-gray-800/70",
    "icon": "h-5 w-5 text-white sm:h-6 sm:w-6 dark:text-gray-800"
  },
  "scrollContainer": {
    "base": "flex h-full snap-mandatory overflow-y-hidden overflow-x-scroll scroll-smooth rounded-lg",
    "snap": "snap-x"
  }
}
```

## References

- [Flowbite Carousel](https://flowbite.com/docs/components/carousel/)


---

## Clipboard

# React Clipboard - Flowbite

> Use the clipboard component to copy text, data or lines of code to the clipboard with a single click based on various styles and examples coded with Tailwind CSS and Flowbite

The copy to clipboard component allows you to copy text, lines of code, contact details or any other data to the clipboard with a single click on a trigger element such as a button. This component can be used to copy text from an input field, textarea, code block or even address fields in a form element.

These components are built with Tailwind CSS and Flowbite React and can be found on the internet on websites such as Bitly, Cloudflare, Amazon AWS and almost all open-source projects and documentations.

Import the component from `flowbite-react` to use the clipboard element:

```jsx
import { Clipboard } from "flowbite-react";
```

## Default copy to clipboard

Use this example to copy the content of an input text field by clicking on a button and update the button text.

```tsx
// index.tsx

import { Clipboard } from "flowbite-react"

export function Component() {
  return (
    <div className="grid w-full max-w-[23rem] grid-cols-8 gap-2">
      <label htmlFor="npm-install" className="sr-only">
        Label
      </label>
      <input
        id="npm-install"
        type="text"
        className="col-span-6 block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-500 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-400 dark:placeholder:text-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
        value="npm install flowbite-react"
        disabled
        readOnly
      />
      <Clipboard valueToCopy="npm install flowbite-react" label="Copy" />
    </div>
  );
}
```

## Input with copy button

This example can be used to copy the content of an input field by clicking on a button with an icon positioned inside the form element and also show a tooltip with a message when the text has been copied.

```tsx
// index.tsx


import { ClipboardWithIcon } from "flowbite-react";

export function Component() {
  return (
    <div className="grid w-full max-w-64">
      <div className="relative">
        <label htmlFor="npm-install" className="sr-only">
          Label
        </label>
        <input
          id="npm-install"
          type="text"
          className="col-span-6 block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-500 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-400 dark:placeholder:text-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
          value="npm install flowbite-react"
          disabled
          readOnly
        />
        <ClipboardWithIcon valueToCopy="npm install flowbite-react" />
      </div>
    </div>
  );
}
```

## Copy button with text

Use this example to show a copy button inside the input field with a text label and icon that updates to a success state when the text has been copied.

```tsx
// index.tsx

import { ClipboardWithIconText } from "flowbite-react"

export function Component() {
  return (
    <div className="grid w-full max-w-80">
      <div className="relative">
        <label htmlFor="npm-install" className="sr-only">
          Label
        </label>
        <input
          id="npm-install"
          type="text"
          className="col-span-6 block w-full rounded-lg border border-gray-300 bg-gray-50 px-2.5 py-4 text-sm text-gray-500 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-400 dark:placeholder:text-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
          value="npm install flowbite-react"
          disabled
          readOnly
        />
        <ClipboardWithIconText valueToCopy="npm install flowbite-react" />
      </div>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "button": {
    "base": "inline-flex w-full items-center justify-center rounded-lg bg-blue-700 px-5 py-3 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
    "label": "text-center text-sm font-medium text-white sm:w-auto"
  },
  "withIcon": {
    "base": "absolute end-2 top-1/2 inline-flex -translate-y-1/2 items-center justify-center rounded-lg p-2 text-gray-500 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-800",
    "icon": {
      "defaultIcon": "h-4 w-4",
      "successIcon": "h-4 w-4 text-blue-700 dark:text-blue-500"
    }
  },
  "withIconText": {
    "base": "absolute end-2.5 top-1/2 inline-flex -translate-y-1/2 items-center justify-center rounded-lg border border-gray-200 bg-white px-2.5 py-2 text-gray-900 hover:bg-gray-100 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700",
    "icon": {
      "defaultIcon": "me-1.5 h-3 w-3",
      "successIcon": "me-1.5 h-3 w-3 text-blue-700 dark:text-blue-500"
    },
    "label": {
      "base": "inline-flex items-center",
      "defaultText": "text-xs font-semibold",
      "successText": "text-xs font-semibold text-blue-700 dark:text-blue-500"
    }
  }
}
```

## References

- [Flowbite Datepicker](https://flowbite.com/docs/components/clipboard/)


---

## Datepicker

# React Datepicker - Flowbite

> Use the datepicker component to select a date from a calendar view based on an input element by selecting the day, month, and year values using React and Tailwind CSS

The Datepicker component from Flowbite React is an advanced UI element that you can use to allow users to pick a date from a calendar view by selecting the day, month, and year values which then will be available in the input field and state of the component.

Follow the examples below to see how you can use the Datepicker component by importing it from the Flowbite React library, customize the colors and behaviour of the component by overriding the default theme variables and using the props from React.

Import the component from `flowbite-react` to use the datepicker element:

```jsx
import { Datepicker } from "flowbite-react";
```

## Default Datepicker

Use this example to show a simple datepicker component.

```tsx
// index.tsx

import { Datepicker } from "flowbite-react";

export function Component() {
  return <Datepicker />;
}
```

## Localization

Use the `language` prop to set the language of the datepicker component.

The `labelTodayButton` and `labelClearButton` can also be used to update the text of the buttons.

```tsx
// index.tsx

import { Datepicker } from "flowbite-react";

export function Component() {
  return <Datepicker language="pt-BR" labelTodayButton="Hoje" labelClearButton="Limpar" />;
}
```

## Limit the date

By using the `minDate` and `maxDate` props you can limit the date range that the user can select.

```tsx
// index.tsx

import { Datepicker } from "flowbite-react";

export function Component() {
  return <Datepicker minDate={new Date(2023, 0, 1)} maxDate={new Date(2023, 3, 30)} />;
}
```

## Week start

The `weekStart` prop can be used to set the first day of the week inside the datepicker component.

```json
{
  "0": "Sunday",
  "1": "Monday",
  "2": "Tuesday",
  "3": "Wednesday",
  "4": "Thursday",
  "5": "Friday",
  "6": "Saturday"
}
```

```tsx
// index.tsx

import { Datepicker } from "flowbite-react";

export function Component() {
  return (
    <Datepicker
      weekStart={1} // Monday
    />
  );
}
```

## Autohide

By setting the `autoHide` prop you can either enable or disable automatically hiding the datepicker component when selecting a value.

```tsx
// index.tsx

import { Datepicker } from "flowbite-react";

export function Component() {
  return <Datepicker autoHide={false} />;
}
```

## Title

You can use the `title` prop to set a title for the datepicker component.

```tsx
// index.tsx

import { Datepicker } from "flowbite-react";

export function Component() {
  return <Datepicker title="Flowbite Datepicker" />
}
```

## Inline

Use the `inline` prop to show the datepicker component without having to click inside an input field.

```tsx
// index.tsx

import { Datepicker } from "flowbite-react";

export function Component() {
  return <Datepicker inline />;
}
```

## Controlled Date/Datepicker.

Use `<Datepicker value={}` to create a controlled `<Datepicker />`. Pass `null` to clear the input.

<Example name="datepicker.value" />

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "relative"
  },
  "popup": {
    "root": {
      "base": "absolute top-10 z-50 block pt-2",
      "inline": "relative top-0 z-auto",
      "inner": "inline-block rounded-lg bg-white p-4 shadow-lg dark:bg-gray-700"
    },
    "header": {
      "base": "",
      "title": "px-2 py-3 text-center font-semibold text-gray-900 dark:text-white",
      "selectors": {
        "base": "mb-2 flex justify-between",
        "button": {
          "base": "rounded-lg bg-white px-5 py-2.5 text-sm font-semibold text-gray-900 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600",
          "prev": "",
          "next": "",
          "view": ""
        }
      }
    },
    "view": {
      "base": "p-1"
    },
    "footer": {
      "base": "mt-2 flex space-x-2",
      "button": {
        "base": "w-full rounded-lg px-5 py-2 text-center text-sm font-medium focus:ring-4 focus:ring-primary-300",
        "today": "bg-primary-700 text-white hover:bg-primary-800 dark:bg-primary-600 dark:hover:bg-primary-700",
        "clear": "border border-gray-300 bg-white text-gray-900 hover:bg-gray-100 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600"
      }
    }
  },
  "views": {
    "days": {
      "header": {
        "base": "mb-1 grid grid-cols-7",
        "title": "h-6 text-center text-sm font-medium leading-6 text-gray-500 dark:text-gray-400"
      },
      "items": {
        "base": "grid w-64 grid-cols-7",
        "item": {
          "base": "block flex-1 cursor-pointer rounded-lg border-0 text-center text-sm font-semibold leading-9 text-gray-900 hover:bg-gray-100 dark:text-white dark:hover:bg-gray-600",
          "selected": "bg-primary-700 text-white hover:bg-primary-600",
          "disabled": "text-gray-500"
        }
      }
    },
    "months": {
      "items": {
        "base": "grid w-64 grid-cols-4",
        "item": {
          "base": "block flex-1 cursor-pointer rounded-lg border-0 text-center text-sm font-semibold leading-9 text-gray-900 hover:bg-gray-100 dark:text-white dark:hover:bg-gray-600",
          "selected": "bg-primary-700 text-white hover:bg-primary-600",
          "disabled": "text-gray-500"
        }
      }
    },
    "years": {
      "items": {
        "base": "grid w-64 grid-cols-4",
        "item": {
          "base": "block flex-1 cursor-pointer rounded-lg border-0 text-center text-sm font-semibold leading-9 text-gray-900 hover:bg-gray-100 dark:text-white dark:hover:bg-gray-600",
          "selected": "bg-primary-700 text-white hover:bg-primary-600",
          "disabled": "text-gray-500"
        }
      }
    },
    "decades": {
      "items": {
        "base": "grid w-64 grid-cols-4",
        "item": {
          "base": "block flex-1 cursor-pointer rounded-lg border-0 text-center text-sm font-semibold leading-9 text-gray-900 hover:bg-gray-100 dark:text-white dark:hover:bg-gray-600",
          "selected": "bg-primary-700 text-white hover:bg-primary-600",
          "disabled": "text-gray-500"
        }
      }
    }
  }
}
```

## References

- [Flowbite Datepicker](https://flowbite.com/docs/plugins/datepicker/)


---

## Drawer

# React Drawer (offcanvas) - Flowbite

> The Drawer component can be used as a hidden off-canvas sidebar for navigation and to show other information based on multiple styles and placements

Use the Drawer component (or "off-canvas") to show a fixed element relative to the document page from any side for navigation, contact forms, informational purposes or other user actions.

You can set multiple options such as the placement, activate body scrolling, show or hide the backdrop and even use the swipeable edge functionality to show a small part of the drawer when it is not shown completely.

To start using the drawer component you need to import it from `flowbite-react`:

```jsx
import { Drawer } from "flowbite-react";
```

## Default drawer

```tsx
// index.tsx

"use client";

import { Button, Drawer, DrawerHeader, DrawerItems } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show drawer</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose}>
        <DrawerHeader title="Drawer" />
        <DrawerItems>
          <p className="mb-6 text-sm text-gray-500 dark:text-gray-400">
            Supercharge your hiring by taking advantage of our&nbsp;
            <a href="#" className="text-cyan-600 underline hover:no-underline dark:text-cyan-500">
              limited-time sale
            </a>
            &nbsp;for Flowbite Docs + Job Board. Unlimited access to over 190K top-ranked candidates and the #1 design
            job board.
          </p>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <a
              href="#"
              className="rounded-lg border border-gray-200 bg-white px-4 py-2 text-center text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-cyan-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700"
            >
              Learn more
            </a>
            <a
              href="#"
              className="inline-flex items-center rounded-lg bg-cyan-700 px-4 py-2 text-center text-sm font-medium text-white hover:bg-cyan-800 focus:outline-none focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"
            >
              Get access&nbsp;
              <svg
                className="ms-2 h-3.5 w-3.5 rtl:rotate-180"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 14 10"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M1 5h12m0 0L9 1m4 4L9 9"
                />
              </svg>
            </a>
          </div>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

## Drawer navigation

Use this example to show a navigational sidebar inside the drawer component.

```tsx
// index.tsx

"use client";

import {
  Button,
  Drawer,
  DrawerHeader,
  DrawerItems,
  Sidebar,
  SidebarItem,
  SidebarItemGroup,
  SidebarItems,
  TextInput,
} from "flowbite-react";
import { useState } from "react";
import {
  HiChartPie,
  HiClipboard,
  HiCollection,
  HiInformationCircle,
  HiLogin,
  HiPencil,
  HiSearch,
  HiShoppingBag,
  HiUsers,
} from "react-icons/hi";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show navigation</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose}>
        <DrawerHeader title="MENU" titleIcon={() => <></>} />
        <DrawerItems>
          <Sidebar
            aria-label="Sidebar with multi-level dropdown example"
            className="[&>div]:bg-transparent [&>div]:p-0"
          >
            <div className="flex h-full flex-col justify-between py-2">
              <div>
                <form className="pb-3 md:hidden">
                  <TextInput icon={HiSearch} type="search" placeholder="Search" required size={32} />
                </form>
                <SidebarItems>
                  <SidebarItemGroup>
                    <SidebarItem href="/" icon={HiChartPie}>
                      Dashboard
                    </SidebarItem>
                    <SidebarItem href="/e-commerce/products" icon={HiShoppingBag}>
                      Products
                    </SidebarItem>
                    <SidebarItem href="/users/list" icon={HiUsers}>
                      Users list
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-in" icon={HiLogin}>
                      Sign in
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-up" icon={HiPencil}>
                      Sign up
                    </SidebarItem>
                  </SidebarItemGroup>
                  <SidebarItemGroup>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/" icon={HiClipboard}>
                      Docs
                    </SidebarItem>
                    <SidebarItem href="https://flowbite-react.com/" icon={HiCollection}>
                      Components
                    </SidebarItem>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/issues" icon={HiInformationCircle}>
                      Help
                    </SidebarItem>
                  </SidebarItemGroup>
                </SidebarItems>
              </div>
            </div>
          </Sidebar>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

## Contact form

Use this example to show a contact form inside the drawer component.

```tsx
// index.tsx

"use client";

import { Button, Drawer, DrawerHeader, DrawerItems, Label, Textarea, TextInput } from "flowbite-react";
import { useState } from "react";
import { HiEnvelope } from "react-icons/hi2";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show contact form</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose}>
        <DrawerHeader title="CONTACT US" titleIcon={HiEnvelope} />
        <DrawerItems>
          <form action="#">
            <div className="mb-6 mt-3">
              <Label htmlFor="email" className="mb-2 block">
                Your email
              </Label>
              <TextInput id="email" name="email" placeholder="name@company.com" type="email" />
            </div>
            <div className="mb-6">
              <Label htmlFor="subject" className="mb-2 block">
                Subject
              </Label>
              <TextInput id="subject" name="subject" placeholder="Let us know how we can help you" />
            </div>
            <div className="mb-6">
              <Label htmlFor="message" className="mb-2 block">
                Your message
              </Label>
              <Textarea id="message" name="message" placeholder="Your message..." rows={4} />
            </div>
            <div className="mb-6">
              <Button type="submit" className="w-full">
                Send message
              </Button>
            </div>
            <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
              <a href="mailto:info@company.com" className="hover:underline">
                info@company.com
              </a>
            </p>
            <p className="text-sm text-gray-500 dark:text-gray-400">
              <a href="tel:2124567890" className="hover:underline">
                212-456-7890
              </a>
            </p>
          </form>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

## Form elements

Use this example if you want to add form elements inside the drawer component including datepickers.

```tsx
// index.tsx

"use client";

import {
  Avatar,
  AvatarGroup,
  Button,
  Datepicker,
  Drawer,
  DrawerHeader,
  DrawerItems,
  Label,
  Textarea,
  TextInput,
} from "flowbite-react";
import { useState } from "react";
import { HiCalendar, HiUserAdd } from "react-icons/hi";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show drawer</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose}>
        <DrawerHeader title="NEW EVENT" titleIcon={HiCalendar} />
        <DrawerItems>
          <form action="#">
            <div className="mb-6 mt-3">
              <Label htmlFor="title" className="mb-2 block">
                Title
              </Label>
              <TextInput id="title" name="title" placeholder="Apple Keynote" />
            </div>
            <div className="mb-6">
              <Label htmlFor="description" className="mb-2 block">
                Description
              </Label>
              <Textarea id="description" name="description" placeholder="Write event description..." rows={4} />
            </div>
            <div className="mb-6">
              <Datepicker />
            </div>
            <div className="mb-6">
              <TextInput
                id="guests"
                name="guests"
                placeholder="Add guest email"
                type="search"
                rightIcon={() => (
                  <Button size="sm" className="[&>span]:items-center [&>span]:px-2 [&>span]:py-0">
                    <HiUserAdd className="mr-2" />
                    Add
                  </Button>
                )}
                theme={{
                  field: {
                    rightIcon: {
                      base: twMerge(theme.textInput.field.rightIcon.base, "pointer-events-auto"),
                    },
                  },
                }}
              />
            </div>
            <Avatar.Group className="mb-6">
              <Avatar alt="" img="/images/people/profile-picture-5.jpg" rounded size="sm" stacked />
              <Avatar alt="" img="/images/people/profile-picture-2.jpg" rounded size="sm" stacked />
              <Avatar alt="" img="/images/people/profile-picture-3.jpg" rounded size="sm" stacked />
              <Avatar alt="" img="/images/people/profile-picture-4.jpg" rounded size="sm" stacked />
            </Avatar.Group>
            <Button className="w-full">
              <HiCalendar className="mr-2" />
              Create event
            </Button>
          </form>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

## Placement

Use the placement options to position the drawer component either on the top, right, bottom, or left side of the document page. This can be done using the `position="{top|right|bottom|left}"` attribute where the default value is "left".

### Left drawer

Use this example where you can position the drawer component on the left side of the page.

```tsx
// index.tsx

"use client";

import { Button, Drawer, DrawerHeader, DrawerItems } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show left drawer</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose} position="left">
        <DrawerHeader title="Drawer" />
        <DrawerItems>
          <p className="mb-6 text-sm text-gray-500 dark:text-gray-400">
            Supercharge your hiring by taking advantage of our&nbsp;
            <a href="#" className="text-cyan-600 underline hover:no-underline dark:text-cyan-500">
              limited-time sale
            </a>
            &nbsp;for Flowbite Docs + Job Board. Unlimited access to over 190K top-ranked candidates and the #1 design
            job board.
          </p>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <a
              href="#"
              className="rounded-lg border border-gray-200 bg-white px-4 py-2 text-center text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-cyan-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700"
            >
              Learn more
            </a>
            <a
              href="#"
              className="inline-flex items-center rounded-lg bg-cyan-700 px-4 py-2 text-center text-sm font-medium text-white hover:bg-cyan-800 focus:outline-none focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"
            >
              Get access&nbsp;
              <svg
                className="ms-2 h-3.5 w-3.5 rtl:rotate-180"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 14 10"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M1 5h12m0 0L9 1m4 4L9 9"
                />
              </svg>
            </a>
          </div>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

### Right drawer

Use this example to show the drawer component on the right side of the page.

```tsx
// index.tsx

"use client";

import { Button, Drawer, DrawerHeader, DrawerItems } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show right drawer</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose} position="right">
        <DrawerHeader title="Drawer" />
        <DrawerItems>
          <p className="mb-6 text-sm text-gray-500 dark:text-gray-400">
            Supercharge your hiring by taking advantage of our&nbsp;
            <a href="#" className="text-cyan-600 underline hover:no-underline dark:text-cyan-500">
              limited-time sale
            </a>
            &nbsp;for Flowbite Docs + Job Board. Unlimited access to over 190K top-ranked candidates and the #1 design
            job board.
          </p>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <a
              href="#"
              className="rounded-lg border border-gray-200 bg-white px-4 py-2 text-center text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-cyan-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700"
            >
              Learn more
            </a>
            <a
              href="#"
              className="inline-flex items-center rounded-lg bg-cyan-700 px-4 py-2 text-center text-sm font-medium text-white hover:bg-cyan-800 focus:outline-none focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"
            >
              Get access&nbsp;
              <svg
                className="ms-2 h-3.5 w-3.5 rtl:rotate-180"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 14 10"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M1 5h12m0 0L9 1m4 4L9 9"
                />
              </svg>
            </a>
          </div>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

### Top drawer

Use this example to show the drawer on the top side of the page.

```tsx
// index.tsx

"use client";

import { Button, Drawer, DrawerHeader, DrawerItems } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show top drawer</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose} position="top">
        <DrawerHeader title="Drawer" />
        <DrawerItems>
          <p className="mb-6 text-sm text-gray-500 dark:text-gray-400">
            Supercharge your hiring by taking advantage of our&nbsp;
            <a href="#" className="text-cyan-600 underline hover:no-underline dark:text-cyan-500">
              limited-time sale
            </a>
            &nbsp;for Flowbite Docs + Job Board. Unlimited access to over 190K top-ranked candidates and the #1 design
            job board.
          </p>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <a
              href="#"
              className="rounded-lg border border-gray-200 bg-white px-4 py-2 text-center text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-cyan-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700"
            >
              Learn more
            </a>
            <a
              href="#"
              className="inline-flex items-center rounded-lg bg-cyan-700 px-4 py-2 text-center text-sm font-medium text-white hover:bg-cyan-800 focus:outline-none focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"
            >
              Get access&nbsp;
              <svg
                className="ms-2 h-3.5 w-3.5 rtl:rotate-180"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 14 10"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M1 5h12m0 0L9 1m4 4L9 9"
                />
              </svg>
            </a>
          </div>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

### Bottom drawer

Use this example to show the drawer on the bottom side of the page.

```tsx
// index.tsx

"use client";

import { Button, Drawer, DrawerHeader, DrawerItems } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show bottom drawer</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose} position="bottom">
        <DrawerHeader title="Drawer" />
        <DrawerItems>
          <p className="mb-6 text-sm text-gray-500 dark:text-gray-400">
            Supercharge your hiring by taking advantage of our&nbsp;
            <a href="#" className="text-cyan-600 underline hover:no-underline dark:text-cyan-500">
              limited-time sale
            </a>
            &nbsp;for Flowbite Docs + Job Board. Unlimited access to over 190K top-ranked candidates and the #1 design
            job board.
          </p>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <a
              href="#"
              className="rounded-lg border border-gray-200 bg-white px-4 py-2 text-center text-sm font-medium text-gray-900 hover:bg-gray-100 hover:text-cyan-700 focus:z-10 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white dark:focus:ring-gray-700"
            >
              Learn more
            </a>
            <a
              href="#"
              className="inline-flex items-center rounded-lg bg-cyan-700 px-4 py-2 text-center text-sm font-medium text-white hover:bg-cyan-800 focus:outline-none focus:ring-4 focus:ring-cyan-300 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"
            >
              Get access&nbsp;
              <svg
                className="ms-2 h-3.5 w-3.5 rtl:rotate-180"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 14 10"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M1 5h12m0 0L9 1m4 4L9 9"
                />
              </svg>
            </a>
          </div>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

## Body scrolling

By default, body scrolling is disabled when the drawer is visible, however, you can choose to enable it using the `bodyScrolling="{true|false}"` attribute.

### Disabled (default)

This is an example where the body scrolling behaviour is disabled when the drawer is visible.

```tsx
// index.tsx

"use client";

import {
  Button,
  Drawer,
  DrawerHeader,
  DrawerItems,
  Sidebar,
  SidebarItem,
  SidebarItemGroup,
  SidebarItems,
  TextInput,
} from "flowbite-react";
import { useState } from "react";
import {
  HiChartPie,
  HiClipboard,
  HiCollection,
  HiInformationCircle,
  HiLogin,
  HiPencil,
  HiSearch,
  HiShoppingBag,
  HiUsers,
} from "react-icons/hi";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show navigation</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose}>
        <DrawerHeader title="MENU" titleIcon={() => <></>} />
        <DrawerItems>
          <Sidebar
            aria-label="Sidebar with multi-level dropdown example"
            className="[&>div]:bg-transparent [&>div]:p-0"
          >
            <div className="flex h-full flex-col justify-between py-2">
              <div>
                <form className="pb-3 md:hidden">
                  <TextInput icon={HiSearch} type="search" placeholder="Search" required size={32} />
                </form>
                <SidebarItems>
                  <SidebarItemGroup>
                    <SidebarItem href="/" icon={HiChartPie}>
                      Dashboard
                    </SidebarItem>
                    <SidebarItem href="/e-commerce/products" icon={HiShoppingBag}>
                      Products
                    </SidebarItem>
                    <SidebarItem href="/users/list" icon={HiUsers}>
                      Users list
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-in" icon={HiLogin}>
                      Sign in
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-up" icon={HiPencil}>
                      Sign up
                    </SidebarItem>
                  </SidebarItemGroup>
                  <SidebarItemGroup>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/" icon={HiClipboard}>
                      Docs
                    </SidebarItem>
                    <SidebarItem href="https://flowbite-react.com/" icon={HiCollection}>
                      Components
                    </SidebarItem>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/issues" icon={HiInformationCircle}>
                      Help
                    </SidebarItem>
                  </SidebarItemGroup>
                </SidebarItems>
              </div>
            </div>
          </Sidebar>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

### Enabled

Get started with this example in order to enable body scrolling even if the drawer component is visible by applying `overflow-y: auto` to your `<body>`.

```tsx
// index.tsx

"use client";

import {
  Button,
  Drawer,
  DrawerHeader,
  DrawerItems,
  Sidebar,
  SidebarItem,
  SidebarItemGroup,
  SidebarItems,
  TextInput,
} from "flowbite-react";
import { useState } from "react";
import {
  HiChartPie,
  HiClipboard,
  HiCollection,
  HiInformationCircle,
  HiLogin,
  HiPencil,
  HiSearch,
  HiShoppingBag,
  HiUsers,
} from "react-icons/hi";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <div className="h-[300px] max-h-[300px]">
      <div className="flex flex-col items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show body scrolling</Button>
      </div>
      <div className="mx-auto max-w-lg">
        <div role="status" className="my-7 animate-pulse">
          <div className="mb-4 h-2.5 w-48 rounded-full bg-gray-300 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[500px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[450px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[380px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <span className="sr-only">Loading...</span>
        </div>
        <div role="status" className="mb-7 max-w-lg animate-pulse">
          <div className="flex h-48 w-full items-center justify-center rounded bg-gray-300 dark:bg-gray-700">
            <svg
              className="h-12 w-12 text-gray-200"
              xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true"
              fill="currentColor"
              viewBox="0 0 640 512"
            >
              <path d="M480 80C480 35.82 515.8 0 560 0C604.2 0 640 35.82 640 80C640 124.2 604.2 160 560 160C515.8 160 480 124.2 480 80zM0 456.1C0 445.6 2.964 435.3 8.551 426.4L225.3 81.01C231.9 70.42 243.5 64 256 64C268.5 64 280.1 70.42 286.8 81.01L412.7 281.7L460.9 202.7C464.1 196.1 472.2 192 480 192C487.8 192 495 196.1 499.1 202.7L631.1 419.1C636.9 428.6 640 439.7 640 450.9C640 484.6 612.6 512 578.9 512H55.91C25.03 512 .0006 486.1 .0006 456.1L0 456.1z"></path>
            </svg>
          </div>
          <span className="sr-only">Loading...</span>
        </div>
        <div role="status" className="my-6 animate-pulse">
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[450px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[500px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[450px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[380px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <span className="sr-only">Loading...</span>
        </div>
        <div role="status" className="my-6 animate-pulse">
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[450px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[500px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <span className="sr-only">Loading...</span>
        </div>
        <div role="status" className="mb-6 mt-7 animate-pulse">
          <div className="mb-4 h-2.5 w-48 rounded-full bg-gray-300 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[450px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[500px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[450px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[380px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[500px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <span className="sr-only">Loading...</span>
        </div>
        <div role="status" className="my-6 animate-pulse">
          <div className="mb-2.5 h-2 max-w-[460px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <div className="mb-2.5 h-2 max-w-[450px] rounded-full bg-gray-200 dark:bg-gray-700"></div>
          <span className="sr-only">Loading...</span>
        </div>
      </div>
      <Drawer open={isOpen} onClose={handleClose}>
        <DrawerHeader title="MENU" titleIcon={() => <></>} />
        <DrawerItems>
          <Sidebar
            aria-label="Sidebar with multi-level dropdown example"
            className="[&>div]:bg-transparent [&>div]:p-0"
          >
            <div className="flex h-full flex-col justify-between py-2">
              <div>
                <form className="pb-3 md:hidden">
                  <TextInput icon={HiSearch} type="search" placeholder="Search" required size={32} />
                </form>
                <SidebarItems>
                  <SidebarItemGroup>
                    <SidebarItem href="/" icon={HiChartPie}>
                      Dashboard
                    </SidebarItem>
                    <SidebarItem href="/e-commerce/products" icon={HiShoppingBag}>
                      Products
                    </SidebarItem>
                    <SidebarItem href="/users/list" icon={HiUsers}>
                      Users list
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-in" icon={HiLogin}>
                      Sign in
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-up" icon={HiPencil}>
                      Sign up
                    </SidebarItem>
                  </SidebarItemGroup>
                  <SidebarItemGroup>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/" icon={HiClipboard}>
                      Docs
                    </SidebarItem>
                    <SidebarItem href="https://flowbite-react.com/" icon={HiCollection}>
                      Components
                    </SidebarItem>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/issues" icon={HiInformationCircle}>
                      Help
                    </SidebarItem>
                  </SidebarItemGroup>
                </SidebarItems>
              </div>
            </div>
          </Sidebar>
        </DrawerItems>
      </Drawer>
    </div>
  );
}
```

## Backdrop

The backdrop element can be used to dim out the background elements when the drawer is visible and also automatically hide the component when clicking outside of it.

Use the `backdrop="{true|false}"` attribute where you can disable or enable the backdrop element.

### Enabled (default)

Use this example to enable the backdrop element by default.

```tsx
// index.tsx

"use client";

import {
  Button,
  Drawer,
  DrawerHeader,
  DrawerItems,
  Sidebar,
  SidebarItem,
  SidebarItemGroup,
  SidebarItems,
  TextInput,
} from "flowbite-react";
import { useState } from "react";
import {
  HiChartPie,
  HiClipboard,
  HiCollection,
  HiInformationCircle,
  HiLogin,
  HiPencil,
  HiSearch,
  HiShoppingBag,
  HiUsers,
} from "react-icons/hi";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show navigation</Button>
      </div>
      <Drawer open={isOpen} onClose={handleClose}>
        <DrawerHeader title="MENU" titleIcon={() => <></>} />
        <DrawerItems>
          <Sidebar
            aria-label="Sidebar with multi-level dropdown example"
            className="[&>div]:bg-transparent [&>div]:p-0"
          >
            <div className="flex h-full flex-col justify-between py-2">
              <div>
                <form className="pb-3 md:hidden">
                  <TextInput icon={HiSearch} type="search" placeholder="Search" required size={32} />
                </form>
                <SidebarItems>
                  <SidebarItemGroup>
                    <SidebarItem href="/" icon={HiChartPie}>
                      Dashboard
                    </SidebarItem>
                    <SidebarItem href="/e-commerce/products" icon={HiShoppingBag}>
                      Products
                    </SidebarItem>
                    <SidebarItem href="/users/list" icon={HiUsers}>
                      Users list
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-in" icon={HiLogin}>
                      Sign in
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-up" icon={HiPencil}>
                      Sign up
                    </SidebarItem>
                  </SidebarItemGroup>
                  <SidebarItemGroup>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/" icon={HiClipboard}>
                      Docs
                    </SidebarItem>
                    <SidebarItem href="https://flowbite-react.com/" icon={HiCollection}>
                      Components
                    </SidebarItem>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/issues" icon={HiInformationCircle}>
                      Help
                    </SidebarItem>
                  </SidebarItemGroup>
                </SidebarItems>
              </div>
            </div>
          </Sidebar>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

### Disabled

Use the `backdrop="false"` attribute to disable the backdrop element when the drawer is shown.

```tsx
// index.tsx

"use client";

import {
  Button,
  Drawer,
  DrawerHeader,
  DrawerItems,
  Sidebar,
  SidebarItem,
  SidebarItemGroup,
  SidebarItems,
  TextInput,
} from "flowbite-react";
import { useState } from "react";
import {
  HiChartPie,
  HiClipboard,
  HiCollection,
  HiInformationCircle,
  HiLogin,
  HiPencil,
  HiSearch,
  HiShoppingBag,
  HiUsers,
} from "react-icons/hi";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show navigation</Button>
      </div>
      <Drawer backdrop={false} open={isOpen} onClose={handleClose}>
        <DrawerHeader title="MENU" titleIcon={() => <></>} />
        <DrawerItems>
          <Sidebar
            aria-label="Sidebar with multi-level dropdown example"
            className="[&>div]:bg-transparent [&>div]:p-0"
          >
            <div className="flex h-full flex-col justify-between py-2">
              <div>
                <form className="pb-3 md:hidden">
                  <TextInput icon={HiSearch} type="search" placeholder="Search" required size={32} />
                </form>
                <SidebarItems>
                  <SidebarItemGroup>
                    <SidebarItem href="/" icon={HiChartPie}>
                      Dashboard
                    </SidebarItem>
                    <SidebarItem href="/e-commerce/products" icon={HiShoppingBag}>
                      Products
                    </SidebarItem>
                    <SidebarItem href="/users/list" icon={HiUsers}>
                      Users list
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-in" icon={HiLogin}>
                      Sign in
                    </SidebarItem>
                    <SidebarItem href="/authentication/sign-up" icon={HiPencil}>
                      Sign up
                    </SidebarItem>
                  </SidebarItemGroup>
                  <SidebarItemGroup>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/" icon={HiClipboard}>
                      Docs
                    </SidebarItem>
                    <SidebarItem href="https://flowbite-react.com/" icon={HiCollection}>
                      Components
                    </SidebarItem>
                    <SidebarItem href="https://github.com/themesberg/flowbite-react/issues" icon={HiInformationCircle}>
                      Help
                    </SidebarItem>
                  </SidebarItemGroup>
                </SidebarItems>
              </div>
            </div>
          </Sidebar>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

## Swipeable edge

The drawer edge functionality allows you to show a small part of the drawer when it is not shown completely by applying the `edge="{true|false}"` attribute, specifying the edge you'd like to set with, e.g., `theme={{ edge: "bottom-16" }}`, and adding `onClick={() => setIsOpen(!isOpen)}` to `<DrawerHeader/>`.

```tsx
// index.tsx

"use client";

import { Button, Drawer, DrawerHeader, DrawerItems } from "flowbite-react";
import { useState } from "react";
import { HiBars2, HiSquaresPlus } from "react-icons/hi2";

export function Component() {
  const [isOpen, setIsOpen] = useState(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <div className="flex min-h-[50vh] items-center justify-center">
        <Button onClick={() => setIsOpen(true)}>Show swipeable drawer</Button>
      </div>
      <Drawer edge open={isOpen} onClose={handleClose} position="bottom" className="p-0">
        <DrawerHeader
          closeIcon={HiBars2}
          title="Add widget"
          titleIcon={HiSquaresPlus}
          onClick={() => setIsOpen(!isOpen)}
          className="cursor-pointer px-4 pt-4 hover:bg-gray-50 dark:hover:bg-gray-700"
        />
        <DrawerItems className="p-4">
          <div className="grid grid-cols-3 gap-4 p-4 lg:grid-cols-4">
            <div className="cursor-pointer rounded-lg bg-gray-50 p-4 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600">
              <div className="mx-auto mb-2 flex h-[48px] max-h-[48px] w-[48px] max-w-[48px] items-center justify-center rounded-full bg-gray-200 p-2 dark:bg-gray-600">
                <svg
                  className="inline h-5 w-5 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 22 21"
                >
                  <path d="M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z" />
                  <path d="M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z" />
                </svg>
              </div>
              <div className="text-center font-medium text-gray-500 dark:text-gray-400">Chart</div>
            </div>
            <div className="cursor-pointer rounded-lg bg-gray-50 p-4 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600">
              <div className="mx-auto mb-2 flex h-[48px] max-h-[48px] w-[48px] max-w-[48px] items-center justify-center rounded-full bg-gray-200 p-2 dark:bg-gray-600">
                <svg
                  className="inline h-5 w-5 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 14"
                >
                  <path d="M18 0H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM9 6v2H2V6h7Zm2 0h7v2h-7V6Zm-9 4h7v2H2v-2Zm9 2v-2h7v2h-7Z" />
                </svg>
              </div>
              <div className="text-center font-medium text-gray-500 dark:text-gray-400">Table</div>
            </div>
            <div className="hidden cursor-pointer rounded-lg bg-gray-50 p-4 hover:bg-gray-100 lg:block dark:bg-gray-700 dark:hover:bg-gray-600">
              <div className="mx-auto mb-2 flex h-[48px] max-h-[48px] w-[48px] max-w-[48px] items-center justify-center rounded-full bg-gray-200 p-2 dark:bg-gray-600">
                <svg
                  className="inline h-5 w-5 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 14 20"
                >
                  <path d="M13.383.076a1 1 0 0 0-1.09.217L11 1.586 9.707.293a1 1 0 0 0-1.414 0L7 1.586 5.707.293a1 1 0 0 0-1.414 0L3 1.586 1.707.293A1 1 0 0 0 0 1v18a1 1 0 0 0 1.707.707L3 18.414l1.293 1.293a1 1 0 0 0 1.414 0L7 18.414l1.293 1.293a1 1 0 0 0 1.414 0L11 18.414l1.293 1.293A1 1 0 0 0 14 19V1a1 1 0 0 0-.617-.924ZM10 15H4a1 1 0 1 1 0-2h6a1 1 0 0 1 0 2Zm0-4H4a1 1 0 1 1 0-2h6a1 1 0 1 1 0 2Zm0-4H4a1 1 0 0 1 0-2h6a1 1 0 1 1 0 2Z" />
                </svg>
              </div>
              <div className="hidden text-center font-medium text-gray-500 dark:text-gray-400">Ticket</div>
            </div>
            <div className="cursor-pointer rounded-lg bg-gray-50 p-4 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600">
              <div className="mx-auto mb-2 flex h-[48px] max-h-[48px] w-[48px] max-w-[48px] items-center justify-center rounded-full bg-gray-200 p-2 dark:bg-gray-600">
                <svg
                  className="inline h-5 w-5 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 18 20"
                >
                  <path d="M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z" />
                </svg>
              </div>
              <div className="text-center font-medium text-gray-500 dark:text-gray-400">List</div>
            </div>
            <div className="cursor-pointer rounded-lg bg-gray-50 p-4 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600">
              <div className="mx-auto mb-2 flex h-[48px] max-h-[48px] w-[48px] max-w-[48px] items-center justify-center rounded-full bg-gray-200 p-2 dark:bg-gray-600">
                <svg
                  className="inline h-5 w-5 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 20 16"
                >
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M5 2a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1M2 5h12a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1Zm8 5a2 2 0 1 1-4 0 2 2 0 0 1 4 0Z"
                  />
                </svg>
              </div>
              <div className="text-center font-medium text-gray-500 dark:text-gray-400">Price</div>
            </div>
            <div className="cursor-pointer rounded-lg bg-gray-50 p-4 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600">
              <div className="mx-auto mb-2 flex h-[48px] max-h-[48px] w-[48px] max-w-[48px] items-center justify-center rounded-full bg-gray-200 p-2 dark:bg-gray-600">
                <svg
                  className="inline h-5 w-5 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 18"
                >
                  <path d="M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z" />
                </svg>
              </div>
              <div className="text-center font-medium text-gray-500 dark:text-gray-400">Users</div>
            </div>
            <div className="hidden cursor-pointer rounded-lg bg-gray-50 p-4 hover:bg-gray-100 lg:block dark:bg-gray-700 dark:hover:bg-gray-600">
              <div className="mx-auto mb-2 flex h-[48px] max-h-[48px] w-[48px] max-w-[48px] items-center justify-center rounded-full bg-gray-200 p-2 dark:bg-gray-600">
                <svg
                  className="inline h-5 w-5 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 18"
                >
                  <path d="M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9Zm-1.391 7.361.707-3.535a3 3 0 0 1 .82-1.533L7.929 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h4.259a2.975 2.975 0 0 1-.15-1.639ZM8.05 17.95a1 1 0 0 1-.981-1.2l.708-3.536a1 1 0 0 1 .274-.511l6.363-6.364a3.007 3.007 0 0 1 4.243 0 3.007 3.007 0 0 1 0 4.243l-6.365 6.363a1 1 0 0 1-.511.274l-3.536.708a1.07 1.07 0 0 1-.195.023Z" />
                </svg>
              </div>
              <div className="text-center font-medium text-gray-500 dark:text-gray-400">Task</div>
            </div>
            <div className="cursor-pointer rounded-lg bg-gray-50 p-4 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600">
              <div className="mx-auto mb-2 flex h-[48px] max-h-[48px] w-[48px] max-w-[48px] items-center justify-center rounded-full bg-gray-200 p-2 dark:bg-gray-600">
                <svg
                  className="inline h-5 w-5 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 20 20"
                >
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M4 12.25V1m0 11.25a2.25 2.25 0 0 0 0 4.5m0-4.5a2.25 2.25 0 0 1 0 4.5M4 19v-2.25m6-13.5V1m0 2.25a2.25 2.25 0 0 0 0 4.5m0-4.5a2.25 2.25 0 0 1 0 4.5M10 19V7.75m6 4.5V1m0 11.25a2.25 2.25 0 1 0 0 4.5 2.25 2.25 0 0 0 0-4.5ZM16 19v-2"
                  />
                </svg>
              </div>
              <div className="text-center font-medium text-gray-500 dark:text-gray-400">Custom</div>
            </div>
          </div>
        </DrawerItems>
      </Drawer>
    </>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "fixed z-40 overflow-y-auto bg-white p-4 transition-transform dark:bg-gray-800",
    "backdrop": "fixed inset-0 z-30 bg-gray-900/50 dark:bg-gray-900/80",
    "edge": "bottom-16",
    "position": {
      "top": {
        "on": "left-0 right-0 top-0 w-full transform-none",
        "off": "left-0 right-0 top-0 w-full -translate-y-full"
      },
      "right": {
        "on": "right-0 top-0 h-screen w-80 transform-none",
        "off": "right-0 top-0 h-screen w-80 translate-x-full"
      },
      "bottom": {
        "on": "bottom-0 left-0 right-0 w-full transform-none",
        "off": "bottom-0 left-0 right-0 w-full translate-y-full"
      },
      "left": {
        "on": "left-0 top-0 h-screen w-80 transform-none",
        "off": "left-0 top-0 h-screen w-80 -translate-x-full"
      }
    }
  },
  "header": {
    "inner": {
      "closeButton": "absolute end-2.5 top-2.5 flex h-8 w-8 items-center justify-center rounded-lg bg-transparent text-sm text-gray-400 hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-600 dark:hover:text-white",
      "closeIcon": "h-4 w-4",
      "titleCloseIcon": "sr-only",
      "titleIcon": "me-2.5 h-4 w-4",
      "titleText": "mb-4 inline-flex items-center text-base font-semibold text-gray-500 dark:text-gray-400"
    },
    "collapsed": {
      "on": "hidden",
      "off": "block"
    }
  },
  "items": {
    "base": ""
  }
}
```

## References

- [Flowbite Drawer](https://flowbite.com/docs/components/drawer/)


---

## Dropdown

# React Dropdown - Flowbite

> Use the dropdown component to trigger a list of menu items when clicking on an element such as a button or link based on multiple styles, sizes, and placements with React

The dropdown component is a UI element built with React that displays a list of items when a trigger element (e.g., a button) is clicked. You can use it to build dropdown menus, lists, and more.

The default styles are built using utility classes from Tailwind CSS. You can customize the behavior and positioning of the dropdowns using custom props from React.

To start using the component make sure that you have imported it from Flowbite React:

```jsx
import { Dropdown } from "flowbite-react";
```

## Default dropdown

Use this example to create a simple dropdown with a list of menu items by adding child `<DropdownItem>` components inside the main `<Dropdown>` component.

```tsx
// index.tsx

import { Dropdown, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <Dropdown label="Dropdown button" dismissOnClick={false}>
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownItem>Sign out</DropdownItem>
    </Dropdown>
  );
}
```

## Dropdown divider

Use the `<DropdownDivider>` component to add a divider between the dropdown items.

```tsx
// index.tsx

import { Dropdown, DropdownDivider, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <Dropdown label="Dropdown button">
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownDivider />
      <DropdownItem>Separated link</DropdownItem>
    </Dropdown>
  );
}
```

## Dropdown header

Use the `<DropdownHeader>` component to add a header to the dropdown. You can use this to add a user profile image and name, for example.

For more complex headers that include an `<input>` or `<TextInput>` control, set `enableTypeAhead` to `false` on the `<Dropdown>` to prevent keystrokes from being interpreted as item searches.

```tsx
// index.tsx

import { Dropdown, DropdownDivider, DropdownHeader, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <Dropdown label="Dropdown button">
      <DropdownHeader>
        <span className="block text-sm">Bonnie Green</span>
        <span className="block truncate text-sm font-medium">bonnie@flowbite.com</span>
      </DropdownHeader>
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownDivider />
      <DropdownItem>Sign out</DropdownItem>
    </Dropdown>
  );
}
```

## Dropdown items with icon

Add custom icons next to the menu items by using the `icon` prop on the `<DropdownItem>` component.

```tsx
// index.tsx

"use client";

import { Dropdown, DropdownDivider, DropdownHeader, DropdownItem } from "flowbite-react";
import { HiCog, HiCurrencyDollar, HiLogout, HiViewGrid } from "react-icons/hi";

export function Component() {
  return (
    <Dropdown label="Dropdown">
      <DropdownHeader>
        <span className="block text-sm">Bonnie Green</span>
        <span className="block truncate text-sm font-medium">bonnie@flowbite.com</span>
      </DropdownHeader>
      <DropdownItem icon={HiViewGrid}>Dashboard</DropdownItem>
      <DropdownItem icon={HiCog}>Settings</DropdownItem>
      <DropdownItem icon={HiCurrencyDollar}>Earnings</DropdownItem>
      <DropdownDivider />
      <DropdownItem icon={HiLogout}>Sign out</DropdownItem>
    </Dropdown>
  );
}
```

## Inline dropdown

Use the `inline` prop to make the dropdown appear inline with the trigger element.

```tsx
// index.tsx

import { Dropdown, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <Dropdown label="Dropdown" inline>
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownItem>Sign out</DropdownItem>
    </Dropdown>
  );
}
```

## Dropdown sizes

You can use the `size` prop to change the size of the dropdown. The default size is `md`.

```tsx
// index.tsx

import { Dropdown, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <div className="flex items-center gap-4">
      <Dropdown label="Small dropdown" size="sm">
        <DropdownItem>Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownItem>Sign out</DropdownItem>
      </Dropdown>
      <Dropdown label="Large dropdown" size="lg">
        <DropdownItem>Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownItem>Sign out</DropdownItem>
      </Dropdown>
    </div>
  );
}
```

## Placement options

Use the `placement` prop to change the placement of the dropdown by choosing one of the following options: `top`, `right`, `bottom` or `left`. If there is not enough space then the dropdown will be automatically repositioned.

```tsx
// index.tsx

import { Dropdown, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-4">
      <Dropdown label="Dropdown top" placement="top">
        <DropdownItem>Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownItem>Sign out</DropdownItem>
      </Dropdown>
      <Dropdown label="Dropdown right" placement="right">
        <DropdownItem>Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownItem>Sign out</DropdownItem>
      </Dropdown>
      <Dropdown label="Dropdown bottom" placement="bottom">
        <DropdownItem>Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownItem>Sign out</DropdownItem>
      </Dropdown>
      <Dropdown label="Dropdown left" placement="left">
        <DropdownItem>Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownItem>Sign out</DropdownItem>
      </Dropdown>
      <Dropdown label="Dropdown left start" placement="left-start">
        <DropdownItem>Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownItem>Sign out</DropdownItem>
      </Dropdown>
      <Dropdown label="Dropdown right start" placement="right-start">
        <DropdownItem>Dashboard</DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownItem>Sign out</DropdownItem>
      </Dropdown>
    </div>
  );
}
```

## Click event handler

Add a custom `onClick` event handler to the `<DropdownItem>` component to handle the click event.

```tsx
// index.tsx

"use client";

import { Dropdown, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <Dropdown label="Dropdown">
      <DropdownItem onClick={() => alert("Dashboard!")}>Dashboard</DropdownItem>
      <DropdownItem onClick={() => alert("Settings!")}>Settings</DropdownItem>
      <DropdownItem onClick={() => alert("Earnings!")}>Earnings</DropdownItem>
      <DropdownItem onClick={() => alert("Sign out!")}>Sign out</DropdownItem>
    </Dropdown>
  );
}
```

## Custom trigger

To customize the trigger element, you can use the `renderTrigger` property.

```tsx
// index.tsx

"use client";

import { Dropdown, DropdownItem } from "flowbite-react";

export function Component() {
  return (
    <Dropdown label="" dismissOnClick={false} renderTrigger={() => <span>My custom trigger</span>}>
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownItem>Sign out</DropdownItem>
    </Dropdown>
  );
}
```

## Custom item

To customize the `Dropdown.Item` base element you can use the `as` property.

```tsx
// index.tsx

import { Dropdown, DropdownItem } from "flowbite-react";
import Link from "next/link";

export function Component() {
  return (
    <Dropdown dismissOnClick={false} label="My custom item">
      <DropdownItem as={Link} href="#">
        Home
      </DropdownItem>
      <DropdownItem as="a" href="https://flowbite.com/" target="_blank">
        External link
      </DropdownItem>
    </Dropdown>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "arrowIcon": "ml-2 h-4 w-4",
  "content": "py-1 focus:outline-none",
  "floating": {
    "animation": "transition-opacity",
    "arrow": {
      "base": "absolute z-10 h-2 w-2 rotate-45",
      "style": {
        "dark": "bg-gray-900 dark:bg-gray-700",
        "light": "bg-white",
        "auto": "bg-white dark:bg-gray-700"
      },
      "placement": "-4px"
    },
    "base": "z-10 w-fit divide-y divide-gray-100 rounded shadow focus:outline-none",
    "content": "py-1 text-sm text-gray-700 dark:text-gray-200",
    "divider": "my-1 h-px bg-gray-100 dark:bg-gray-600",
    "header": "block px-4 py-2 text-sm text-gray-700 dark:text-gray-200",
    "hidden": "invisible opacity-0",
    "item": {
      "container": "",
      "base": "flex w-full cursor-pointer items-center justify-start px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:bg-gray-600 dark:focus:text-white",
      "icon": "mr-2 h-4 w-4"
    },
    "style": {
      "dark": "bg-gray-900 text-white dark:bg-gray-700",
      "light": "border border-gray-200 bg-white text-gray-900",
      "auto": "border border-gray-200 bg-white text-gray-900 dark:border-none dark:bg-gray-700 dark:text-white"
    },
    "target": "w-fit"
  },
  "inlineWrapper": "flex items-center"
}
```

## References

- [Flowbite Dropdown](https://flowbite.com/docs/components/dropdowns/)


---

## Footer

# React Footer - Flowbite

> Use the footer component at the end of your page to show content such as sitemap links, brand logo, social icons and more using React and Tailwind CSS

The footer component is an important section of a website where you should provide content such as sitemap links, copyright text, logo of your brand, social media account links, and more.

Get started with the examples from Flowbite React based on multiple styles, sizes, and colors by using React components and the utility classes from Tailwind CSS.

To start using the footer component you need to import it from `flowbite-react`:

```jsx
import { Footer } from "flowbite-react";
```

## Default footer

Use this example to create a simple and responsive footer component with copyright text and links by adding the `<FooterCopyright>` and `<FooterLink>` items inside the `<Footer>` component.

Use the `href` prop to add a link to the footer link item and the `year` prop to add the current year.

```tsx
// index.tsx

import { Footer, FooterCopyright, FooterLink, FooterLinkGroup } from "flowbite-react";

export function Component() {
  return (
    <Footer container>
      <FooterCopyright href="#" by="Flowbite™" year={2022} />
      <FooterLinkGroup>
        <FooterLink href="#">About</FooterLink>
        <FooterLink href="#">Privacy Policy</FooterLink>
        <FooterLink href="#">Licensing</FooterLink>
        <FooterLink href="#">Contact</FooterLink>
      </FooterLinkGroup>
    </Footer>
  );
}
```

## Footer with logo

Use the `<FooterBrand>` component to add a logo to the footer component.

```tsx
// index.tsx

import { Footer, FooterBrand, FooterCopyright, FooterDivider, FooterLink, FooterLinkGroup } from "flowbite-react";

export function Component() {
  return (
    <Footer container>
      <div className="w-full text-center">
        <div className="w-full justify-between sm:flex sm:items-center sm:justify-between">
          <FooterBrand
            href="https://flowbite.com"
            src="https://flowbite.com/docs/images/logo.svg"
            alt="Flowbite Logo"
            name="Flowbite"
          />
          <FooterLinkGroup>
            <FooterLink href="#">About</FooterLink>
            <FooterLink href="#">Privacy Policy</FooterLink>
            <FooterLink href="#">Licensing</FooterLink>
            <FooterLink href="#">Contact</FooterLink>
          </FooterLinkGroup>
        </div>
        <FooterDivider />
        <FooterCopyright href="#" by="Flowbite™" year={2022} />
      </div>
    </Footer>
  );
}
```

## Social media icons

Feature social media accounts by adding the `<FooterIcon>` component inside the `<Footer>` component.

```tsx
// index.tsx

"use client";

import {
  Footer,
  FooterBrand,
  FooterCopyright,
  FooterDivider,
  FooterIcon,
  FooterLink,
  FooterLinkGroup,
  FooterTitle,
} from "flowbite-react";
import { BsDribbble, BsFacebook, BsGithub, BsInstagram, BsTwitter } from "react-icons/bs";

export function Component() {
  return (
    <Footer container>
      <div className="w-full">
        <div className="grid w-full justify-between sm:flex sm:justify-between md:flex md:grid-cols-1">
          <div>
            <FooterBrand
              href="https://flowbite.com"
              src="https://flowbite.com/docs/images/logo.svg"
              alt="Flowbite Logo"
              name="Flowbite"
            />
          </div>
          <div className="grid grid-cols-2 gap-8 sm:mt-4 sm:grid-cols-3 sm:gap-6">
            <div>
              <FooterTitle title="about" />
              <FooterLinkGroup col>
                <FooterLink href="#">Flowbite</FooterLink>
                <FooterLink href="#">Tailwind CSS</FooterLink>
              </FooterLinkGroup>
            </div>
            <div>
              <FooterTitle title="Follow us" />
              <FooterLinkGroup col>
                <FooterLink href="#">Github</FooterLink>
                <FooterLink href="#">Discord</FooterLink>
              </FooterLinkGroup>
            </div>
            <div>
              <FooterTitle title="Legal" />
              <FooterLinkGroup col>
                <FooterLink href="#">Privacy Policy</FooterLink>
                <FooterLink href="#">Terms &amp; Conditions</FooterLink>
              </FooterLinkGroup>
            </div>
          </div>
        </div>
        <FooterDivider />
        <div className="w-full sm:flex sm:items-center sm:justify-between">
          <FooterCopyright href="#" by="Flowbite™" year={2022} />
          <div className="mt-4 flex space-x-6 sm:mt-0 sm:justify-center">
            <FooterIcon href="#" icon={BsFacebook} />
            <FooterIcon href="#" icon={BsInstagram} />
            <FooterIcon href="#" icon={BsTwitter} />
            <FooterIcon href="#" icon={BsGithub} />
            <FooterIcon href="#" icon={BsDribbble} />
          </div>
        </div>
      </div>
    </Footer>
  );
}
```

## Sitemap links

Add sitemap links to the footer component by using the `<FooterLinkGroup>` and `<FooterLink>` components. You can also use the `<FooterTitle>` component to add a title to the sitemap links and group links together.

```tsx
// index.tsx

"use client";

import { Footer, FooterCopyright, FooterIcon, FooterLink, FooterLinkGroup, FooterTitle } from "flowbite-react";
import { BsDribbble, BsFacebook, BsGithub, BsInstagram, BsTwitter } from "react-icons/bs";

export function Component() {
  return (
    <Footer bgDark>
      <div className="w-full">
        <div className="grid w-full grid-cols-2 gap-8 px-6 py-8 md:grid-cols-4">
          <div>
            <FooterTitle title="Company" />
            <FooterLinkGroup col>
              <FooterLink href="#">About</FooterLink>
              <FooterLink href="#">Careers</FooterLink>
              <FooterLink href="#">Brand Center</FooterLink>
              <FooterLink href="#">Blog</FooterLink>
            </FooterLinkGroup>
          </div>
          <div>
            <FooterTitle title="help center" />
            <FooterLinkGroup col>
              <FooterLink href="#">Discord Server</FooterLink>
              <FooterLink href="#">Twitter</FooterLink>
              <FooterLink href="#">Facebook</FooterLink>
              <FooterLink href="#">Contact Us</FooterLink>
            </FooterLinkGroup>
          </div>
          <div>
            <FooterTitle title="legal" />
            <FooterLinkGroup col>
              <FooterLink href="#">Privacy Policy</FooterLink>
              <FooterLink href="#">Licensing</FooterLink>
              <FooterLink href="#">Terms &amp; Conditions</FooterLink>
            </FooterLinkGroup>
          </div>
          <div>
            <FooterTitle title="download" />
            <FooterLinkGroup col>
              <FooterLink href="#">iOS</FooterLink>
              <FooterLink href="#">Android</FooterLink>
              <FooterLink href="#">Windows</FooterLink>
              <FooterLink href="#">MacOS</FooterLink>
            </FooterLinkGroup>
          </div>
        </div>
        <div className="w-full bg-gray-700 px-4 py-6 sm:flex sm:items-center sm:justify-between">
          <FooterCopyright href="#" by="Flowbite™" year={2022} />
          <div className="mt-4 flex space-x-6 sm:mt-0 sm:justify-center">
            <FooterIcon href="#" icon={BsFacebook} />
            <FooterIcon href="#" icon={BsInstagram} />
            <FooterIcon href="#" icon={BsTwitter} />
            <FooterIcon href="#" icon={BsGithub} />
            <FooterIcon href="#" icon={BsDribbble} />
          </div>
        </div>
      </div>
    </Footer>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "w-full rounded-lg bg-white shadow md:flex md:items-center md:justify-between dark:bg-gray-800",
    "container": "w-full p-6",
    "bgDark": "bg-gray-800"
  },
  "groupLink": {
    "base": "flex flex-wrap text-sm text-gray-500 dark:text-white",
    "link": {
      "base": "me-4 last:mr-0 md:mr-6",
      "href": "hover:underline"
    },
    "col": "flex-col space-y-4"
  },
  "icon": {
    "base": "text-gray-500 dark:hover:text-white",
    "size": "h-5 w-5"
  },
  "title": {
    "base": "mb-6 text-sm font-semibold uppercase text-gray-500 dark:text-white"
  },
  "divider": {
    "base": "my-6 w-full border-gray-200 sm:mx-auto lg:my-8 dark:border-gray-700"
  },
  "copyright": {
    "base": "text-sm text-gray-500 sm:text-center dark:text-gray-400",
    "href": "ml-1 hover:underline",
    "span": "ml-1"
  },
  "brand": {
    "base": "mb-4 flex items-center sm:mb-0",
    "img": "mr-3 h-8",
    "span": "self-center whitespace-nowrap text-2xl font-semibold text-gray-800 dark:text-white"
  }
}
```

## References

- [Flowbite Footer](https://flowbite.com/docs/components/footer/)


---

## Forms

# React Forms - Flowbite

> Use the forms elements from Flowbite React to start receiving user input data based on input elements, checkboxes, radio buttons, file uploads based on multiple sizes, colors, and styles

The form elements from Flowbite React can help you to collect input data from your website visitors by using input field elements, checkboxes, radios, file upload elements, and more based on React and Tailwind CSS.

These components can be used to create form submission pages, authentication features for your users and you can use the elements together with other components from Flowbite React such as with modals, cards, and more.

Check out the form elements from Flowbite React on this page and customize the value and options using the React props API and customize the styles using Tailwind CSS.

Make sure that you import the appropiate components from the `flowbite-react` library:

```jsx
// only import what you want to use
import {
  Button,
  Checkbox,
  FileInput,
  Label,
  Radio,
  RangeSlider,
  Select,
  Textarea,
  TextInput,
  ToggleSwitch,
} from "flowbite-react";
```

## Default form

Use this example of a form component with `<TextInput>`, `<Checkbox>`, `<Label>` and `<Button>` elements to create a basic user authentication form and access the value of the component by accessing the `value` attribute.

```tsx
// index.tsx

import { Button, Checkbox, Label, TextInput } from "flowbite-react";

export function Component() {
  return (
    <form className="flex max-w-md flex-col gap-4">
      <div>
        <div className="mb-2 block">
          <Label htmlFor="email1">Your email</Label>
        </div>
        <TextInput id="email1" type="email" placeholder="name@flowbite.com" required />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password1">Your password</Label>
        </div>
        <TextInput id="password1" type="password" required />
      </div>
      <div className="flex items-center gap-2">
        <Checkbox id="remember" />
        <Label htmlFor="remember">Remember me</Label>
      </div>
      <Button type="submit">Submit</Button>
    </form>
  );
}
```

## Input sizing

Use the `sizing` prop on the `<TextInput>` form component from React to set the size of the input fields. You can choose from the `sm`, `md`, and `lg` size options.

```tsx
// index.tsx

import { Label, TextInput } from "flowbite-react";

export function Component() {
  return (
    <div className="flex max-w-md flex-col gap-4">
      <div>
        <div className="mb-2 block">
          <Label htmlFor="small">Small input</Label>
        </div>
        <TextInput id="small" type="text" sizing="sm" />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="base">Base input</Label>
        </div>
        <TextInput id="base" type="text" sizing="md" />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="large">Large input</Label>
        </div>
        <TextInput id="large" type="text" sizing="lg" />
      </div>
    </div>
  );
}
```

## Disabled inputs

Disable the input fields by passing the `disabled` and `readOnly` props to the `<TextInput>` React component.

```tsx
// index.tsx

import { Label, TextInput } from "flowbite-react";

export function Component() {
  return (
    <div className="flex max-w-md flex-col gap-4">
      <Label htmlFor="disabledInput1">API token</Label>
      <TextInput type="text" id="disabledInput1" placeholder="Disabled input" disabled />
      <Label htmlFor="disabledInput2">Personal access token</Label>
      <TextInput type="text" id="disabledInput2" placeholder="Disabled readonly input" disabled readOnly />
    </div>
  );
}
```

## Inputs with shadow

Pass the `shadow` prop to the form components from React to automatically add a shadow style.

```tsx
// index.tsx

import { Button, Checkbox, Label, TextInput } from "flowbite-react";
import Link from "next/link";

export function Component() {
  return (
    <form className="flex max-w-md flex-col gap-4">
      <div>
        <div className="mb-2 block">
          <Label htmlFor="email2">Your email</Label>
        </div>
        <TextInput id="email2" type="email" placeholder="name@flowbite.com" required shadow />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password2">Your password</Label>
        </div>
        <TextInput id="password2" type="password" required shadow />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="repeat-password">Repeat password</Label>
        </div>
        <TextInput id="repeat-password" type="password" required shadow />
      </div>
      <div className="flex items-center gap-2">
        <Checkbox id="agree" />
        <Label htmlFor="agree" className="flex">
          I agree with the&nbsp;
          <Link href="#" className="text-cyan-600 hover:underline dark:text-cyan-500">
            terms and conditions
          </Link>
        </Label>
      </div>
      <Button type="submit">Register new account</Button>
    </form>
  );
}
```

## Form helper text

Show a helper and descriptive text next to the input field to improve UI/UX when submitting forms.

```tsx
// index.tsx

import { HelperText, Label, TextInput } from "flowbite-react";

export function Component() {
  return (
    <div className="max-w-md">
      <div className="mb-2 block">
        <Label htmlFor="email3">Your email</Label>
      </div>
      <TextInput id="email3" type="email" placeholder="name@flowbite.com" required />
      <HelperText>
        We’ll never share your details. Read our
        <a href="#" className="ml-1 font-medium text-cyan-600 hover:underline dark:text-cyan-500">
          Privacy Policy
        </a>
        .
      </HelperText>
    </div>
  );
}
```

## Input groups with icon

Use this example to show an icon inside the input component by passing the `icon` prop.

```tsx
// index.tsx

"use client";

import { Label, TextInput } from "flowbite-react";
import { HiMail } from "react-icons/hi";

export function Component() {
  return (
    <div className="max-w-md">
      <div className="mb-2 block">
        <Label htmlFor="email4">Your email</Label>
      </div>
      <TextInput id="email4" type="email" icon={HiMail} placeholder="name@flowbite.com" required />
    </div>
  );
}
```

Show the icon on the right side of the input element by passing the `rightIcon` property.

```tsx
// index.tsx

"use client";

import { Label, TextInput } from "flowbite-react";
import { HiMail } from "react-icons/hi";

export function Component() {
  return (
    <div className="max-w-md">
      <div className="mb-2 block">
        <Label htmlFor="email4">Your email</Label>
      </div>
      <TextInput id="email4" type="email" rightIcon={HiMail} placeholder="name@flowbite.com" required />
    </div>
  );
}
```

Show an icon both on the left and right side of the component by passing both the `icon` and `rightIcon` props to the input field component from React.

```tsx
// index.tsx

"use client";

import { Label, TextInput } from "flowbite-react";
import { HiMail } from "react-icons/hi";

export function Component() {
  return (
    <div className="max-w-md">
      <div className="mb-2 block">
        <Label htmlFor="email4">Your email</Label>
      </div>
      <TextInput id="email4" type="email" icon={HiMail} rightIcon={HiMail} placeholder="name@flowbite.com" required />
    </div>
  );
}
```

Use this example to show an input element with an alternatively style for showing icons.

```tsx
// index.tsx

import { Label, TextInput } from "flowbite-react";

export function Component() {
  return (
    <div className="max-w-md">
      <div className="mb-2 block">
        <Label htmlFor="username3">Username</Label>
      </div>
      <TextInput id="username3" placeholder="Bonnie Green" addon="@" required />
    </div>
  );
}
```

## Form validation

Show form validation for success and error messages by using the `color` prop on the input field element and label components.

```tsx
// index.tsx

import { HelperText, Label, TextInput } from "flowbite-react";

export function Component() {
  return (
    <div className="flex max-w-md flex-col gap-4">
      <div>
        <div className="mb-2 block">
          <Label htmlFor="username3" color="success">
            Your name
          </Label>
        </div>
        <TextInput id="username" placeholder="Bonnie Green" required color="success" />
        <HelperText>
          <span className="font-medium">Alright!</span> Username available!
        </HelperText>
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="username4" color="failure">
            Your name
          </Label>
        </div>
        <TextInput id="username4" placeholder="Bonnie Green" required color="failure" />
        <HelperText>
          <span className="font-medium">Oops!</span> Username already taken!
        </HelperText>
      </div>
    </div>
  );
}
```

## Input element colors

Update the color of the form elements by passing the `color` props to the input field components from React.

```tsx
// index.tsx

import { Label, TextInput } from "flowbite-react";

export function Component() {
  return (
    <div className="flex max-w-md flex-col gap-4">
      <div>
        <div className="mb-2 block">
          <Label htmlFor="input-gray" color="gray">
            Gray
          </Label>
        </div>
        <TextInput id="input-gray" placeholder="Input Gray" required color="gray" />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="input-info" color="info">
            Info
          </Label>
        </div>
        <TextInput id="input-info" placeholder="Input Info" required color="info" />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="input-success" color="success">
            Success
          </Label>
        </div>
        <TextInput id="input-success" placeholder="Input Success" required color="success" />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="input-failure" color="failure">
            Failure
          </Label>
        </div>
        <TextInput id="input-failure" placeholder="Input Failure" required color="failure" />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="input-warning" color="warning">
            Warning
          </Label>
        </div>
        <TextInput id="input-warning" placeholder="Input Warning" required color="warning" />
      </div>
    </div>
  );
}
```

## Textarea element

Use this example to show a textarea component in React and receive longer text from your users.

```tsx
// index.tsx

import { Label, Textarea } from "flowbite-react";

export function Component() {
  return (
    <div className="max-w-md">
      <div className="mb-2 block">
        <Label htmlFor="comment">Your message</Label>
      </div>
      <Textarea id="comment" placeholder="Leave a comment..." required rows={4} />
    </div>
  );
}
```

## Select input

This component can be used to allow users to select from multiple options based on the `<Select>` component.

```tsx
// index.tsx

import { Label, Select } from "flowbite-react";

export function Component() {
  return (
    <div className="max-w-md">
      <div className="mb-2 block">
        <Label htmlFor="countries">Select your country</Label>
      </div>
      <Select id="countries" required>
        <option>United States</option>
        <option>Canada</option>
        <option>France</option>
        <option>Germany</option>
      </Select>
    </div>
  );
}
```

## Checkbox

Use this example to show a list of options to your users that they can choose from by using the `<Checkbox> component.`

```tsx
// index.tsx

import { Checkbox, Label } from "flowbite-react";

export function Component() {
  return (
    <div className="flex max-w-md flex-col gap-4" id="checkbox">
      <div className="flex items-center gap-2">
        <Checkbox id="accept" defaultChecked />
        <Label htmlFor="accept" className="flex">
          I agree with the&nbsp;
          <a href="#" className="text-cyan-600 hover:underline dark:text-cyan-500">
            terms and conditions
          </a>
        </Label>
      </div>
      <div className="flex items-center gap-2">
        <Checkbox id="promotion" />
        <Label htmlFor="promotion">I want to get promotional offers</Label>
      </div>
      <div className="flex items-center gap-2">
        <Checkbox id="age" />
        <Label htmlFor="age">I am 18 years or older</Label>
      </div>
      <div className="flex gap-2">
        <div className="flex h-5 items-center">
          <Checkbox id="shipping" />
        </div>
        <div className="flex flex-col">
          <Label htmlFor="shipping">Free shipping via Flowbite</Label>
          <div className="text-gray-500 dark:text-gray-300">
            <span className="text-xs font-normal">
              For orders shipped from Flowbite from <span className="font-medium">€ 25</span> in books or&nbsp;
              <span>€ 29</span> on other categories
            </span>
          </div>
        </div>
      </div>
      <div className="flex items-center gap-2">
        <Checkbox id="disabled" disabled />
        <Label htmlFor="disabled" disabled>
          Eligible for international shipping (disabled)
        </Label>
      </div>
    </div>
  );
}
```

## Radio button

Ask your users to choose only one value from multiple options based on the `<Radio>` component from React.

```tsx
// index.tsx

import { Label, Radio } from "flowbite-react";

export function Component() {
  return (
    <div className="flex max-w-md flex-col gap-4">
      <div className="flex items-center gap-2">
        <Radio id="united-state" name="countries" value="USA" defaultChecked />
        <Label htmlFor="united-state">United States</Label>
      </div>
      <div className="flex items-center gap-2">
        <Radio id="germany" name="countries" value="Germany" />
        <Label htmlFor="germany">Germany</Label>
      </div>
      <div className="flex items-center gap-2">
        <Radio id="spain" name="countries" value="Spain" />
        <Label htmlFor="spain">Spain</Label>
      </div>
      <div className="flex items-center gap-2">
        <Radio id="uk" name="countries" value="United Kingdom" />
        <Label htmlFor="uk">United Kingdom</Label>
      </div>
      <div className="flex items-center gap-2">
        <Radio id="china" name="countries" value="China" disabled />
        <Label htmlFor="china" disabled>
          China (disabled)
        </Label>
      </div>
    </div>
  );
}
```

## File upload

Use the `<FileInput>` component to allow users to upload files from their browser.

```tsx
// index.tsx

import { FileInput, HelperText, Label } from "flowbite-react";

export function Component() {
  return (
    <div id="fileUpload" className="max-w-md">
      <Label className="mb-2 block" htmlFor="file">
        Upload file
      </Label>
      <FileInput id="file" />
      <HelperText className="mt-1">A profile picture is useful to confirm your are logged into your account</HelperText>
    </div>
  );
}
```

## Toggle switch

Use the `<ToggleSwitch>` component to ask users to enable or disable an option such as newsletter settings.

```tsx
// index.tsx

"use client";

import { ToggleSwitch } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [switch1, setSwitch1] = useState(false);
  const [switch2, setSwitch2] = useState(true);
  const [switch3, setSwitch3] = useState(true);

  return (
    <div className="flex max-w-md flex-col items-start gap-4">
      <ToggleSwitch checked={switch1} label="Toggle me" onChange={setSwitch1} />
      <ToggleSwitch checked={switch2} label="Toggle me (checked)" onChange={setSwitch2} />
      <ToggleSwitch checked={false} disabled label="Toggle me (disabled)" onChange={() => undefined} />
      <ToggleSwitch checked={true} disabled label="Toggle me (disabled)" onChange={() => undefined} />
      <ToggleSwitch checked={switch3} onChange={setSwitch3} />
    </div>
  );
}
```

## Range slider

The `<RangeSlider>` component can be used to allow users to select a number based on a minimum and maximum value.

```tsx
// index.tsx

import { Label, RangeSlider } from "flowbite-react";

export function Component() {
  return (
    <div className="flex max-w-md flex-col gap-4">
      <div>
        <div className="mb-1 block">
          <Label htmlFor="default-range">Default</Label>
        </div>
        <RangeSlider id="default-range" />
      </div>
      <div>
        <div className="mb-1 block">
          <Label htmlFor="disbaled-range">Disabled</Label>
        </div>
        <RangeSlider id="disabled-range" disabled />
      </div>
      <div>
        <div className="mb-1 block">
          <Label htmlFor="sm-range">Small</Label>
        </div>
        <RangeSlider id="sm-range" sizing="sm" />
      </div>
      <div>
        <div className="mb-1 block">
          <Label htmlFor="md-range">Medium</Label>
        </div>
        <RangeSlider id="md-range" sizing="md" />
      </div>
      <div>
        <div className="mb-1 block">
          <Label htmlFor="lg-range">Large</Label>
        </div>
        <RangeSlider id="lg-range" sizing="lg" />
      </div>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

### File input theme

```json
{
  "base": "block w-full cursor-pointer rounded-lg border file:-ms-4 file:me-4 file:cursor-pointer file:border-none file:bg-gray-800 file:py-2.5 file:pe-4 file:ps-8 file:text-sm file:font-medium file:leading-[inherit] file:text-white hover:file:bg-gray-700 focus:outline-none focus:ring-1 dark:file:bg-gray-600 dark:hover:file:bg-gray-500",
  "sizes": {
    "sm": "text-xs",
    "md": "text-sm",
    "lg": "text-lg"
  },
  "colors": {
    "gray": "border-gray-300 bg-gray-50 text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-400 dark:placeholder-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500",
    "info": "border-cyan-500 bg-cyan-50 text-cyan-900 placeholder-cyan-700 focus:border-cyan-500 focus:ring-cyan-500 dark:border-cyan-400 dark:bg-cyan-100 dark:focus:border-cyan-500 dark:focus:ring-cyan-500",
    "failure": "border-red-500 bg-red-50 text-red-900 placeholder-red-700 focus:border-red-500 focus:ring-red-500 dark:border-red-400 dark:bg-red-100 dark:focus:border-red-500 dark:focus:ring-red-500",
    "warning": "border-yellow-500 bg-yellow-50 text-yellow-900 placeholder-yellow-700 focus:border-yellow-500 focus:ring-yellow-500 dark:border-yellow-400 dark:bg-yellow-100 dark:focus:border-yellow-500 dark:focus:ring-yellow-500",
    "success": "border-green-500 bg-green-50 text-green-900 placeholder-green-700 focus:border-green-500 focus:ring-green-500 dark:border-green-400 dark:bg-green-100 dark:focus:border-green-500 dark:focus:ring-green-500"
  }
}
```

### Label theme

```json
{
  "root": {
    "base": "text-sm font-medium",
    "disabled": "opacity-50",
    "colors": {
      "default": "text-gray-900 dark:text-white",
      "info": "text-cyan-500 dark:text-cyan-600",
      "failure": "text-red-700 dark:text-red-500",
      "warning": "text-yellow-500 dark:text-yellow-600",
      "success": "text-green-700 dark:text-green-500"
    }
  }
}
```

### Radio button theme

```json
{
  "base": "h-4 w-4 appearance-none rounded-full border border-gray-300 bg-gray-100 bg-[length:1em_1em] bg-center bg-no-repeat checked:border-transparent checked:bg-current checked:bg-dot-icon focus:outline-none focus:ring-2 focus:ring-offset-2 dark:border-gray-600 dark:bg-gray-700 dark:checked:border-transparent dark:checked:bg-current",
  "color": {
    "default": "text-primary-600 focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-primary-600",
    "dark": "text-gray-800 focus:ring-gray-800 dark:ring-offset-gray-800 dark:focus:ring-gray-800",
    "failure": "text-red-900 focus:ring-red-900 dark:ring-offset-red-900 dark:focus:ring-red-900",
    "gray": "text-gray-900 focus:ring-gray-900 dark:ring-offset-gray-900 dark:focus:ring-gray-900",
    "info": "text-cyan-800 focus:ring-cyan-800 dark:ring-offset-gray-800 dark:focus:ring-cyan-800",
    "light": "text-gray-900 focus:ring-gray-900 dark:ring-offset-gray-900 dark:focus:ring-gray-900",
    "purple": "text-purple-600 focus:ring-purple-600 dark:ring-offset-purple-600 dark:focus:ring-purple-600",
    "success": "text-green-800 focus:ring-green-800 dark:ring-offset-green-800 dark:focus:ring-green-800",
    "warning": "text-yellow-400 focus:ring-yellow-400 dark:ring-offset-yellow-400 dark:focus:ring-yellow-400",
    "blue": "text-blue-700 focus:ring-blue-600 dark:ring-offset-blue-700 dark:focus:ring-blue-700",
    "cyan": "text-cyan-600 focus:ring-cyan-600 dark:ring-offset-cyan-600 dark:focus:ring-cyan-600",
    "green": "text-green-600 focus:ring-green-600 dark:ring-offset-green-600 dark:focus:ring-green-600",
    "indigo": "text-indigo-700 focus:ring-indigo-700 dark:ring-offset-indigo-700 dark:focus:ring-indigo-700",
    "lime": "text-lime-700 focus:ring-lime-700 dark:ring-offset-lime-700 dark:focus:ring-lime-700",
    "pink": "text-pink-600 focus:ring-pink-600 dark:ring-offset-pink-600 dark:focus:ring-pink-600",
    "red": "text-red-600 focus:ring-red-600 dark:ring-offset-red-600 dark:focus:ring-red-600",
    "teal": "text-teal-600 focus:ring-teal-600 dark:ring-offset-teal-600 dark:focus:ring-teal-600",
    "yellow": "text-yellow-400 focus:ring-yellow-400 dark:ring-offset-yellow-400 dark:focus:ring-yellow-400"
  }
}
```

### Range slider theme

```json
{
  "root": {
    "base": "flex"
  },
  "field": {
    "base": "relative w-full",
    "input": {
      "base": "w-full cursor-pointer appearance-none rounded-lg bg-gray-200 dark:bg-gray-700",
      "sizes": {
        "sm": "h-1",
        "md": "h-2",
        "lg": "h-3"
      }
    }
  }
}
```

### Text input theme

```json
{
  "base": "flex",
  "addon": "inline-flex items-center rounded-l-md border border-r-0 border-gray-300 bg-gray-200 px-3 text-sm text-gray-900 dark:border-gray-600 dark:bg-gray-600 dark:text-gray-400",
  "field": {
    "base": "relative w-full",
    "icon": {
      "base": "pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3",
      "svg": "h-5 w-5 text-gray-500 dark:text-gray-400"
    },
    "rightIcon": {
      "base": "pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3",
      "svg": "h-5 w-5 text-gray-500 dark:text-gray-400"
    },
    "input": {
      "base": "block w-full border focus:outline-none focus:ring-1 disabled:cursor-not-allowed disabled:opacity-50",
      "sizes": {
        "sm": "p-2 sm:text-xs",
        "md": "p-2.5 text-sm",
        "lg": "p-4 sm:text-base"
      },
      "colors": {
        "gray": "border-gray-300 bg-gray-50 text-gray-900 placeholder-gray-500 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500",
        "info": "border-cyan-500 bg-cyan-50 text-cyan-900 placeholder-cyan-700 focus:border-cyan-500 focus:ring-cyan-500 dark:border-cyan-400 dark:bg-cyan-100 dark:focus:border-cyan-500 dark:focus:ring-cyan-500",
        "failure": "border-red-500 bg-red-50 text-red-900 placeholder-red-700 focus:border-red-500 focus:ring-red-500 dark:border-red-400 dark:bg-red-100 dark:focus:border-red-500 dark:focus:ring-red-500",
        "warning": "border-yellow-500 bg-yellow-50 text-yellow-900 placeholder-yellow-700 focus:border-yellow-500 focus:ring-yellow-500 dark:border-yellow-400 dark:bg-yellow-100 dark:focus:border-yellow-500 dark:focus:ring-yellow-500",
        "success": "border-green-500 bg-green-50 text-green-900 placeholder-green-700 focus:border-green-500 focus:ring-green-500 dark:border-green-400 dark:bg-green-100 dark:focus:border-green-500 dark:focus:ring-green-500"
      },
      "withRightIcon": {
        "on": "pr-10",
        "off": ""
      },
      "withIcon": {
        "on": "pl-10",
        "off": ""
      },
      "withAddon": {
        "on": "rounded-r-lg",
        "off": "rounded-lg"
      },
      "withShadow": {
        "on": "shadow-sm dark:shadow-sm-light",
        "off": ""
      }
    }
  }
}
```

### Textarea theme

```json
{
  "base": "block w-full rounded-lg border p-2.5 text-sm focus:outline-none focus:ring-1 disabled:cursor-not-allowed disabled:opacity-50",
  "colors": {
    "gray": "border-gray-300 bg-gray-50 text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500",
    "info": "border-cyan-500 bg-cyan-50 text-cyan-900 placeholder-cyan-700 focus:border-cyan-500 focus:ring-cyan-500 dark:border-cyan-400 dark:bg-cyan-100 dark:focus:border-cyan-500 dark:focus:ring-cyan-500",
    "failure": "border-red-500 bg-red-50 text-red-900 placeholder-red-700 focus:border-red-500 focus:ring-red-500 dark:border-red-400 dark:bg-red-100 dark:focus:border-red-500 dark:focus:ring-red-500",
    "warning": "border-yellow-500 bg-yellow-50 text-yellow-900 placeholder-yellow-700 focus:border-yellow-500 focus:ring-yellow-500 dark:border-yellow-400 dark:bg-yellow-100 dark:focus:border-yellow-500 dark:focus:ring-yellow-500",
    "success": "border-green-500 bg-green-50 text-green-900 placeholder-green-700 focus:border-green-500 focus:ring-green-500 dark:border-green-400 dark:bg-green-100 dark:focus:border-green-500 dark:focus:ring-green-500"
  },
  "withShadow": {
    "on": "shadow-sm dark:shadow-sm-light",
    "off": ""
  }
}
```

### Toggle switch theme

```json
{
  "root": {
    "base": "group flex rounded-lg focus:outline-none",
    "active": {
      "on": "cursor-pointer",
      "off": "cursor-not-allowed opacity-50"
    },
    "label": "ms-3 mt-0.5 text-start text-sm font-medium text-gray-900 dark:text-gray-300",
    "input": "sr-only"
  },
  "toggle": {
    "base": "relative rounded-full after:absolute after:rounded-full after:border after:bg-white after:transition-all group-focus:ring-4",
    "checked": {
      "on": "after:translate-x-full after:border-transparent rtl:after:-translate-x-full",
      "off": "bg-gray-200 after:border-gray-300 dark:bg-gray-700",
      "color": {
        "default": "bg-primary-700 group-focus:ring-primary-300 dark:group-focus:ring-primary-800",
        "blue": "bg-blue-700 group-focus:ring-blue-300 dark:group-focus:ring-blue-800",
        "dark": "bg-gray-700 group-focus:ring-gray-300 dark:group-focus:ring-gray-800",
        "failure": "bg-red-700 group-focus:ring-red-300 dark:group-focus:ring-red-800",
        "gray": "bg-gray-500 group-focus:ring-gray-300 dark:group-focus:ring-gray-800",
        "green": "bg-green-600 group-focus:ring-green-300 dark:group-focus:ring-green-800",
        "light": "bg-gray-300 group-focus:ring-gray-300 dark:group-focus:ring-gray-800",
        "red": "bg-red-700 group-focus:ring-red-300 dark:group-focus:ring-red-800",
        "purple": "bg-purple-700 group-focus:ring-purple-300 dark:group-focus:ring-purple-800",
        "success": "bg-green-500 group-focus:ring-green-300 dark:group-focus:ring-green-800",
        "yellow": "bg-yellow-400 group-focus:ring-yellow-300 dark:group-focus:ring-yellow-800",
        "warning": "bg-yellow-600 group-focus:ring-yellow-300 dark:group-focus:ring-yellow-800",
        "cyan": "bg-cyan-500 group-focus:ring-cyan-300 dark:group-focus:ring-cyan-800",
        "lime": "bg-lime-400 group-focus:ring-lime-300 dark:group-focus:ring-lime-800",
        "indigo": "bg-indigo-400 group-focus:ring-indigo-300 dark:group-focus:ring-indigo-800",
        "teal": "bg-teal-400 group-focus:ring-teal-300 dark:group-focus:ring-teal-800",
        "info": "bg-cyan-600 group-focus:ring-cyan-300 dark:group-focus:ring-cyan-800",
        "pink": "bg-pink-600 group-focus:ring-pink-300 dark:group-focus:ring-pink-800"
      }
    },
    "sizes": {
      "sm": "h-5 w-9 min-w-9 after:left-0.5 after:top-0.5 after:h-4 after:w-4 rtl:after:right-0.5",
      "md": "h-6 w-11 min-w-11 after:left-0.5 after:top-0.5 after:h-5 after:w-5 rtl:after:right-0.5",
      "lg": "h-7 w-[52px] min-w-[52px] after:left-0.5 after:top-0.5 after:h-6 after:w-6 rtl:after:right-0.5"
    }
  }
}
```

### Checkbox theme

```json
{
  "base": "h-4 w-4 appearance-none rounded border border-gray-300 bg-gray-100 bg-[length:0.55em_0.55em] bg-center bg-no-repeat checked:border-transparent checked:bg-current checked:bg-check-icon focus:outline-none focus:ring-2 focus:ring-offset-2 dark:border-gray-600 dark:bg-gray-700 dark:checked:border-transparent dark:checked:bg-current",
  "color": {
    "default": "text-primary-600 focus:ring-primary-600 dark:ring-offset-gray-800 dark:focus:ring-primary-600",
    "dark": "text-gray-800 focus:ring-gray-800 dark:ring-offset-gray-800 dark:focus:ring-gray-800",
    "failure": "text-red-900 focus:ring-red-900 dark:ring-offset-red-900 dark:focus:ring-red-900",
    "gray": "text-gray-900 focus:ring-gray-900 dark:ring-offset-gray-900 dark:focus:ring-gray-900",
    "info": "text-cyan-800 focus:ring-cyan-800 dark:ring-offset-gray-800 dark:focus:ring-cyan-800",
    "light": "text-gray-900 focus:ring-gray-900 dark:ring-offset-gray-900 dark:focus:ring-gray-900",
    "purple": "text-purple-600 focus:ring-purple-600 dark:ring-offset-purple-600 dark:focus:ring-purple-600",
    "success": "text-green-800 focus:ring-green-800 dark:ring-offset-green-800 dark:focus:ring-green-800",
    "warning": "text-yellow-400 focus:ring-yellow-400 dark:ring-offset-yellow-400 dark:focus:ring-yellow-400",
    "blue": "text-blue-700 focus:ring-blue-600 dark:ring-offset-blue-700 dark:focus:ring-blue-700",
    "cyan": "text-cyan-600 focus:ring-cyan-600 dark:ring-offset-cyan-600 dark:focus:ring-cyan-600",
    "green": "text-green-600 focus:ring-green-600 dark:ring-offset-green-600 dark:focus:ring-green-600",
    "indigo": "text-indigo-700 focus:ring-indigo-700 dark:ring-offset-indigo-700 dark:focus:ring-indigo-700",
    "lime": "text-lime-700 focus:ring-lime-700 dark:ring-offset-lime-700 dark:focus:ring-lime-700",
    "pink": "text-pink-600 focus:ring-pink-600 dark:ring-offset-pink-600 dark:focus:ring-pink-600",
    "red": "text-red-600 focus:ring-red-600 dark:ring-offset-red-600 dark:focus:ring-red-600",
    "teal": "text-teal-600 focus:ring-teal-600 dark:ring-offset-teal-600 dark:focus:ring-teal-600",
    "yellow": "text-yellow-400 focus:ring-yellow-400 dark:ring-offset-yellow-400 dark:focus:ring-yellow-400"
  },
  "indeterminate": "border-transparent bg-current bg-dash-icon dark:border-transparent dark:bg-current"
}
```

## References

- [Flowbite Forms](https://flowbite.com/docs/components/forms/)


---

## KBD

# React KBD (Keyboard) - Flowbite

> Use the KBD component as an inline element to denote textual user input from the keyboard inside paragraphs, tables, and other components

The KBD (Keyboard) component can be used to indicate a textual user input from the keyboard inside other elements such as in text, tables, cards, and more.

Use the semantic `<Kbd>` keyboard input tag to use the default monospace font which is best suited for representing input keys.

To start using the `<Kbd>` component you need to import it from `flowbite-react`:

```jsx
import { Kbd } from "flowbite-react";
```

## Default KBD

Here's a list of KBD components that you can use inside any other element.

```tsx
// index.tsx

import { Kbd } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-1">
      <Kbd>Shift</Kbd>
      <Kbd>Ctrl</Kbd>
      <Kbd>Tab</Kbd>
      <Kbd>Caps Lock</Kbd>
      <Kbd>Esc</Kbd>
      <Kbd>Spacebar</Kbd>
      <Kbd>Enter</Kbd>
    </div>
  );
}
```

## KBD inside text

Use this example by nesting an inline KBD component inside a paragraph.

```tsx
// index.tsx

import { Kbd } from "flowbite-react";

export function Component() {
  return (
    <>
      Please press <Kbd>Ctrl</Kbd> + <Kbd>Shift</Kbd> + <Kbd>R</Kbd> to re-render an MDN page.
    </>
  );
}
```

## KBD inside table

The KBD component can also be used inside table components to denote what type of key can be pressed for certain descriptions.

```tsx
// index.tsx

"use client";

import { Kbd, Table, TableBody, TableCell, TableHead, TableHeadCell, TableRow } from "flowbite-react";
import { MdKeyboardArrowDown, MdKeyboardArrowLeft, MdKeyboardArrowRight, MdKeyboardArrowUp } from "react-icons/md";

export function Component() {
  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableHeadCell>Key</TableHeadCell>
          <TableHeadCell>Description</TableHeadCell>
        </TableRow>
      </TableHead>
      <TableBody className="divide-y">
        <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
          <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
            <Kbd>Shift</Kbd> <span>or</span> <Kbd>Tab</Kbd>
          </TableCell>
          <TableCell>Navigate to interactive elements</TableCell>
        </TableRow>
        <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
          <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
            <Kbd>Enter</Kbd> or <Kbd>Spacebar</Kbd>
          </TableCell>
          <TableCell>Ensure elements with ARIA role="button" can be activated with both key commands.</TableCell>
        </TableRow>
        <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
          <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
            <span className="inline-flex gap-1">
              <Kbd icon={MdKeyboardArrowUp} />
              <Kbd icon={MdKeyboardArrowDown} />
            </span>
            <span> or </span>
            <span className="inline-flex gap-1">
              <Kbd icon={MdKeyboardArrowLeft} />
              <Kbd icon={MdKeyboardArrowRight} />
            </span>
          </TableCell>
          <TableCell>Choose and activate previous/next tab.</TableCell>
        </TableRow>
      </TableBody>
    </Table>
  );
}
```

## Arrow keys

Use this example to show arrow keys inside the KBD styled element.

```tsx
// index.tsx

"use client";

import { Kbd } from "flowbite-react";
import { MdKeyboardArrowDown, MdKeyboardArrowLeft, MdKeyboardArrowRight, MdKeyboardArrowUp } from "react-icons/md";

export function Component() {
  return (
    <div className="flex flex-wrap gap-1">
      <Kbd icon={MdKeyboardArrowUp} />
      <Kbd icon={MdKeyboardArrowDown} />
      <Kbd icon={MdKeyboardArrowLeft} />
      <Kbd icon={MdKeyboardArrowRight} />
    </div>
  );
}
```

## Letter Keys

Use this example to show arrow keys inside the KBD styled element.

```tsx
// index.tsx

import { Kbd } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-1">
      <Kbd>Q</Kbd>
      <Kbd>W</Kbd>
      <Kbd>E</Kbd>
      <Kbd>R</Kbd>
      <Kbd>T</Kbd>
      <Kbd>Y</Kbd>
      <Kbd>I</Kbd>
      <Kbd>O</Kbd>
      <Kbd>P</Kbd>
      <Kbd>A</Kbd>
      <Kbd>S</Kbd>
      <Kbd>D</Kbd>
      <Kbd>F</Kbd>
      <Kbd>G</Kbd>
      <Kbd>H</Kbd>
      <Kbd>J</Kbd>
      <Kbd>K</Kbd>
      <Kbd>L</Kbd>
      <Kbd>Z</Kbd>
      <Kbd>X</Kbd>
      <Kbd>C</Kbd>
      <Kbd>V</Kbd>
      <Kbd>B</Kbd>
      <Kbd>N</Kbd>
      <Kbd>M</Kbd>
    </div>
  );
}
```

## Number Keys

Use this example to show a key inside a KBD component from the english numeral system.

```tsx
// index.tsx

import { Kbd } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-1">
      <Kbd>1</Kbd>
      <Kbd>2</Kbd>
      <Kbd>3</Kbd>
      <Kbd>4</Kbd>
      <Kbd>5</Kbd>
      <Kbd>6</Kbd>
      <Kbd>7</Kbd>
      <Kbd>8</Kbd>
      <Kbd>9</Kbd>
      <Kbd>0</Kbd>
    </div>
  );
}
```

## Function keys

This example can be used to denote function keys inside the KBD component.

```tsx
// index.tsx

import { Kbd } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-1">
      <Kbd>F1</Kbd>
      <Kbd>F2</Kbd>
      <Kbd>F3</Kbd>
      <Kbd>F4</Kbd>
      <Kbd>F5</Kbd>
      <Kbd>F6</Kbd>
      <Kbd>F7</Kbd>
      <Kbd>F8</Kbd>
      <Kbd>F9</Kbd>
      <Kbd>F10</Kbd>
      <Kbd>F11</Kbd>
      <Kbd>F12</Kbd>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "rounded-lg border border-gray-200 bg-gray-100 px-2 py-1.5 text-xs font-semibold text-gray-800 dark:border-gray-500 dark:bg-gray-600 dark:text-gray-100",
    "icon": "inline-block"
  }
}
```

## References

- [Flowbite Kbd](https://flowbite.com/docs/components/kbd/)


---

## List group

# React List Group - Flowbite

> Use the list group component to display a series of items, buttons or links inside a single element

The list group component can be used to show a list of items inside of an unordered list for website navigation, show a list of items inside of a card, and more.

You can choose from one of the examples below based on various styles and options and you can customize the component with React props and the classes from Tailwind CSS.

Start using the list group component by first importing it from Flowbite React:

```jsx
import { ListGroup } from "flowbite-react";
```

## Default list group

Use the default example to create a simple list of items inside of a menu by using the `ListGroup` component with `ListGroupItem` child components inside of it.

```tsx
// index.tsx

import { ListGroup, ListGroupItem } from "flowbite-react";

export function Component() {
  return (
    <div className="flex justify-center">
      <ListGroup className="w-48">
        <ListGroupItem>Profile</ListGroupItem>
        <ListGroupItem>Settings</ListGroupItem>
        <ListGroupItem>Messages</ListGroupItem>
        <ListGroupItem disabled>Download</ListGroupItem>
      </ListGroup>
    </div>
  );
}
```

## List items as links

Convert the list items into links by adding the `href` prop to the `ListGroupItem` component.

```tsx
// index.tsx

import { ListGroup, ListGroupItem } from "flowbite-react";

export function Component() {
  return (
    <div className="flex justify-center">
      <ListGroup className="w-48">
        <ListGroupItem href="#" active>
          Profile
        </ListGroupItem>
        <ListGroupItem href="#">Settings</ListGroupItem>
        <ListGroupItem href="#">Messages</ListGroupItem>
        <ListGroupItem href="#">Download</ListGroupItem>
      </ListGroup>
    </div>
  );
}
```

## List group with buttons

To create custom actions inside of the list group, use the `onClick` prop on the `ListGroupItem` component.

```tsx
// index.tsx

"use client";

import { ListGroup, ListGroupItem } from "flowbite-react";

export function Component() {
  return (
    <div className="flex justify-center">
      <ListGroup className="w-48">
        <ListGroupItem onClick={() => alert("Profile clicked!")} active>
          Profile
        </ListGroupItem>
        <ListGroupItem>Settings</ListGroupItem>
        <ListGroupItem>Messages</ListGroupItem>
        <ListGroupItem>Download</ListGroupItem>
      </ListGroup>
    </div>
  );
}
```

## List group with icons

Add icons to the list group items by using the `icon` prop on the `ListGroupItem` component.

```tsx
// index.tsx

"use client";

import { ListGroup, ListGroupItem } from "flowbite-react";
import { HiCloudDownload, HiInbox, HiOutlineAdjustments, HiUserCircle } from "react-icons/hi";

export function Component() {
  return (
    <div className="flex justify-center">
      <ListGroup className="w-48">
        <ListGroupItem icon={HiUserCircle} active>
          Profile
        </ListGroupItem>
        <ListGroupItem icon={HiOutlineAdjustments}>Settings</ListGroupItem>
        <ListGroupItem icon={HiInbox}>Messages</ListGroupItem>
        <ListGroupItem icon={HiCloudDownload}>Download</ListGroupItem>
      </ListGroup>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "list-none rounded-lg border border-gray-200 bg-white text-left text-sm font-medium text-gray-900 dark:border-gray-600 dark:bg-gray-700 dark:text-white"
  },
  "item": {
    "base": "[&>*]:first:rounded-t-lg [&>*]:last:rounded-b-lg [&>*]:last:border-b-0",
    "link": {
      "base": "flex w-full items-center border-b border-gray-200 px-4 py-2 dark:border-gray-600",
      "active": {
        "off": "hover:bg-gray-100 hover:text-cyan-700 focus:text-cyan-700 focus:outline-none focus:ring-2 focus:ring-cyan-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:text-white dark:focus:ring-gray-500",
        "on": "bg-cyan-700 text-white dark:bg-gray-800"
      },
      "disabled": {
        "off": "",
        "on": "cursor-not-allowed bg-gray-100 text-gray-900 hover:bg-gray-100 hover:text-gray-900 focus:text-gray-900"
      },
      "href": {
        "off": "",
        "on": ""
      },
      "icon": "mr-2 h-4 w-4 fill-current"
    }
  }
}
```

## References

- [Flowbite List Group](https://flowbite.com/docs/components/list-group/)


---

## Mega menu

# React Mega Menu - Flowbite

> Use the mega menu component as a full-width dropdown inside the navbar to show a list of menu items based on multiple sizes, variants, and styles.

The mega menu component is a full-width dropdown that can be triggered by clicking on the menu item and it shows a list of links that you can use to navigate through the pages on a website.

To start using the mega menu component you need to import it from `flowbite-react`:

```jsx
import { MegaMenu } from "flowbite-react";
```

## Default mega menu

Use this example to show a list of links aligned on three columns inside the mega menu dropdown.

```tsx
// index.tsx

import {
  Button,
  MegaMenu,
  MegaMenuDropdown,
  NavbarBrand,
  NavbarCollapse,
  NavbarLink,
  NavbarToggle,
} from "flowbite-react";

function Component() {
  return (
    <MegaMenu>
      <NavbarBrand href="/">
        <img alt="" src="/favicon.svg" className="mr-3 h-6 sm:h-9" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite</span>
      </NavbarBrand>
      <div className="order-2 hidden items-center md:flex">
        <a
          href="#"
          className="mr-1 rounded-lg px-4 py-2 text-sm font-medium text-gray-800 hover:bg-gray-50 focus:outline-none focus:ring-4 focus:ring-gray-300 md:mr-2 md:px-5 md:py-2.5 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-800"
        >
          Login
        </a>
        <Button href="#">Sign up</Button>
      </div>
      <NavbarToggle />
      <NavbarCollapse>
        <NavbarLink href="#">Home</NavbarLink>
        <NavbarLink>
          <MegaMenuDropdown toggle={<>Company</>}>
            <ul className="grid grid-cols-3">
              <div className="space-y-4 p-4">
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    About Us
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Library
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Resources
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Pro Version
                  </a>
                </li>
              </div>
              <div className="space-y-4 p-4">
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Contact Us
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Support Center
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Terms
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Blog
                  </a>
                </li>
              </div>
              <div className="space-y-4 p-4">
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Newsletter
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    Playground
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-primary-600 dark:hover:text-primary-500">
                    License
                  </a>
                </li>
              </div>
            </ul>
          </MegaMenuDropdown>
        </NavbarLink>
        <NavbarLink href="#">Team</NavbarLink>
        <NavbarLink href="#">Contact</NavbarLink>
      </NavbarCollapse>
    </MegaMenu>
  );
}
```

## Mega menu with icons

This example of a mega menu dropdown can be used to also show an icon near the text of the link.

```tsx
// index.tsx

import {
  Button,
  MegaMenu,
  MegaMenuDropdown,
  NavbarBrand,
  NavbarCollapse,
  NavbarLink,
  NavbarToggle,
} from "flowbite-react";

function Component() {
  return (
    <MegaMenu>
      <NavbarBrand href="/">
        <img alt="" src="/favicon.svg" className="mr-3 h-6 sm:h-9" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite</span>
      </NavbarBrand>
      <div className="order-2 hidden items-center md:flex">
        <a
          href="#"
          className="mr-1 rounded-lg px-4 py-2 text-sm font-medium text-gray-800 hover:bg-gray-50 focus:outline-none focus:ring-4 focus:ring-gray-300 md:mr-2 md:px-5 md:py-2.5 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-800"
        >
          Login
        </a>
        <Button href="#">Sign up</Button>
      </div>
      <NavbarToggle />
      <NavbarCollapse>
        <NavbarLink href="#">Home</NavbarLink>
        <MegaMenuDropdown toggle={<>Company</>}>
          <ul className="grid grid-cols-3">
            <div className="space-y-4 p-4">
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                  </svg>
                  About Us
                </a>
              </li>
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path d="m1.56 6.245 8 3.924a1 1 0 0 0 .88 0l8-3.924a1 1 0 0 0 0-1.8l-8-3.925a1 1 0 0 0-.88 0l-8 3.925a1 1 0 0 0 0 1.8Z" />
                    <path d="M18 8.376a1 1 0 0 0-1 1v.163l-7 3.434-7-3.434v-.163a1 1 0 0 0-2 0v.786a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.786a1 1 0 0 0-1-1Z" />
                    <path d="M17.993 13.191a1 1 0 0 0-1 1v.163l-7 3.435-7-3.435v-.163a1 1 0 1 0-2 0v.787a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.787a1 1 0 0 0-1-1Z" />
                  </svg>
                  Library
                </a>
              </li>
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 18 18"
                  >
                    <path d="M15.977.783A1 1 0 0 0 15 0H3a1 1 0 0 0-.977.783L.2 9h4.239a2.99 2.99 0 0 1 2.742 1.8 1.977 1.977 0 0 0 3.638 0A2.99 2.99 0 0 1 13.561 9H17.8L15.977.783ZM6 2h6a1 1 0 1 1 0 2H6a1 1 0 0 1 0-2Zm7 5H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Z" />
                    <path d="M1 18h16a1 1 0 0 0 1-1v-6h-4.439a.99.99 0 0 0-.908.6 3.978 3.978 0 0 1-7.306 0 .99.99 0 0 0-.908-.6H0v6a1 1 0 0 0 1 1Z" />
                  </svg>
                  Resources
                </a>
              </li>
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path d="m7.164 3.805-4.475.38L.327 6.546a1.114 1.114 0 0 0 .63 1.89l3.2.375 3.007-5.006ZM11.092 15.9l.472 3.14a1.114 1.114 0 0 0 1.89.63l2.36-2.362.38-4.475-5.102 3.067Zm8.617-14.283A1.613 1.613 0 0 0 18.383.291c-1.913-.33-5.811-.736-7.556 1.01-1.98 1.98-6.172 9.491-7.477 11.869a1.1 1.1 0 0 0 .193 1.316l.986.985.985.986a1.1 1.1 0 0 0 1.316.193c2.378-1.3 9.889-5.5 11.869-7.477 1.746-1.745 1.34-5.643 1.01-7.556Zm-3.873 6.268a2.63 2.63 0 1 1-3.72-3.72 2.63 2.63 0 0 1 3.72 3.72Z" />
                  </svg>
                  Pro Version
                </a>
              </li>
            </div>
            <div className="space-y-4 p-4">
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path d="M19 4h-1a1 1 0 1 0 0 2v11a1 1 0 0 1-2 0V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3V5a1 1 0 0 0-1-1ZM3 4a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4Zm9 13H4a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-3H4a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-3H4a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-3h-2a1 1 0 0 1 0-2h2a1 1 0 1 1 0 2Zm0-3h-2a1 1 0 0 1 0-2h2a1 1 0 1 1 0 2Z" />
                    <path d="M6 5H5v1h1V5Z" />
                  </svg>
                  Blog
                </a>
              </li>
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                  >
                    <path d="m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z" />
                  </svg>
                  Newsletter
                </a>
              </li>
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 18 18"
                  >
                    <path d="M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10ZM17 13h-2v-2a1 1 0 0 0-2 0v2h-2a1 1 0 0 0 0 2h2v2a1 1 0 0 0 2 0v-2h2a1 1 0 0 0 0-2Z" />
                  </svg>
                  Playground
                </a>
              </li>
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 14 20"
                  >
                    <path d="M13.383.076a1 1 0 0 0-1.09.217L11 1.586 9.707.293a1 1 0 0 0-1.414 0L7 1.586 5.707.293a1 1 0 0 0-1.414 0L3 1.586 1.707.293A1 1 0 0 0 0 1v18a1 1 0 0 0 1.707.707L3 18.414l1.293 1.293a1 1 0 0 0 1.414 0L7 18.414l1.293 1.293a1 1 0 0 0 1.414 0L11 18.414l1.293 1.293A1 1 0 0 0 14 19V1a1 1 0 0 0-.617-.924ZM10 15H4a1 1 0 1 1 0-2h6a1 1 0 0 1 0 2Zm0-4H4a1 1 0 1 1 0-2h6a1 1 0 1 1 0 2Zm0-4H4a1 1 0 0 1 0-2h6a1 1 0 1 1 0 2Z" />
                  </svg>
                  License
                </a>
              </li>
            </div>
            <div className="space-y-4 p-4">
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 14 20"
                  >
                    <path d="M12 0H2a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM7.5 17.5h-1a1 1 0 0 1 0-2h1a1 1 0 0 1 0 2ZM12 13H2V4h10v9Z" />
                  </svg>
                  Contact Us
                </a>
              </li>
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 21 21"
                  >
                    <path d="m5.4 2.736 3.429 3.429A5.046 5.046 0 0 1 10.134 6c.356.01.71.06 1.056.147l3.41-3.412c.136-.133.287-.248.45-.344A9.889 9.889 0 0 0 10.269 1c-1.87-.041-3.713.44-5.322 1.392a2.3 2.3 0 0 1 .454.344Zm11.45 1.54-.126-.127a.5.5 0 0 0-.706 0l-2.932 2.932c.029.023.049.054.078.077.236.194.454.41.65.645.034.038.078.067.11.107l2.927-2.927a.5.5 0 0 0 0-.707Zm-2.931 9.81c-.024.03-.057.052-.081.082a4.963 4.963 0 0 1-.633.639c-.041.036-.072.083-.115.117l2.927 2.927a.5.5 0 0 0 .707 0l.127-.127a.5.5 0 0 0 0-.707l-2.932-2.931Zm-1.442-4.763a3.036 3.036 0 0 0-1.383-1.1l-.012-.007a2.955 2.955 0 0 0-1-.213H10a2.964 2.964 0 0 0-2.122.893c-.285.29-.509.634-.657 1.013l-.01.016a2.96 2.96 0 0 0-.21 1 2.99 2.99 0 0 0 .489 1.716c.009.014.022.026.032.04a3.04 3.04 0 0 0 1.384 1.1l.012.007c.318.129.657.2 1 .213.392.015.784-.05 1.15-.192.012-.005.02-.013.033-.018a3.011 3.011 0 0 0 1.676-1.7v-.007a2.89 2.89 0 0 0 0-2.207 2.868 2.868 0 0 0-.27-.515c-.007-.012-.02-.025-.03-.039Zm6.137-3.373a2.53 2.53 0 0 1-.35.447L14.84 9.823c.112.428.166.869.16 1.311-.01.356-.06.709-.147 1.054l3.413 3.412c.132.134.249.283.347.444A9.88 9.88 0 0 0 20 11.269a9.912 9.912 0 0 0-1.386-5.319ZM14.6 19.264l-3.421-3.421c-.385.1-.781.152-1.18.157h-.134c-.356-.01-.71-.06-1.056-.147l-3.41 3.412a2.503 2.503 0 0 1-.443.347A9.884 9.884 0 0 0 9.732 21H10a9.9 9.9 0 0 0 5.044-1.388 2.519 2.519 0 0 1-.444-.348ZM1.735 15.6l3.426-3.426a4.608 4.608 0 0 1-.013-2.367L1.735 6.4a2.507 2.507 0 0 1-.35-.447 9.889 9.889 0 0 0 0 10.1c.1-.164.217-.316.35-.453Zm5.101-.758a4.957 4.957 0 0 1-.651-.645c-.033-.038-.077-.067-.11-.107L3.15 17.017a.5.5 0 0 0 0 .707l.127.127a.5.5 0 0 0 .706 0l2.932-2.933c-.03-.018-.05-.053-.078-.076ZM6.08 7.914c.03-.037.07-.063.1-.1.183-.22.384-.423.6-.609.047-.04.082-.092.129-.13L3.983 4.149a.5.5 0 0 0-.707 0l-.127.127a.5.5 0 0 0 0 .707L6.08 7.914Z" />
                  </svg>
                  Support Center
                </a>
              </li>
              <li>
                <a href="#" className="group flex items-center hover:text-primary-600 dark:hover:text-primary-500">
                  <svg
                    className="me-2 h-3 w-3 text-gray-400 group-hover:text-primary-600 dark:text-gray-500 dark:group-hover:text-primary-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="currentColor"
                    viewBox="0 0 18 20"
                  >
                    <path d="M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z" />
                  </svg>
                  Terms
                </a>
              </li>
            </div>
          </ul>
        </MegaMenuDropdown>
        <NavbarLink href="#">Team</NavbarLink>
      </NavbarCollapse>
    </MegaMenu>
  );
}
```

## Full width dropdown

Use this example to show a mega menu dropdown that spans the entire width of the document page.

```tsx
// index.tsx

import {
  MegaMenu,
  MegaMenuDropdown,
  MegaMenuDropdownToggle,
  NavbarBrand,
  NavbarCollapse,
  NavbarLink,
  NavbarToggle,
} from "flowbite-react";
import { HiChevronDown } from "react-icons/hi";

function Component() {
  return (
    <MegaMenu>
      <NavbarBrand href="/">
        <img alt="" src="/favicon.svg" className="mr-3 h-6 sm:h-9" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite</span>
      </NavbarBrand>
      <NavbarToggle />
      <NavbarCollapse>
        <NavbarLink href="/">Home</NavbarLink>
        <NavbarLink as="span">
          <MegaMenuDropdownToggle>
            Company
            <HiChevronDown className="ml-2" />
          </MegaMenuDropdownToggle>
        </NavbarLink>
        <NavbarLink href="/">Marketplace</NavbarLink>
        <NavbarLink href="/">Resources</NavbarLink>
        <NavbarLink href="/">Contact</NavbarLink>
      </NavbarCollapse>
      <MegaMenuDropdown>
        <ul className="mx-auto mt-6 grid max-w-screen-xl border-y border-gray-200 px-2 py-5 shadow-sm sm:grid-cols-2 md:grid-cols-3 dark:border-gray-600 dark:bg-gray-800 dark:text-white">
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Online Stores</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Segmentation</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Marketing CRM</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Online Stores</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Segmentation</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Marketing CRM</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Audience Management</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Creative Tools</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
          <li>
            <a href="#" className="block rounded-lg p-3 hover:bg-gray-50 dark:hover:bg-gray-700">
              <div className="font-semibold">Marketing Automation</div>
              <span className="text-sm text-gray-500 dark:text-gray-400">
                Connect with third-party tools that you're already using.
              </span>
            </a>
          </li>
        </ul>
      </MegaMenuDropdown>
    </MegaMenu>
  );
}
```

## Full width with CTA

This example can be used to also show a CTA button or link next to the menu items inside the dropdown.

```tsx
// index.tsx

import {
  MegaMenu,
  MegaMenuDropdown,
  MegaMenuDropdownToggle,
  NavbarBrand,
  NavbarCollapse,
  NavbarLink,
  NavbarToggle,
} from "flowbite-react";
import { HiArrowRight, HiChevronDown } from "react-icons/hi";

function Component() {
  return (
    <MegaMenu>
      <NavbarBrand href="/">
        <img alt="" src="/favicon.svg" className="mr-3 h-6 sm:h-9" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite</span>
      </NavbarBrand>
      <NavbarToggle />
      <NavbarCollapse>
        <NavbarLink href="/">Home</NavbarLink>
        <MegaMenuDropdownToggle>
          Company
          <HiChevronDown className="ml-2" />
        </MegaMenuDropdownToggle>
        <NavbarLink href="/">Marketplace</NavbarLink>
        <NavbarLink href="/">Resources</NavbarLink>
        <NavbarLink href="/">Contact</NavbarLink>
      </NavbarCollapse>
      <MegaMenuDropdown>
        <div className="mx-auto mt-6 grid max-w-screen-xl border-y border-gray-200 px-2 py-5 text-sm shadow-sm sm:grid-cols-2 md:grid-cols-3 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400">
          <ul className="space-y-4 sm:mb-4 md:mb-0">
            <li>
              <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                Online Stores
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                Segmentation
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                Marketing CRM
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                Online Stores
              </a>
            </li>
          </ul>
          <ul className="mb-4 hidden space-y-4 sm:block md:mb-0">
            <li>
              <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                Our Blog
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                Terms & Conditions
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                License
              </a>
            </li>
            <li>
              <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                Resources
              </a>
            </li>
          </ul>
          <div className="mt-4 md:mt-0">
            <h2 className="mb-2 font-semibold text-gray-900 dark:text-white">Our brands</h2>
            <p className="mb-2 text-gray-500 dark:text-gray-400">
              At Flowbite, we have a portfolio of brands that cater to a variety of preferences.
            </p>
            <a
              href="#"
              className="inline-flex items-center text-sm font-medium text-primary-600 hover:text-primary-600 dark:text-primary-500 dark:hover:text-primary-700"
            >
              Explore our brands
              <span className="sr-only">Explore our brands</span>
              <HiArrowRight className="ml-2" />
            </a>
          </div>
        </div>
      </MegaMenuDropdown>
    </MegaMenu>
  );
}
```

## Full width with image

This example can be used to also show a CTA with a background image inside the dropdown next to the other menu items and links.

```tsx
// index.tsx

import {
  MegaMenu,
  MegaMenuDropdown,
  MegaMenuDropdownToggle,
  NavbarBrand,
  NavbarCollapse,
  NavbarLink,
  NavbarToggle,
} from "flowbite-react";
import { HiArrowRight, HiChevronDown } from "react-icons/hi";

function Component() {
  return (
    <MegaMenu>
      <NavbarBrand href="#">
        <img alt="" src="/favicon.svg" className="mr-3 h-6 sm:h-9" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite</span>
      </NavbarBrand>
      <NavbarToggle />
      <NavbarCollapse>
        <NavbarLink href="#">Home</NavbarLink>
        <MegaMenuDropdownToggle>
          Company
          <HiChevronDown className="ml-2" />
        </MegaMenuDropdownToggle>
        <NavbarLink href="#">Marketplace</NavbarLink>
        <NavbarLink href="#">Resources</NavbarLink>
        <NavbarLink href="#">Contact</NavbarLink>
      </NavbarCollapse>
      <MegaMenuDropdown>
        <div className="mt-6 border-y border-gray-200 bg-white shadow-sm dark:border-gray-600 dark:bg-gray-800">
          <div className="mx-auto grid max-w-screen-xl px-4 py-5 text-sm text-gray-500 md:grid-cols-3 md:px-6 dark:text-gray-400">
            <ul className="mb-4 hidden space-y-4 md:mb-0 md:block" aria-labelledby="mega-menu-full-image-button">
              <li>
                <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                  Online Stores
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                  Segmentation
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                  Marketing CRM
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                  Online Stores
                </a>
              </li>
            </ul>
            <ul className="mb-4 space-y-4 md:mb-0">
              <li>
                <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                  Our Blog
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                  Terms & Conditions
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                  License
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-primary-600 hover:underline dark:hover:text-primary-500">
                  Resources
                </a>
              </li>
            </ul>
            <a
              href="#"
              className="rounded-lg bg-gray-500 bg-cover bg-local bg-center bg-no-repeat p-8 text-left bg-blend-multiply hover:bg-blend-soft-light dark:hover:bg-blend-darken"
              style={{
                backgroundImage: 'url("/dashboard-overview.png")',
              }}
            >
              <p className="mb-5 max-w-xl font-extrabold leading-tight tracking-tight text-white">
                Preview the new Flowbite dashboard navigation.
              </p>
              <button
                type="button"
                className="inline-flex items-center rounded-lg border border-white px-2.5 py-1.5 text-center text-xs font-medium text-white hover:bg-white hover:text-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-700"
              >
                Get started
                <HiArrowRight className="ml-2" />
              </button>
            </a>
          </div>
        </div>
      </MegaMenuDropdown>
    </MegaMenu>
  );
}
```

## Theme

Note:

- `<MegaMenu>`'s theme has all of the same options as [`<Navbar>`](https://flowbite-react.com/docs/components/navbar.md)'s, with slightly different defaults
- `<MegaMenuDropdown toggle={..} />`'s theme, `megaMenu.dropdown.toggle`, is identical to [`<Dropdown>`](https://flowbite-react.com/docs/components/dropdown.md), with slightly different defaults

```json
{
  "root": {
    "base": "bg-white px-2 py-2.5 sm:px-4 dark:border-gray-700 dark:bg-gray-800",
    "rounded": {
      "on": "rounded",
      "off": ""
    },
    "bordered": {
      "on": "border",
      "off": ""
    },
    "inner": {
      "base": "mx-auto flex flex-wrap items-center justify-between",
      "fluid": {
        "on": "",
        "off": "container"
      }
    }
  },
  "brand": {
    "base": "flex items-center"
  },
  "collapse": {
    "base": "w-full md:block md:w-auto",
    "list": "mt-4 flex flex-col md:mt-0 md:flex-row md:space-x-8 md:text-sm md:font-medium",
    "hidden": {
      "on": "hidden",
      "off": ""
    }
  },
  "link": {
    "base": "block py-2 pl-3 pr-4 md:p-0",
    "active": {
      "on": "bg-primary-700 text-white md:bg-transparent md:text-primary-700 dark:text-white",
      "off": "border-b border-gray-100 text-gray-700 hover:bg-gray-50 md:border-0 md:hover:bg-transparent md:hover:text-primary-700 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent md:dark:hover:text-white"
    },
    "disabled": {
      "on": "text-gray-400 hover:cursor-not-allowed dark:text-gray-600",
      "off": ""
    }
  },
  "toggle": {
    "base": "inline-flex items-center rounded-lg p-2 text-sm text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 md:hidden dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600",
    "icon": "h-6 w-6 shrink-0",
    "title": "sr-only"
  },
  "dropdown": {
    "base": "",
    "toggle": {
      "arrowIcon": "ml-2 h-4 w-4",
      "content": "py-1 focus:outline-none",
      "floating": {
        "animation": "transition-opacity",
        "arrow": {
          "base": "absolute z-10 h-2 w-2 rotate-45",
          "style": {
            "dark": "bg-gray-900 dark:bg-gray-700",
            "light": "bg-white",
            "auto": "bg-white dark:bg-gray-700"
          },
          "placement": "-4px"
        },
        "base": "z-10 w-fit divide-y divide-gray-100 rounded shadow focus:outline-none mt-2 block",
        "content": "py-1 text-sm text-gray-500 dark:text-gray-400",
        "divider": "my-1 h-px bg-gray-100 dark:bg-gray-600",
        "header": "block px-4 py-2 text-sm text-gray-700 dark:text-gray-200",
        "hidden": "invisible opacity-0",
        "item": {
          "container": "",
          "base": "flex w-full cursor-pointer items-center justify-start px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none dark:text-gray-200 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:bg-gray-600 dark:focus:text-white",
          "icon": "mr-2 h-4 w-4"
        },
        "style": {
          "dark": "bg-gray-900 text-white dark:bg-gray-700",
          "light": "border border-gray-200 bg-white text-gray-900",
          "auto": "border border-gray-200 bg-white dark:border-none dark:bg-gray-700 text-gray-500 dark:text-gray-400"
        },
        "target": "w-fit"
      },
      "inlineWrapper": "flex w-full items-center justify-between"
    }
  },
  "dropdownToggle": {
    "base": "py-2 pl-3 pr-4 md:p-0 border-b border-gray-100 text-gray-700 hover:bg-gray-50 md:border-0 md:hover:bg-transparent md:hover:text-primary-700 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent md:dark:hover:text-white flex w-full items-center justify-between"
  }
}
```

## References

- [Flowbite Mega Menu](https://flowbite.com/docs/components/mega-menu/)


---

## Modal

# React Modal - Flowbite

> Use the modal component to show an interactive dialog to your website users that overlays the main content based on multiple sizes, layouts, and styles

The modal component can be used to show any type of content such as text, form elements, and notifications to your website visitors by creating an off-canvas box on top of the main content area of your website.

You can choose from multiple examples based on various styles, layouts, and elements inside the modal component and you can customize the behaviour, placement, and sizing using our custom React props and the utility classes from Tailwind CSS.

To get started with the modal component you first need to import it from Flowbite React:

```jsx
import { Modal } from "flowbite-react";
```

## Default modal

Use the `<Modal>` React component to show a dialog element to the user with a header, body, and footer where you can add any type of content such as text or form elements.

The visibility of the component can be set by passing a boolean value to the `show` prop on the `<Modal>` component and we recommend you to do this via the React state.

Using a `openModal` and `setOpenModal` state for the main React component should allow you to easily manage the state of the Modal component and use inline functions on event listeners such as `onClick` or `onClose`.

```tsx
// index.tsx

"use client";

import { Button, Modal, ModalBody, ModalFooter, ModalHeader } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [openModal, setOpenModal] = useState(true);

  return (
    <>
      <Button onClick={() => setOpenModal(true)}>Toggle modal</Button>
      <Modal show={openModal} onClose={() => setOpenModal(false)}>
        <ModalHeader>Terms of Service</ModalHeader>
        <ModalBody>
          <div className="space-y-6">
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              With less than a month to go before the European Union enacts new consumer privacy laws for its citizens,
              companies around the world are updating their terms of service agreements to comply.
            </p>
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              The European Union’s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant
              to ensure a common set of data rights in the European Union. It requires organizations to notify users as
              soon as possible of high-risk data breaches that could personally affect them.
            </p>
          </div>
        </ModalBody>
        <ModalFooter>
          <Button onClick={() => setOpenModal(false)}>I accept</Button>
          <Button color="alternative" onClick={() => setOpenModal(false)}>
            Decline
          </Button>
        </ModalFooter>
      </Modal>
    </>
  );
}
```

## Backdrop dismissible

To enable the modal to be dismissed when clicking outside of the component (ie. the backdrop) then you can pass the `dismissible` prop to the `<Modal>` component from React.

```tsx
// index.tsx

"use client";

import { Button, Modal, ModalBody, ModalFooter, ModalHeader } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [openModal, setOpenModal] = useState(true);

  return (
    <>
      <Button onClick={() => setOpenModal(true)}>Toggle modal</Button>
      <Modal dismissible show={openModal} onClose={() => setOpenModal(false)}>
        <ModalHeader>Terms of Service</ModalHeader>
        <ModalBody>
          <div className="space-y-6">
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              With less than a month to go before the European Union enacts new consumer privacy laws for its citizens,
              companies around the world are updating their terms of service agreements to comply.
            </p>
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              The European Union’s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant
              to ensure a common set of data rights in the European Union. It requires organizations to notify users as
              soon as possible of high-risk data breaches that could personally affect them.
            </p>
          </div>
        </ModalBody>
        <ModalFooter>
          <Button onClick={() => setOpenModal(false)}>I accept</Button>
          <Button color="alternative" onClick={() => setOpenModal(false)}>
            Decline
          </Button>
        </ModalFooter>
      </Modal>
    </>
  );
}
```

## Pop-up modal

Use this example by passing the `popup` prop from React to the modal component to show a dialog to the user asking for a decision such as when confirming an item deletion from the database.

```tsx
// index.tsx

"use client";

import { Button, Modal, ModalBody, ModalHeader } from "flowbite-react";
import { useState } from "react";
import { HiOutlineExclamationCircle } from "react-icons/hi";

export function Component() {
  const [openModal, setOpenModal] = useState(true);

  return (
    <>
      <Button onClick={() => setOpenModal(true)}>Toggle modal</Button>
      <Modal show={openModal} size="md" onClose={() => setOpenModal(false)} popup>
        <ModalHeader />
        <ModalBody>
          <div className="text-center">
            <HiOutlineExclamationCircle className="mx-auto mb-4 h-14 w-14 text-gray-400 dark:text-gray-200" />
            <h3 className="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">
              Are you sure you want to delete this product?
            </h3>
            <div className="flex justify-center gap-4">
              <Button color="red" onClick={() => setOpenModal(false)}>
                Yes, I'm sure
              </Button>
              <Button color="alternative" onClick={() => setOpenModal(false)}>
                No, cancel
              </Button>
            </div>
          </div>
        </ModalBody>
      </Modal>
    </>
  );
}
```

## Modal with form elements

You can also add form elements inside of the modal component by adding the markup that you want inside the `<ModalBody>` component. Form elements can be used to show user authentication or surveys modal elements.

```tsx
// index.tsx

"use client";

import { Button, Checkbox, Label, Modal, ModalBody, ModalHeader, TextInput } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [openModal, setOpenModal] = useState(true);
  const [email, setEmail] = useState("");

  function onCloseModal() {
    setOpenModal(false);
    setEmail("");
  }

  return (
    <>
      <Button onClick={() => setOpenModal(true)}>Toggle modal</Button>
      <Modal show={openModal} size="md" onClose={onCloseModal} popup>
        <ModalHeader />
        <ModalBody>
          <div className="space-y-6">
            <h3 className="text-xl font-medium text-gray-900 dark:text-white">Sign in to our platform</h3>
            <div>
              <div className="mb-2 block">
                <Label htmlFor="email">Your email</Label>
              </div>
              <TextInput
                id="email"
                placeholder="name@company.com"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                required
              />
            </div>
            <div>
              <div className="mb-2 block">
                <Label htmlFor="password">Your password</Label>
              </div>
              <TextInput id="password" type="password" required />
            </div>
            <div className="flex justify-between">
              <div className="flex items-center gap-2">
                <Checkbox id="remember" />
                <Label htmlFor="remember">Remember me</Label>
              </div>
              <a href="#" className="text-sm text-primary-700 hover:underline dark:text-primary-500">
                Lost Password?
              </a>
            </div>
            <div className="w-full">
              <Button>Log in to your account</Button>
            </div>
            <div className="flex justify-between text-sm font-medium text-gray-500 dark:text-gray-300">
              Not registered?&nbsp;
              <a href="#" className="text-primary-700 hover:underline dark:text-primary-500">
                Create account
              </a>
            </div>
          </div>
        </ModalBody>
      </Modal>
    </>
  );
}
```

## Initial focus

The `initialFocus` property in the `<Modal />` component sets the initial focus on a specific element when the modal opens, enhancing user experience by directing attention to key inputs such as those in authentication forms or surveys.

```tsx
// index.tsx

"use client";

import { Button, Checkbox, Label, Modal, ModalBody, ModalHeader, TextInput } from "flowbite-react";
import { useRef, useState } from "react";

export function Component() {
  const [openModal, setOpenModal] = useState(true);
  const emailInputRef = useRef<HTMLInputElement>(null);

  return (
    <>
      <Button onClick={() => setOpenModal(true)}>Toggle modal</Button>
      <Modal show={openModal} size="md" popup onClose={() => setOpenModal(false)} initialFocus={emailInputRef}>
        <ModalHeader />
        <ModalBody>
          <div className="space-y-6">
            <h3 className="text-xl font-medium text-gray-900 dark:text-white">Sign in to our platform</h3>
            <div>
              <div className="mb-2 block">
                <Label htmlFor="email">Your email</Label>
              </div>
              <TextInput id="email" ref={emailInputRef} placeholder="name@company.com" required />
            </div>
            <div>
              <div className="mb-2 block">
                <Label htmlFor="password">Your password</Label>
              </div>
              <TextInput id="password" type="password" required />
            </div>
            <div className="flex justify-between">
              <div className="flex items-center gap-2">
                <Checkbox id="remember" />
                <Label htmlFor="remember">Remember me</Label>
              </div>
              <a href="#" className="text-sm text-primary-700 hover:underline dark:text-primary-500">
                Lost Password?
              </a>
            </div>
            <div className="w-full">
              <Button>Log in to your account</Button>
            </div>
            <div className="flex justify-between text-sm font-medium text-gray-500 dark:text-gray-300">
              Not registered?&nbsp;
              <a href="#" className="text-primary-700 hover:underline dark:text-primary-500">
                Create account
              </a>
            </div>
          </div>
        </ModalBody>
      </Modal>
    </>
  );
}
```

## Sizing options

To make the modal component smaller or larger you can pass the `size` prop to the `<Modal>` React component and you can choose from `sm`, `md`, `lg`, `xl` and all the way to `7xl`.

```tsx
// index.tsx

"use client";

import { Button, Modal, ModalBody, ModalFooter, ModalHeader, Select } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [openModal, setOpenModal] = useState(true);
  const [modalSize, setModalSize] = useState<string>("md");

  return (
    <>
      <div className="flex flex-wrap gap-4">
        <div className="w-40">
          <Select defaultValue="md" onChange={(event) => setModalSize(event.target.value)}>
            <option value="sm">sm</option>
            <option value="md">md</option>
            <option value="lg">lg</option>
            <option value="xl">xl</option>
            <option value="2xl">2xl</option>
            <option value="3xl">3xl</option>
            <option value="4xl">4xl</option>
            <option value="5xl">5xl</option>
            <option value="6xl">6xl</option>
            <option value="7xl">7xl</option>
          </Select>
        </div>
        <Button onClick={() => setOpenModal(true)}>Toggle modal</Button>
      </div>
      <Modal show={openModal} size={modalSize} onClose={() => setOpenModal(false)}>
        <ModalHeader>Small modal</ModalHeader>
        <ModalBody>
          <div className="space-y-6 p-6">
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              With less than a month to go before the European Union enacts new consumer privacy laws for its citizens,
              companies around the world are updating their terms of service agreements to comply.
            </p>
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              The European Union’s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant
              to ensure a common set of data rights in the European Union. It requires organizations to notify users as
              soon as possible of high-risk data breaches that could personally affect them.
            </p>
          </div>
        </ModalBody>
        <ModalFooter>
          <Button onClick={() => setOpenModal(false)}>I accept</Button>
          <Button color="alternative" onClick={() => setOpenModal(false)}>
            Decline
          </Button>
        </ModalFooter>
      </Modal>
    </>
  );
}
```

## Placement options

To set the position of the modal component relative to the page you can use the `position` prop on the modal component and you can choose from `center`, `top-left`, `top-center`, `bottom-right`, and more based on the selector options below.

```tsx
// index.tsx

"use client";

import { Button, Modal, ModalBody, ModalFooter, ModalHeader, Select } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [openModal, setOpenModal] = useState(true);
  const [modalPlacement, setModalPlacement] = useState("center");

  return (
    <>
      <div className="flex flex-wrap gap-4">
        <div className="w-40">
          <Select defaultValue="center" onChange={(event) => setModalPlacement(event.target.value)}>
            <option value="center">Center</option>
            <option value="top-left">Top left</option>
            <option value="top-center">Top center</option>
            <option value="top-right">Top right</option>
            <option value="center-left">Center left</option>
            <option value="center-right">Center right</option>
            <option value="bottom-right">Bottom right</option>
            <option value="bottom-center">Bottom center</option>
            <option value="bottom-left">Bottom left</option>
          </Select>
        </div>
        <Button onClick={() => setOpenModal(true)}>Toggle modal</Button>
      </div>
      <Modal show={openModal} position={modalPlacement} onClose={() => setOpenModal(false)}>
        <ModalHeader>Small modal</ModalHeader>
        <ModalBody>
          <div className="space-y-6 p-6">
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              With less than a month to go before the European Union enacts new consumer privacy laws for its citizens,
              companies around the world are updating their terms of service agreements to comply.
            </p>
            <p className="text-base leading-relaxed text-gray-500 dark:text-gray-400">
              The European Union’s General Data Protection Regulation (G.D.P.R.) goes into effect on May 25 and is meant
              to ensure a common set of data rights in the European Union. It requires organizations to notify users as
              soon as possible of high-risk data breaches that could personally affect them.
            </p>
          </div>
        </ModalBody>
        <ModalFooter>
          <Button onClick={() => setOpenModal(false)}>I accept</Button>
          <Button color="alternative" onClick={() => setOpenModal(false)}>
            Decline
          </Button>
        </ModalFooter>
      </Modal>
    </>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "fixed inset-x-0 top-0 z-50 h-screen overflow-y-auto overflow-x-hidden md:inset-0 md:h-full",
    "show": {
      "on": "flex bg-gray-900/50 dark:bg-gray-900/80",
      "off": "hidden"
    },
    "sizes": {
      "sm": "max-w-sm",
      "md": "max-w-md",
      "lg": "max-w-lg",
      "xl": "max-w-xl",
      "2xl": "max-w-2xl",
      "3xl": "max-w-3xl",
      "4xl": "max-w-4xl",
      "5xl": "max-w-5xl",
      "6xl": "max-w-6xl",
      "7xl": "max-w-7xl"
    },
    "positions": {
      "top-left": "items-start justify-start",
      "top-center": "items-start justify-center",
      "top-right": "items-start justify-end",
      "center-left": "items-center justify-start",
      "center": "items-center justify-center",
      "center-right": "items-center justify-end",
      "bottom-right": "items-end justify-end",
      "bottom-center": "items-end justify-center",
      "bottom-left": "items-end justify-start"
    }
  },
  "content": {
    "base": "relative h-full w-full p-4 md:h-auto",
    "inner": "relative flex max-h-[90dvh] flex-col rounded-lg bg-white shadow dark:bg-gray-700"
  },
  "body": {
    "base": "flex-1 overflow-auto p-6",
    "popup": "pt-0"
  },
  "header": {
    "base": "flex items-start justify-between rounded-t border-b p-5 dark:border-gray-600",
    "popup": "border-b-0 p-2",
    "title": "text-xl font-medium text-gray-900 dark:text-white",
    "close": {
      "base": "ml-auto inline-flex items-center rounded-lg bg-transparent p-1.5 text-sm text-gray-400 hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-600 dark:hover:text-white",
      "icon": "h-5 w-5"
    }
  },
  "footer": {
    "base": "flex items-center space-x-2 rounded-b border-gray-200 p-6 dark:border-gray-600",
    "popup": "border-t"
  }
}
```

## References

- [Flowbite Modal](https://flowbite.com/docs/components/modal/)


---

## Navbar

# React Navbar - Flowbite

> The navbar component can be used to show a list of navigation links positioned on the top side of your page based on multiple layouts, sizes, and dropdowns

The navbar component is an important section of any website as it is the first section that appears on any page and it serves the purpose of allowing your users to navigate throughout your website.

Generally, the navigation bar consists of the logo of your website, a list of menu items for navigation and other secondary elements such as buttons, dropdowns, and a hamburger menu for mobile devices.

All interactivity and options are handled by using React properties and you can customise the appearance of the navbar using the classes from Tailwind CSS.

To start using the navbar component you need to import it from Flowbite React:

```jsx
import { Navbar } from "flowbite-react";
```

## Default navbar

Use the default navbar component to showcase the logo and a list of menu items with links to other pages of your website by adding the `<NavbarBrand>` and `<NavbarLink>` components inside the `<Navbar>` component.

On mobile device the navigation bar will be collapsed and you will be able to use the hamburger menu to toggle the menu items by adding the `<NavbarToggle>` component.

```tsx
// index.tsx

import { Navbar, NavbarBrand, NavbarCollapse, NavbarLink, NavbarToggle } from "flowbite-react";
import Link from "next/link";

export function Component() {
  return (
    <Navbar fluid rounded>
      <NavbarBrand as={Link} href="https://flowbite-react.com">
        <img src="/favicon.svg" className="mr-3 h-6 sm:h-9" alt="Flowbite React Logo" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite React</span>
      </NavbarBrand>
      <NavbarToggle />
      <NavbarCollapse>
        <NavbarLink href="#" active>
          Home
        </NavbarLink>
        <NavbarLink as={Link} href="#">
          About
        </NavbarLink>
        <NavbarLink href="#">Services</NavbarLink>
        <NavbarLink href="#">Pricing</NavbarLink>
        <NavbarLink href="#">Contact</NavbarLink>
      </NavbarCollapse>
    </Navbar>
  );
}
```

## Navbar with CTA button

Use this example to show a CTA button inside the navbar component for marketing advantages and to increase the conversion rate of your website.

```tsx
// index.tsx

import { Button, Navbar, NavbarBrand, NavbarCollapse, NavbarLink, NavbarToggle } from "flowbite-react";

export function Component() {
  return (
    <Navbar fluid rounded>
      <NavbarBrand href="https://flowbite-react.com">
        <img src="/favicon.svg" className="mr-3 h-6 sm:h-9" alt="Flowbite React Logo" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite React</span>
      </NavbarBrand>
      <div className="flex md:order-2">
        <Button>Get started</Button>
        <NavbarToggle />
      </div>
      <NavbarCollapse>
        <NavbarLink href="#" active>
          Home
        </NavbarLink>
        <NavbarLink href="#">About</NavbarLink>
        <NavbarLink href="#">Services</NavbarLink>
        <NavbarLink href="#">Pricing</NavbarLink>
        <NavbarLink href="#">Contact</NavbarLink>
      </NavbarCollapse>
    </Navbar>
  );
}
```

## Navbar with dropdown

Use this example to feature a dropdown menu when clicking on the user avatar inside the navbar by importing the `<Avatar>` and `<Dropdown>` components.

```tsx
// index.tsx

import {
  Avatar,
  Dropdown,
  DropdownDivider,
  DropdownHeader,
  DropdownItem,
  Navbar,
  NavbarBrand,
  NavbarCollapse,
  NavbarLink,
  NavbarToggle,
} from "flowbite-react";

export function Component() {
  return (
    <Navbar fluid rounded>
      <NavbarBrand href="https://flowbite-react.com">
        <img src="/favicon.svg" className="mr-3 h-6 sm:h-9" alt="Flowbite React Logo" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite React</span>
      </NavbarBrand>
      <div className="flex md:order-2">
        <Dropdown
          arrowIcon={false}
          inline
          label={
            <Avatar alt="User settings" img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" rounded />
          }
        >
          <DropdownHeader>
            <span className="block text-sm">Bonnie Green</span>
            <span className="block truncate text-sm font-medium">name@flowbite.com</span>
          </DropdownHeader>
          <DropdownItem>Dashboard</DropdownItem>
          <DropdownItem>Settings</DropdownItem>
          <DropdownItem>Earnings</DropdownItem>
          <DropdownDivider />
          <DropdownItem>Sign out</DropdownItem>
        </Dropdown>
        <NavbarToggle />
      </div>
      <NavbarCollapse>
        <NavbarLink href="#" active>
          Home
        </NavbarLink>
        <NavbarLink href="#">About</NavbarLink>
        <NavbarLink href="#">Services</NavbarLink>
        <NavbarLink href="#">Pricing</NavbarLink>
        <NavbarLink href="#">Contact</NavbarLink>
      </NavbarCollapse>
    </Navbar>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "bg-white px-2 py-2.5 sm:px-4 dark:border-gray-700 dark:bg-gray-800",
    "rounded": {
      "on": "rounded",
      "off": ""
    },
    "bordered": {
      "on": "border",
      "off": ""
    },
    "inner": {
      "base": "mx-auto flex flex-wrap items-center justify-between",
      "fluid": {
        "on": "",
        "off": "container"
      }
    }
  },
  "brand": {
    "base": "flex items-center"
  },
  "collapse": {
    "base": "w-full md:block md:w-auto",
    "list": "mt-4 flex flex-col md:mt-0 md:flex-row md:space-x-8 md:text-sm md:font-medium",
    "hidden": {
      "on": "hidden",
      "off": ""
    }
  },
  "link": {
    "base": "block py-2 pl-3 pr-4 md:p-0",
    "active": {
      "on": "bg-primary-700 text-white md:bg-transparent md:text-primary-700 dark:text-white",
      "off": "border-b border-gray-100 text-gray-700 hover:bg-gray-50 md:border-0 md:hover:bg-transparent md:hover:text-primary-700 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent md:dark:hover:text-white"
    },
    "disabled": {
      "on": "text-gray-400 hover:cursor-not-allowed dark:text-gray-600",
      "off": ""
    }
  },
  "toggle": {
    "base": "inline-flex items-center rounded-lg p-2 text-sm text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 md:hidden dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600",
    "icon": "h-6 w-6 shrink-0",
    "title": "sr-only"
  }
}
```

## References

- [Flowbite Navbar](https://flowbite.com/docs/components/navbar/)


---

## Pagination

# React Pagination - Flowbite

> Get started with the pagination component to indicate the number of pages with number, link, and control buttons and allow the user to navigate through these pages

The pagination component can be used to show a list of pages with numbers and links to allow the users to navigate through multiple pages, data from tables, and more.

Choose one of the examples below based on various styles and sizes and customize them using the React props API and the utility classes from Tailwind CSS.

You need to import the pagination component from the `flowbite-react` library before using it:

```jsx
import { Pagination } from "flowbite-react";
```

## Default pagination

Use the `<Pagination>` component to create a default pagination element and use the `currentPage` prop to set the currently active page, the `totalPages` prop to set how many pages there are in total and update the `onPageChange` even listener to set the state of the pagination component via React.

```tsx
// index.tsx

"use client";

import { Pagination } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [currentPage, setCurrentPage] = useState(1);

  const onPageChange = (page: number) => setCurrentPage(page);

  return (
    <div className="flex overflow-x-auto sm:justify-center">
      <Pagination currentPage={currentPage} totalPages={100} onPageChange={onPageChange} />
    </div>
  );
}
```

## Pagination with icons

Add next and previous icons to the pagination component by passing the `showIcons` prop via React.

```tsx
// index.tsx

"use client";

import { Pagination } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [currentPage, setCurrentPage] = useState(1);

  const onPageChange = (page: number) => setCurrentPage(page);

  return (
    <div className="flex overflow-x-auto sm:justify-center">
      <Pagination currentPage={currentPage} totalPages={100} onPageChange={onPageChange} showIcons />
    </div>
  );
}
```

## Previous and next

Show only the next and previous control buttons by passing the `layout="navigation"` prop from React.

```tsx
// index.tsx

"use client";

import { Pagination } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [currentPage, setCurrentPage] = useState(1);

  const onPageChange = (page: number) => setCurrentPage(page);

  return (
    <div className="flex overflow-x-auto sm:justify-center">
      <Pagination layout="navigation" currentPage={currentPage} totalPages={100} onPageChange={onPageChange} />
    </div>
  );
}
```

## Control button icons

Show the control buttons with icons by passing both the `layout="navigation"` and `showIcons` props.

```tsx
// index.tsx

"use client";

import { Pagination } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [currentPage, setCurrentPage] = useState(1);

  const onPageChange = (page: number) => setCurrentPage(page);

  return (
    <div className="flex overflow-x-auto sm:justify-center">
      <Pagination
        layout="navigation"
        currentPage={currentPage}
        totalPages={100}
        onPageChange={onPageChange}
        showIcons
      />
    </div>
  );
}
```

## Table data navigation

Use this example show table data navigation by using the `layout="table"` prop from React.

```tsx
// index.tsx

"use client";

import { Pagination } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [currentPage, setCurrentPage] = useState(1);

  const onPageChange = (page: number) => setCurrentPage(page);

  return (
    <div className="flex overflow-x-auto sm:justify-center">
      <Pagination layout="table" currentPage={currentPage} itemsPerPage={10} totalItems={100} onPageChange={onPageChange} />
    </div>
  );
}
```

## Table data navigation with icons

Show icons for the next and previous control buttons for table navigation by passing the `showIcons` prop.

```tsx
// index.tsx

"use client";

import { Pagination } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [currentPage, setCurrentPage] = useState(1);

  const onPageChange = (page: number) => setCurrentPage(page);

  return (
    <div className="flex overflow-x-auto sm:justify-center">
      <Pagination layout="table" currentPage={currentPage} itemsPerPage={10} totalItems={100} onPageChange={onPageChange} showIcons />
    </div>
  );
}
```

## Control button text

Customize the text for the next and previous buttons by passing the `previousLabel` and `nextLabel` props.

```tsx
// index.tsx

"use client";

import { Pagination } from "flowbite-react";
import { useState } from "react";

export function Component() {
  const [currentPage, setCurrentPage] = useState(1);

  const onPageChange = (page: number) => setCurrentPage(page);

  return (
    <div className="flex overflow-x-auto sm:justify-center">
      <Pagination
        layout="pagination"
        currentPage={currentPage}
        totalPages={1000}
        onPageChange={onPageChange}
        previousLabel="Go back"
        nextLabel="Go forward"
        showIcons
      />
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "",
  "layout": {
    "table": {
      "base": "text-sm text-gray-700 dark:text-gray-400",
      "span": "font-semibold text-gray-900 dark:text-white"
    }
  },
  "pages": {
    "base": "xs:mt-0 mt-2 inline-flex items-center -space-x-px",
    "showIcon": "inline-flex",
    "previous": {
      "base": "ml-0 rounded-l-lg border border-gray-300 bg-white px-3 py-2 leading-tight text-gray-500 enabled:hover:bg-gray-100 enabled:hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 enabled:dark:hover:bg-gray-700 enabled:dark:hover:text-white",
      "icon": "h-5 w-5"
    },
    "next": {
      "base": "rounded-r-lg border border-gray-300 bg-white px-3 py-2 leading-tight text-gray-500 enabled:hover:bg-gray-100 enabled:hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 enabled:dark:hover:bg-gray-700 enabled:dark:hover:text-white",
      "icon": "h-5 w-5"
    },
    "selector": {
      "base": "w-12 border border-gray-300 bg-white py-2 leading-tight text-gray-500 enabled:hover:bg-gray-100 enabled:hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 enabled:dark:hover:bg-gray-700 enabled:dark:hover:text-white",
      "active": "bg-cyan-50 text-cyan-600 hover:bg-cyan-100 hover:text-cyan-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white",
      "disabled": "cursor-not-allowed opacity-50"
    }
  }
}
```

## References

- [Flowbite Pagination](https://flowbite.com/docs/components/pagination/)


---

## Popover

# React Popover - Flowbite

> Use the popover component to show detailed information inside a pop-up box relative to the element that is being clicked or hovered based on multiple styles

Use the popover component to show detailed information inside a pop-up box relative to the element that is being clicked or hovered based on multiple styles

Get started with the popover component to show any type of content inside a pop-up box when hovering or clicking over a trigger element. There are multiple examples that you can choose from, such as showing more information about a user profile, company profile, password strength, and more.

Before using the popover component, make sure to import the component in your React project:

```jsx
import { Popover } from "flowbite-react";
```

## Default popover

Wrap the trigger component with the `<Popover>` component and pass the popover content to the `content` prop of the `<Popover>` component.

This will render the popover whenever you click the trigger component.

```tsx
// index.tsx

import { Button, Popover } from "flowbite-react";

export function Component() {
  return (
    <Popover
      aria-labelledby="default-popover"
      content={
        <div className="w-64 text-sm text-gray-500 dark:text-gray-400">
          <div className="border-b border-gray-200 bg-gray-100 px-3 py-2 dark:border-gray-600 dark:bg-gray-700">
            <h3 id="default-popover" className="font-semibold text-gray-900 dark:text-white">
              Popover title
            </h3>
          </div>
          <div className="px-3 py-2">
            <p>And here's some amazing content. It's very engaging. Right?</p>
          </div>
        </div>
      }
    >
      <Button>Default popover</Button>
    </Popover>
  );
}
```

## Company profile

This example can be used to show more information about a company profile.

```tsx
// index.tsx

import { Button, Popover } from "flowbite-react";

export function Component() {
  return (
    <Popover
      aria-labelledby="profile-popover"
      content={
        <div className="w-64 p-3">
          <div className="mb-2 flex items-center justify-between">
            <a href="#">
              <img
                className="h-10 w-10 rounded-full"
                src="https://flowbite.com/docs/images/people/profile-picture-1.jpg"
                alt="Jese Leos"
              />
            </a>
            <div>
              <button
                type="button"
                className="rounded-lg bg-blue-700 px-3 py-1.5 text-xs font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              >
                Follow
              </button>
            </div>
          </div>
          <p id="profile-popover" className="text-base font-semibold leading-none text-gray-900 dark:text-white">
            <a href="#">Jese Leos</a>
          </p>
          <p className="mb-3 text-sm font-normal">
            <a href="#" className="hover:underline">
              @jeseleos
            </a>
          </p>
          <p className="mb-4 text-sm">
            Open-source contributor. Building{" "}
            <a href="#" className="text-blue-600 hover:underline dark:text-blue-500">
              flowbite.com
            </a>
            .
          </p>
          <ul className="flex text-sm">
            <li className="me-2">
              <a href="#" className="hover:underline">
                <span className="font-semibold text-gray-900 dark:text-white">799</span>
                <span>Following</span>
              </a>
            </li>
            <li>
              <a href="#" className="hover:underline">
                <span className="font-semibold text-gray-900 dark:text-white">3,758</span>
                <span>Followers</span>
              </a>
            </li>
          </ul>
        </div>
      }
    >
      <Button>Company profile</Button>
    </Popover>
  );
}
```

## Image popover

Use this example to trigger a popover component with detailed information and an image when hovering over a portion of highlighted text inspired by Wikipedia and other large news outlets.

```tsx
// index.tsx

import { Popover } from "flowbite-react";

export function Component() {
  return (
    <p className="text-gray-500 dark:text-gray-400">
      Due to its central geographic location in Southern Europe,{" "}
      <Popover
        trigger="hover"
        content={
          <div className="w-96 text-sm text-gray-500 dark:border-gray-600 dark:bg-gray-800 dark:text-gray-400">
            <div className="grid grid-cols-5">
              <div className="col-span-3 p-3">
                <div className="space-y-2">
                  <h3 className="font-semibold text-gray-900 dark:text-white">About Italy</h3>
                  <p>
                    Italy is located in the middle of the Mediterranean Sea, in Southern Europe it is also considered
                    part of Western Europe. A unitary parliamentary republic with Rome as its capital and largest city.
                  </p>
                  <a
                    href="#"
                    className="flex items-center font-medium text-blue-600 hover:text-blue-700 hover:underline dark:text-blue-500 dark:hover:text-blue-600"
                  >
                    Read more{" "}
                    <svg
                      className="ms-1.5 h-2 w-2 rtl:rotate-180"
                      aria-hidden="true"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 6 10"
                    >
                      <path
                        stroke="currentColor"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="m1 9 4-4-4-4"
                      />
                    </svg>
                  </a>
                </div>
              </div>
              <img
                src="https://flowbite.com/docs/images/popovers/italy.png"
                className="col-span-2 h-full"
                alt="Italy map"
              />
            </div>
          </div>
        }
      >
        <a href="#" className="text-blue-600 underline hover:no-underline dark:text-blue-500">
          Italy
        </a>
      </Popover>{" "}
      has historically been home to myriad peoples and cultures. In addition to the various ancient peoples dispersed
      throughout what is now modern-day Italy, the most predominant being the Indo-European Italic peoples who gave the
      peninsula its name, beginning from the classical era, Phoenicians and Carthaginians founded colonies mostly in
      insular Italy
    </p>
  );
}
```

## Password strength

Dynamically show the password strength progress when creating a new password positioned relative to the input element.

```tsx
// index.tsx

"use client";

import { Button, Checkbox, Label, Popover, TextInput } from "flowbite-react";

export function Component() {
  return (
    <form className="flex max-w-md flex-col gap-4">
      <div>
        <div className="mb-2 block">
          <Label htmlFor="email1">Your email</Label>
        </div>
        <TextInput id="email1" type="email" placeholder="name@flowbite.com" required />
      </div>
      <div>
        <div className="mb-2 block">
          <Label htmlFor="password1">Your password</Label>
        </div>
        <Popover
          trigger="hover"
          content={
            <div className="space-y-2 p-3">
              <h3 className="font-semibold text-gray-900 dark:text-white">Must have at least 6 characters</h3>
              <div className="grid grid-cols-4 gap-2">
                <div className="h-1 bg-orange-300 dark:bg-orange-400"></div>
                <div className="h-1 bg-orange-300 dark:bg-orange-400"></div>
                <div className="h-1 bg-gray-200 dark:bg-gray-600"></div>
                <div className="h-1 bg-gray-200 dark:bg-gray-600"></div>
              </div>
              <p>It’s better to have:</p>
              <ul>
                <li className="mb-1 flex items-center">
                  <svg
                    className="me-2 h-3.5 w-3.5 text-green-400 dark:text-green-500"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 16 12"
                  >
                    <path
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M1 5.917 5.724 10.5 15 1.5"
                    />
                  </svg>
                  Upper & lower case letters
                </li>
                <li className="mb-1 flex items-center">
                  <svg
                    className="me-2.5 h-3 w-3 text-gray-300 dark:text-gray-400"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 14 14"
                  >
                    <path
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                    />
                  </svg>
                  A symbol (#$&)
                </li>
                <li className="flex items-center">
                  <svg
                    className="me-2.5 h-3 w-3 text-gray-300 dark:text-gray-400"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 14 14"
                  >
                    <path
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                    />
                  </svg>
                  A longer password (min. 12 chars.)
                </li>
              </ul>
            </div>
          }
        >
          <TextInput id="password1" type="password" required />
        </Popover>
      </div>
      <div className="flex items-center gap-2">
        <Checkbox id="remember" />
        <Label htmlFor="remember">Remember me</Label>
      </div>
      <Button type="submit">Submit</Button>
    </form>
  );
}
```

## Controlled

Manages visibility via `open` and `openOnChange` props, allowing fine-tuned control over its display. Ideal for scenarios where Popover behavior needs to align with specific application logic or user interactions.

```tsx
// index.tsx

"use client";

import { Button, Label, Popover, TextInput } from "flowbite-react";
import { useState } from "react";
import { BiCaretDown } from "react-icons/bi";

export function Component() {
  const [open, setOpen] = useState(false);

  return (
    <Popover
      open={open}
      onOpenChange={setOpen}
      content={
        <div className="flex w-64 flex-col gap-4 p-4 text-sm text-gray-500 dark:text-gray-400">
          <div>
            <h2 className="text-base text-gray-500">Area (sqft)</h2>
            <div className="mb-2 block">
              <Label htmlFor="minsqft">Minimum sqft</Label>
            </div>
            <TextInput id="minsqft" type="number" />
          </div>
          <div>
            <div className="mb-2 block">
              <Label htmlFor="maxsqft">Maximum sqft</Label>
            </div>
            <TextInput id="maxsqft" type="number" />
          </div>
          <div className="flex gap-2">
            <Button color="gray">Reset</Button>
            <Button color="success" onClick={() => setOpen(false)}>
              Save
            </Button>
          </div>
        </div>
      }
    >
      <Button>
        Area <BiCaretDown className="ml-2" />
      </Button>
    </Popover>
  );
}
```

## Placement

Update the placement of the popover using the `placement` prop. The default placement is `bottom` and you can also use `right`, `top`, and `left`.

```tsx
// index.tsx

import { Button, Popover } from "flowbite-react";

export function Component() {
  const content = (
    <div className="w-64 text-sm text-gray-500 dark:text-gray-400">
      <div className="border-b border-gray-200 bg-gray-100 px-3 py-2 dark:border-gray-600 dark:bg-gray-700">
        <h3 className="font-semibold text-gray-900 dark:text-white">Popover title</h3>
      </div>
      <div className="px-3 py-2">
        <p>And here's some amazing content. It's very engaging. Right?</p>
      </div>
    </div>
  );

  return (
    <div className="flex gap-2">
      <Popover content={content} placement="top">
        <Button>Popover top</Button>
      </Popover>
      <Popover content={content} placement="right">
        <Button>Popover right</Button>
      </Popover>
      <Popover content={content} placement="bottom">
        <Button>Popover bottom</Button>
      </Popover>
      <Popover content={content} placement="left">
        <Button>Popover left</Button>
      </Popover>
    </div>
  );
}
```

## Trigger type

Use the `trigger` prop to change the trigger type of the popover if you want to show the popover when clicking on the hover element instead of clicking on it.

The default trigger type is `hover` and you can also use `click`.

```tsx
// index.tsx

import { Button, Popover } from "flowbite-react";

export function Component() {
  const content = (
    <div className="w-64 text-sm text-gray-500 dark:text-gray-400">
      <div className="border-b border-gray-200 bg-gray-100 px-3 py-2 dark:border-gray-600 dark:bg-gray-700">
        <h3 className="font-semibold text-gray-900 dark:text-white">Popover title</h3>
      </div>
      <div className="px-3 py-2">
        <p>And here's some amazing content. It's very engaging. Right?</p>
      </div>
    </div>
  );

  return (
    <div className="flex gap-2">
      <Popover content={content} trigger="hover">
        <Button>Popover hover</Button>
      </Popover>
      <Popover content={content} trigger="click">
        <Button>Popover click</Button>
      </Popover>
    </div>
  );
}
```

## Disable arrow

You can disable the arrow of the popover component by passing the `arrow` prop with a value of `false`.

```tsx
// index.tsx

import { Button, Popover } from "flowbite-react";

export function Component() {
  return (
    <Popover
      aria-labelledby="default-popover"
      content={
        <div className="w-64 text-sm text-gray-500 dark:text-gray-400">
          <div className="border-b border-gray-200 bg-gray-100 px-3 py-2 dark:border-gray-600 dark:bg-gray-700">
            <h3 id="default-popover" className="font-semibold text-gray-900 dark:text-white">
              Popover title
            </h3>
          </div>
          <div className="px-3 py-2">
            <p>And here's some amazing content. It's very engaging. Right?</p>
          </div>
        </div>
      }
      arrow={false}
    >
      <Button>No Arrow Popover</Button>
    </Popover>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "absolute z-20 inline-block w-max max-w-[100vw] rounded-lg border border-gray-200 bg-white shadow-sm outline-none dark:border-gray-600 dark:bg-gray-800",
  "inner": "relative",
  "content": "z-10 overflow-hidden rounded-[7px]",
  "arrow": {
    "base": "absolute z-0 h-2 w-2 rotate-45 border border-gray-200 bg-white mix-blend-lighten dark:border-gray-600 dark:bg-gray-800 dark:mix-blend-color",
    "placement": "-4px"
  }
}
```

## References

- [Flowbite Popover](https://flowbite.com/docs/components/popover/)


---

## Progress bar

# React Progress Bar - Flowbite

> The progress bar component is used to show the completion rate of a given task in the form of a filled bar where you can also add a label indicating percentage

Use the progress bar component from Flowbite React to show the percentage and completion rate of a given task using a visually friendly bar meter based on multiple styles and sizes.

Choose one of the examples below for your application and use the React props to update the progress fill rate, label, sizing, and colors and customize with the classes from Tailwind CSS.

To start using the progress bar component make sure you import it first from Flowbite React:

```jsx
import { Progress } from "flowbite-react";
```

## Default progress bar

Use this example to show a progress bar where you can set the progress rate using the `progress` prop from React which should be a number from 1 to 100.

```tsx
// index.tsx

import { Progress } from "flowbite-react";

export function Component() {
  return <Progress progress={45} />;
}
```

## Progress bar with labels

Use this example to show a progress bar with a label. You can set the label text using the `textLabel` prop and the progress text using the `labelText` prop.

```tsx
// index.tsx

import { Progress } from "flowbite-react";

export function Component() {
  return <Progress progress={50} textLabel="Flowbite" size="lg" labelProgress labelText />;
}
```

## Label positioning

This example shows how you can position the label text inside the progress bar by using the React props called `progressLabelPosition` and `textLabelPosition` on the `<Progress>` component in React.

```tsx
// index.tsx

import { Progress } from "flowbite-react";

export function Component() {
  return (
    <Progress
      progress={45}
      progressLabelPosition="inside"
      textLabel="Flowbite"
      textLabelPosition="outside"
      size="lg"
      labelProgress
      labelText
    />
  );
}
```

## Sizing

The `size` prop from React can be used on the `<Progress>` component to set the size of the progress bar. You can choose from `sm`, `md`, `lg` and `xl`.

```tsx
// index.tsx

import { Progress } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-col gap-2">
      <div className="text-base font-medium dark:text-white">Small</div>
      <Progress progress={45} size="sm" />
      <div className="text-base font-medium dark:text-white">Default</div>
      <Progress progress={45} size="md" />
      <div className="text-lg font-medium dark:text-white">Large</div>
      <Progress progress={45} size="lg" />
      <div className="text-lg font-medium dark:text-white">Extra Large</div>
      <Progress progress={45} size="xl" />
    </div>
  );
}
```

## Colors

Set your own custom colors for the progress bar component by using the `color` prop from React and the utility classes from Tailwind CSS.

```tsx
// index.tsx

import { Progress } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-col gap-4">
      <div className="space-y-1">
        <div className="text-base font-medium dark:text-white">Dark</div>
        <Progress progress={45} color="dark" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-blue-700 dark:text-blue-500">Blue</div>
        <Progress progress={45} color="blue" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-red-700 dark:text-red-500">Red</div>
        <Progress progress={45} color="red" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-green-700 dark:text-green-500">Green</div>
        <Progress progress={45} color="green" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-yellow-700 dark:text-yellow-500">Yellow</div>
        <Progress progress={45} color="yellow" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-indigo-700 dark:text-indigo-500">Indigo</div>
        <Progress progress={45} color="indigo" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-purple-700 dark:text-purple-500">Purple</div>
        <Progress progress={45} color="purple" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-cyan-700 dark:text-cyan-500">Cyan</div>
        <Progress progress={45} color="cyan" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-gray-700 dark:text-gray-500">Gray</div>
        <Progress progress={45} color="gray" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-lime-700 dark:text-lime-500">Lime</div>
        <Progress progress={45} color="lime" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-pink-700 dark:text-pink-500">Pink</div>
        <Progress progress={45} color="pink" />
      </div>
      <div className="space-y-1">
        <div className="text-base font-medium text-teal-700 dark:text-teal-500">Teal</div>
        <Progress progress={45} color="teal" />
      </div>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "w-full overflow-hidden rounded-full bg-gray-200 dark:bg-gray-700",
  "label": "mb-1 flex justify-between font-medium dark:text-white",
  "bar": "space-x-2 rounded-full text-center font-medium leading-none text-primary-300 dark:text-primary-100",
  "color": {
    "default": "bg-primary-600",
    "dark": "bg-gray-600 dark:bg-gray-300",
    "blue": "bg-blue-600",
    "red": "bg-red-600 dark:bg-red-500",
    "green": "bg-green-600 dark:bg-green-500",
    "yellow": "bg-yellow-400",
    "indigo": "bg-indigo-600 dark:bg-indigo-500",
    "purple": "bg-purple-600 dark:bg-purple-500",
    "cyan": "bg-cyan-600",
    "gray": "bg-gray-500",
    "lime": "bg-lime-600",
    "pink": "bg-pink-500",
    "teal": "bg-teal-600"
  },
  "size": {
    "sm": "h-1.5",
    "md": "h-2.5",
    "lg": "h-4",
    "xl": "h-6"
  }
}
```

## References

- [Flowbite Progress Bar](https://flowbite.com/docs/components/progress/)


---

## Rating

# React Rating - Flowbite

> Get started with the rating component from Flowbite React to show testimonials and user reviews of your products using stars, labels and advanced layouts

The rating component can be used to show user reviews and testimonials in the form of stars, reviews, and labels based on multiple styles and layouts built with React and Tailwind CSS.

Check out the rating components from Flowbite React and choose one that suits your needs and customize them using the custom props API and the utility classes from Tailwind CSS.

Start using the rating component by importing it from the `flowbite-react` library:

```jsx
import { Rating } from "flowbite-react";
```

## Default rating

Use this example to show a list of star elements that can be either filled or not to indicate the average user reviews of a product by using the `filled` prop from React on the `<Rating>` component.

```tsx
// index.tsx

import { Rating, RatingStar } from "flowbite-react";

export function Component() {
  return (
    <Rating>
      <RatingStar />
      <RatingStar />
      <RatingStar />
      <RatingStar />
      <RatingStar filled={false} />
    </Rating>
  );
}
```

## Rating with text

This example can be used to show a text label next to the user review stars to indicate the average score.

```tsx
// index.tsx

import { Rating, RatingStar } from "flowbite-react";

export function Component() {
  return (
    <Rating>
      <RatingStar />
      <RatingStar />
      <RatingStar />
      <RatingStar />
      <RatingStar filled={false} />
      <p className="ml-2 text-sm font-medium text-gray-500 dark:text-gray-400">4.95 out of 5</p>
    </Rating>
  );
}
```

## Rating count

Use this example to show the number of reviews a product received next to the average stars and scores.

```tsx
// index.tsx

import { Rating, RatingStar } from "flowbite-react";

export function Component() {
  return (
    <Rating>
      <RatingStar />
      <p className="ml-2 text-sm font-bold text-gray-900 dark:text-white">4.95</p>
      <span className="mx-1.5 h-1 w-1 rounded-full bg-gray-500 dark:bg-gray-400" />
      <a href="#" className="text-sm font-medium text-gray-900 underline hover:no-underline dark:text-white">
        73 reviews
      </a>
    </Rating>
  );
}
```

## Star sizing

The `size` prop can be used on the `<Rating>` component to customize the default size of the rating component. You can choose from `md` or `lg` and the default is `sm`.

```tsx
// index.tsx

import { Rating, RatingStar } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-col gap-2">
      <Rating>
        <RatingStar />
        <RatingStar />
        <RatingStar />
        <RatingStar />
        <RatingStar filled={false} />
      </Rating>
      <Rating size="md">
        <RatingStar />
        <RatingStar />
        <RatingStar />
        <RatingStar />
        <RatingStar filled={false} />
      </Rating>
      <Rating size="lg">
        <RatingStar />
        <RatingStar />
        <RatingStar />
        <RatingStar />
        <RatingStar filled={false} />
      </Rating>
    </div>
  );
}
```

## Advanced rating

Use this component as an advanced layout for user ratings that include both the average score, total rating count, and a percentage filled progress bar to indicate in depth statistics of how many reviews were received for each score category.

```tsx
// index.tsx

import { Rating, RatingAdvanced, RatingStar } from "flowbite-react";

export function Component() {
  return (
    <>
      <Rating className="mb-2">
        <RatingStar />
        <RatingStar />
        <RatingStar />
        <RatingStar />
        <RatingStar filled={false} />
        <p className="ml-2 text-sm font-medium text-gray-500 dark:text-gray-400">4.95 out of 5</p>
      </Rating>
      <p className="mb-4 text-sm font-medium text-gray-500 dark:text-gray-400">1,745 global ratings</p>
      <RatingAdvanced percentFilled={70} className="mb-2">
        5 star
      </RatingAdvanced>
      <RatingAdvanced percentFilled={17} className="mb-2">
        4 star
      </RatingAdvanced>
      <RatingAdvanced percentFilled={8} className="mb-2">
        3 star
      </RatingAdvanced>
      <RatingAdvanced percentFilled={4} className="mb-2">
        2 star
      </RatingAdvanced>
      <RatingAdvanced percentFilled={1}>1 star</RatingAdvanced>
    </>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

### Rating theme

```json
{
  "root": {
    "base": "flex items-center"
  },
  "star": {
    "empty": "text-gray-300 dark:text-gray-500",
    "filled": "text-yellow-400",
    "sizes": {
      "sm": "h-5 w-5",
      "md": "h-7 w-7",
      "lg": "h-10 w-10"
    }
  }
}
```

### Advanced rating theme

```json
{
  "base": "flex items-center",
  "label": "text-sm font-medium text-cyan-600 dark:text-cyan-500",
  "progress": {
    "base": "mx-4 h-5 w-2/4 rounded bg-gray-200 dark:bg-gray-700",
    "fill": "h-5 rounded bg-yellow-400",
    "label": "text-sm font-medium text-cyan-600 dark:text-cyan-500"
  }
}
```

## References

- [Flowbite Rating](https://flowbite.com/docs/components/rating/)


---

## Sidebar

# React Sidebar - Flowbite

> Use the sidebar component to show a list of menu items including multi-level dropdown menu on the left or right side of your page for admin dashboards and applications

The sidebar component is an UI component that you can use for the navigation mechanism in your website or application that you would position to the left or right side of your page.

A sidebar can include content such as menu list items, dropdown, user profile information, CTA buttons, and more - you can use the custom props from React to customize the options and the utility classes from Tailwind CSS to update the styles.

To start using the sidebar component make sure you import it from the Flowbite React library:

```jsx
import { Sidebar } from "flowbite-react";
```

## Default sidebar

Use this example to show a list of navigation menu items by adding `<SidebarItem>` children components inside the `<Sidebar>` component and pass the `href` prop to set a URL and `icon` to apply any icons from the `react-icons` icon library.

You can also add a text label as a badge by using the `label` prop from React and the `labelColor` to set the color of the label background.

```tsx
// index.tsx

"use client";

import { Sidebar, SidebarItem, SidebarItemGroup, SidebarItems } from "flowbite-react";
import { HiArrowSmRight, HiChartPie, HiInbox, HiShoppingBag, HiTable, HiUser, HiViewBoards } from "react-icons/hi";

export function Component() {
  return (
    <Sidebar aria-label="Default sidebar example">
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={HiChartPie}>
            Dashboard
          </SidebarItem>
          <SidebarItem href="#" icon={HiViewBoards} label="Pro" labelColor="dark">
            Kanban
          </SidebarItem>
          <SidebarItem href="#" icon={HiInbox} label="3">
            Inbox
          </SidebarItem>
          <SidebarItem href="#" icon={HiUser}>
            Users
          </SidebarItem>
          <SidebarItem href="#" icon={HiShoppingBag}>
            Products
          </SidebarItem>
          <SidebarItem href="#" icon={HiArrowSmRight}>
            Sign In
          </SidebarItem>
          <SidebarItem href="#" icon={HiTable}>
            Sign Up
          </SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
    </Sidebar>
  );
}
```

## Multi-level dropdown

Use this example to learn how to stack multiple sidebar menu items inside one dropdown menu by using the `<SidebarCollapse>` component.

```tsx
// index.tsx

"use client";

import { Sidebar, SidebarCollapse, SidebarItem, SidebarItemGroup, SidebarItems } from "flowbite-react";
import { HiArrowSmRight, HiChartPie, HiInbox, HiShoppingBag, HiTable, HiUser } from "react-icons/hi";

export function Component() {
  return (
    <Sidebar aria-label="Sidebar with multi-level dropdown example">
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={HiChartPie}>
            Dashboard
          </SidebarItem>
          <SidebarCollapse icon={HiShoppingBag} label="E-commerce">
            <SidebarItem href="#">Products</SidebarItem>
            <SidebarItem href="#">Sales</SidebarItem>
            <SidebarItem href="#">Refunds</SidebarItem>
            <SidebarItem href="#">Shipping</SidebarItem>
          </SidebarCollapse>
          <SidebarItem href="#" icon={HiInbox}>
            Inbox
          </SidebarItem>
          <SidebarItem href="#" icon={HiUser}>
            Users
          </SidebarItem>
          <SidebarItem href="#" icon={HiShoppingBag}>
            Products
          </SidebarItem>
          <SidebarItem href="#" icon={HiArrowSmRight}>
            Sign In
          </SidebarItem>
          <SidebarItem href="#" icon={HiTable}>
            Sign Up
          </SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
    </Sidebar>
  );
}
```

## Multi-level dropdown with custom chevron

The `chevronIcon` property offers customization for the chevron icon. Alternatively, for more complex scenarios, the `renderChevronIcon` option can be utilized. Here's an example:

```tsx
// index.tsx

"use client";

import { Sidebar, SidebarCollapse, SidebarItem, SidebarItemGroup, SidebarItems } from "flowbite-react";
import {
  HiArrowSmRight,
  HiChartPie,
  HiInbox,
  HiOutlineMinusSm,
  HiOutlinePlusSm,
  HiShoppingBag,
  HiTable,
  HiUser,
} from "react-icons/hi";
import { twMerge } from "tailwind-merge";

export function Component() {
  return (
    <Sidebar aria-label="Sidebar with multi-level dropdown example">
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={HiChartPie}>
            Dashboard
          </SidebarItem>
          <SidebarCollapse
            icon={HiShoppingBag}
            label="E-commerce"
            renderChevronIcon={(theme, open) => {
              const IconComponent = open ? HiOutlineMinusSm : HiOutlinePlusSm;

              return <IconComponent aria-hidden className={twMerge(theme.label.icon.open[open ? "on" : "off"])} />;
            }}
          >
            <SidebarItem href="#">Products</SidebarItem>
            <SidebarItem href="#">Sales</SidebarItem>
            <SidebarItem href="#">Refunds</SidebarItem>
            <SidebarItem href="#">Shipping</SidebarItem>
          </SidebarCollapse>
          <SidebarItem href="#" icon={HiInbox}>
            Inbox
          </SidebarItem>
          <SidebarItem href="#" icon={HiUser}>
            Users
          </SidebarItem>
          <SidebarItem href="#" icon={HiShoppingBag}>
            Products
          </SidebarItem>
          <SidebarItem href="#" icon={HiArrowSmRight}>
            Sign In
          </SidebarItem>
          <SidebarItem href="#" icon={HiTable}>
            Sign Up
          </SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
    </Sidebar>
  );
}
```

## Content separator

Use this example to separate content inside of the sidebar using a horizontal line.

```tsx
// index.tsx

"use client";

import { Sidebar, SidebarItem, SidebarItemGroup, SidebarItems } from "flowbite-react";
import { BiBuoy } from "react-icons/bi";
import { HiArrowSmRight, HiChartPie, HiInbox, HiShoppingBag, HiTable, HiUser, HiViewBoards } from "react-icons/hi";

export function Component() {
  return (
    <Sidebar aria-label="Sidebar with content separator example">
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={HiChartPie}>
            Dashboard
          </SidebarItem>
          <SidebarItem href="#" icon={HiViewBoards}>
            Kanban
          </SidebarItem>
          <SidebarItem href="#" icon={HiInbox}>
            Inbox
          </SidebarItem>
          <SidebarItem href="#" icon={HiUser}>
            Users
          </SidebarItem>
          <SidebarItem href="#" icon={HiShoppingBag}>
            Products
          </SidebarItem>
          <SidebarItem href="#" icon={HiArrowSmRight}>
            Sign In
          </SidebarItem>
          <SidebarItem href="#" icon={HiTable}>
            Sign Up
          </SidebarItem>
        </SidebarItemGroup>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={HiChartPie}>
            Upgrade to Pro
          </SidebarItem>
          <SidebarItem href="#" icon={HiViewBoards}>
            Documentation
          </SidebarItem>
          <SidebarItem href="#" icon={BiBuoy}>
            Help
          </SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
    </Sidebar>
  );
}
```

## Sidebar with button

This example can be used to show a call to action button inside the sidebar next to the menu items.

```tsx
// index.tsx

"use client";

import { Badge, Sidebar, SidebarCTA, SidebarItem, SidebarItemGroup, SidebarItems } from "flowbite-react";
import { HiArrowSmRight, HiChartPie, HiInbox, HiShoppingBag, HiTable, HiUser, HiViewBoards } from "react-icons/hi";

export function Component() {
  return (
    <Sidebar aria-label="Sidebar with call to action button example">
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={HiChartPie}>
            Dashboard
          </SidebarItem>
          <SidebarItem href="#" icon={HiViewBoards}>
            Kanban
          </SidebarItem>
          <SidebarItem href="#" icon={HiInbox}>
            Inbox
          </SidebarItem>
          <SidebarItem href="#" icon={HiUser}>
            Users
          </SidebarItem>
          <SidebarItem href="#" icon={HiShoppingBag}>
            Products
          </SidebarItem>
          <SidebarItem href="#" icon={HiArrowSmRight}>
            Sign In
          </SidebarItem>
          <SidebarItem href="#" icon={HiTable}>
            Sign Up
          </SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
      <SidebarCTA>
        <div className="mb-3 flex items-center">
          <Badge color="warning">Beta</Badge>
          <button
            aria-label="Close"
            className="-m-1.5 ml-auto inline-flex h-6 w-6 rounded-lg bg-gray-100 p-1 text-cyan-900 hover:bg-gray-200 focus:ring-2 focus:ring-gray-400 dark:bg-gray-700 dark:text-gray-400 dark:hover:bg-gray-600"
            type="button"
          >
            <svg
              aria-hidden
              className="h-4 w-4"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fillRule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clipRule="evenodd"
              />
            </svg>
          </button>
        </div>
        <div className="mb-3 text-sm text-cyan-900 dark:text-gray-400">
          Preview the new Flowbite dashboard navigation! You can turn the new navigation off for a limited time in your
          profile.
        </div>
        <a
          className="text-sm text-cyan-900 underline hover:text-cyan-800 dark:text-gray-400 dark:hover:text-gray-300"
          href="#"
        >
          Turn new navigation off
        </a>
      </SidebarCTA>
    </Sidebar>
  );
}
```

## Sidebar with logo

Feature the branded logo of your company on the top side of the sidebar using this example.

```tsx
// index.tsx

"use client";

import { Sidebar, SidebarItem, SidebarItemGroup, SidebarItems, SidebarLogo } from "flowbite-react";
import { HiArrowSmRight, HiChartPie, HiInbox, HiShoppingBag, HiTable, HiUser, HiViewBoards } from "react-icons/hi";

export function Component() {
  return (
    <Sidebar aria-label="Sidebar with logo branding example">
      <SidebarLogo href="#" img="/favicon.svg" imgAlt="Flowbite logo">
        Flowbite
      </SidebarLogo>
      <SidebarItems>
        <SidebarItemGroup>
          <SidebarItem href="#" icon={HiChartPie}>
            Dashboard
          </SidebarItem>
          <SidebarItem href="#" icon={HiViewBoards}>
            Kanban
          </SidebarItem>
          <SidebarItem href="#" icon={HiInbox}>
            Inbox
          </SidebarItem>
          <SidebarItem href="#" icon={HiUser}>
            Users
          </SidebarItem>
          <SidebarItem href="#" icon={HiShoppingBag}>
            Products
          </SidebarItem>
          <SidebarItem href="#" icon={HiArrowSmRight}>
            Sign In
          </SidebarItem>
          <SidebarItem href="#" icon={HiTable}>
            Sign Up
          </SidebarItem>
        </SidebarItemGroup>
      </SidebarItems>
    </Sidebar>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "h-full",
    "collapsed": {
      "on": "w-16",
      "off": "w-64"
    },
    "inner": "h-full overflow-y-auto overflow-x-hidden rounded bg-gray-50 px-3 py-4 dark:bg-gray-800"
  },
  "collapse": {
    "button": "group flex w-full items-center rounded-lg p-2 text-base font-normal text-gray-900 transition duration-75 hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700",
    "icon": {
      "base": "h-6 w-6 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white",
      "open": {
        "off": "",
        "on": "text-gray-900"
      }
    },
    "label": {
      "base": "ml-3 flex-1 whitespace-nowrap text-left",
      "title": "sr-only",
      "icon": {
        "base": "h-6 w-6 transition delay-0 ease-in-out",
        "open": {
          "on": "rotate-180",
          "off": ""
        }
      }
    },
    "list": "space-y-2 py-2"
  },
  "cta": {
    "base": "mt-6 rounded-lg bg-gray-100 p-4 dark:bg-gray-700",
    "color": {
      "blue": "bg-cyan-50 dark:bg-cyan-900",
      "dark": "bg-dark-50 dark:bg-dark-900",
      "failure": "bg-red-50 dark:bg-red-900",
      "gray": "bg-gray-50 dark:bg-gray-900",
      "green": "bg-green-50 dark:bg-green-900",
      "light": "bg-light-50 dark:bg-light-900",
      "red": "bg-red-50 dark:bg-red-900",
      "purple": "bg-purple-50 dark:bg-purple-900",
      "success": "bg-green-50 dark:bg-green-900",
      "yellow": "bg-yellow-50 dark:bg-yellow-900",
      "warning": "bg-yellow-50 dark:bg-yellow-900"
    }
  },
  "item": {
    "base": "flex items-center justify-center rounded-lg p-2 text-base font-normal text-gray-900 hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700",
    "active": "bg-gray-100 dark:bg-gray-700",
    "collapsed": {
      "insideCollapse": "group w-full pl-8 transition duration-75",
      "noIcon": "font-bold"
    },
    "content": {
      "base": "flex-1 whitespace-nowrap px-3"
    },
    "icon": {
      "base": "h-6 w-6 shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white",
      "active": "text-gray-700 dark:text-gray-100"
    },
    "label": "",
    "listItem": ""
  },
  "items": {
    "base": ""
  },
  "itemGroup": {
    "base": "mt-4 space-y-2 border-t border-gray-200 pt-4 first:mt-0 first:border-t-0 first:pt-0 dark:border-gray-700"
  },
  "logo": {
    "base": "mb-5 flex items-center pl-2.5",
    "collapsed": {
      "on": "hidden",
      "off": "self-center whitespace-nowrap text-xl font-semibold dark:text-white"
    },
    "img": "mr-3 h-6 sm:h-7"
  }
}
```

## References

- [Flowbite Sidebar](https://flowbite.com/docs/components/sidebar/)


---

## Spinner

# React Spinner (Loader) - Flowbite

> Indicate a loading status when fetching data by using the spinner component built with React and animated with Tailwind CSS based on multiple colors and sizes

The spinner component should be used to indicate a loading status of the content that you're fetching from your database and you can choose from multiple styles, colors, sizes, and animations based on React and Tailwind CSS.

Import the spinner component from Flowbite React to start using it in your project:

```jsx
import { Spinner } from "flowbite-react";
```

## Default spinner

Use the default spinner element by adding the `<Spinner>` React component inside your code and integrate the `aria-label` attribute to allow screen readers parse the component for accessibility.

```tsx
// index.tsx

import { Spinner } from "flowbite-react";

export function Component() {
  return <Spinner aria-label="Default status example" />;
}
```

## Spinner colors

Update the colors of the loading spinner by using the `color` React prop.

```tsx
// index.tsx

import { Spinner } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Spinner color="info" aria-label="Info spinner example" />
      <Spinner color="success" aria-label="Success spinner example" />
      <Spinner color="failure" aria-label="Failure spinner example" />
      <Spinner color="warning" aria-label="Warning spinner example" />
      <Spinner color="pink" aria-label="Pink spinner example" />
      <Spinner color="purple" aria-label="Purple spinner example" />
    </div>
  );
}
```

## Sizing options

Make the size of the spinner smaller or larger by using the `size` prop. Choose from `xs`, `sm`, `md`, `lg`, or `xl`.

```tsx
// index.tsx

import { Spinner } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap items-center gap-2">
      <Spinner aria-label="Extra small spinner example" size="xs" />
      <Spinner aria-label="Small spinner example" size="sm" />
      <Spinner aria-label="Medium sized spinner example" size="md" />
      <Spinner aria-label="Large spinner example" size="lg" />
      <Spinner aria-label="Extra large spinner example" size="xl" />
    </div>
  );
}
```

## Alignment

Align the spinner to the left, center or right side of the page by using the utility classes from Tailwind CSS.

```tsx
// index.tsx

import { Spinner } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-col gap-2">
      <div className="text-left">
        <Spinner aria-label="Left-aligned spinner example" />
      </div>
      <div className="text-center">
        <Spinner aria-label="Center-aligned spinner example" />
      </div>
      <div className="text-right">
        <Spinner aria-label="Right-aligned spinner example" />
      </div>
    </div>
  );
}
```

## Loading buttons

Add the loading spinner inside a button to indicate fetching status directly inside form submission buttons.

```tsx
// index.tsx

import { Button, Spinner } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-row gap-3">
      <Button>
        <Spinner aria-label="Spinner button example" size="sm" light />
        <span className="pl-3">Loading...</span>
      </Button>
      <Button color="alternative">
        <Spinner aria-label="Alternate spinner button example" size="sm" />
        <span className="pl-3">Loading...</span>
      </Button>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "inline animate-spin text-gray-200",
  "color": {
    "default": "fill-primary-600",
    "failure": "fill-red-600",
    "gray": "fill-gray-600",
    "info": "fill-cyan-600",
    "pink": "fill-pink-600",
    "purple": "fill-purple-600",
    "success": "fill-green-500",
    "warning": "fill-yellow-400"
  },
  "light": {
    "off": {
      "base": "dark:text-gray-600",
      "color": {
        "default": "",
        "failure": "",
        "gray": "dark:fill-gray-300",
        "info": "",
        "pink": "",
        "purple": "",
        "success": "",
        "warning": ""
      }
    },
    "on": {
      "base": "",
      "color": {
        "default": "",
        "failure": "",
        "gray": "",
        "info": "",
        "pink": "",
        "purple": "",
        "success": "",
        "warning": ""
      }
    }
  },
  "size": {
    "xs": "h-3 w-3",
    "sm": "h-4 w-4",
    "md": "h-6 w-6",
    "lg": "h-8 w-8",
    "xl": "h-10 w-10"
  }
}
```

## References

- [Flowbite Spinner](https://flowbite.com/docs/components/spinner/)


---

## Table

# React Table - Flowbite

> Get started with the table component to show data such as text, numbers, images, and links using a structured set of data based on rows and columns based on React

The table component is an important UI component that you can use to effectively show complex amounts of data in the form of numbers, text, images, buttons, and links inside a structured layout of rows and columns.

Use the custom React components from Flowbite and the API reference of props to customize the table layout and content and the utility classes from Tailwind CSS to update the styles.

Start using the table component by importing it from the `flowbite-react` library:

```jsx
import { Table } from "flowbite-react";
```

## Default table

Use this example to show a responsive table component with table head and body featuring cells and rows on multiple levels by using the `<Table>` React component and the children components such as `<TableHead>`, `<TableBody>`, `<TableRow>` and `<TableCell>`.

```tsx
// index.tsx

import { Table, TableBody, TableCell, TableHead, TableHeadCell, TableRow } from "flowbite-react";

export function Component() {
  return (
    <div className="overflow-x-auto">
      <Table>
        <TableHead>
          <TableRow>
            <TableHeadCell>Product name</TableHeadCell>
            <TableHeadCell>Color</TableHeadCell>
            <TableHeadCell>Category</TableHeadCell>
            <TableHeadCell>Price</TableHeadCell>
            <TableHeadCell>
              <span className="sr-only">Edit</span>
            </TableHeadCell>
          </TableRow>
        </TableHead>
        <TableBody className="divide-y">
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Apple MacBook Pro 17"
            </TableCell>
            <TableCell>Sliver</TableCell>
            <TableCell>Laptop</TableCell>
            <TableCell>$2999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Microsoft Surface Pro
            </TableCell>
            <TableCell>White</TableCell>
            <TableCell>Laptop PC</TableCell>
            <TableCell>$1999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">Magic Mouse 2</TableCell>
            <TableCell>Black</TableCell>
            <TableCell>Accessories</TableCell>
            <TableCell>$99</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  );
}
```

## Striped rows

Use the `striped` React prop on the `<Table>` component to alternate the background of every second row of the table to increase contrast and readability.

```tsx
// index.tsx

import { Table, TableBody, TableCell, TableHead, TableHeadCell, TableRow } from "flowbite-react";

export function Component() {
  return (
    <div className="overflow-x-auto">
      <Table striped>
        <TableHead>
          <TableHeadCell>Product name</TableHeadCell>
          <TableHeadCell>Color</TableHeadCell>
          <TableHeadCell>Category</TableHeadCell>
          <TableHeadCell>Price</TableHeadCell>
          <TableHeadCell>
            <span className="sr-only">Edit</span>
          </TableHeadCell>
        </TableHead>
        <TableBody className="divide-y">
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Apple MacBook Pro 17"
            </TableCell>
            <TableCell>Sliver</TableCell>
            <TableCell>Laptop</TableCell>
            <TableCell>$2999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Microsoft Surface Pro
            </TableCell>
            <TableCell>White</TableCell>
            <TableCell>Laptop PC</TableCell>
            <TableCell>$1999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">Magic Mouse 2</TableCell>
            <TableCell>Black</TableCell>
            <TableCell>Accessories</TableCell>
            <TableCell>$99</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Google Pixel Phone
            </TableCell>
            <TableCell>Gray</TableCell>
            <TableCell>Phone</TableCell>
            <TableCell>$799</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">Apple Watch 5</TableCell>
            <TableCell>Red</TableCell>
            <TableCell>Wearables</TableCell>
            <TableCell>$999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  );
}
```

## Table hover state

Add the `hoverable` prop to the `<Table>` React component to show a hover effect when moving the mouse over a table row. This also helps with readability.

```tsx
// index.tsx

import { Table, TableBody, TableCell, TableHead, TableHeadCell, TableRow } from "flowbite-react";

export function Component() {
  return (
    <div className="overflow-x-auto">
      <Table hoverable>
        <TableHead>
          <TableRow>
            <TableHeadCell>Product name</TableHeadCell>
            <TableHeadCell>Color</TableHeadCell>
            <TableHeadCell>Category</TableHeadCell>
            <TableHeadCell>Price</TableHeadCell>
            <TableHeadCell>
              <span className="sr-only">Edit</span>
            </TableHeadCell>
          </TableRow>
        </TableHead>
        <TableBody className="divide-y">
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Apple MacBook Pro 17"
            </TableCell>
            <TableCell>Sliver</TableCell>
            <TableCell>Laptop</TableCell>
            <TableCell>$2999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Microsoft Surface Pro
            </TableCell>
            <TableCell>White</TableCell>
            <TableCell>Laptop PC</TableCell>
            <TableCell>$1999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">Magic Mouse 2</TableCell>
            <TableCell>Black</TableCell>
            <TableCell>Accessories</TableCell>
            <TableCell>$99</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  );
}
```

## Table with checkboxes

Use this example to show multiple checkbox form elements for each table row that you can use when performing bulk actions.

```tsx
// index.tsx

import { Checkbox, Table, TableBody, TableCell, TableHead, TableHeadCell, TableRow } from "flowbite-react";

export function Component() {
  return (
    <div className="overflow-x-auto">
      <Table hoverable>
        <TableHead>
          <TableRow>
            <TableHeadCell className="p-4">
              <Checkbox />
            </TableHeadCell>
            <TableHeadCell>Product name</TableHeadCell>
            <TableHeadCell>Color</TableHeadCell>
            <TableHeadCell>Category</TableHeadCell>
            <TableHeadCell>Price</TableHeadCell>
            <TableHeadCell>
              <span className="sr-only">Edit</span>
            </TableHeadCell>
          </TableRow>
        </TableHead>
        <TableBody className="divide-y">
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="p-4">
              <Checkbox />
            </TableCell>
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Apple MacBook Pro 17"
            </TableCell>
            <TableCell>Sliver</TableCell>
            <TableCell>Laptop</TableCell>
            <TableCell>$2999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="p-4">
              <Checkbox />
            </TableCell>
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">
              Microsoft Surface Pro
            </TableCell>
            <TableCell>White</TableCell>
            <TableCell>Laptop PC</TableCell>
            <TableCell>$1999</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
          <TableRow className="bg-white dark:border-gray-700 dark:bg-gray-800">
            <TableCell className="p-4">
              <Checkbox />
            </TableCell>
            <TableCell className="whitespace-nowrap font-medium text-gray-900 dark:text-white">Magic Mouse 2</TableCell>
            <TableCell>Black</TableCell>
            <TableCell>Accessories</TableCell>
            <TableCell>$99</TableCell>
            <TableCell>
              <a href="#" className="font-medium text-primary-600 hover:underline dark:text-primary-500">
                Edit
              </a>
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "w-full text-left text-sm text-gray-500 dark:text-gray-400",
    "shadow": "absolute left-0 top-0 -z-10 h-full w-full rounded-lg bg-white drop-shadow-md dark:bg-black",
    "wrapper": "relative"
  },
  "body": {
    "base": "group/body",
    "cell": {
      "base": "px-6 py-4 group-first/body:group-first/row:first:rounded-tl-lg group-first/body:group-first/row:last:rounded-tr-lg group-last/body:group-last/row:first:rounded-bl-lg group-last/body:group-last/row:last:rounded-br-lg"
    }
  },
  "head": {
    "base": "group/head text-xs uppercase text-gray-700 dark:text-gray-400",
    "cell": {
      "base": "bg-gray-50 px-6 py-3 group-first/head:first:rounded-tl-lg group-first/head:last:rounded-tr-lg dark:bg-gray-700"
    }
  },
  "row": {
    "base": "group/row",
    "hovered": "hover:bg-gray-50 dark:hover:bg-gray-600",
    "striped": "odd:bg-white even:bg-gray-50 odd:dark:bg-gray-800 even:dark:bg-gray-700"
  }
}
```

## References

- [Flowbite Table](https://flowbite.com/docs/components/tables/)


---

## Tabs

# React Tabs - Flowbite

> Get started with the tabs component from Flowbite React to show a list of tab items where you can switch between them using multiple styles, colors and layouts

The tabs component can be used to show a list of tab items that you can click on to change the content inside of the main tabs component using React state reactivity.

Choose one of the examples below based on various styles, layouts, and content types that you can customize with React components, props and the utility classes from Tailwind CSS.

Make sure that you import the component from the `flowbite-react` library:

```jsx
import { TabItem, Tabs } from "flowbite-react";
```

## Default tabs

Add the `<TabItem>` child component to the `<Tabs>` component to create a tab item and you can add any type of markup and React components inside of it and it will be shown when clicking on the associated tab item.

You can also choose to add the `active` prop to the `<TabItem>` component to make it active by default and set the title of the tab item using the `title` prop.

Additionally, if you pass the `disabled` prop to the `<TabItem>` component, it will be disabled and you won't be able to click on it.

```tsx
// index.tsx

import { TabItem, Tabs } from "flowbite-react";
import { HiAdjustments, HiClipboardList, HiUserCircle } from "react-icons/hi";
import { MdDashboard } from "react-icons/md";

export function Component() {
  return (
    <Tabs aria-label="Default tabs" variant="default">
      <TabItem active title="Profile" icon={HiUserCircle}>
        This is <span className="font-medium text-gray-800 dark:text-white">Profile tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Dashboard" icon={MdDashboard}>
        This is <span className="font-medium text-gray-800 dark:text-white">Dashboard tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Settings" icon={HiAdjustments}>
        This is <span className="font-medium text-gray-800 dark:text-white">Settings tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Contacts" icon={HiClipboardList}>
        This is <span className="font-medium text-gray-800 dark:text-white">Contacts tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem disabled title="Disabled">
        Disabled content
      </TabItem>
    </Tabs>
  );
}
```

## Tabs with underline

Pass the `variant="underline"` prop to the `<Tabs>` component to make the tabs have an underline style.

```tsx
// index.tsx

"use client";

import { TabItem, Tabs } from "flowbite-react";
import { HiAdjustments, HiClipboardList, HiUserCircle } from "react-icons/hi";
import { MdDashboard } from "react-icons/md";

export function Component() {
  return (
    <Tabs aria-label="Tabs with underline" variant="underline">
      <TabItem active title="Profile" icon={HiUserCircle}>
        This is <span className="font-medium text-gray-800 dark:text-white">Profile tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Dashboard" icon={MdDashboard}>
        This is <span className="font-medium text-gray-800 dark:text-white">Dashboard tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Settings" icon={HiAdjustments}>
        This is <span className="font-medium text-gray-800 dark:text-white">Settings tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Contacts" icon={HiClipboardList}>
        This is <span className="font-medium text-gray-800 dark:text-white">Contacts tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem disabled title="Disabled">
        Disabled content
      </TabItem>
    </Tabs>
  );
}
```

## Tabs with icons

Pass the `icon` prop to the `<TabItem>` component to add an icon to the tab item.

```tsx
// index.tsx

import { TabItem, Tabs } from "flowbite-react";
import { HiAdjustments, HiClipboardList, HiUserCircle } from "react-icons/hi";
import { MdDashboard } from "react-icons/md";

export function Component() {
  return (
    <Tabs aria-label="Tabs with icons" variant="underline">
      <TabItem active title="Profile" icon={HiUserCircle}>
        This is <span className="font-medium text-gray-800 dark:text-white">Profile tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Dashboard" icon={MdDashboard}>
        This is <span className="font-medium text-gray-800 dark:text-white">Dashboard tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Settings" icon={HiAdjustments}>
        This is <span className="font-medium text-gray-800 dark:text-white">Settings tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem title="Contacts" icon={HiClipboardList}>
        This is <span className="font-medium text-gray-800 dark:text-white">Contacts tab's associated content</span>.
        Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
        control the content visibility and styling.
      </TabItem>
      <TabItem disabled title="Disabled">
        Disabled content
      </TabItem>
    </Tabs>
  );
}
```

## Tabs with pills

Add the `variant="pills"` prop to the `<Tabs>` component to make the tabs have a pills style with rounded corners as an alternative style.

```tsx
// index.tsx

import { TabItem, Tabs } from "flowbite-react";

export function Component() {
  return (
    <Tabs aria-label="Pills" variant="pills">
      <TabItem active title="Tab 1">
        <p className="text-sm text-gray-500 dark:text-gray-400">Content 1</p>
      </TabItem>
      <TabItem title="Tab 2">
        <p className="text-sm text-gray-500 dark:text-gray-400">Content 2</p>
      </TabItem>
      <TabItem title="Tab 3">
        <p className="text-sm text-gray-500 dark:text-gray-400">Content 3</p>
      </TabItem>
      <TabItem title="Tab 4">
        <p className="text-sm text-gray-500 dark:text-gray-400">Content 4</p>
      </TabItem>
      <TabItem disabled title="Tab 5">
        <p className="text-sm text-gray-500 dark:text-gray-400">Content 5</p>
      </TabItem>
    </Tabs>
  );
}
```

## Full width tabs

Make the tabs span the full width of their container, pass the `variant="fullWidth"` prop to the `<Tabs>`

```tsx
// index.tsx

import { TabItem, Tabs } from "flowbite-react";
import { HiAdjustments, HiClipboardList, HiUserCircle } from "react-icons/hi";
import { MdDashboard } from "react-icons/md";

export function Component() {
  return (
    <div className="overflow-x-auto">
      <Tabs aria-label="Full width tabs" variant="fullWidth">
        <TabItem active title="Profile" icon={HiUserCircle}>
          This is <span className="font-medium text-gray-800 dark:text-white">Profile tab's associated content</span>.
          Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
          control the content visibility and styling.
        </TabItem>
        <TabItem title="Dashboard" icon={MdDashboard}>
          This is <span className="font-medium text-gray-800 dark:text-white">Dashboard tab's associated content</span>.
          Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
          control the content visibility and styling.
        </TabItem>
        <TabItem title="Settings" icon={HiAdjustments}>
          This is <span className="font-medium text-gray-800 dark:text-white">Settings tab's associated content</span>.
          Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
          control the content visibility and styling.
        </TabItem>
        <TabItem title="Contacts" icon={HiClipboardList}>
          This is <span className="font-medium text-gray-800 dark:text-white">Contacts tab's associated content</span>.
          Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
          control the content visibility and styling.
        </TabItem>
        <TabItem disabled title="Disabled">
          Disabled content
        </TabItem>
      </Tabs>
    </div>
  );
}
```

## React state options

Here's an example on how you can set the activate tab programatically using the React state variables and functions of `activateTab` and `setActivateTab`.

```tsx
// index.tsx

"use client";

import { Button, ButtonGroup, TabItem, Tabs, type TabsRef } from "flowbite-react";
import { useRef, useState } from "react";
import { HiAdjustments, HiClipboardList, HiUserCircle } from "react-icons/hi";
import { MdDashboard } from "react-icons/md";

export function Component() {
  const tabsRef = useRef<TabsRef>(null);
  const [activeTab, setActiveTab] = useState(0);

  return (
    <div className="flex flex-col gap-3">
      <Tabs aria-label="Default tabs" variant="default" ref={tabsRef} onActiveTabChange={(tab) => setActiveTab(tab)}>
        <TabItem active title="Profile" icon={HiUserCircle}>
          This is <span className="font-medium text-gray-800 dark:text-white">Profile tab's associated content</span>.
          Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
          control the content visibility and styling.
        </TabItem>
        <TabItem title="Dashboard" icon={MdDashboard}>
          This is <span className="font-medium text-gray-800 dark:text-white">Dashboard tab's associated content</span>.
          Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
          control the content visibility and styling.
        </TabItem>
        <TabItem title="Settings" icon={HiAdjustments}>
          This is <span className="font-medium text-gray-800 dark:text-white">Settings tab's associated content</span>.
          Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
          control the content visibility and styling.
        </TabItem>
        <TabItem title="Contacts" icon={HiClipboardList}>
          This is <span className="font-medium text-gray-800 dark:text-white">Contacts tab's associated content</span>.
          Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
          control the content visibility and styling.
        </TabItem>
        <TabItem disabled title="Disabled">
          Disabled content
        </TabItem>
      </Tabs>
      <div className="text-sm text-gray-500 dark:text-gray-400">Active tab: {activeTab}</div>
      <ButtonGroup>
        <Button color="gray" onClick={() => tabsRef.current?.setActiveTab(0)}>
          Profile
        </Button>
        <Button color="gray" onClick={() => tabsRef.current?.setActiveTab(1)}>
          Dashboard
        </Button>
        <Button color="gray" onClick={() => tabsRef.current?.setActiveTab(2)}>
          Settings
        </Button>
        <Button color="gray" onClick={() => tabsRef.current?.setActiveTab(3)}>
          Contacts
        </Button>
      </ButtonGroup>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "flex flex-col gap-2",
  "tablist": {
    "base": "flex text-center",
    "variant": {
      "default": "flex-wrap border-b border-gray-200 dark:border-gray-700",
      "underline": "-mb-px flex-wrap border-b border-gray-200 dark:border-gray-700",
      "pills": "flex-wrap space-x-2 text-sm font-medium text-gray-500 dark:text-gray-400",
      "fullWidth": "grid w-full grid-flow-col divide-x divide-gray-200 rounded-none text-sm font-medium shadow dark:divide-gray-700 dark:text-gray-400"
    },
    "tabitem": {
      "base": "flex items-center justify-center rounded-t-lg p-4 text-sm font-medium first:ml-0 focus:outline-none disabled:cursor-not-allowed disabled:text-gray-400 disabled:dark:text-gray-500",
      "variant": {
        "default": {
          "base": "rounded-t-lg",
          "active": {
            "on": "bg-gray-100 text-primary-600 dark:bg-gray-800 dark:text-primary-500",
            "off": "text-gray-500 hover:bg-gray-50 hover:text-gray-600 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-gray-300"
          }
        },
        "underline": {
          "base": "rounded-t-lg",
          "active": {
            "on": "rounded-t-lg border-b-2 border-primary-600 text-primary-600 dark:border-primary-500 dark:text-primary-500",
            "off": "border-b-2 border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-600 dark:text-gray-400 dark:hover:text-gray-300"
          }
        },
        "pills": {
          "base": "",
          "active": {
            "on": "rounded-lg bg-primary-600 text-white",
            "off": "rounded-lg hover:bg-gray-100 hover:text-gray-900 dark:hover:bg-gray-800 dark:hover:text-white"
          }
        },
        "fullWidth": {
          "base": "ml-0 flex w-full rounded-none first:ml-0",
          "active": {
            "on": "rounded-none bg-gray-100 p-4 text-gray-900 dark:bg-gray-700 dark:text-white",
            "off": "rounded-none bg-white hover:bg-gray-50 hover:text-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700 dark:hover:text-white"
          }
        }
      },
      "icon": "mr-2 h-5 w-5"
    }
  },
  "tabitemcontainer": {
    "base": "",
    "variant": {
      "default": "",
      "underline": "",
      "pills": "",
      "fullWidth": ""
    }
  },
  "tabpanel": "py-3"
}
```

## References

- [Flowbite Tabs](https://flowbite.com/docs/components/tabs/)


---

## Timeline

# React Timeline - Flowbite

> Use the timeline component from Flowbite React to display a list of items and events in a chronological order based on multiples styles, colors and layouts

The timeline component can be used to show a list of events and items in a chronological order with a vertical or horizontal alignment based on multiple examples, styles, layouts, and colors.

You can customize the content and options of the timeline component by using the custom React props API from Flowbite React and the utility classes from Tailwind CSS for quick style changes.

In order to use the timeline component make sure to import it first from Flowbite React:

```jsx
import { Timeline } from "flowbite-react";
```

## Default timeline

Use the `<Timeline>` React component and the child components to create a list of items inside the timeline component featuring the date, title, description and even a button.

```tsx
// index.tsx

import {
  Button,
  Timeline,
  TimelineBody,
  TimelineContent,
  TimelineItem,
  TimelinePoint,
  TimelineTime,
  TimelineTitle,
} from "flowbite-react";
import { HiArrowNarrowRight } from "react-icons/hi";

export function Component() {
  return (
    <Timeline>
      <TimelineItem>
        <TimelinePoint />
        <TimelineContent>
          <TimelineTime>February 2022</TimelineTime>
          <TimelineTitle>Application UI code in Tailwind CSS</TimelineTitle>
          <TimelineBody>
            Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order
            E-commerce & Marketing pages.
          </TimelineBody>
          <Button color="gray">
            Learn More
            <HiArrowNarrowRight className="ml-2 h-3 w-3" />
          </Button>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelinePoint />
        <TimelineContent>
          <TimelineTime>March 2022</TimelineTime>
          <TimelineTitle>Marketing UI design in Figma</TimelineTitle>
          <TimelineBody>
            All of the pages and components are first designed in Figma and we keep a parity between the two versions
            even as we update the project.
          </TimelineBody>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelinePoint />
        <TimelineContent>
          <TimelineTime>April 2022</TimelineTime>
          <TimelineTitle>E-Commerce UI code in Tailwind CSS</TimelineTitle>
          <TimelineBody>
            Get started with dozens of web components and interactive elements built on top of Tailwind CSS.
          </TimelineBody>
        </TimelineContent>
      </TimelineItem>
    </Timeline>
  );
}
```

## Vertical timeline

Use this example to show the timeline component and the child components in a vertical alignment.

```tsx
// index.tsx

"use client";

import {
  Button,
  Timeline,
  TimelineBody,
  TimelineContent,
  TimelineItem,
  TimelinePoint,
  TimelineTime,
  TimelineTitle,
} from "flowbite-react";
import { HiArrowNarrowRight, HiCalendar } from "react-icons/hi";

export function Component() {
  return (
    <Timeline>
      <TimelineItem>
        <TimelinePoint icon={HiCalendar} />
        <TimelineContent>
          <TimelineTime>February 2022</TimelineTime>
          <TimelineTitle>Application UI code in Tailwind CSS</TimelineTitle>
          <TimelineBody>
            Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order
            E-commerce & Marketing pages.
          </TimelineBody>
          <Button color="gray">
            Learn More
            <HiArrowNarrowRight className="ml-2 h-3 w-3" />
          </Button>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelinePoint icon={HiCalendar} />
        <TimelineContent>
          <TimelineTime>March 2022</TimelineTime>
          <TimelineTitle>Marketing UI design in Figma</TimelineTitle>
          <TimelineBody>
            All of the pages and components are first designed in Figma and we keep a parity between the two versions
            even as we update the project.
          </TimelineBody>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelinePoint icon={HiCalendar} />
        <TimelineContent>
          <TimelineTime>April 2022</TimelineTime>
          <TimelineTitle>E-Commerce UI code in Tailwind CSS</TimelineTitle>
          <TimelineBody>
            Get started with dozens of web components and interactive elements built on top of Tailwind CSS.
          </TimelineBody>
        </TimelineContent>
      </TimelineItem>
    </Timeline>
  );
}
```

## Horizontal timeline

Use the `horizontal` prop to show the timeline component and the child components in a horizontal alignment.

```tsx
// index.tsx

"use client";

import {
  Button,
  Timeline,
  TimelineBody,
  TimelineContent,
  TimelineItem,
  TimelinePoint,
  TimelineTime,
  TimelineTitle,
} from "flowbite-react";
import { HiArrowNarrowRight, HiCalendar } from "react-icons/hi";

export function Component() {
  return (
    <Timeline horizontal>
      <TimelineItem>
        <TimelinePoint icon={HiCalendar} />
        <TimelineContent>
          <TimelineTime>February 2022</TimelineTime>
          <TimelineTitle>Application UI code in Tailwind CSS</TimelineTitle>
          <TimelineBody>
            Get access to over 20+ pages including a dashboard layout, charts, kanban board, calendar, and pre-order
            E-commerce & Marketing pages.
          </TimelineBody>
          <Button color="gray">
            Learn More
            <HiArrowNarrowRight className="ml-2 h-3 w-3" />
          </Button>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelinePoint icon={HiCalendar} />
        <TimelineContent>
          <TimelineTime>March 2022</TimelineTime>
          <TimelineTitle>Marketing UI design in Figma</TimelineTitle>
          <TimelineBody>
            All of the pages and components are first designed in Figma and we keep a parity between the two versions
            even as we update the project.
          </TimelineBody>
        </TimelineContent>
      </TimelineItem>
      <TimelineItem>
        <TimelinePoint icon={HiCalendar} />
        <TimelineContent>
          <TimelineTime>April 2022</TimelineTime>
          <TimelineTitle>E-Commerce UI code in Tailwind CSS</TimelineTitle>
          <TimelineBody>
            Get started with dozens of web components and interactive elements built on top of Tailwind CSS.
          </TimelineBody>
        </TimelineContent>
      </TimelineItem>
    </Timeline>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "direction": {
      "horizontal": "sm:flex",
      "vertical": "relative border-l border-gray-200 dark:border-gray-700"
    }
  },
  "item": {
    "root": {
      "horizontal": "relative mb-6 sm:mb-0",
      "vertical": "mb-10 ml-6"
    },
    "content": {
      "root": {
        "base": "",
        "horizontal": "mt-3 sm:pr-8",
        "vertical": ""
      },
      "body": {
        "base": "mb-4 text-base font-normal text-gray-500 dark:text-gray-400"
      },
      "time": {
        "base": "mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500"
      },
      "title": {
        "base": "text-lg font-semibold text-gray-900 dark:text-white"
      }
    },
    "point": {
      "horizontal": "flex items-center",
      "line": "hidden h-0.5 w-full bg-gray-200 sm:flex dark:bg-gray-700",
      "marker": {
        "base": {
          "horizontal": "absolute -left-1.5 h-3 w-3 rounded-full border border-white bg-gray-200 dark:border-gray-900 dark:bg-gray-700",
          "vertical": "absolute -left-1.5 mt-1.5 h-3 w-3 rounded-full border border-white bg-gray-200 dark:border-gray-900 dark:bg-gray-700"
        },
        "icon": {
          "base": "h-3 w-3 text-primary-600 dark:text-primary-300",
          "wrapper": "absolute -left-3 flex h-6 w-6 items-center justify-center rounded-full bg-primary-200 ring-8 ring-white dark:bg-primary-900 dark:ring-gray-900"
        }
      },
      "vertical": ""
    }
  }
}
```

## References

- [Flowbite Timeline](https://flowbite.com/docs/components/timeline/)


---

## Toast

# React Toast - Flowbite

> Push notifications to your website visitors using the toast component and choose from multiple sizes, colors, styles, position and icons based on React and Tailwind CSS

The toast component can be used to show notifications to your users in a non-intrusive way by positioning it to the corner of the screen. It can be used to show simple messages or more complex ones with buttons and other elements.

Choose from one of the examples below that include different layouts, colors, styles, and icons that you can also customize using React props and the utility classes from Tailwind CSS.

To start using the toast component make sure you import it from Flowbite React:

```jsx
import { Toast } from "flowbite-react";
```

## Default toast

Use the default `<Toast>` React component to show a simple toast message with an icon and a text message.

```tsx
// index.tsx

import { Toast, ToastToggle } from "flowbite-react";
import { HiFire } from "react-icons/hi";

export function Component() {
  return (
    <Toast>
      <div className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-cyan-100 text-cyan-500 dark:bg-cyan-800 dark:text-cyan-200">
        <HiFire className="h-5 w-5" />
      </div>
      <div className="ml-3 text-sm font-normal">Set yourself free.</div>
      <ToastToggle />
    </Toast>
  );
}
```

## Toast colors

Choose one of the following toast examples based on form submission messages to update the color of the component by using the `bg` and `text` utility classes from Tailwind CSS.

```tsx
// index.tsx

import { Toast, ToastToggle } from "flowbite-react";
import { HiCheck, HiExclamation, HiX } from "react-icons/hi";

export function Component() {
  return (
    <div className="flex flex-col gap-4">
      <Toast>
        <div className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-green-100 text-green-500 dark:bg-green-800 dark:text-green-200">
          <HiCheck className="h-5 w-5" />
        </div>
        <div className="ml-3 text-sm font-normal">Item moved successfully.</div>
        <ToastToggle />
      </Toast>
      <Toast>
        <div className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-red-100 text-red-500 dark:bg-red-800 dark:text-red-200">
          <HiX className="h-5 w-5" />
        </div>
        <div className="ml-3 text-sm font-normal">Item has been deleted.</div>
        <ToastToggle />
      </Toast>
      <Toast>
        <div className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-orange-100 text-orange-500 dark:bg-orange-700 dark:text-orange-200">
          <HiExclamation className="h-5 w-5" />
        </div>
        <div className="ml-3 text-sm font-normal">Improve password difficulty.</div>
        <ToastToggle />
      </Toast>
    </div>
  );
}
```

## Feedback toast

Use this example to show a message based on form submission to indicate errors or successful actions.

```tsx
// index.tsx

import { Toast } from "flowbite-react";
import { FaTelegramPlane } from "react-icons/fa";

export function Component() {
  return (
    <Toast>
      <FaTelegramPlane className="h-5 w-5 text-cyan-600 dark:text-cyan-500" />
      <div className="pl-4 text-sm font-normal">Message sent successfully.</div>
    </Toast>
  );
}
```

## Toast with button

Add a button to the toast component to allow the user to perform an action or close the toast.

```tsx
// index.tsx

import { Toast, ToastToggle } from "flowbite-react";

export function Component() {
  return (
    <Toast>
      <div className="text-sm font-normal">Conversation archived.</div>
      <div className="ml-auto flex items-center space-x-2">
        <a
          href="#"
          className="rounded-lg p-1.5 text-sm font-medium text-primary-600 hover:bg-primary-100 dark:text-primary-500 dark:hover:bg-gray-700"
        >
          Undo
        </a>
        <ToastToggle />
      </div>
    </Toast>
  );
}
```

## Interactive toast

This component can be used to show more complex messages with buttons and other elements that can be used to perform actions and use the `<ToastToggle>` component to allow the user to close the toast component.

```tsx
// index.tsx

import { Button, Toast, ToastToggle } from "flowbite-react";
import { MdLoop } from "react-icons/md";

export function Component() {
  return (
    <Toast>
      <div className="flex items-start">
        <div className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-cyan-100 text-cyan-500 dark:bg-cyan-900 dark:text-cyan-300">
          <MdLoop className="h-5 w-5" />
        </div>
        <div className="ml-3 text-sm font-normal">
          <span className="mb-1 text-sm font-semibold text-gray-900 dark:text-white">Update available</span>
          <div className="mb-2 text-sm font-normal">A new software version is available for download.</div>
          <div className="flex gap-2">
            <div className="w-auto">
              <Button size="xs">Update</Button>
            </div>
            <div className="w-auto">
              <Button color="light" size="xs">
                Not now
              </Button>
            </div>
          </div>
        </div>
        <ToastToggle />
      </div>
    </Toast>
  );
}
```

## Custom dismissal handling

By passing the `onDismiss` callback prop to the `<ToastToggle>` component, you gain the ability to define your preferred dismissal handling (ex: using other toast libraries like `react-toastfy`). When `onDismiss` is provided, the internal state of the `<Toast />` component will remain unchanged upon clicking `<ToastToggle>`.

```tsx
// index.tsx

"use client";

import { Button, Toast, ToastToggle } from "flowbite-react";
import { useState } from "react";
import { HiFire } from "react-icons/hi";

export function Component() {
  const [showToast, setShowToast] = useState(false);

  return (
    <div className="space-y-4">
      <Button onClick={() => setShowToast((state) => !state)}>Toggle toast</Button>
      {showToast && (
        <Toast>
          <div className="inline-flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-cyan-100 text-cyan-500 dark:bg-cyan-800 dark:text-cyan-200">
            <HiFire className="h-5 w-5" />
          </div>
          <div className="ml-3 text-sm font-normal">Set yourself free.</div>
          <ToastToggle onDismiss={() => setShowToast(false)} />
        </Toast>
      )}
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "flex w-full max-w-xs items-center rounded-lg bg-white p-4 text-gray-500 shadow dark:bg-gray-800 dark:text-gray-400",
    "closed": "opacity-0 ease-out"
  },
  "toggle": {
    "base": "-m-1.5 ml-auto inline-flex h-8 w-8 rounded-lg bg-white p-1.5 text-gray-400 hover:bg-gray-100 hover:text-gray-900 focus:ring-2 focus:ring-gray-300 dark:bg-gray-800 dark:text-gray-500 dark:hover:bg-gray-700 dark:hover:text-white",
    "icon": "h-5 w-5 shrink-0"
  }
}
```

## References

- [Flowbite Toast](https://flowbite.com/docs/components/toast/)


---

## Tooltip

# React Tooltip - Flowbite

> Use the tooltip component to show a descriptive text when hovering over an element such as a button and customize the content and style with React and Tailwind CSS

Use the tooltip component from Flowbite React to indicate helpful information when hovering over an element such as a button or link to improve the UI/UX of your website.

Choose from multiple options, layouts, styles, colors, and animations from the examples below and customize the content and options using the custom React API props and the utility classes from Tailwind CSS.

Before using the tooltip component, make sure to import the component in your React project:

```jsx
import { Tooltip } from "flowbite-react";
```

## Default tooltip

Wrap the trigger component with the `<Tooltip>` component and pass the tooltip content to the `content` prop of the `<Tooltip>` component.

This will render the tooltip whenever you hover over the trigger component.

```tsx
// index.tsx

import { Button, Tooltip } from "flowbite-react";

export function Component() {
  return (
    <Tooltip content="Tooltip content">
      <Button>Default tooltip</Button>
    </Tooltip>
  );
}
```

## Tooltip styles

Use the `style` prop to change the style of the tooltip. The default style is `light` and you can also use `dark`.

```tsx
// index.tsx

import { Button, Tooltip } from "flowbite-react";

export function Component() {
  return (
    <div className="flex gap-2">
      <Tooltip content="Tooltip content" style="light">
        <Button>Light tooltip</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" style="dark">
        <Button>Dark tooltip</Button>
      </Tooltip>
    </div>
  );
}
```

## Placement

Update the placement of the tooltip using the `placement` prop. The default placement is `top` and you can also use `right`, `bottom`, and `left`.

```tsx
// index.tsx

import { Button, Tooltip } from "flowbite-react";

export function Component() {
  return (
    <div className="flex gap-2">
      <Tooltip content="Tooltip content" placement="top">
        <Button>Tooltip top</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" placement="right">
        <Button>Tooltip right</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" placement="bottom">
        <Button>Tooltip bottom</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" placement="left">
        <Button>Tooltip left</Button>
      </Tooltip>
    </div>
  );
}
```

## Trigger type

Use the `trigger` prop to change the trigger type of the tooltip if you want to show the tooltip when clicking on the trigger element instead of hovering over it.

The default trigger type is `hover` and you can also use `click`.

```tsx
// index.tsx

import { Button, Tooltip } from "flowbite-react";

export function Component() {
  return (
    <div className="flex gap-2">
      <Tooltip content="Tooltip content" trigger="hover">
        <Button>Tooltip hover</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" trigger="click">
        <Button>Tooltip click</Button>
      </Tooltip>
    </div>
  );
}
```

## Animation

Update the default animation of the tooltip component by using the `animation` prop. The default animation is `duration-300` and you can also use `duration-150`, `duration-500`, and `duration-1000`.

```tsx
// index.tsx

import { Button, Tooltip } from "flowbite-react";

export function Component() {
  return (
    <div className="flex flex-wrap gap-2">
      <Tooltip content="Tooltip content" animation={false}>
        <Button>Not animated tooltip</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" animation="duration-150">
        <Button>Fast animation</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" animation="duration-300">
        <Button>Normal speed animation</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" animation="duration-500">
        <Button>Slow animation</Button>
      </Tooltip>
      <Tooltip content="Tooltip content" animation="duration-1000">
        <Button>Really slow animation</Button>
      </Tooltip>
    </div>
  );
}
```

## Disable arrow

You can disable the arrow of the tooltip component by passing the `arrow` prop with a value of `false`.

```tsx
// index.tsx

import { Button, Tooltip } from "flowbite-react";

export function Component() {
  return (
    <Tooltip content="Tooltip content" arrow={false}>
      <Button>Default tooltip</Button>
    </Tooltip>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "target": "w-fit",
  "animation": "transition-opacity",
  "arrow": {
    "base": "absolute z-10 h-2 w-2 rotate-45",
    "style": {
      "dark": "bg-gray-900 dark:bg-gray-700",
      "light": "bg-white",
      "auto": "bg-white dark:bg-gray-700"
    },
    "placement": "-4px"
  },
  "base": "absolute z-10 inline-block rounded-lg px-3 py-2 text-sm font-medium shadow-sm",
  "hidden": "invisible opacity-0",
  "style": {
    "dark": "bg-gray-900 text-white dark:bg-gray-700",
    "light": "border border-gray-200 bg-white text-gray-900",
    "auto": "border border-gray-200 bg-white text-gray-900 dark:border-none dark:bg-gray-700 dark:text-white"
  },
  "content": "relative z-20"
}
```

## References

- [Flowbite Tooltip](https://flowbite.com/docs/components/tooltips/)


---

# Forms

## File Input

# React File Input - Flowbite

> Get started with the file input component to let the user to upload one or more files from their device storage based on multiple styles and sizes

The `<FileInput>` component can be used to upload one or more files from the device storage of the user available in multiple sizes, styles, and variants and built with the utility-first classes from Tailwind CSS including support for dark mode.

Make sure that you have included Flowbite as a plugin inside your Tailwind CSS project to apply all the necessary styles for the `<FileInput>` component.

To start using the component make sure that you have imported it from Flowbite React:

```jsx
import { FileInput } from "flowbite-react";
```

## File upload example

Get started with a simple `<FileInput>` component to let users upload one single file.

```tsx
// index.tsx

import { FileInput, Label } from "flowbite-react";

export function Component() {
  return (
    <>
      <Label className="mb-2 block" htmlFor="file-upload">
        Upload file
      </Label>
      <FileInput id="file-upload" />
    </>
  );
}
```

## Helper text

Add a descriptive helper text to inform users the allowed extensions and sizes of the files.

```tsx
// index.tsx

import { FileInput, HelperText, Label } from "flowbite-react";

export function Component() {
  return (
    <>
      <Label className="mb-2 block" htmlFor="file-upload-helper-text">
        Upload file
      </Label>
      <FileInput id="file-upload-helper-text" />
      <HelperText className="mt-1">SVG, PNG, JPG or GIF (MAX. 800x400px).</HelperText>
    </>
  );
}
```

## Multiple files

Apply the multiple attribute to the `<FileInput>` component to allow more files to be uploaded.

```tsx
// index.tsx

import { FileInput, Label } from "flowbite-react";

export function Component() {
  return (
    <>
      <Label className="mb-2 block" htmlFor="multiple-file-upload">
        Upload multiple files
      </Label>
      <FileInput id="multiple-file-upload" multiple />
    </>
  );
}
```

## Sizes

Choose from the small, default, and large `<FileInput>` sizing options.

```tsx
// index.tsx

import { FileInput, Label } from "flowbite-react";

export function Component() {
  return (
    <div className="space-y-5">
      <div>
        <Label className="mb-2 block" htmlFor="small-file-upload">
          Small file input
        </Label>
        <FileInput id="small-file-upload" sizing="sm" />
      </div>
      <div>
        <Label className="mb-2 block" htmlFor="default-file-upload">
          Default size file input
        </Label>
        <FileInput id="default-file-upload" />
      </div>
      <div>
        <Label className="mb-2 block" htmlFor="large-file-upload">
          Large file input
        </Label>
        <FileInput id="large-file-upload" sizing="lg" />
      </div>
    </div>
  );
}
```

## Dropzone

The dropzone `<FileInput>` component can be used to upload one or more files by clicking anywhere in the area.

```tsx
// index.tsx

import { FileInput, Label } from "flowbite-react";

export function Component() {
  return (
    <div className="flex w-full items-center justify-center">
      <Label
        htmlFor="dropzone-file"
        className="flex h-64 w-full cursor-pointer flex-col items-center justify-center rounded-lg border-2 border-dashed border-gray-300 bg-gray-50 hover:bg-gray-100 dark:border-gray-600 dark:bg-gray-700 dark:hover:border-gray-500 dark:hover:bg-gray-600"
      >
        <div className="flex flex-col items-center justify-center pb-6 pt-5">
          <svg
            className="mb-4 h-8 w-8 text-gray-500 dark:text-gray-400"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 20 16"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
            />
          </svg>
          <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
            <span className="font-semibold">Click to upload</span> or drag and drop
          </p>
          <p className="text-xs text-gray-500 dark:text-gray-400">SVG, PNG, JPG or GIF (MAX. 800x400px)</p>
        </div>
        <FileInput id="dropzone-file" className="hidden" />
      </Label>
    </div>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "base": "block w-full cursor-pointer rounded-lg border file:-ms-4 file:me-4 file:cursor-pointer file:border-none file:bg-gray-800 file:py-2.5 file:pe-4 file:ps-8 file:text-sm file:font-medium file:leading-[inherit] file:text-white hover:file:bg-gray-700 focus:outline-none focus:ring-1 dark:file:bg-gray-600 dark:hover:file:bg-gray-500",
  "sizes": {
    "sm": "text-xs",
    "md": "text-sm",
    "lg": "text-lg"
  },
  "colors": {
    "gray": "border-gray-300 bg-gray-50 text-gray-900 focus:border-primary-500 focus:ring-primary-500 dark:border-gray-600 dark:bg-gray-700 dark:text-gray-400 dark:placeholder-gray-400 dark:focus:border-primary-500 dark:focus:ring-primary-500",
    "info": "border-cyan-500 bg-cyan-50 text-cyan-900 placeholder-cyan-700 focus:border-cyan-500 focus:ring-cyan-500 dark:border-cyan-400 dark:bg-cyan-100 dark:focus:border-cyan-500 dark:focus:ring-cyan-500",
    "failure": "border-red-500 bg-red-50 text-red-900 placeholder-red-700 focus:border-red-500 focus:ring-red-500 dark:border-red-400 dark:bg-red-100 dark:focus:border-red-500 dark:focus:ring-red-500",
    "warning": "border-yellow-500 bg-yellow-50 text-yellow-900 placeholder-yellow-700 focus:border-yellow-500 focus:ring-yellow-500 dark:border-yellow-400 dark:bg-yellow-100 dark:focus:border-yellow-500 dark:focus:ring-yellow-500",
    "success": "border-green-500 bg-green-50 text-green-900 placeholder-green-700 focus:border-green-500 focus:ring-green-500 dark:border-green-400 dark:bg-green-100 dark:focus:border-green-500 dark:focus:ring-green-500"
  }
}
```

## References

- [Flowbite File Input](https://flowbite.com/docs/forms/file-input/)


---

## Floating Label

# React Floating Label - Flowbite

> Use the floating label style for the input field elements to replicate the Material UI design system from Google and choose from multiple styles and sizes

The floating label style was first pioneered by Google in its infamous Material UI design system and it's basically a label tag which floats just above the input field when it is being focused or already has content inside.

On this page you will find a three different input field styles including a standard, outlined, and filled style including validation styles and sizes coded with Tailwind CSS and supported for dark mod

## Floating label example

Get started with the following three styles for the floating label component and use the label tag as a visual placeholder using the peer-placeholder-shown and peer-focus utility classes from Tailwind CSS.

```tsx
// index.tsx

import { FloatingLabel } from "flowbite-react";

export function Component() {
  return (
    <div className="grid grid-flow-col justify-stretch space-x-4">
      <FloatingLabel variant="filled" label="Label" />
      <FloatingLabel variant="outlined" label="Label" />
      <FloatingLabel variant="standard" label="Label" />
    </div>
  );
}
```

## Disabled state

Apply the disabled attribute to the input fields to disallow the user from changing the content.

```tsx
// index.tsx

import { FloatingLabel } from "flowbite-react";

export function Component() {
  return (
    <div className="grid grid-flow-col justify-stretch space-x-4">
      <FloatingLabel variant="filled" label="Label" disabled={true} />
      <FloatingLabel variant="outlined" label="Label" disabled={true} />
      <FloatingLabel variant="standard" label="Label" disabled={true} />
    </div>
  );
}
```

## Validation

Use the following examples of input validation for the success and error messages by applying the validation text below the input field and using the green or red color classes from Tailwind CSS.

```tsx
// index.tsx

import { FloatingLabel } from "flowbite-react";

export function Component() {
  return (
    <>
      <div className="grid grid-flow-col justify-stretch space-x-4">
        <FloatingLabel variant="filled" label="Filled Success" color="success" />
        <FloatingLabel variant="outlined" label="Outlined Success" color="success" />
        <FloatingLabel variant="standard" label="Standard Success" color="success" />
      </div>
      <div className="grid grid-flow-col justify-stretch space-x-4">
        <FloatingLabel variant="filled" label="Filled Error" color="error" />
        <FloatingLabel variant="outlined" label="Outlined Error" color="error" />
        <FloatingLabel variant="standard" label="Standard Error" color="error" />
      </div>
    </>
  );
}
```

## Sizes

Use the small and default sizes of the floating label input fields from the following example.

```tsx
// index.tsx

import { FloatingLabel } from "flowbite-react";

export function Component() {
  return (
    <>
      <div className="grid grid-flow-col justify-stretch space-x-4">
        <FloatingLabel variant="filled" label="Small Filled" sizing="sm" />
        <FloatingLabel variant="outlined" label="Small Outlined" sizing="sm" />
        <FloatingLabel variant="standard" label="Small Standard" sizing="sm" />
      </div>
      <div className="grid grid-flow-col justify-stretch space-x-4">
        <FloatingLabel variant="filled" label="Default Filled" />
        <FloatingLabel variant="outlined" label="Default Outlined" />
        <FloatingLabel variant="standard" label="Default Standard" />
      </div>
    </>
  );
}
```

## Helper text

Add a helper text in addition to the label if you want to show more information below the input field.

```tsx
// index.tsx

import { FloatingLabel, HelperText } from "flowbite-react";

export function Component() {
  return (
    <>
      <FloatingLabel variant="filled" label="Floating Helper" />
      <HelperText>Remember, contributions to this topic should follow our Community Guidelines.</HelperText>
    </>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "input": {
    "default": {
      "filled": {
        "sm": "peer block w-full appearance-none rounded-t-lg border-0 border-b-2 border-gray-300 bg-gray-50 px-2.5 pb-2.5 pt-5 text-xs text-gray-900 focus:border-primary-600 focus:outline-none focus:ring-0 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-primary-500",
        "md": "peer block w-full appearance-none rounded-t-lg border-0 border-b-2 border-gray-300 bg-gray-50 px-2.5 pb-2.5 pt-5 text-sm text-gray-900 focus:border-primary-600 focus:outline-none focus:ring-0 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-primary-500"
      },
      "outlined": {
        "sm": "peer block w-full appearance-none rounded-lg border border-gray-300 bg-transparent px-2.5 pb-2.5 pt-4 text-xs text-gray-900 focus:border-primary-600 focus:outline-none focus:ring-0 dark:border-gray-600 dark:text-white dark:focus:border-primary-500",
        "md": "peer block w-full appearance-none rounded-lg border border-gray-300 bg-transparent px-2.5 pb-2.5 pt-4 text-sm text-gray-900 focus:border-primary-600 focus:outline-none focus:ring-0 dark:border-gray-600 dark:text-white dark:focus:border-primary-500"
      },
      "standard": {
        "sm": "peer block w-full appearance-none border-0 border-b-2 border-gray-300 bg-transparent px-0 py-2.5 text-xs text-gray-900 focus:border-primary-600 focus:outline-none focus:ring-0 dark:border-gray-600 dark:text-white dark:focus:border-primary-500",
        "md": "peer block w-full appearance-none border-0 border-b-2 border-gray-300 bg-transparent px-0 py-2.5 text-sm text-gray-900 focus:border-primary-600 focus:outline-none focus:ring-0 dark:border-gray-600 dark:text-white dark:focus:border-primary-500"
      }
    },
    "success": {
      "filled": {
        "sm": "peer block w-full appearance-none rounded-t-lg border-0 border-b-2 border-green-600 bg-gray-50 px-2.5 pb-2.5 pt-5 text-xs text-gray-900 focus:border-green-600 focus:outline-none focus:ring-0 dark:border-green-500 dark:bg-gray-700 dark:text-white dark:focus:border-green-500",
        "md": "peer block w-full appearance-none rounded-t-lg border-0 border-b-2 border-green-600 bg-gray-50 px-2.5 pb-2.5 pt-5 text-sm text-gray-900 focus:border-green-600 focus:outline-none focus:ring-0 dark:border-green-500 dark:bg-gray-700 dark:text-white dark:focus:border-green-500"
      },
      "outlined": {
        "sm": "peer block w-full appearance-none rounded-lg border border-green-600 bg-transparent px-2.5 pb-2.5 pt-4 text-xs text-gray-900 focus:border-green-600 focus:outline-none focus:ring-0 dark:border-green-500 dark:text-white dark:focus:border-green-500",
        "md": "peer block w-full appearance-none rounded-lg border border-green-600 bg-transparent px-2.5 pb-2.5 pt-4 text-sm text-gray-900 focus:border-green-600 focus:outline-none focus:ring-0 dark:border-green-500 dark:text-white dark:focus:border-green-500"
      },
      "standard": {
        "sm": "peer block w-full appearance-none border-0 border-b-2 border-green-600 bg-transparent px-0 py-2.5 text-xs text-gray-900 focus:border-green-600 focus:outline-none focus:ring-0 dark:border-green-500 dark:text-white dark:focus:border-green-500",
        "md": "peer block w-full appearance-none border-0 border-b-2 border-green-600 bg-transparent px-0 py-2.5 text-sm text-gray-900 focus:border-green-600 focus:outline-none focus:ring-0 dark:border-green-500 dark:text-white dark:focus:border-green-500"
      }
    },
    "error": {
      "filled": {
        "sm": "peer block w-full appearance-none rounded-t-lg border-0 border-b-2 border-red-600 bg-gray-50 px-2.5 pb-2.5 pt-5 text-xs text-gray-900 focus:border-red-600 focus:outline-none focus:ring-0 dark:border-red-500 dark:bg-gray-700 dark:text-white dark:focus:border-red-500",
        "md": "peer block w-full appearance-none rounded-t-lg border-0 border-b-2 border-red-600 bg-gray-50 px-2.5 pb-2.5 pt-5 text-sm text-gray-900 focus:border-red-600 focus:outline-none focus:ring-0 dark:border-red-500 dark:bg-gray-700 dark:text-white dark:focus:border-red-500"
      },
      "outlined": {
        "sm": "peer block w-full appearance-none rounded-lg border border-red-600 bg-transparent px-2.5 pb-2.5 pt-4 text-xs text-gray-900 focus:border-red-600 focus:outline-none focus:ring-0 dark:border-red-500 dark:text-white dark:focus:border-red-500",
        "md": "peer block w-full appearance-none rounded-lg border border-red-600 bg-transparent px-2.5 pb-2.5 pt-4 text-sm text-gray-900 focus:border-red-600 focus:outline-none focus:ring-0 dark:border-red-500 dark:text-white dark:focus:border-red-500"
      },
      "standard": {
        "sm": "peer block w-full appearance-none border-0 border-b-2 border-red-600 bg-transparent px-0 py-2.5 text-xs text-gray-900 focus:border-red-600 focus:outline-none focus:ring-0 dark:border-red-500 dark:text-white dark:focus:border-red-500",
        "md": "peer block w-full appearance-none border-0 border-b-2 border-red-600 bg-transparent px-0 py-2.5 text-sm text-gray-900 focus:border-red-600 focus:outline-none focus:ring-0 dark:border-red-500 dark:text-white dark:focus:border-red-500"
      }
    }
  },
  "label": {
    "default": {
      "filled": {
        "sm": "absolute left-2.5 top-4 z-10 origin-[0] -translate-y-4 scale-75 text-xs text-gray-500 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:text-primary-600 dark:text-gray-400 peer-focus:dark:text-primary-500",
        "md": "absolute left-2.5 top-4 z-10 origin-[0] -translate-y-4 scale-75 text-sm text-gray-500 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:text-primary-600 dark:text-gray-400 peer-focus:dark:text-primary-500"
      },
      "outlined": {
        "sm": "absolute left-1 top-2 z-10 origin-[0] -translate-y-4 scale-75 bg-white px-2 text-xs text-gray-500 transition-transform duration-300 peer-placeholder-shown:top-1/2 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:scale-100 peer-focus:top-2 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:px-2 peer-focus:text-primary-600 dark:bg-gray-900 dark:text-gray-400 peer-focus:dark:text-primary-500",
        "md": "absolute left-1 top-2 z-10 origin-[0] -translate-y-4 scale-75 bg-white px-2 text-sm text-gray-500 transition-transform duration-300 peer-placeholder-shown:top-1/2 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:scale-100 peer-focus:top-2 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:px-2 peer-focus:text-primary-600 dark:bg-gray-900 dark:text-gray-400 peer-focus:dark:text-primary-500"
      },
      "standard": {
        "sm": "absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 text-xs text-gray-500 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-primary-600 dark:text-gray-400 peer-focus:dark:text-primary-500",
        "md": "absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 text-sm text-gray-500 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-primary-600 dark:text-gray-400 peer-focus:dark:text-primary-500"
      }
    },
    "success": {
      "filled": {
        "sm": "absolute left-2.5 top-4 z-10 origin-[0] -translate-y-4 scale-75 text-sm text-green-600 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:-translate-y-4 peer-focus:scale-75 dark:text-green-500",
        "md": "absolute left-2.5 top-4 z-10 origin-[0] -translate-y-4 scale-75 text-sm text-green-600 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:-translate-y-4 peer-focus:scale-75 dark:text-green-500"
      },
      "outlined": {
        "sm": "absolute left-1 top-2 z-10 origin-[0] -translate-y-4 scale-75 bg-white px-2 text-sm text-green-600 transition-transform duration-300 peer-placeholder-shown:top-1/2 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:scale-100 peer-focus:top-2 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:px-2 dark:bg-gray-900 dark:text-green-500",
        "md": "absolute left-1 top-2 z-10 origin-[0] -translate-y-4 scale-75 bg-white px-2 text-sm text-green-600 transition-transform duration-300 peer-placeholder-shown:top-1/2 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:scale-100 peer-focus:top-2 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:px-2 dark:bg-gray-900 dark:text-green-500"
      },
      "standard": {
        "sm": "absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 text-xs text-green-600 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 dark:text-green-500",
        "md": "absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 text-sm text-green-600 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 dark:text-green-500"
      }
    },
    "error": {
      "filled": {
        "sm": "absolute left-2.5 top-4 z-10 origin-[0] -translate-y-4 scale-75 text-xs text-red-600 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:-translate-y-4 peer-focus:scale-75 dark:text-red-500",
        "md": "absolute left-2.5 top-4 z-10 origin-[0] -translate-y-4 scale-75 text-xs text-red-600 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:-translate-y-4 peer-focus:scale-75 dark:text-red-500"
      },
      "outlined": {
        "sm": "absolute left-1 top-2 z-10 origin-[0] -translate-y-4 scale-75 bg-white px-2 text-xs text-red-600 transition-transform duration-300 peer-placeholder-shown:top-1/2 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:scale-100 peer-focus:top-2 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:px-2 dark:bg-gray-900 dark:text-red-500",
        "md": "absolute left-1 top-2 z-10 origin-[0] -translate-y-4 scale-75 bg-white px-2 text-xs text-red-600 transition-transform duration-300 peer-placeholder-shown:top-1/2 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:scale-100 peer-focus:top-2 peer-focus:-translate-y-4 peer-focus:scale-75 peer-focus:px-2 dark:bg-gray-900 dark:text-red-500"
      },
      "standard": {
        "sm": "absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 text-xs text-red-600 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 dark:text-red-500",
        "md": "absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 text-sm text-red-600 transition-transform duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 dark:text-red-500"
      }
    }
  }
}
```

## References

- [Flowbite Floating Label](https://flowbite.com/docs/forms/floating-label/)


---

# Typography

## Blockquote

# React Blockquote - Flowbite

> The blockquote component can be used to quote text content from an external source that can be used for testimonials, reviews, and quotes inside an article

Get started with a collection of blockquote components when quoting external sources such as quotes inside an article, user reviews, and testimonials based on multiple examples of layouts, styles, and contexts.

The main `<Blockquote>` component can be used together with the `<cite>` tag or attribute to also mention the source of the quote content.

To start using the component make sure that you have imported it from Flowbite React:

```jsx
import { Blockquote } from "flowbite-react";
```

## Default blockquote

Use this example to quote an external source inside a `<Blockquote>` component.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <Blockquote>
      "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
      complex dashboard. Perfect choice for your next SaaS application."
    </Blockquote>
  );
}
```

## Solid background

This example can be used as an alternative style to the default one by applying a solid background color.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <>
      <p className="text-gray-500 dark:text-gray-400">
        Does your user know how to exit out of screens? Can they follow your intended user journey and buy something
        from the site you’ve designed? By running a usability test, you’ll be able to see how users will interact with
        your design once it’s live.
      </p>
      <Blockquote className="my-4 border-l-4 border-gray-300 bg-gray-50 p-4 dark:border-gray-500 dark:bg-gray-800">
        "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
        complex dashboard. Perfect choice for your next SaaS application."
      </Blockquote>
      First of all you need to understand how Flowbite works. This library is not another framework. Rather, it is a set
      of components based on Tailwind CSS that you can just copy-paste from the documentation.
    </>
  );
}
```

## Blockquote icon

Use this example to show an icon above the blockquote text content.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <Blockquote>
      <svg
        className="mb-4 h-8 w-8 text-gray-400 dark:text-gray-600"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        viewBox="0 0 18 14"
      >
        <path d="M6 0H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3H2a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Zm10 0h-4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3h-1a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Z" />
      </svg>
      "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
      complex dashboard. Perfect choice for your next SaaS application."
    </Blockquote>
  );
}
```

## Paragraph context

Use this example to show a `<Blockquote>` component between multiple paragraph elements.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <>
      <p className="mb-3 text-gray-500 dark:text-gray-400">
        Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest
        data from other software development tools, so your IT support and operations teams have richer contextual
        information to rapidly respond to requests, incidents, and changes.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 md:gap-6">
        <p className="mb-3 text-gray-500 dark:text-gray-400">
          Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest
          data from other software development tools, so your IT support and operations teams have richer contextual
          information to rapidly respond to requests, incidents, and changes.
        </p>
        <Blockquote className="mb-3">
          <p className="text-xl font-semibold italic text-gray-900 dark:text-white">
            " Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen
            to complex dashboard. Perfect choice for your next SaaS application. "
          </p>
        </Blockquote>
      </div>
      <p className="mb-3 text-gray-500 dark:text-gray-400">
        Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate
        critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every
        change.
      </p>
    </>
  );
}
```

## User testimonial

This example can be used for user testimonials by mentioning the author and occupation of the author.

```tsx
// index.tsx

import { Avatar, Blockquote } from "flowbite-react";

export function Component() {
  return (
    <figure className="mx-auto max-w-screen-md text-center">
      <svg
        className="mx-auto mb-3 h-10 w-10 text-gray-400 dark:text-gray-600"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        viewBox="0 0 18 14"
      >
        <path d="M6 0H2a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3H2a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Zm10 0h-4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h4v1a3 3 0 0 1-3 3h-1a1 1 0 0 0 0 2h1a5.006 5.006 0 0 0 5-5V2a2 2 0 0 0-2-2Z" />
      </svg>
      <Blockquote>
        <p className="text-2xl font-medium italic text-gray-900 dark:text-white">
          "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
          complex dashboard. Perfect choice for your next SaaS application."
        </p>
      </Blockquote>
      <figcaption className="mt-6 flex items-center justify-center space-x-3">
        <Avatar rounded size="xs" img="/images/people/profile-picture-5.jpg" alt="profile picture" />
        <div className="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
          <cite className="pr-3 font-medium text-gray-900 dark:text-white">Micheal Gough</cite>
          <cite className="pl-3 text-sm text-gray-500 dark:text-gray-400">CEO at Google</cite>
        </div>
      </figcaption>
    </figure>
  );
}
```

## User Review

Use this example to show a user review with rating stars and the name and occupation of the author.

```tsx
// index.tsx

import { Avatar, Blockquote, Rating, RatingStar } from "flowbite-react";

export function Component() {
  return (
    <figure className="max-w-screen-md">
      <div className="mb-4 flex items-center">
        <Rating size="md">
          <RatingStar />
          <RatingStar />
          <RatingStar />
          <RatingStar />
          <RatingStar />
        </Rating>
      </div>
      <Blockquote>
        <p className="text-2xl font-semibold text-gray-900 dark:text-white">
          "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
          complex dashboard. Perfect choice for your next SaaS application."
        </p>
      </Blockquote>
      <figcaption className="mt-6 flex items-center space-x-3">
        <Avatar rounded size="xs" img="/images/people/profile-picture-3.jpg" alt="profile picture" />
        <div className="flex items-center divide-x-2 divide-gray-300 dark:divide-gray-700">
          <cite className="pr-3 font-medium text-gray-900 dark:text-white">Bonnie Green</cite>
          <cite className="pl-3 text-sm text-gray-500 dark:text-gray-400">CTO at Flowbite</cite>
        </div>
      </figcaption>
    </figure>
  );
}
```

## Alignment

Choose from the following examples the blockquote text alignment from starting from left, center to right based on the utility classes from Tailwind CSS.

### Left

The default alignment of the blockquote text content is the left side of the document.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <Blockquote>
      "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
      complex dashboard. Perfect choice for your next SaaS application."
    </Blockquote>
  );
}
```

### Center

Use the text-center class from Tailwind CSS to align the text content inside the blockquote to the center.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <Blockquote className="text-center">
      "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
      complex dashboard. Perfect choice for your next SaaS application."
    </Blockquote>
  );
}
```

### Right

Use the text-right utility class from Tailwind CSS to align the blockquote text content to the right side of the page.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <Blockquote className="text-right">
      "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
      complex dashboard. Perfect choice for your next SaaS application."
    </Blockquote>
  );
}
```

## Sizes

Choose from one of the multiple sizes for the default blockquote component based on the surrounding elements and sizes.

### Small

Use the text-lg font size class from Tailwind CSS to apply the small size for the blockquote component.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <Blockquote className="text-lg">
      "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
      complex dashboard. Perfect choice for your next SaaS application."
    </Blockquote>
  );
}
```

### Medium

Use the text-xl utility class to set the default size for the blockquote element.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <Blockquote className="text-xl">
      "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
      complex dashboard. Perfect choice for your next SaaS application."
    </Blockquote>
  );
}
```

### Large

The text-2xl class can be used to set a large size for the blockquote component.

```tsx
// index.tsx

import { Blockquote } from "flowbite-react";

export function Component() {
  return (
    <Blockquote className="text-2xl">
      "Flowbite is just awesome. It contains tons of predesigned components and pages starting from login screen to
      complex dashboard. Perfect choice for your next SaaS application."
    </Blockquote>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "text-xl font-semibold italic text-gray-900 dark:text-white"
  }
}
```

## References

- [Flowbite Blockquote](https://flowbite.com/docs/typography/blockquote/)


---

## HR

# React Horizontal Line (HR) - Flowbite

> Create a horizontal line using the HR tag to separate content such as paragraphs, blockquotes, and other elements using the utility classes from Tailwind CSS

The HR component can be used to separate content using a horizontal line by adding space between elements based on multiple styles, variants, and layouts.

## Default HR

Use this example to separate text content with a `<hr />` horizontal line.

```tsx
// index.tsx

import { HR } from "flowbite-react";

function Component() {
  return (
    <>
      <p className="text-gray-500 dark:text-gray-400">
        Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest
        data from other software development tools, so your IT support and operations teams have richer contextual
        information to rapidly respond to requests, incidents, and changes.
      </p>
      <HR />
      <p className="text-gray-500 dark:text-gray-400">
        Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate
        critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every
        change.
      </p>
    </>
  );
}
```

## Trimmed

Use this example to show a shorter version of the horizontal line.

```tsx
// index.tsx

import { HRTrimmed } from "flowbite-react";

function Component() {
  return (
    <>
      <p className="text-gray-500 dark:text-gray-400">
        Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest
        data from other software development tools, so your IT support and operations teams have richer contextual
        information to rapidly respond to requests, incidents, and changes.
      </p>
      <HRTrimmed />
      <p className="text-gray-500 dark:text-gray-400">
        Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate
        critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every
        change.
      </p>
    </>
  );
}
```

## Icon HR

This example can be used to set a custom [SVG icon](https://flowbite.com/icons/) in the middle of the HR element.

```tsx
// index.tsx

import { HRIcon } from "flowbite-react";

function Component() {
  return (
    <>
      <p className="text-gray-500 dark:text-gray-400">
        Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest
        data from other software development tools, so your IT support and operations teams have richer contextual
        information to rapidly respond to requests, incidents, and changes.
      </p>
      <HRIcon />
      <p className="text-gray-500 dark:text-gray-400">
        Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate
        critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every
        change.
      </p>
    </>
  );
}
```

## HR with Text

Use this example to add a text in the middle of the HR component.

```tsx
// index.tsx

import { HRText } from "flowbite-react";

function Component() {
  return (
    <>
      <p className="text-gray-500 dark:text-gray-400">
        Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest
        data from other software development tools, so your IT support and operations teams have richer contextual
        information to rapidly respond to requests, incidents, and changes.
      </p>
      <HRText text="or" />
      <p className="text-gray-500 dark:text-gray-400">
        Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate
        critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every
        change.
      </p>
    </>
  );
}
```

## HR Shape (square)

This example can be used to separate content with an HR tag as a shape instead of a line.

```tsx
// index.tsx

import { HRSquare } from "flowbite-react";

function Component() {
  return (
    <>
      <p className="text-gray-500 dark:text-gray-400">
        Track work across the enterprise through an open, collaborative platform. Link issues across Jira and ingest
        data from other software development tools, so your IT support and operations teams have richer contextual
        information to rapidly respond to requests, incidents, and changes.
      </p>
      <HRSquare />
      <p className="text-gray-500 dark:text-gray-400">
        Deliver great service experiences fast - without the complexity of traditional ITSM solutions.Accelerate
        critical development work, eliminate toil, and deploy changes with ease, with a complete audit trail for every
        change.
      </p>
    </>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "my-8 h-px border-0 bg-gray-200 dark:bg-gray-700"
  },
  "trimmed": {
    "base": "mx-auto my-4 h-1 w-48 rounded border-0 bg-gray-100 md:my-10 dark:bg-gray-700"
  },
  "icon": {
    "base": "inline-flex w-full items-center justify-center",
    "hrLine": "my-8 h-1 w-64 rounded border-0 bg-gray-200 dark:bg-gray-700",
    "icon": {
      "base": "absolute left-1/2 -translate-x-1/2 bg-white px-4 dark:bg-gray-900",
      "icon": "h-4 w-4 text-gray-700 dark:text-gray-300"
    }
  },
  "text": {
    "base": "inline-flex w-full items-center justify-center",
    "hrLine": "my-8 h-px w-64 border-0 bg-gray-200 dark:bg-gray-700",
    "text": "absolute left-1/2 -translate-x-1/2 bg-white px-3 font-medium text-gray-900 dark:bg-gray-900 dark:text-white"
  },
  "square": {
    "base": "mx-auto my-8 h-8 w-8 rounded border-0 bg-gray-200 md:my-12 dark:bg-gray-700"
  }
}
```

## References

- [Flowbite HR](https://flowbite.com/docs/typography/hr/)


---

## List

# React Lists - Flowbite

> Use the list component to show an unordered or ordered list of items based on multiple styles, layouts, and variants built with Tailwind CSS and Flowbite

Get started with a collection of list components built with Tailwind CSS for ordered and unordered lists with bullets, numbers, or icons and other styles and layouts to show a list of items inside an article or throughout your web page.

Start using the list component by first importing it from Flowbite React:

```jsx
import { List } from "flowbite-react";
```

## Default list

Use this example to create a default unordered list of items using the `List` component with `List.Item` child components inside of it.

```tsx
// index.tsx

import { List, ListItem } from "flowbite-react";

export function Component() {
  return (
    <List>
      <ListItem>At least 10 characters (and up to 100 characters)</ListItem>
      <ListItem>At least one lowercase character</ListItem>
      <ListItem>Inclusion of at least one special character, e.g., ! @ # ?</ListItem>
    </List>
  );
}
```

## Icons

This example can be used to apply custom icons instead of the default bullets for the list items.

```tsx
// index.tsx

"use client";

import { List, ListItem } from "flowbite-react";
import { HiCheckCircle } from "react-icons/hi";

export function Component() {
  return (
    <List>
      <ListItem icon={HiCheckCircle}>At least 10 characters (and up to 100 characters)</ListItem>
      <ListItem icon={HiCheckCircle}>At least one lowercase character</ListItem>
      <ListItem icon={HiCheckCircle}>Inclusion of at least one special character, e.g., ! @ # ?</ListItem>
    </List>
  );
}
```

## Nested

Use this example to nest another list of items inside the parent list element.

```tsx
// index.tsx

import { List, ListItem } from "flowbite-react";

export function Component() {
  return (
    <List>
      <ListItem>
        List item one
        <List ordered nested>
          <ListItem>You might feel like you are being really "organized" o</ListItem>
          <ListItem>Nested navigation in UIs is a bad idea too, keep things as flat as possible.</ListItem>
          <ListItem>Nesting tons of folders in your source code is also not helpful.</ListItem>
        </List>
      </ListItem>
      <ListItem>
        List item two
        <List ordered nested>
          <ListItem>I'm not sure if we'll bother styling more than two levels deep.</ListItem>
          <ListItem>Two is already too much, three is guaranteed to be a bad idea.</ListItem>
          <ListItem>If you nest four levels deep you belong in prison.</ListItem>
        </List>
      </ListItem>
      <ListItem>
        List item three
        <List ordered nested>
          <ListItem>Again please don't nest lists if you want</ListItem>
          <ListItem>Nobody wants to look at this.</ListItem>
          <ListItem>I'm upset that we even have to bother styling this.</ListItem>
        </List>
      </ListItem>
    </List>
  );
}
```

## Unstyled

Use the `unstyled` prop to disable the list style bullets or numbers.

```tsx
// index.tsx

import { List, ListItem } from "flowbite-react";

export function Component() {
  return (
    <List unstyled>
      <ListItem>At least 10 characters (and up to 100 characters)</ListItem>
      <ListItem>At least one lowercase character</ListItem>
      <ListItem>Inclusion of at least one special character, e.g., ! @ # ?</ListItem>
    </List>
  );
}
```

## Ordered list

Use the `ordered` prop tag to create an ordered list of items with numbers.

```tsx
// index.tsx

import { List, ListItem } from "flowbite-react";

export function Component() {
  return (
    <List ordered>
      <ListItem>At least 10 characters (and up to 100 characters)</ListItem>
      <ListItem>At least one lowercase character</ListItem>
      <ListItem>Inclusion of at least one special character, e.g., ! @ # ?</ListItem>
    </List>
  );
}
```

## Advanced layout

This example can be used to show more details for each list item such as the user's name, email and profile picture.

```tsx
// index.tsx

import { Avatar, List, ListItem } from "flowbite-react";

export function Component() {
  return (
    <List unstyled className="max-w-md divide-y divide-gray-200 dark:divide-gray-700">
      <ListItem className="pb-3 sm:pb-4">
        <div className="flex items-center space-x-4 rtl:space-x-reverse">
          <Avatar img="/images/people/profile-picture-1.jpg" alt="Neil image" rounded size="sm" />
          <div className="min-w-0 flex-1">
            <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Neil Sims</p>
            <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@flowbite.com</p>
          </div>
          <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">$320</div>
        </div>
      </ListItem>
      <ListItem className="py-3 sm:py-4">
        <div className="flex items-center space-x-4 rtl:space-x-reverse">
          <Avatar img="/images/people/profile-picture-3.jpg" alt="Neil image" rounded size="sm" />
          <div className="min-w-0 flex-1">
            <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Bonnie Green</p>
            <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@flowbite.com</p>
          </div>
          <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">$3467</div>
        </div>
      </ListItem>
      <ListItem className="py-3 sm:py-4">
        <div className="flex items-center space-x-4 rtl:space-x-reverse">
          <Avatar img="/images/people/profile-picture-2.jpg" alt="Neil image" rounded size="sm" />
          <div className="min-w-0 flex-1">
            <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Michael Gough</p>
            <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@flowbite.com</p>
          </div>
          <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">$67</div>
        </div>
      </ListItem>
      <ListItem className="py-3 sm:py-4">
        <div className="flex items-center space-x-4 rtl:space-x-reverse">
          <Avatar img="/images/people/profile-picture-5.jpg" alt="Neil image" rounded size="sm" />
          <div className="min-w-0 flex-1">
            <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Thomas Lean</p>
            <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@flowbite.com</p>
          </div>
          <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">$2367</div>
        </div>
      </ListItem>
      <ListItem className="pb-0 pt-3 sm:pt-4">
        <div className="flex items-center space-x-4 rtl:space-x-reverse">
          <Avatar img="/images/people/profile-picture-4.jpg" alt="Neil image" rounded size="sm" />
          <div className="min-w-0 flex-1">
            <p className="truncate text-sm font-medium text-gray-900 dark:text-white">Lana Byrd</p>
            <p className="truncate text-sm text-gray-500 dark:text-gray-400">email@flowbite.com</p>
          </div>
          <div className="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white">$367</div>
        </div>
      </ListItem>
    </List>
  );
}
```

## Horizontal list

Use this example to create a horizontally aligned list of items.

```tsx
// index.tsx

import { List, ListItem } from "flowbite-react";

export function Component() {
  return (
    <List horizontal>
      <ListItem>About</ListItem>
      <ListItem>Premium</ListItem>
      <ListItem>Campaigns</ListItem>
      <ListItem>Blog</ListItem>
      <ListItem>Affiliate Program</ListItem>
      <ListItem>FAQs</ListItem>
      <ListItem>Contact</ListItem>
    </List>
  );
}
```

## Theme

To learn more about how to customize the appearance of components, please see the [Theme docs](https://flowbite-react.com/docs/customize/theme.md).

```json
{
  "root": {
    "base": "list-inside space-y-1 text-gray-500 dark:text-gray-400",
    "ordered": {
      "off": "list-disc",
      "on": "list-decimal"
    },
    "horizontal": "flex list-none flex-wrap items-center justify-center space-x-4 space-y-0",
    "unstyled": "list-none",
    "nested": "mt-2 ps-5"
  },
  "item": {
    "withIcon": {
      "off": "",
      "on": "flex items-center"
    },
    "icon": "me-2 h-3.5 w-3.5 shrink-0"
  }
}
```

## References

- [Flowbite List](https://flowbite.com/docs/typography/list/)


---