---
title: Usage
description: Usage of OpenAPI React Query Codegen.
---

After generating the React Query hooks and functions, you can start using them in your React application.

## Using the generated `useQuery` hooks

```tsx
import { useFindPets } from "../openapi/queries";
function App() {
  const { data } = useFindPets();

  return (
    <div className="App">
      <h1>Pet List</h1>
      <ul>{data?.map((pet) => <li key={pet.id}>{pet.name}</li>)}</ul>
    </div>
  );
}

export default App;
```

Optionally, you can also use the pure ts client in `openapi/requests/services.gen.ts` to customize your query.

```tsx
import { useQuery } from "@tanstack/react-query";
import { findPets } from "../openapi/requests/services.gen";
import { useFindPetsKey } from "../openapi/queries";

function App() {
  // You can still use the auto-generated query key
  const { data } = useQuery({
    queryKey: [useFindPetsKey],
    queryFn: () => {
      // Do something here
      return findPets();
    },
  });

  return <div className="App">{/* .... */}</div>;
}

export default App;
```

## Using the generated `useQuerySuspense` hooks

```tsx
import { useFindPetsSuspense } from "../openapi/queries/suspense";
function ChildComponent() {
  const { data } = useFindPetsSuspense({
    query: { tags: [], limit: 10 },
  });

  return <ul>{data?.map((pet, index) => <li key={pet.id}>{pet.name}</li>)}</ul>;
}

function ParentComponent() {
  return (
    <>
      <Suspense fallback={<>loading...</>}>
        <ChildComponent />
      </Suspense>
    </>
  );
}

function App() {
  return (
    <div className="App">
      <h1>Pet List</h1>
      <ParentComponent />
    </div>
  );
}

export default App;
```

## Using the generated `useMutation` hooks

```tsx
import { useAddPet } from "../openapi/queries";

function App() {
  const { mutate } = useAddPet();

  const handleAddPet = () => {
    mutate({ body: { name: "Fluffy" } });
  };

  return (
    <div className="App">
      <h1>Add Pet</h1>
      <button onClick={handleAddPet}>Add Pet</button>
    </div>
  );
}

export default App;
```

Invalidating queries after a mutation is important to ensure the cache is updated with the new data. This is done by calling the `queryClient.invalidateQueries` function with the query key used by the query hook.

Learn more about invalidating queries [here](https://tanstack.com/query/latest/docs/framework/react/guides/query-invalidation).

To ensure the query key is created the same way as the query hook, you can use the query key function exported by the generated query hooks.

```tsx
import {
  useFindPetsByStatus,
  useAddPet,
  UseFindPetsByStatusKeyFn,
} from "../openapi/queries";

function App() {
  const [status, setStatus] = React.useState(["available"]);
  const { data } = useFindPetsByStatus({ query: { status } });
  const { mutate } = useAddPet({
    onSuccess: () => {
      queryClient.invalidateQueries({
        // Call the query key function to get the query key
        // This is important to ensure the query key is created the same way as the query hook
        // This insures the cache is invalidated correctly and is typed correctly
        queryKey: [UseFindPetsByStatusKeyFn({
          status
        })],
      });
    },
  });

  return (
    <div className="App">
      <h1>Pet List</h1>
      <ul>{data?.map((pet) => <li key={pet.id}>{pet.name}</li>)}</ul>
      <button
        onClick={() => {
          mutate({ name: "Fluffy", status: "available" });
        }}
      >
        Add Pet
      </button>
    </div>
  );
}

export default App;
```


## Using the generated `useInfiniteQuery` hooks

This feature will generate a function in infiniteQueries.ts when the name specified by the `pageParam` option exists in the query parameters and the name specified by the `nextPageParam` option exists in the response.

The `initialPageParam` option can be specified to set the intial page to load, defaults to 1. The `nextPageParam` supports dot notation for nested values (i.e. `meta.next`).

Example Schema:

```yml /name: page|nextPage:/
paths:
  /paginated-pets:
    get:
      description: |
        Returns paginated pets from the system that the user has access to
      operationId: findPaginatedPets
      parameters:
        - name: page
          in: query
          description: page number
          required: false
          schema:
            type: integer
            format: int32
        - name: tags
          in: query
          description: tags to filter by
          required: false
          style: form
          schema:
            type: array
            items:
              type: string
        - name: limit
          in: query
          description: maximum number of results to return
          required: false
          schema:
            type: integer
            format: int32
      responses:
        '200':
          description: pet response
          content:
            application/json:
              schema:
                type: object
                properties:
                  pets:
                    type: array
                    items:
                      $ref: '#/components/schemas/Pet'
                  nextPage: 
                    type: integer
                    format: int32
                    minimum: 1
```

Usage of Generated Hooks:

```ts
import { useFindPaginatedPetsInfinite } from "@/openapi/queries/infiniteQueries";

const { data, fetchNextPage } = useFindPaginatedPetsInfinite({
  query: { tags: [], limit: 10 }
});
```



