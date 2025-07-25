// Generated by React Router

import "react-router"

declare module "react-router" {
  interface Register {
    pages: Pages
    routeFiles: RouteFiles
  }
}

type Pages = {
  "/": {
    params: {};
  };
  "/login": {
    params: {};
  };
  "/signup": {
    params: {};
  };
  "/about": {
    params: {};
  };
  "/oauth2-success": {
    params: {};
  };
  "/listener-programs": {
    params: {};
  };
  "/listener-programs/create": {
    params: {};
  };
  "/listener-programs/:programId": {
    params: {
      "programId": string;
    };
  };
  "/listener-programs/:programId/edit": {
    params: {
      "programId": string;
    };
  };
  "/listener-programs/:programId/segments/create": {
    params: {
      "programId": string;
    };
  };
};

type RouteFiles = {
  "root.tsx": {
    id: "root";
    page: "/" | "/login" | "/signup" | "/about" | "/oauth2-success" | "/listener-programs" | "/listener-programs/create" | "/listener-programs/:programId" | "/listener-programs/:programId/edit" | "/listener-programs/:programId/segments/create";
  };
  "../components/PublicRoute.tsx": {
    id: "../components/PublicRoute";
    page: "/" | "/login" | "/signup" | "/about" | "/oauth2-success";
  };
  "./routes/home.tsx": {
    id: "routes/home";
    page: "/";
  };
  "./routes/login.tsx": {
    id: "routes/login";
    page: "/login";
  };
  "./routes/signup.tsx": {
    id: "routes/signup";
    page: "/signup";
  };
  "./routes/about.tsx": {
    id: "routes/about";
    page: "/about";
  };
  "./routes/oauth2-success.tsx": {
    id: "routes/oauth2-success";
    page: "/oauth2-success";
  };
  "../components/ProtectedRoute.tsx": {
    id: "../components/ProtectedRoute";
    page: "/listener-programs" | "/listener-programs/create" | "/listener-programs/:programId" | "/listener-programs/:programId/edit" | "/listener-programs/:programId/segments/create";
  };
  "./routes/listener-programs/list.tsx": {
    id: "routes/listener-programs/list";
    page: "/listener-programs";
  };
  "./routes/listener-programs/create.tsx": {
    id: "routes/listener-programs/create";
    page: "/listener-programs/create";
  };
  "./routes/listener-programs/detail.tsx": {
    id: "routes/listener-programs/detail";
    page: "/listener-programs/:programId";
  };
  "./routes/listener-programs/edit.tsx": {
    id: "routes/listener-programs/edit";
    page: "/listener-programs/:programId/edit";
  };
  "./routes/listener-programs/segments/create.tsx": {
    id: "routes/listener-programs/segments/create";
    page: "/listener-programs/:programId/segments/create";
  };
};