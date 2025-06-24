# React Router v7

> React Router v7 is a powerful, multi-strategy routing library for React, bridging the gap from React 18 to React 19. It enables developers to build client-side, server-side, or statically pre-rendered web applications with robust data loading, mutations, and navigation features. You can use it maximally as a React framework or as minimally as you want.

React Router v7 offers a comprehensive solution for routing in React applications, supporting various rendering strategies and data management patterns. It aims to simplify data fetching, mutations, and state synchronization with the server, while providing a great developer and user experience.

## Getting Started
### Picking a Mode
React Router v7 can be used in three primary modes, offering different levels of features and control:
-   **Declarative Mode**: Provides basic routing capabilities using JSX components like `<BrowserRouter>`, `<Routes>`, and `<Route>`. Suitable for simple client-side SPAs or when integrating with an existing data layer.
-   **Data Mode**: Introduces data loading (`loader`), data mutations (`action`), and pending UI states. Uses `createBrowserRouter` (or other data router creators) and `<RouterProvider>`. This mode brings powerful data management features directly into your routing layer.
-   **Framework Mode**: The most comprehensive mode, built on top of Data Mode and integrated with a Vite plugin (`@react-router/dev`). It offers features like automatic code splitting, route module type safety, server-side rendering (SSR), static site generation (SSG), and file-based routing conventions.

The choice of mode depends on your project's needs, from simple client-side routing to full-stack application development.

### Installation
**Framework Mode:**
Typically started with a template:
```shell
npx create-react-router@latest my-react-router-app
cd my-react-router-app
npm install
npm run dev
```
This sets up a Vite project with `@react-router/dev` and necessary configurations.

**Data Mode:**
Bootstrap your React app (e.g., with Vite) and install `react-router`:
```shell
npm install react-router
```
Then, create a router and render it using `<RouterProvider>`:
```tsx
import { createBrowserRouter, RouterProvider } from "react-router";
import ReactDOM from "react-dom/client";

const router = createBrowserRouter([
  { path: "/", element: <div>Hello World</div> },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <RouterProvider router={router} />
);
```

**Declarative Mode:**
Bootstrap your React app and install `react-router`:
```shell
npm install react-router
```
Wrap your application with `<BrowserRouter>`:
```tsx
import { BrowserRouter } from "react-router";
import ReactDOM from "react-dom/client";
import App from "./App"; // Your main app component

ReactDOM.createRoot(document.getElementById("root")!).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

### Basic Routing
**Framework Mode:**
Routes are configured in `app/routes.ts` using helper functions or file conventions.
Example `app/routes.ts`:
```ts
import { type RouteConfig, route, index } from "@react-router/dev/routes";

export default [
  index("./home.tsx"), // Root index route
  route("about", "./about.tsx"), // Matches /about
  route("users/:userId", "./user.tsx"), // Matches /users/someId
] satisfies RouteConfig;
```
Route modules (e.g., `home.tsx`) export components, loaders, actions, etc.

**Data Mode:**
Routes are defined as an array of route objects passed to `createBrowserRouter`.
```tsx
const router = createBrowserRouter([
  {
    path: "/",
    Component: HomePage,
    children: [
      { index: true, Component: HomeIndexPage },
      { path: "about", Component: AboutPage },
      { path: "users/:userId", Component: UserPage, loader: userLoader },
    ],
  },
]);
```

**Declarative Mode:**
Routes are defined using `<Routes>` and `<Route>` JSX components.
```tsx
import { Routes, Route } from "react-router";

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />}>
        <Route index element={<HomeIndexPage />} />
        <Route path="about" element={<AboutPage />} />
        <Route path="users/:userId" element={<UserPage />} />
      </Route>
    </Routes>
  );
}
```
**Common Routing Concepts:**
-   **Nested Routes**: Child routes render within a parent route's `<Outlet />` component.
-   **Layout Routes**: Routes that group children under a shared UI layout without adding to the URL path.
-   **Index Routes**: Default component for a parent's path.
-   **Dynamic Segments**: Path segments like `:userId` capture values from the URL, accessible via `params`.
-   **Splat Routes**: Path segments like `*` or `files/*` match any remaining URL parts.

## Core Features & Concepts

### Route Definitions and Modules
-   **Framework Mode**: Route modules (e.g., `app/routes/user.tsx`) are central. They export:
    -   `default` (Component): The React component to render.
    -   `loader`: Function to load data for the route.
    -   `action`: Function to handle data mutations.
    -   `ErrorBoundary`: Component to render if errors occur.
    -   `meta`, `links`, `headers`: For SEO and document metadata.
    -   `HydrateFallback`: Component shown during client-side hydration if `clientLoader.hydrate=true`.
-   **Data Mode**: Route objects passed to `createBrowserRouter` can have `Component`, `loader`, `action`, `errorElement`, `children`, etc. properties.
-   **Declarative Mode**: `<Route>` components take `path`, `element`, and `children`. Data loading/actions are not directly supported in this mode's route definitions.
-   **`<Outlet />`**: A component used in parent routes to render their matching child route. Context can be passed via `<Outlet context={...} />`.

### Data Loading
Data loading functions provide data to components before they render.
-   **`loader` function**: Defined in a route module (Framework) or route object (Data).
    -   Receives `{ request, params, context }`. `context` is server-specific.
    -   Can return any serializable data, or a `Response` (e.g., for redirects or 404s).
    -   In SSR/pre-rendering, runs on the server/build-time. For client navigations, called via `fetch`.
    ```tsx
    // Example loader
    export async function loader({ params }) {
      const product = await fetchProduct(params.productId);
      if (!product) throw new Response("Not Found", { status: 404 });
      return { product };
    }
    ```
-   **`clientLoader` function**: Runs only in the browser.
    -   Receives `{ request, params, serverLoader }`. `serverLoader` is a function to call the server `loader` if needed.
    -   Useful for client-only data or combining server and client data.
    -   Set `clientLoader.hydrate = true` to run during initial hydration; requires a `HydrateFallback` component.
    ```tsx
    // Example clientLoader
    export async function clientLoader({ params, serverLoader }) {
      const serverData = await serverLoader(); // Optional: get server data
      const clientSideData = await fetchClientSpecificData(params.id);
      return { ...serverData, ...clientSideData };
    }
    clientLoader.hydrate = true; // Run on hydration
    ```
-   **Accessing Data**:
    -   Via `loaderData` prop passed to the route component (Framework/Data with `Component` prop). Typesafe in Framework mode.
    -   Via `useLoaderData()` hook.
-   **`HydrateFallback`**: A component exported from a route module (Framework) or specified in a route object (Data) to display while `clientLoader` (with `hydrate=true`) is running on initial page load.

### Data Mutations (Actions)
Actions handle data changes (e.g., form submissions).
-   **`action` function**: Defined in a route module (Framework) or route object (Data).
    -   Receives `{ request, params, context }`.
    -   Typically handles `POST`, `PUT`, `PATCH`, `DELETE` requests.
    -   Can return data (becomes `actionData`), or a `Response` (e.g., `redirect("/new-path")`).
    -   After an action completes, React Router automatically revalidates data for all active loaders.
    ```tsx
    // Example action
    export async function action({ request, params }) {
      const formData = await request.formData();
      const updates = Object.fromEntries(formData);
      await updateProject(params.projectId, updates);
      return redirect(`/projects/${params.projectId}`);
    }
    ```
-   **`clientAction` function**: Runs only in the browser.
    -   Receives `{ request, params, serverAction }`.
-   **`<Form>` component**: A progressively enhanced HTML `<form>`.
    -   Submits data to route actions via `fetch`.
    -   Handles serialization of form data.
    -   `method="post"` (or put/patch/delete) targets an `action`. `method="get"` updates URL search params and calls `loader`s.
    ```tsx
    <Form method="post" action="/tasks">
      <input name="title" />
      <button type="submit">Create Task</button>
    </Form>
    ```
-   **`useSubmit()` hook**: Programmatically submits a form.
-   **Accessing Action Data**:
    -   Via `actionData` prop (Framework/Data).
    -   Via `useActionData()` hook.

### Navigation
-   **`<Link to="path">`**: Client-side navigation component, renders an `<a>` tag.
    -   Props: `relative`, `replace`, `state`, `preventScrollReset`, `reloadDocument`, `viewTransition`.
    -   Framework mode: `prefetch`, `discover`.
-   **`<NavLink to="path">`**: A special version of `<Link>` that knows whether or not it is "active" or "pending".
    -   Accepts functions for `className`, `style`, `children` to apply styles/content based on `isActive`, `isPending`, `isTransitioning` state.
    ```tsx
    <NavLink
      to="/messages"
      className={({ isActive }) = isActive ? "font-bold" : ""}
    >
      Messages
    </NavLink>
    ```
-   **`useNavigate()` hook**: Returns a function to navigate programmatically.
    -   `navigate("/path")`, `navigate(-1)` (back), `navigate("/path", { replace: true, state: {} })`.
-   **`redirect(url, init?)` utility**: Used in loaders/actions to return a `Response` that triggers a client-side or server-side redirect.
    -   `init` can specify `status` (e.g., 301, 302) and `headers`.

### Error Handling
React Router provides robust error handling mechanisms.
-   **`ErrorBoundary` export (Framework Mode) / `errorElement` prop (Data Mode)**:
    -   A React component that renders when an error is thrown in its corresponding route or its children (if they don't have their own error boundary).
    -   Catches errors from loaders, actions, and component rendering.
-   **`useRouteError()` hook**: Accesses the error object within an `ErrorBoundary` or `errorElement`.
    -   The error can be an `Error` instance, a `Response` object (if thrown from loader/action), or any other value.
-   **`isRouteErrorResponse(error)` utility**: Type guard to check if an error is a `Response` thrown by React Router (e.g., `throw new Response("Not Found", { status: 404 })`).
    ```tsx
    // Example ErrorBoundary
    import { useRouteError, isRouteErrorResponse } from "react-router";

    export function ErrorBoundary() {
      const error = useRouteError();
      if (isRouteErrorResponse(error)) {
        return <div><h1>{error.status}</h1><p>{error.data || error.statusText}</p></div>;
      }
      return <div><h1>Something went wrong</h1><p>{error.message}</p></div>;
    }
    ```
-   **`handleError` export (in `entry.server.tsx`, Framework Mode)**: A function to customize server-side error logging/reporting for unhandled errors.

### Pending UI & Optimistic UI
-   **`useNavigation()` hook**: Provides information about the current navigation state (`idle`, `loading`, `submitting`).
    -   `navigation.state`: Current state.
    -   `navigation.location`: The target location of the pending navigation.
    -   `navigation.formData`: FormData of a pending submission.
    -   Used for global loading indicators (e.g., spinners).
    ```tsx
    const navigation = useNavigation();
    // { navigation.state === "loading" && <Spinner /> }
    ```
-   **`NavLink` Pending States**: `isPending` and `isTransitioning` props in `className`/`style`/`children` functions.
-   **Fetcher Pending States**: `fetcher.state` (`idle`, `loading`, `submitting`) from `useFetcher()`.
-   **Optimistic UI**: Update UI immediately based on submitted form data (`fetcher.formData`) before the action completes. If the action fails, UI reverts.
    ```tsx
    // Example Optimistic UI with fetcher
    const fetcher = useFetcher();
    const isFavorite = fetcher.formData ? fetcher.formData.get("favorite") === "true" : contact.favorite;
    // ... render UI based on isFavorite
    ```

### Rendering Strategies
-   **Client-Side Rendering (CSR) / Single Page App (SPA)**:
    -   Set `ssr: false` in `react-router.config.ts` (Framework) or simply use a client-side router like `createBrowserRouter` without server integration (Data/Declarative).
    -   The app is rendered entirely in the browser. Initial HTML can be minimal.
    -   Framework mode can still pre-render the root route for a better initial shell in SPA mode.
-   **Server-Side Rendering (SSR)**:
    -   Set `ssr: true` (default in Framework mode).
    -   Initial HTML is rendered on the server, sent to the browser, then "hydrated" with JavaScript.
    -   Improves perceived performance and SEO.
    -   Requires a Node.js or compatible server environment.
-   **Static Pre-rendering / Static Site Generation (SSG)**:
    -   Configure the `prerender` option in `react-router.config.ts` (Framework) with an array of paths or an async function returning paths.
    -   HTML files are generated at build time for specified routes.
    -   Route `loader`s run at build time.
    -   Can be combined with SSR (paths not pre-rendered will be SSR'd) or used for fully static sites (`ssr: false`).

### Fetchers (`useFetcher()`)
Fetchers allow components to communicate with loaders and actions without causing a full navigation.
-   **Use Cases**:
    -   Submitting data that updates parts of the page (e.g., "like" button, adding to cart).
    -   Loading data for UI elements like comboboxes or auto-suggestions.
    -   Form validation messages.
-   **`fetcher.Form` / `fetcher.submit()`**: Submit data to a loader (with `method="get"`) or an action.
-   **`fetcher.load(href)`**: Loads data from a route's loader.
-   **State**: `fetcher.state` (`idle`, `loading`, `submitting`), `fetcher.data` (returned data), `fetcher.formData`.
    ```tsx
    const fetcher = useFetcher();
    // To submit a favorite toggle
    <fetcher.Form method="post" action={`/products/${id}/toggle-favorite`}>
      <button name="favorite" value={isFavorite ? "false" : "true"}>
        {isFavorite ? "★" : "☆"}
      </button>
    </fetcher.Form>
    // To load data for a combobox
    // useEffect(() => { fetcher.load(`/api/suggestions?q=${query}`); }, [query]);
    // { fetcher.data && <SuggestionList suggestions={fetcher.data} /> }
    ```

### Streaming with Suspense
Defer loading of non-critical data to speed up initial page renders.
-   Return a `Promise` for a data field from your `loader` instead of `await`ing it.
    ```tsx
    export async function loader() {
      const criticalData = await fetchCritical();
      const nonCriticalData = fetchNonCritical(); // Returns a Promise
      return { criticalData, nonCriticalData };
    }
    ```
-   Use `<React.Suspense fallback={...}>` and `<Await resolve={promise}>` in your component.
    ```tsx
    import { Await } from "react-router";
    import * as React from "react";

    function MyComponent({ loaderData }) {
      return (
        <div>
          <ShowData data={loaderData.criticalData} />
          <React.Suspense fallback={<LoadingSpinner />}>
            <Await resolve={loaderData.nonCriticalData}>
              {(resolvedNonCriticalData) => <ShowData data={resolvedNonCriticalData} />}
            </Await>
          </React.Suspense>
        </div>
      );
    }
    ```
-   With React 19, `React.use(promise)` can be used within a component wrapped by `<React.Suspense>`.
-   `streamTimeout` export in `entry.server.tsx` (Framework) controls server-side timeout for streamed promises.

## Advanced Topics & How-To Guides

### Form Validation
-   Actions can validate `request.formData()`.
-   If validation fails, return data (e.g., an errors object) with a non-2xx status (e.g., 400).
    ```tsx
    export async function action({ request }) {
      const formData = await request.formData();
      const email = formData.get("email");
      const errors = {};
      if (!email || !email.includes("@")) {
        errors.email = "Invalid email address";
      }
      if (Object.keys(errors).length) {
        return data({ errors }, { status: 400 }); // `data` utility
      }
      // ... process valid data
      return redirect("/success");
    }
    ```
-   Component uses `useActionData()` or `fetcher.data` to display errors.
    ```tsx
    const actionData = useActionData(); // or fetcher.data
    // {actionData?.errors?.email && <p>{actionData.errors.email}</p>}
    ```

### File Uploads
-   Use `enctype="multipart/form-data"` on your `<Form>`.
-   Parse `request.formData()` in your `action`. For streaming and easier handling, libraries like `@mjackson/form-data-parser` can be used with an `uploadHandler`.
-   Store uploaded files (e.g., using `@mjackson/file-storage` for local storage or cloud storage).
-   Serve files via a resource route.

### Sessions and Cookies
-   Manage user sessions for authentication, preferences, etc.
-   `createCookie(name, options)`: Creates a cookie definition. Options include `maxAge`, `httpOnly`, `secure`, `sameSite`, `secrets` (for signing).
-   `createCookieSessionStorage({ cookie })`: Stores session data in a cookie.
    -   Returns `{ getSession, commitSession, destroySession }`.
-   In `loader`/`action`:
    -   `const session = await getSession(request.headers.get("Cookie"));`
    -   `session.get("key")`, `session.set("key", value)`, `session.has("key")`, `session.unset("key")`, `session.flash("key", value)`.
    -   Responses must include `Set-Cookie` header: `headers: { "Set-Cookie": await commitSession(session) }`.
-   Custom session storage adapters can be created for databases.

### Navigation Blocking
-   Use `useBlocker(shouldBlockFn)` to prevent navigation when a condition is met (e.g., unsaved form data).
    -   `shouldBlockFn` is a callback `() => boolean` or `({ currentLocation, nextLocation, historyAction }) => boolean`.
-   `blocker.state` can be `unblocked`, `blocked`, or `proceeding`.
-   If `blocked`, render a confirmation UI.
    -   `blocker.proceed()`: Allows the navigation.
    -   `blocker.reset()`: Cancels the navigation and resets the blocker.
    ```tsx
    const [isDirty, setIsDirty] = useState(false);
    const blocker = useBlocker(() => isDirty);

    // In UI:
    // if (blocker.state === "blocked") { Show confirmation with proceed/reset buttons }
    ```

### Resource Routes
-   Routes that serve non-HTML content like JSON APIs, PDFs, images, sitemaps.
-   A route module becomes a resource route if it exports a `loader` or `action` but NO default component.
-   The `loader` (for GET) or `action` (for POST, etc.) must return a `Response` object.
    ```tsx
    // Example: pdf-report.ts
    export async function loader({ params }) {
      const pdfBuffer = await generatePdfForReport(params.id);
      return new Response(pdfBuffer, {
        status: 200,
        headers: { "Content-Type": "application/pdf" },
      });
    }
    ```
-   Links to resource routes should use `<a href>` or `<Link reloadDocument>`.

### HTTP Headers & Status Codes
-   **From Route Modules (Framework Mode)**: Export a `headers({ loaderHeaders, actionHeaders, parentHeaders })` function. It should return a `Headers` object or `HeadersInit`.
-   **From Loaders/Actions**: Return data wrapped with the `data(payload, { status, headers })` utility.
    ```tsx
    // In a loader/action
    if (!project) {
      throw data(null, { status: 404 }); // Throws a Response-like object for ErrorBoundary
    }
    return data({ project }, { status: 200, headers: { "Cache-Control": "max-age=60" } });
    ```
    Headers from `data()` must be explicitly passed up by the route's `headers` function. `Set-Cookie` is an exception and is often preserved.
-   **From `entry.server.tsx` (Framework Mode)**: Modify `responseHeaders` in `handleRequest`.

### View Transitions
-   Enable smooth animations between page states using the browser's View Transitions API.
-   Add `viewTransition` prop to `<Link>`, `<NavLink>`, or `<Form>`.
-   For programmatic navigation: `navigate("/path", { viewTransition: true })`.
-   Use CSS `view-transition-name` to identify elements that should transition.
-   `useViewTransitionState(href)` hook or `isTransitioning` render prop in `<NavLink>` allows applying styles/names conditionally during the transition.

### File Route Conventions (Framework Mode)
-   Use `@react-router/fs-routes` package to define routes based on file and folder names in `app/routes/` (configurable).
    ```ts
    // app/routes.ts
    import { flatRoutes } from "@react-router/fs-routes";
    export default flatRoutes();
    ```
-   Conventions:
    -   `_index.tsx`: Index route for a directory.
    -   `about.tsx`: Matches `/about`.
    -   `concerts.trending.tsx`: Matches `/concerts/trending` and nests under `concerts.tsx` if it exists.
    -   `$city.tsx`: Dynamic segment, e.g., `/slc` makes `params.city` be "slc".
    -   `concerts_.mine.tsx`: `_` after segment opts out of layout nesting with `concerts.tsx`.
    -   `_auth.login.tsx`: `_` before segment creates a pathless layout route `_auth.tsx`.
    -   `($lang)._index.tsx`: `()` makes segment optional.
    -   `$.tsx` or `files.$.tsx`: Splat/catch-all routes.
    -   `sitemap[.]xml.tsx`: `[]` escape special characters.
    -   Folders: `app/routes/concerts/route.tsx` is equivalent to `app/routes/concerts.tsx`. Other files in `concerts/` are co-located.

### Route Module Type Safety (Framework Mode)
-   React Router generates TypeScript types for each route module (e.g., for `loader` args, `loaderData`, `action` args, `params`).
-   Generated types are placed in `.react-router/types/`.
-   Configure `tsconfig.json`:
    ```json
    {
      "include": [".react-router/types/**/*"],
      "compilerOptions": {
        "rootDirs": [".", "./.react-router/types"]
      }
    }
    ```
-   Import types like: `import type { Route } from "./+types/product";` then use `Route.LoaderArgs`, `Route.ComponentProps`, etc.
-   `react-router typegen` command can manually generate types.

### Testing
-   Use `createRoutesStub(routesArray, context?)` to test components that rely on router context (hooks like `useLoaderData`, `useParams`, components like `<Link>`).
-   `routesArray` is an array of objects mimicking route modules.
    ```tsx
    import { createRoutesStub } from "react-router";
    // test("LoginForm renders", () => {
    //   const Stub = createRoutesStub([{ path: "/login", Component: LoginForm, action: () => ({}) }]);
    //   render(<Stub initialEntries={["/login"]} />);
    //   // ... assertions
    // });
    ```

### Security (Content Security Policy - CSP)
-   If using CSP with `unsafe-inline` and a `nonce`, provide the nonce to React Router components that render inline scripts:
    -   `<Scripts nonce={cspNonce} />` (in `root.tsx`)
    -   `<ScrollRestoration nonce={cspNonce} />` (in `root.tsx`)
    -   `<ServerRouter nonce={cspNonce} />` (in `entry.server.tsx`)
    -   Also pass to React's `renderToPipeableStream` or `renderToReadableStream`.

## Key Explanations

### Progressive Enhancement
React Router (especially in Framework mode with SSR) supports progressive enhancement.
-   HTML forms (`<Form>`) and links (`<Link>`) work even before JavaScript loads, relying on standard browser behavior.
-   When JavaScript loads, React Router enhances these elements for client-side routing, smoother UX, and advanced features like pending UI, without changing the fundamental HTML structure or server logic.
-   This leads to resilient applications that are accessible and performant on varying network conditions and device capabilities.

### Code Splitting (Framework Mode)
-   The Vite plugin automatically code-splits your application by route. Each route module (e.g., `about.tsx`) becomes a separate chunk.
-   Only the JavaScript necessary for the current route (and its active layouts) is loaded initially, significantly reducing bundle sizes and improving load times.
-   Server-only code within route module exports (like `loader`, `action`, `headers`) is automatically removed from client bundles.

### Race Conditions
React Router is designed to handle common network race conditions:
-   **Navigation Interruption**: If a new navigation (link click, form submission) starts while a previous one is in-flight, the earlier navigation's data requests are canceled, and the new one is processed, similar to browser behavior.
-   **Fetcher Interruption**: A fetcher will cancel its own pending requests if a new `fetcher.submit()` or `fetcher.load()` is called on it.
-   **Revalidation**: After actions, multiple loaders revalidate. React Router ensures that only the freshest data is committed, canceling stale revalidation requests. This helps prevent inconsistent UI states.

### State Management Philosophy
React Router's data features often reduce the need for complex client-side state management libraries for server state.
-   **Server as Source of Truth**: Loaders fetch data directly from the server. Actions mutate server data. Revalidation keeps client UI in sync.
-   **URL as State**: Many UI states can be represented in the URL (path params, search params). React Router provides tools to manage these (`useParams`, `useSearchParams`).
-   **Cookies & Sessions**: For persistent user-specific state.
-   **React Router's Internal State**: Hooks like `useNavigation` and `useFetcher` expose network and submission states, reducing the need to manage this manually with `useState`/`useEffect`.
-   Focus on server state synchronization and use client state for ephemeral UI state not tied to URLs or server data.

### Hot Module Replacement (HMR) (Framework Mode)
-   The Vite plugin supports HMR with React Fast Refresh.
-   Component changes update in place without losing component state (for function components and most hooks).
-   Changes to route module exports like `loader`, `action` are also handled.
-   Some limitations exist (e.g., class component state, adding/removing hooks might reset state for that update).

### Special Files (Framework Mode)
These files have specific roles in a Framework Mode application:
-   **`react-router.config.ts` (optional)**: Configures app directory, SSR, pre-rendering, etc.
-   **`app/root.tsx` (required)**: The root route of the application. Renders the `<html>` document shell. Exports `Layout` (optional, for shared shell structure), `default` (App component), `ErrorBoundary`, `HydrateFallback`. Renders `<Meta>`, `<Links>`, `<Scripts>`, `<ScrollRestoration>`, `<Outlet>`.
-   **`app/routes.ts` (required)**: Defines the route configuration, mapping URL patterns to route modules.
-   **`app/root.tsx` (optional)**: Client-side entry point. Hydrates the server-rendered HTML. Renders `<HydratedRouter />`.
-   **`app/entry.server.tsx` (optional)**: Server-side entry point. Handles requests, renders HTML using `<ServerRouter />`, and sends the response. Exports `handleRequest`, and optionally `streamTimeout`, `handleDataRequest`, `handleError`.
-   **`.server.tsx` / `.client.tsx` files**: Mark modules as server-only or client-only, affecting bundling.

## API Overview
React Router v7 provides a rich API surface.

### Core Components
-   **`<Link to>`/`<NavLink to>`**: For declarative, accessible navigation. `NavLink` adds styling capabilities for active/pending states.
-   **`<Outlet context?>`**: Renders the matched child route component within a parent route's layout.
-   **`<Form action? method?>`**: Handles data submissions to route `action`s, enabling progressive enhancement.
-   **`<Routes>`/`<Route path element>`**: For defining routes declaratively in JSX (primarily Declarative Mode or for sub-routing).
-   **`<Await resolve errorElement?>`**: Used with `<React.Suspense>` to render deferred data (promises) from loaders.
-   **`<ScrollRestoration nonce?>`**: Manages scroll position during navigations.
-   **(Framework Mode)** `<Scripts nonce?>`, `<Meta />`, `<Links />`: Render critical parts of the HTML document shell.

### Core Hooks
-   **`useParams()`**: Accesses dynamic URL parameters (e.g., `:id`).
-   **`useLocation()`**: Returns the current location object (`pathname`, `search`, `hash`, `state`, `key`).
-   **`useNavigate()`**: Returns a function for programmatic navigation.
-   **`useLoaderData()`**: Accesses data returned by the current route's `loader` or `clientLoader`.
-   **`useActionData()`**: Accesses data returned by the last executed `action`.
-   **`useFetcher()`**: Manages non-navigational data fetching/submission (e.g., for "like" buttons, autosuggestions). Returns a `fetcher` object with `load`, `submit`, `Form`, `state`, `data`.
-   **`useSubmit()`**: Programmatically submits a form, similar to `fetcher.submit` but for navigational forms.
-   **`useNavigation()`**: Provides global navigation state (`state`, `location`, `formData`).
-   **`useRouteError()`**: Accesses the error object within an `ErrorBoundary` or `errorElement`.
-   **`useBlocker(shouldBlockFn)`**: Prevents navigation based on a condition, allowing for user confirmation.
-   **`useSearchParams()`**: Reads and writes URL search parameters.

### Router Creation & Configuration
-   **`createBrowserRouter(routes, opts?)`**: Creates a router for browser environments using the History API (Data/Declarative Mode).
-   **`createHashRouter(routes, opts?)`**: Creates a router using URL hash for routing.
-   **`createMemoryRouter(routes, opts?)`**: Creates a router that stores history in memory (useful for testing, non-browser environments).
-   **`<RouterProvider router>`**: Renders a data router instance.
-   **(Server-Side)** `createStaticHandler(routes, opts?)`, `createStaticRouter(routes, context, opts?)`, `<StaticRouterProvider router context>`.
-   **(Framework Mode)** Routing is configured via `app/routes.ts` and the Vite plugin.

### Data Handling Utilities
-   **`redirect(url, init?)`**: Creates a `Response` object for redirection, used in loaders/actions. `init` can set `status` and `headers`.
-   **`data(payload, init?)`**: Utility to return data from loaders/actions along with `status` and `headers` without creating a full `Response` object. Useful for non-Response data that still needs metadata.

### Session & Cookie Management
-   **`createCookie(name, options?)`**: Defines a cookie with attributes like `maxAge`, `secrets` (for signing), `httpOnly`.
-   **`createCookieSessionStorage({ cookie })`**: Creates session storage backed by a cookie. Provides `getSession`, `commitSession`, `destroySession`.

## Tutorial: Address Book App Summary
The Address Book tutorial demonstrates key React Router v7 concepts by building a contacts application:
1.  **Setup**: Using `create-react-router` with a template.
2.  **Root Route (`app/root.tsx`)**: Basic layout, `Outlet` for child routes.
3.  **Contact Route**: Creating a dynamic route (`contacts/:contactId`) and its component.
4.  **Data Loading**:
    -   Using `clientLoader` to fetch a list of contacts for the sidebar.
    -   Using `loader` (server-side) to fetch individual contact details based on `params.contactId`.
    -   Type safety for `loaderData` using generated types (`Route.ComponentProps`, `Route.LoaderArgs`).
5.  **Error Handling**: Throwing a `Response` (e.g., 404) from a loader if a contact isn't found, handled by `ErrorBoundary`.
6.  **Mutations with Actions**:
    -   Creating new contacts: An `action` in the root route handles a "New" button POST request.
    -   Updating contacts: An `action` in the edit route (`contacts/:contactId/edit`) processes form data from `<Form method="post">`. `request.formData()` is used to access submitted values.
    -   Automatic revalidation: Loaders are re-run after actions complete, updating the UI.
7.  **Redirects**: Using `redirect()` from actions to navigate after a mutation (e.g., to the new contact's page or back to the contact view).
8.  **Navigation**:
    -   Using `<Link>` for client-side navigation.
    -   Using `<NavLink>` for navigation links that require active/pending styling.
    -   Using `useNavigate()` for programmatic navigation (e.g., cancel button `navigate(-1)`).
9.  **Pending UI**:
    -   Global pending UI using `useNavigation().state` to show a loading indicator during navigations.
    -   Local pending UI with `NavLink`'s `isPending` state.
10. **URL Search Params**: Implementing search/filtering using a GET form.
    -   `loader` reads search query from `request.url` (`URLSearchParams`).
    -   Synchronizing form input state with URL search params using `defaultValue` and `useEffect` or controlled components.
    -   Submitting form `onChange` using `useSubmit()`. Using `replace: true` option to manage history stack.
11. **Fetchers (`useFetcher`)**:
    -   For mutations that don't require a full navigation (e.g., "favorite" button).
    -   `fetcher.Form` submits to an action.
    -   Optimistic UI by reading `fetcher.formData` to update the UI immediately.
12. **Layouts**: Using layout routes to share UI structure among a subset of routes.
13. **Pre-rendering**: Statically rendering the "About" page via `prerender` config.
14. **SSR**: Enabling server-side rendering via `ssr: true` config and switching `clientLoader` to `loader`.

## Upgrading to v7

### From v6
-   Ensure all v6 [future flags](https://reactrouter.com/docs/v7/upgrading/future/) are enabled in your v6 app.
-   Key flags include `v7_relativeSplatPath`, `v7_startTransition`, `v7_fetcherPersist`, `v7_normalizeFormMethod`, `v7_partialHydration`, `v7_skipActionErrorRevalidation`.
-   Update code according to each flag's requirements (e.g., splitting multi-segment splat routes, handling uppercase form methods).
-   `json()` and `defer()` utilities are deprecated; return raw objects or use native `Response.json()`.
-   Install `react-router` and uninstall `react-router-dom`.
-   Update all imports from `react-router-dom` to `react-router`.
-   DOM-specific APIs like `RouterProvider` and `HydratedRouter` are now imported from `react-router/dom`.

### From Remix v2
React Router v7 is the successor to Remix v2.
-   Enable all Remix v2 future flags.
-   Many `@remix-run/*` packages are replaced by `react-router` or `@react-router/*` equivalents. A [codemod](https://codemod.com/registry/remix-2-react-router-upgrade) can automate much of this.
    -   `@remix-run/react` -> `react-router`
    -   `@remix-run/node` -> `@react-router/node` (for Node-specific APIs like `createFileSessionStorage`)
    -   `@remix-run/dev` -> `@react-router/dev`
    -   `@remix-run/serve` -> `@react-router/serve`
-   Update `package.json` scripts: `remix vite:dev` -> `react-router dev`, etc.
-   Route configuration moves from Vite plugin options to `app/routes.ts`. Use `@react-router/fs-routes` or `@react-router/remix-routes-option-adapter` for compatibility if needed.
-   Remix Vite plugin options (like `ssr`, future flags) move to `react-router.config.ts`.
-   Replace `remix` Vite plugin with `reactRouter` from `@react-router/dev/vite`.
-   Update `tsconfig.json` for new type generation paths (`.react-router/types/**/*`) and update `@remix-run/*` types to `@react-router/*`.
-   Rename `RemixServer` to `ServerRouter` (in `entry.server.tsx`) and `RemixBrowser` to `HydratedRouter` (in `root.tsx`).
-   Augment `AppLoadContext` for `react-router` if using custom server context.

---