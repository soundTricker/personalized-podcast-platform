└── docs
    └── framework
        └── react
            ├── community
                ├── balastrong-tutorial.md
                └── tutorials.md
            ├── guides
                ├── arrays.md
                ├── async-initial-values.md
                ├── basic-concepts.md
                ├── custom-errors.md
                ├── debugging.md
                ├── form-composition.md
                ├── linked-fields.md
                ├── listeners.md
                ├── react-native.md
                ├── reactivity.md
                ├── ssr.md
                ├── submission-handling.md
                ├── ui-libraries.md
                └── validation.md
            ├── quick-start.md
            └── reference
                ├── functions
                    ├── createformhook.md
                    ├── createformhookcontexts.md
                    ├── field.md
                    ├── usefield.md
                    ├── useform.md
                    ├── usestore.md
                    └── usetransform.md
                ├── index.md
                ├── interfaces
                    ├── reactformapi.md
                    └── withformprops.md
                └── type-aliases
                    ├── fieldcomponent.md
                    ├── reactformextendedapi.md
                    └── usefield.md


/docs/framework/react/community/balastrong-tutorial.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: balastrong-tutorial
 3 | title: Balastrong's Tutorial
 4 | ---
 5 | 
 6 | TanStack Form maintainer [Balastrong](https://bsky.app/profile/leonardomontini.dev) has created a series of video tutorials showcasing the most relevant features of the library. You'll find step by step guides that give you some extra insights into what you can build with TanStack Form, plus some nice tips and tricks.
 7 | 
 8 | [Watch the full playlist](https://www.youtube.com/playlist?list=PLOQjd5dsGSxInTKUWTxyqSKwZCjDIUs0Y)
 9 | 
10 | ## 1. [Setup and validation](https://youtu.be/Pf1qn35bgjs)
11 | 
12 | The first steps into TanStack Form learning all the basics, from setting up the library to creating a simple form with text fields and validation (sync, debounced and async). [Watch video (8:16)](https://youtu.be/Pf1qn35bgjs)
13 | 
14 | ## 2. [Advanced validation](https://youtu.be/Pys2ExswZT0)
15 | 
16 | An example of data being validated through a backend API while ensuring a smooth user experience by controlling loading state, error messages and linked fields. [Watch video (8:05)](https://youtu.be/Pys2ExswZT0)
17 | 
18 | ## 3. [Array fields](https://youtu.be/0IPPHdjvrzk)
19 | 
20 | How to handle array fields with primitives (strings, numbers) and objects (nested fields), with validation and reordering. [Watch video (6:53)](https://youtu.be/0IPPHdjvrzk)
21 | 
22 | ## 4. [Reactivity](https://youtu.be/UXRZvNCnE-s)
23 | 
24 | Learn why form values may not update in real time, why this behavior is intentional, and how to trigger UI updates efficiently. [Watch video (4:26)](https://youtu.be/UXRZvNCnE-s)
25 | 
26 | ## 5. [Form validation with schema libraries](https://youtu.be/HSboMHfPuZA)
27 | 
28 | Use schema libraries like zod, yup or valibot to define your schema with validation rules. Pass it to TanStack Form through an adapter to validate all fields at once. [Watch video (6:29)](https://youtu.be/HSboMHfPuZA)
29 | 
30 | ## 6. [Side effects and listeners](https://youtu.be/A-w2IG7DAso)
31 | 
32 | Similarly to field validators, you can attach events to field listeners and react to them, for example to reset a field when another one it depends on has changed. [Watch video (5:50)](https://youtu.be/A-w2IG7DAso)
33 | 
34 | ## 7. [Composable Fields for Large Forms](https://youtu.be/YJ3rW85fnKo)
35 | 
36 | With the Composition APIs you can create reusable components, pre-bound and connected to a generic form context, heavily reducing repetitive code in all form instances across the app. This is especially useful for large forms with many fields. [Watch video (11:01)](https://youtu.be/YJ3rW85fnKo)
37 | 


--------------------------------------------------------------------------------
/docs/framework/react/community/tutorials.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: community-tutorials
 3 | title: Community Tutorials
 4 | ---
 5 | 
 6 | This page is a collection of community-created tutorials, articles, and videos that can help you learn more about TanStack Form from other developers. If you created a resource that you would like to add to this list, please open a PR! We keep them in chronological order by publish date to ensure the most up to date content is at the top.
 7 | 
 8 | > Please note that the content listed here is entirely community maintained. While it may not be fully aligned with official recommendations and best practices, it can still offer valuable insights and alternative perspectives.
 9 | 
10 | ## TanStack Form Tutorial - Best Form Library for React?
11 | 
12 | [Watch Video](https://youtu.be/5oFQd-uAAHo) (March 7th, 2025)
13 | 
14 | A tutorial from [Atharva Deosthale](https://links.atharva.codes) using TanStack Form in a Next.js project. The video is made for people who are just getting started with knowing TanStack Form and will cover client-side form validation and server-side form validation by taking advantage of the Form SDK. This tutorial expects you to have basic knowledge of working of React and client-server architectures.
15 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/arrays.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: arrays
  3 | title: Arrays
  4 | ---
  5 | 
  6 | TanStack Form supports arrays as values in a form, including sub-object values inside of an array.
  7 | 
  8 | ## Basic Usage
  9 | 
 10 | To use an array, you can use `field.state.value` on an array value:
 11 | 
 12 | ```jsx
 13 | function App() {
 14 |   const form = useForm({
 15 |     defaultValues: {
 16 |       people: [],
 17 |     },
 18 |   })
 19 | 
 20 |   return (
 21 |     <form.Field name="people" mode="array">
 22 |       {(field) => (
 23 |         <div>
 24 |           {field.state.value.map((_, i) => {
 25 |             // ...
 26 |           })}
 27 |         </div>
 28 |       )}
 29 |     </form.Field>
 30 |   )
 31 | }
 32 | ```
 33 | 
 34 | This will generate the mapped JSX every time you run `pushValue` on `field`:
 35 | 
 36 | ```jsx
 37 | <button onClick={() => field.pushValue({ name: '', age: 0 })} type="button">
 38 |   Add person
 39 | </button>
 40 | ```
 41 | 
 42 | Finally, you can use a subfield like so:
 43 | 
 44 | ```jsx
 45 | <form.Field key={i} name={`people[${i}].name`}>
 46 |   {(subField) => (
 47 |     <input
 48 |       value={subField.state.value}
 49 |       onChange={(e) => subField.handleChange(e.target.value)}
 50 |     />
 51 |   )}
 52 | </form.Field>
 53 | ```
 54 | 
 55 | ## Full Example
 56 | 
 57 | ```jsx
 58 | function App() {
 59 |   const form = useForm({
 60 |     defaultValues: {
 61 |       people: [],
 62 |     },
 63 |     onSubmit({ value }) {
 64 |       alert(JSON.stringify(value))
 65 |     },
 66 |   })
 67 | 
 68 |   return (
 69 |     <div>
 70 |       <form
 71 |         onSubmit={(e) => {
 72 |           e.preventDefault()
 73 |           e.stopPropagation()
 74 |           form.handleSubmit()
 75 |         }}
 76 |       >
 77 |         <form.Field name="people" mode="array">
 78 |           {(field) => {
 79 |             return (
 80 |               <div>
 81 |                 {field.state.value.map((_, i) => {
 82 |                   return (
 83 |                     <form.Field key={i} name={`people[${i}].name`}>
 84 |                       {(subField) => {
 85 |                         return (
 86 |                           <div>
 87 |                             <label>
 88 |                               <div>Name for person {i}</div>
 89 |                               <input
 90 |                                 value={subField.state.value}
 91 |                                 onChange={(e) =>
 92 |                                   subField.handleChange(e.target.value)
 93 |                                 }
 94 |                               />
 95 |                             </label>
 96 |                           </div>
 97 |                         )
 98 |                       }}
 99 |                     </form.Field>
100 |                   )
101 |                 })}
102 |                 <button
103 |                   onClick={() => field.pushValue({ name: '', age: 0 })}
104 |                   type="button"
105 |                 >
106 |                   Add person
107 |                 </button>
108 |               </div>
109 |             )
110 |           }}
111 |         </form.Field>
112 |         <form.Subscribe
113 |           selector={(state) => [state.canSubmit, state.isSubmitting]}
114 |           children={([canSubmit, isSubmitting]) => (
115 |             <button type="submit" disabled={!canSubmit}>
116 |               {isSubmitting ? '...' : 'Submit'}
117 |             </button>
118 |           )}
119 |         />
120 |       </form>
121 |     </div>
122 |   )
123 | }
124 | ```
125 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/async-initial-values.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: async-initial-values
 3 | title: Async Initial Values
 4 | ---
 5 | 
 6 | Let's say that you want to fetch some data from an API and use it as the initial value of a form.
 7 | 
 8 | While this problem sounds simple on the surface, there are hidden complexities you might not have thought of thus far.
 9 | 
10 | For example, you might want to show a loading spinner while the data is being fetched, or you might want to handle errors gracefully.
11 | Likewise, you could also find yourself looking for a way to cache the data so that you don't have to fetch it every time the form is rendered.
12 | 
13 | While we could implement many of these features from scratch, it would end up looking a lot like another project we maintain: [TanStack Query](https://tanstack.com/query).
14 | 
15 | As such, this guide shows you how you can mix-n-match TanStack Form with TanStack Query to achieve the desired behavior.
16 | 
17 | ## Basic Usage
18 | 
19 | ```tsx
20 | import { useForm } from '@tanstack/react-form'
21 | import { useQuery } from '@tanstack/react-query'
22 | 
23 | export default function App() {
24 |   const {data, isLoading} = useQuery({
25 |     queryKey: ['data'],
26 |     queryFn: async () => {
27 |       await new Promise((resolve) => setTimeout(resolve, 1000))
28 |       return {firstName: 'FirstName', lastName: "LastName"}
29 |     }
30 |   })
31 | 
32 |   const form = useForm({
33 |     defaultValues: {
34 |       firstName: data?.firstName ?? '',
35 |       lastName: data?.lastName ?? '',
36 |     },
37 |     onSubmit: async ({ value }) => {
38 |       // Do something with form data
39 |       console.log(value)
40 |     },
41 |   })
42 | 
43 |   if (isLoading) return <p>Loading..</p>
44 | 
45 |   return (
46 |     // ...
47 |   )
48 | }
49 | ```
50 | 
51 | This will show a loading spinner until the data is fetched, and then it will render the form with the fetched data as the initial values.
52 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/basic-concepts.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: basic-concepts
  3 | title: Basic Concepts and Terminology
  4 | ---
  5 | 
  6 | This page introduces the basic concepts and terminology used in the `@tanstack/react-form` library. Familiarizing yourself with these concepts will help you better understand and work with the library.
  7 | 
  8 | ## Form Options
  9 | 
 10 | You can create options for your form so that it can be shared between multiple forms by using the `formOptions` function.
 11 | 
 12 | Example:
 13 | 
 14 | ```tsx
 15 | interface User {
 16 |   firstName: string
 17 |   lastName: string
 18 |   hobbies: Array<string>
 19 | }
 20 | const defaultUser: User = { firstName: '', lastName: '', hobbies: [] }
 21 | 
 22 | const formOpts = formOptions({
 23 |   defaultValues: defaultUser,
 24 | })
 25 | ```
 26 | 
 27 | ## Form Instance
 28 | 
 29 | A Form Instance is an object that represents an individual form and provides methods and properties for working with the form. You create a form instance using the `useForm` hook provided by the form options. The hook accepts an object with an `onSubmit` function, which is called when the form is submitted.
 30 | 
 31 | ```tsx
 32 | const form = useForm({
 33 |   ...formOpts,
 34 |   onSubmit: async ({ value }) => {
 35 |     // Do something with form data
 36 |     console.log(value)
 37 |   },
 38 | })
 39 | ```
 40 | 
 41 | You may also create a form instance without using `formOptions` by using the standalone `useForm` API:
 42 | 
 43 | ```tsx
 44 | interface User {
 45 |   firstName: string
 46 |   lastName: string
 47 |   hobbies: Array<string>
 48 | }
 49 | const defaultUser: User = { firstName: '', lastName: '', hobbies: [] }
 50 | 
 51 | const form = useForm({
 52 |   defaultValues: defaultUser,
 53 |   onSubmit: async ({ value }) => {
 54 |     // Do something with form data
 55 |     console.log(value)
 56 |   },
 57 | })
 58 | ```
 59 | 
 60 | ## Field
 61 | 
 62 | A Field represents a single form input element, such as a text input or a checkbox. Fields are created using the form.Field component provided by the form instance. The component accepts a name prop, which should match a key in the form's default values. It also accepts a children prop, which is a render prop function that takes a field object as its argument.
 63 | 
 64 | Example:
 65 | 
 66 | ```tsx
 67 | <form.Field
 68 |   name="firstName"
 69 |   children={(field) => (
 70 |     <>
 71 |       <input
 72 |         value={field.state.value}
 73 |         onBlur={field.handleBlur}
 74 |         onChange={(e) => field.handleChange(e.target.value)}
 75 |       />
 76 |       <FieldInfo field={field} />
 77 |     </>
 78 |   )}
 79 | />
 80 | ```
 81 | 
 82 | ## Field State
 83 | 
 84 | Each field has its own state, which includes its current value, validation status, error messages, and other metadata. You can access a field's state using the `field.state` property.
 85 | 
 86 | Example:
 87 | 
 88 | ```ts
 89 | const {
 90 |   value,
 91 |   meta: { errors, isValidating },
 92 | } = field.state
 93 | ```
 94 | 
 95 | There are four states in the metadata that can be useful to see how the user interacts with a field:
 96 | 
 97 | - _"isTouched"_, after the user changes the field or blurs the field
 98 | - _"isDirty"_, after the field's value has been changed, even if it's been reverted to the default. Opposite of `isPristine`
 99 | - _"isPristine"_, until the user changes the field value. Opposite of `isDirty`
100 | - _"isBlurred"_, after the field has been blurred
101 | 
102 | ```ts
103 | const { isTouched, isDirty, isPristine, isBlurred } = field.state.meta
104 | ```
105 | 
106 | ![Field states](https://raw.githubusercontent.com/TanStack/form/main/docs/assets/field-states.png)
107 | 
108 | ## Understanding 'isDirty' in Different Libraries
109 | 
110 | Non-Persistent `dirty` state
111 | 
112 | - **Libraries**: React Hook Form (RHF), Formik, Final Form.
113 | - **Behavior**: A field is 'dirty' if its value differs from the default. Reverting to the default value makes it 'clean' again.
114 | 
115 | Persistent `dirty` state
116 | 
117 | - **Libraries**: Angular Form, Vue FormKit.
118 | - **Behavior**: A field remains 'dirty' once changed, even if reverted to the default value.
119 | 
120 | We have chosen the persistent 'dirty' state model. To also support a non-persistent 'dirty' state, we introduce an additional flag:
121 | 
122 | - _"isDefaultValue"_, whether the field's current value is the default value
123 | 
124 | ```ts
125 | const { isDefaultValue, isTouched } = field.state.meta
126 | 
127 | // The following line will re-create the non-Persistent `dirty` functionality.
128 | const nonPersistentIsDirty = !isDefaultValue
129 | ```
130 | 
131 | ![Field states extended](https://raw.githubusercontent.com/TanStack/form/main/docs/assets/field-states-extended.png)
132 | 
133 | ## Field API
134 | 
135 | The Field API is an object passed to the render prop function when creating a field. It provides methods for working with the field's state.
136 | 
137 | Example:
138 | 
139 | ```tsx
140 | <input
141 |   value={field.state.value}
142 |   onBlur={field.handleBlur}
143 |   onChange={(e) => field.handleChange(e.target.value)}
144 | />
145 | ```
146 | 
147 | ## Validation
148 | 
149 | `@tanstack/react-form` provides both synchronous and asynchronous validation out of the box. Validation functions can be passed to the `form.Field` component using the `validators` prop.
150 | 
151 | Example:
152 | 
153 | ```tsx
154 | <form.Field
155 |   name="firstName"
156 |   validators={{
157 |     onChange: ({ value }) =>
158 |       !value
159 |         ? 'A first name is required'
160 |         : value.length < 3
161 |           ? 'First name must be at least 3 characters'
162 |           : undefined,
163 |     onChangeAsync: async ({ value }) => {
164 |       await new Promise((resolve) => setTimeout(resolve, 1000))
165 |       return value.includes('error') && 'No "error" allowed in first name'
166 |     },
167 |   }}
168 |   children={(field) => (
169 |     <>
170 |       <input
171 |         value={field.state.value}
172 |         onBlur={field.handleBlur}
173 |         onChange={(e) => field.handleChange(e.target.value)}
174 |       />
175 |       <FieldInfo field={field} />
176 |     </>
177 |   )}
178 | />
179 | ```
180 | 
181 | ## Validation with Standard Schema Libraries
182 | 
183 | In addition to hand-rolled validation options, we also support the [Standard Schema](https://github.com/standard-schema/standard-schema) specification.
184 | 
185 | You can define a schema using any of the libraries implementing the specification and pass it to a form or field validator.
186 | 
187 | Supported libraries include:
188 | 
189 | - [Zod](https://zod.dev/)
190 | - [Valibot](https://valibot.dev/)
191 | - [ArkType](https://arktype.io/)
192 | 
193 | ```tsx
194 | import { z } from 'zod'
195 | 
196 | const userSchema = z.object({
197 |   age: z.number().gte(13, 'You must be 13 to make an account'),
198 | })
199 | 
200 | function App() {
201 |   const form = useForm({
202 |     defaultValues: {
203 |       age: 0,
204 |     },
205 |     validators: {
206 |       onChange: userSchema,
207 |     },
208 |   })
209 |   return (
210 |     <div>
211 |       <form.Field
212 |         name="age"
213 |         children={(field) => {
214 |           return <>{/* ... */}</>
215 |         }}
216 |       />
217 |     </div>
218 |   )
219 | }
220 | ```
221 | 
222 | ## Reactivity
223 | 
224 | `@tanstack/react-form` offers various ways to subscribe to form and field state changes, most notably the `useStore(form.store)` hook and the `form.Subscribe` component. These methods allow you to optimize your form's rendering performance by only updating components when necessary.
225 | 
226 | Example:
227 | 
228 | ```tsx
229 | const firstName = useStore(form.store, (state) => state.values.firstName)
230 | //...
231 | <form.Subscribe
232 |   selector={(state) => [state.canSubmit, state.isSubmitting]}
233 |   children={([canSubmit, isSubmitting]) => (
234 |     <button type="submit" disabled={!canSubmit}>
235 |       {isSubmitting ? '...' : 'Submit'}
236 |     </button>
237 |   )}
238 | />
239 | ```
240 | 
241 | It is important to remember that while the `useStore` hook's `selector` prop is optional, it is strongly recommended to provide one, as omitting it will result in unnecessary re-renders.
242 | 
243 | ```tsx
244 | // Correct use
245 | const firstName = useStore(form.store, (state) => state.values.firstName)
246 | const errors = useStore(form.store, (state) => state.errorMap)
247 | // Incorrect use
248 | const store = useStore(form.store)
249 | ```
250 | 
251 | Note: The usage of the `useField` hook to achieve reactivity is discouraged since it is designed to be used thoughtfully within the `form.Field` component. You might want to use `useStore(form.store)` instead.
252 | 
253 | ## Listeners
254 | 
255 | `@tanstack/react-form` allows you to react to specific triggers and "listen" to them to dispatch side effects.
256 | 
257 | Example:
258 | 
259 | ```tsx
260 | <form.Field
261 |   name="country"
262 |   listeners={{
263 |     onChange: ({ value }) => {
264 |       console.log(`Country changed to: ${value}, resetting province`)
265 |       form.setFieldValue('province', '')
266 |     },
267 |   }}
268 | />
269 | ```
270 | 
271 | More information can be found at [Listeners](../listeners.md)
272 | 
273 | ## Array Fields
274 | 
275 | Array fields allow you to manage a list of values within a form, such as a list of hobbies. You can create an array field using the `form.Field` component with the `mode="array"` prop.
276 | 
277 | When working with array fields, you can use the fields `pushValue`, `removeValue`, `swapValues` and `moveValue` methods to add, remove, and swap values in the array.
278 | 
279 | Example:
280 | 
281 | ```tsx
282 | <form.Field
283 |   name="hobbies"
284 |   mode="array"
285 |   children={(hobbiesField) => (
286 |     <div>
287 |       Hobbies
288 |       <div>
289 |         {!hobbiesField.state.value.length
290 |           ? 'No hobbies found.'
291 |           : hobbiesField.state.value.map((_, i) => (
292 |               <div key={i}>
293 |                 <form.Field
294 |                   name={`hobbies[${i}].name`}
295 |                   children={(field) => {
296 |                     return (
297 |                       <div>
298 |                         <label htmlFor={field.name}>Name:</label>
299 |                         <input
300 |                           id={field.name}
301 |                           name={field.name}
302 |                           value={field.state.value}
303 |                           onBlur={field.handleBlur}
304 |                           onChange={(e) => field.handleChange(e.target.value)}
305 |                         />
306 |                         <button
307 |                           type="button"
308 |                           onClick={() => hobbiesField.removeValue(i)}
309 |                         >
310 |                           X
311 |                         </button>
312 |                         <FieldInfo field={field} />
313 |                       </div>
314 |                     )
315 |                   }}
316 |                 />
317 |                 <form.Field
318 |                   name={`hobbies[${i}].description`}
319 |                   children={(field) => {
320 |                     return (
321 |                       <div>
322 |                         <label htmlFor={field.name}>Description:</label>
323 |                         <input
324 |                           id={field.name}
325 |                           name={field.name}
326 |                           value={field.state.value}
327 |                           onBlur={field.handleBlur}
328 |                           onChange={(e) => field.handleChange(e.target.value)}
329 |                         />
330 |                         <FieldInfo field={field} />
331 |                       </div>
332 |                     )
333 |                   }}
334 |                 />
335 |               </div>
336 |             ))}
337 |       </div>
338 |       <button
339 |         type="button"
340 |         onClick={() =>
341 |           hobbiesField.pushValue({
342 |             name: '',
343 |             description: '',
344 |             yearsOfExperience: 0,
345 |           })
346 |         }
347 |       >
348 |         Add hobby
349 |       </button>
350 |     </div>
351 |   )}
352 | />
353 | ```
354 | 
355 | ## Reset Buttons
356 | 
357 | When using `<button type="reset">` in conjunction with TanStack Form's `form.reset()`, you need to prevent the default HTML reset behavior to avoid unexpected resets of form elements (especially `<select>` elements) to their initial HTML values.
358 | Use `event.preventDefault()` inside the button's `onClick` handler to prevent the native form reset.
359 | 
360 | Example:
361 | 
362 | ```tsx
363 | <button
364 |   type="reset"
365 |   onClick={(event) => {
366 |     event.preventDefault()
367 |     form.reset()
368 |   }}
369 | >
370 |   Reset
371 | </button>
372 | ```
373 | 
374 | Alternatively, you can use `<button type="button">` to prevent the native HTML reset.
375 | 
376 | ```tsx
377 | <button
378 |   type="button"
379 |   onClick={() => {
380 |     form.reset()
381 |   }}
382 | >
383 |   Reset
384 | </button>
385 | ```
386 | 
387 | These are the basic concepts and terminology used in the `@tanstack/react-form` library. Understanding these concepts will help you work more effectively with the library and create complex forms with ease.
388 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/custom-errors.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: custom-errors
  3 | title: Custom Errors
  4 | ---
  5 | 
  6 | TanStack Form provides complete flexibility in the types of error values you can return from validators. String errors are the most common and easy to work with, but the library allows you to return any type of value from your validators.
  7 | 
  8 | As a general rule, any truthy value is considered as an error and will mark the form or field as invalid, while falsy values (`false`, `undefined`, `null`, etc..) mean there is no error, the form or field is valid.
  9 | 
 10 | ## Return String Values from Forms
 11 | 
 12 | ```tsx
 13 | <form.Field
 14 |   name="username"
 15 |   validators={{
 16 |     onChange: ({ value }) =>
 17 |       value.length < 3 ? 'Username must be at least 3 characters' : undefined,
 18 |   }}
 19 | />
 20 | ```
 21 | 
 22 | For form-level validation affecting multiple fields:
 23 | 
 24 | ```tsx
 25 | const form = useForm({
 26 |   defaultValues: {
 27 |     username: '',
 28 |     email: '',
 29 |   },
 30 |   validators: {
 31 |     onChange: ({ value }) => {
 32 |       return {
 33 |         fields: {
 34 |           username:
 35 |             value.username.length < 3 ? 'Username too short' : undefined,
 36 |           email: !value.email.includes('@') ? 'Invalid email' : undefined,
 37 |         },
 38 |       }
 39 |     },
 40 |   },
 41 | })
 42 | ```
 43 | 
 44 | String errors are the most common type and are easily displayed in your UI:
 45 | 
 46 | ```tsx
 47 | {
 48 |   field.state.meta.errors.map((error, i) => (
 49 |     <div key={i} className="error">
 50 |       {error}
 51 |     </div>
 52 |   ))
 53 | }
 54 | ```
 55 | 
 56 | ### Numbers
 57 | 
 58 | Useful for representing quantities, thresholds, or magnitudes:
 59 | 
 60 | ```tsx
 61 | <form.Field
 62 |   name="age"
 63 |   validators={{
 64 |     onChange: ({ value }) => (value < 18 ? 18 - value : undefined),
 65 |   }}
 66 | />
 67 | ```
 68 | 
 69 | Display in UI:
 70 | 
 71 | ```tsx
 72 | {
 73 |   /* TypeScript knows the error is a number based on your validator */
 74 | }
 75 | ;<div className="error">
 76 |   You need {field.state.meta.errors[0]} more years to be eligible
 77 | </div>
 78 | ```
 79 | 
 80 | ### Booleans
 81 | 
 82 | Simple flags to indicate error state:
 83 | 
 84 | ```tsx
 85 | <form.Field
 86 |   name="accepted"
 87 |   validators={{
 88 |     onChange: ({ value }) => (!value ? true : undefined),
 89 |   }}
 90 | />
 91 | ```
 92 | 
 93 | Display in UI:
 94 | 
 95 | ```tsx
 96 | {
 97 |   field.state.meta.errors[0] === true && (
 98 |     <div className="error">You must accept the terms</div>
 99 |   )
100 | }
101 | ```
102 | 
103 | ### Objects
104 | 
105 | Rich error objects with multiple properties:
106 | 
107 | ```tsx
108 | <form.Field
109 |   name="email"
110 |   validators={{
111 |     onChange: ({ value }) => {
112 |       if (!value.includes('@')) {
113 |         return {
114 |           message: 'Invalid email format',
115 |           severity: 'error',
116 |           code: 1001,
117 |         }
118 |       }
119 |       return undefined
120 |     },
121 |   }}
122 | />
123 | ```
124 | 
125 | Display in UI:
126 | 
127 | ```tsx
128 | {
129 |   typeof field.state.meta.errors[0] === 'object' && (
130 |     <div className={`error ${field.state.meta.errors[0].severity}`}>
131 |       {field.state.meta.errors[0].message}
132 |       <small> (Code: {field.state.meta.errors[0].code})</small>
133 |     </div>
134 |   )
135 | }
136 | ```
137 | 
138 | in the example above it depends on the event error you want to display.
139 | 
140 | ### Arrays
141 | 
142 | Multiple error messages for a single field:
143 | 
144 | ```tsx
145 | <form.Field
146 |   name="password"
147 |   validators={{
148 |     onChange: ({ value }) => {
149 |       const errors = []
150 |       if (value.length < 8) errors.push('Password too short')
151 |       if (!/[A-Z]/.test(value)) errors.push('Missing uppercase letter')
152 |       if (!/[0-9]/.test(value)) errors.push('Missing number')
153 | 
154 |       return errors.length ? errors : undefined
155 |     },
156 |   }}
157 | />
158 | ```
159 | 
160 | Display in UI:
161 | 
162 | ```tsx
163 | {
164 |   Array.isArray(field.state.meta.errors) && (
165 |     <ul className="error-list">
166 |       {field.state.meta.errors.map((err, i) => (
167 |         <li key={i}>{err}</li>
168 |       ))}
169 |     </ul>
170 |   )
171 | }
172 | ```
173 | 
174 | ## The `disableErrorFlat` Prop on Fields
175 | 
176 | By default, TanStack Form flattens errors from all validation sources (onChange, onBlur, onSubmit) into a single `errors` array. The `disableErrorFlat` prop preserves the error sources:
177 | 
178 | ```tsx
179 | <form.Field
180 |   name="email"
181 |   disableErrorFlat
182 |   validators={{
183 |     onChange: ({ value }) =>
184 |       !value.includes('@') ? 'Invalid email format' : undefined,
185 |     onBlur: ({ value }) =>
186 |       !value.endsWith('.com') ? 'Only .com domains allowed' : undefined,
187 |     onSubmit: ({ value }) => (value.length < 5 ? 'Email too short' : undefined),
188 |   }}
189 | />
190 | ```
191 | 
192 | Without `disableErrorFlat`, all errors would be combined into `field.state.meta.errors`. With it, you can access errors by their source:
193 | 
194 | ```tsx
195 | {
196 |   field.state.meta.errorMap.onChange && (
197 |     <div className="real-time-error">{field.state.meta.errorMap.onChange}</div>
198 |   )
199 | }
200 | 
201 | {
202 |   field.state.meta.errorMap.onBlur && (
203 |     <div className="blur-feedback">{field.state.meta.errorMap.onBlur}</div>
204 |   )
205 | }
206 | 
207 | {
208 |   field.state.meta.errorMap.onSubmit && (
209 |     <div className="submit-error">{field.state.meta.errorMap.onSubmit}</div>
210 |   )
211 | }
212 | ```
213 | 
214 | This is useful for:
215 | 
216 | - Displaying different types of errors with different UI treatments
217 | - Prioritizing errors (e.g., showing submission errors more prominently)
218 | - Implementing progressive disclosure of errors
219 | 
220 | ## Type Safety of `errors` and `errorMap`
221 | 
222 | TanStack Form provides strong type safety for error handling. Each key in the `errorMap` has exactly the type returned by its corresponding validator, while the `errors` array contains a union type of all the possible error values from all validators:
223 | 
224 | ```tsx
225 | <form.Field
226 |   name="password"
227 |   validators={{
228 |     onChange: ({ value }) => {
229 |       // This returns a string or undefined
230 |       return value.length < 8 ? 'Too short' : undefined
231 |     },
232 |     onBlur: ({ value }) => {
233 |       // This returns an object or undefined
234 |       if (!/[A-Z]/.test(value)) {
235 |         return { message: 'Missing uppercase', level: 'warning' }
236 |       }
237 |       return undefined
238 |     },
239 |   }}
240 |   children={(field) => {
241 |     // TypeScript knows that errors[0] can be string | { message: string, level: string } | undefined
242 |     const error = field.state.meta.errors[0]
243 | 
244 |     // Type-safe error handling
245 |     if (typeof error === 'string') {
246 |       return <div className="string-error">{error}</div>
247 |     } else if (error && typeof error === 'object') {
248 |       return <div className={error.level}>{error.message}</div>
249 |     }
250 | 
251 |     return null
252 |   }}
253 | />
254 | ```
255 | 
256 | The `errorMap` property is also fully typed, matching the return types of your validation functions:
257 | 
258 | ```tsx
259 | // With disableErrorFlat
260 | <form.Field
261 |   name="email"
262 |   disableErrorFlat
263 |   validators={{
264 |     onChange: ({ value }): string | undefined =>
265 |       !value.includes("@") ? "Invalid email" : undefined,
266 |     onBlur: ({ value }): { code: number, message: string } | undefined =>
267 |       !value.endsWith(".com") ? { code: 100, message: "Wrong domain" } : undefined
268 |   }}
269 |   children={(field) => {
270 |     // TypeScript knows the exact type of each error source
271 |     const onChangeError: string | undefined = field.state.meta.errorMap.onChange;
272 |     const onBlurError: { code: number, message: string } | undefined = field.state.meta.errorMap.onBlur;
273 | 
274 |     return (/* ... */);
275 |   }}
276 | />
277 | ```
278 | 
279 | This type safety helps catch errors at compile time instead of runtime, making your code more reliable and maintainable.
280 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/debugging.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: debugging
 3 | title: Debugging React Usage
 4 | ---
 5 | 
 6 | Here's a list of common errors you might see in the console and how to fix them.
 7 | 
 8 | ## Changing an uncontrolled input to be controlled
 9 | 
10 | If you see this error in the console:
11 | 
12 | ```
13 | Warning: A component is changing an uncontrolled input to be controlled. This is likely caused by the value changing from undefined to a defined value, which should not happen. Decide between using a controlled or uncontrolled input element for the lifetime of the component. More info: https://reactjs.org/link/controlled-components
14 | ```
15 | 
16 | It's likely you forgot the `defaultValues` in your `useForm` Hook or `form.Field` component usage. This is occurring
17 | because the input is being rendered before the form value is initialized and is therefore changing from `undefined` to `""` when a text input is made.
18 | 
19 | ## Field value is of type `unknown`
20 | 
21 | If you're using `form.Field` and, upon inspecting the value of `field.state.value`, you see that the value of a field is of type `unknown`, it's likely that your form's type was too large for us to safely evaluate.
22 | 
23 | This typically is a sign that you should break down your form into smaller forms or use a more specific type for your form.
24 | 
25 | A workaround to this problem is to cast `field.state.value` using TypeScript's `as` keyword:
26 | 
27 | ```tsx
28 | const value = field.state.value as string
29 | ```
30 | 
31 | ## `Type instantiation is excessively deep and possibly infinite`
32 | 
33 | If you see this error in the console when running `tsc`:
34 | 
35 | ```
36 | Type instantiation is excessively deep and possibly infinite
37 | ```
38 | 
39 | You've ran into a bug that we didn't catch in our type definitions. While we've done our best to make sure our types are as accurate as possible, there are some edge cases where TypeScript struggled with the complexity of our types.
40 | 
41 | Please [report this issue to us on GitHub](https://github.com/TanStack/form/issues) so we can fix it. Just make sure to include a minimal reproduction so that we're able to help you debug.
42 | 
43 | > Keep in mind that this error is a TypeScript error and not a runtime error. This means that your code will still run on the user's machine as expected.
44 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/form-composition.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: form-composition
  3 | title: Form Composition
  4 | ---
  5 | 
  6 | A common criticism of TanStack Form is its verbosity out-of-the-box. While this _can_ be useful for educational purposes - helping enforce understanding our APIs - it's not ideal in production use cases.
  7 | 
  8 | As a result, while `form.Field` enables the most powerful and flexible usage of TanStack Form, we provide APIs that wrap it and make your application code less verbose.
  9 | 
 10 | ## Custom Form Hooks
 11 | 
 12 | The most powerful way to compose forms is to create custom form hooks. This allows you to create a form hook that is tailored to your application's needs, including pre-bound custom UI components and more.
 13 | 
 14 | At it's most basic, `createFormHook` is a function that takes a `fieldContext` and `formContext` and returns a `useAppForm` hook.
 15 | 
 16 | > This un-customized `useAppForm` hook is identical to `useForm`, but that will quickly change as we add more options to `createFormHook`.
 17 | 
 18 | ```tsx
 19 | import { createFormHookContexts, createFormHook } from '@tanstack/react-form'
 20 | 
 21 | // export useFieldContext for use in your custom components
 22 | export const { fieldContext, formContext, useFieldContext } =
 23 |   createFormHookContexts()
 24 | 
 25 | const { useAppForm } = createFormHook({
 26 |   fieldContext,
 27 |   formContext,
 28 |   // We'll learn more about these options later
 29 |   fieldComponents: {},
 30 |   formComponents: {},
 31 | })
 32 | 
 33 | function App() {
 34 |   const form = useAppForm({
 35 |     // Supports all useForm options
 36 |     defaultValues: {
 37 |       firstName: 'John',
 38 |       lastName: 'Doe',
 39 |     },
 40 |   })
 41 | 
 42 |   return <form.Field /> // ...
 43 | }
 44 | ```
 45 | 
 46 | ### Pre-bound Field Components
 47 | 
 48 | Once this scaffolding is in place, you can start adding custom field and form components to your form hook.
 49 | 
 50 | > Note: the `useFieldContext` must be the same one exported from your custom form context
 51 | 
 52 | ```tsx
 53 | import { useFieldContext } from './form-context.tsx'
 54 | 
 55 | export function TextField({ label }: { label: string }) {
 56 |   // The `Field` infers that it should have a `value` type of `string`
 57 |   const field = useFieldContext<string>()
 58 |   return (
 59 |     <label>
 60 |       <div>{label}</div>
 61 |       <input
 62 |         value={field.state.value}
 63 |         onChange={(e) => field.handleChange(e.target.value)}
 64 |       />
 65 |     </label>
 66 |   )
 67 | }
 68 | ```
 69 | 
 70 | You're then able to register this component with your form hook.
 71 | 
 72 | ```tsx
 73 | import { TextField } from './text-field.tsx'
 74 | 
 75 | const { useAppForm } = createFormHook({
 76 |   fieldContext,
 77 |   formContext,
 78 |   fieldComponents: {
 79 |     TextField,
 80 |   },
 81 |   formComponents: {},
 82 | })
 83 | ```
 84 | 
 85 | And use it in your form:
 86 | 
 87 | ```tsx
 88 | function App() {
 89 |   const form = useAppForm({
 90 |     defaultValues: {
 91 |       firstName: 'John',
 92 |       lastName: 'Doe',
 93 |     },
 94 |   })
 95 | 
 96 |   return (
 97 |     // Notice the `AppField` instead of `Field`; `AppField` provides the required context
 98 |     <form.AppField
 99 |       name="firstName"
100 |       children={(field) => <field.TextField label="First Name" />}
101 |     />
102 |   )
103 | }
104 | ```
105 | 
106 | This not only allows you to reuse the UI of your shared component, but retains the type-safety you'd expect from TanStack Form: Typo `name` and get a TypeScript error.
107 | 
108 | #### A note on performance
109 | 
110 | While context is a valuable tool in the React ecosystem, there's appropriate concern from many users that providing a reactive value through a context will cause unnecessary re-renders.
111 | 
112 | > Unfamiliar with this performance concern? [Mark Erikson's blog post explaining why Redux solves many of these problems](https://blog.isquaredsoftware.com/2021/01/context-redux-differences/) is a great place to start.
113 | 
114 | While this is a good concern to call out, it's not a problem for TanStack Form; the values provided through context are not reactive themselves, but instead are static class instances with reactive properties ([using TanStack Store as our signals implementation to power the show](https://tanstack.com/store)).
115 | 
116 | ### Pre-bound Form Components
117 | 
118 | While `form.AppField` solves many of the problems with Field boilerplate and reusability, it doesn't solve the problem of _form_ boilerplate and reusability.
119 | 
120 | In particular, being able to share instances of `form.Subscribe` for, say, a reactive form submission button is a common usecase.
121 | 
122 | ```tsx
123 | function SubscribeButton({ label }: { label: string }) {
124 |   const form = useFormContext()
125 |   return (
126 |     <form.Subscribe selector={(state) => state.isSubmitting}>
127 |       {(isSubmitting) => (
128 |         <button type="submit" disabled={isSubmitting}>
129 |           {label}
130 |         </button>
131 |       )}
132 |     </form.Subscribe>
133 |   )
134 | }
135 | 
136 | const { useAppForm, withForm } = createFormHook({
137 |   fieldComponents: {},
138 |   formComponents: {
139 |     SubscribeButton,
140 |   },
141 |   fieldContext,
142 |   formContext,
143 | })
144 | 
145 | function App() {
146 |   const form = useAppForm({
147 |     defaultValues: {
148 |       firstName: 'John',
149 |       lastName: 'Doe',
150 |     },
151 |   })
152 | 
153 |   return (
154 |     <form.AppForm>
155 |       // Notice the `AppForm` component wrapper; `AppForm` provides the required
156 |       context
157 |       <form.SubscribeButton label="Submit" />
158 |     </form.AppForm>
159 |   )
160 | }
161 | ```
162 | 
163 | ## Breaking big forms into smaller pieces
164 | 
165 | Sometimes forms get very large; it's just how it goes sometimes. While TanStack Form supports large forms well, it's never fun to work with hundreds or thousands of lines of code long files.
166 | 
167 | To solve this, we support breaking forms into smaller pieces using the `withForm` higher-order component.
168 | 
169 | ```tsx
170 | const { useAppForm, withForm } = createFormHook({
171 |   fieldComponents: {
172 |     TextField,
173 |   },
174 |   formComponents: {
175 |     SubscribeButton,
176 |   },
177 |   fieldContext,
178 |   formContext,
179 | })
180 | 
181 | const ChildForm = withForm({
182 |   // These values are only used for type-checking, and are not used at runtime
183 |   // This allows you to `...formOpts` from `formOptions` without needing to redeclare the options
184 |   defaultValues: {
185 |     firstName: 'John',
186 |     lastName: 'Doe',
187 |   },
188 |   // Optional, but adds props to the `render` function in addition to `form`
189 |   props: {
190 |     // These props are also set as default values for the `render` function
191 |     title: 'Child Form',
192 |   },
193 |   render: function Render({ form, title }) {
194 |     return (
195 |       <div>
196 |         <p>{title}</p>
197 |         <form.AppField
198 |           name="firstName"
199 |           children={(field) => <field.TextField label="First Name" />}
200 |         />
201 |         <form.AppForm>
202 |           <form.SubscribeButton label="Submit" />
203 |         </form.AppForm>
204 |       </div>
205 |     )
206 |   },
207 | })
208 | 
209 | function App() {
210 |   const form = useAppForm({
211 |     defaultValues: {
212 |       firstName: 'John',
213 |       lastName: 'Doe',
214 |     },
215 |   })
216 | 
217 |   return <ChildForm form={form} title={'Testing'} />
218 | }
219 | ```
220 | 
221 | ### `withForm` FAQ
222 | 
223 | > Why a higher-order component instead of a hook?
224 | 
225 | While hooks are the future of React, higher-order components are still a powerful tool for composition. In particular, the API of `withForm` enables us to have strong type-safety without requiring users to pass generics.
226 | 
227 | > Why am I getting ESLint errors about hooks in `render`?
228 | 
229 | ESLint looks for hooks in the top-level of a function, and `render` may not be recogized as a top-level component, depending on how you defined it.
230 | 
231 | ```tsx
232 | // This will cause ESLint errors with hooks usage
233 | const ChildForm = withForm({
234 |   // ...
235 |   render: ({ form, title }) => {
236 |     // ...
237 |   },
238 | })
239 | ```
240 | 
241 | ```tsx
242 | // This works fine
243 | const ChildForm = withForm({
244 |   // ...
245 |   render: function Render({ form, title }) {
246 |     // ...
247 |   },
248 | })
249 | ```
250 | 
251 | ## Tree-shaking form and field components
252 | 
253 | While the above examples are great for getting started, they're not ideal for certain use-cases where you might have hundreds of form and field components.
254 | In particular, you may not want to include all of your form and field components in the bundle of every file that uses your form hook.
255 | 
256 | To solve this, you can mix the `createFormHook` TanStack API with the React `lazy` and `Suspense` components:
257 | 
258 | ```typescript
259 | // src/hooks/form-context.ts
260 | import { createFormHookContexts } from '@tanstack/react-form'
261 | 
262 | export const { fieldContext, useFieldContext, formContext, useFormContext } =
263 |   createFormHookContexts()
264 | ```
265 | 
266 | ```tsx
267 | // src/components/text-field.tsx
268 | import { useFieldContext } from '../hooks/form-context.tsx'
269 | 
270 | export default function TextField({ label }: { label: string }) {
271 |   const field = useFieldContext<string>()
272 | 
273 |   return (
274 |     <label>
275 |       <div>{label}</div>
276 |       <input
277 |         value={field.state.value}
278 |         onChange={(e) => field.handleChange(e.target.value)}
279 |       />
280 |     </label>
281 |   )
282 | }
283 | ```
284 | 
285 | ```tsx
286 | // src/hooks/form.ts
287 | import { lazy } from 'react'
288 | import { createFormHook } from '@tanstack/react-form'
289 | 
290 | const TextField = lazy(() => import('../components/text-fields.tsx'))
291 | 
292 | const { useAppForm, withForm } = createFormHook({
293 |   fieldContext,
294 |   formContext,
295 |   fieldComponents: {
296 |     TextField,
297 |   },
298 |   formComponents: {},
299 | })
300 | ```
301 | 
302 | ```tsx
303 | // src/App.tsx
304 | import { Suspense } from 'react'
305 | import { PeoplePage } from './features/people/page.tsx'
306 | 
307 | export default function App() {
308 |   return (
309 |     <Suspense fallback={<p>Loading...</p>}>
310 |       <PeopleForm />
311 |     </Suspense>
312 |   )
313 | }
314 | ```
315 | 
316 | This will show the Suspense fallback while the `TextField` component is being loaded, and then render the form once it's loaded.
317 | 
318 | ## Putting it all together
319 | 
320 | Now that we've covered the basics of creating custom form hooks, let's put it all together in a single example.
321 | 
322 | ```tsx
323 | // /src/hooks/form.ts, to be used across the entire app
324 | const { fieldContext, useFieldContext, formContext, useFormContext } =
325 |   createFormHookContexts()
326 | 
327 | function TextField({ label }: { label: string }) {
328 |   const field = useFieldContext<string>()
329 |   return (
330 |     <label>
331 |       <div>{label}</div>
332 |       <input
333 |         value={field.state.value}
334 |         onChange={(e) => field.handleChange(e.target.value)}
335 |       />
336 |     </label>
337 |   )
338 | }
339 | 
340 | function SubscribeButton({ label }: { label: string }) {
341 |   const form = useFormContext()
342 |   return (
343 |     <form.Subscribe selector={(state) => state.isSubmitting}>
344 |       {(isSubmitting) => <button disabled={isSubmitting}>{label}</button>}
345 |     </form.Subscribe>
346 |   )
347 | }
348 | 
349 | const { useAppForm, withForm } = createFormHook({
350 |   fieldComponents: {
351 |     TextField,
352 |   },
353 |   formComponents: {
354 |     SubscribeButton,
355 |   },
356 |   fieldContext,
357 |   formContext,
358 | })
359 | 
360 | // /src/features/people/shared-form.ts, to be used across `people` features
361 | const formOpts = formOptions({
362 |   defaultValues: {
363 |     firstName: 'John',
364 |     lastName: 'Doe',
365 |   },
366 | })
367 | 
368 | // /src/features/people/nested-form.ts, to be used in the `people` page
369 | const ChildForm = withForm({
370 |   ...formOpts,
371 |   // Optional, but adds props to the `render` function outside of `form`
372 |   props: {
373 |     title: 'Child Form',
374 |   },
375 |   render: ({ form, title }) => {
376 |     return (
377 |       <div>
378 |         <p>{title}</p>
379 |         <form.AppField
380 |           name="firstName"
381 |           children={(field) => <field.TextField label="First Name" />}
382 |         />
383 |         <form.AppForm>
384 |           <form.SubscribeButton label="Submit" />
385 |         </form.AppForm>
386 |       </div>
387 |     )
388 |   },
389 | })
390 | 
391 | // /src/features/people/page.ts
392 | const Parent = () => {
393 |   const form = useAppForm({
394 |     ...formOpts,
395 |   })
396 | 
397 |   return <ChildForm form={form} title={'Testing'} />
398 | }
399 | ```
400 | 
401 | ## API Usage Guidance
402 | 
403 | Here's a chart to help you decide what APIs you should be using:
404 | 
405 | ![](https://raw.githubusercontent.com/TanStack/form/main/docs/assets/react_form_composability.svg)
406 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/linked-fields.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: linked-fields
 3 | title: Link Two Form Fields Together
 4 | ---
 5 | 
 6 | You may find yourself needing to link two fields together; when one is validated as another field's value has changed.
 7 | One such usage is when you have both a `password` and `confirm_password` field,
 8 | where you want to `confirm_password` to error out when `password`'s value does not match;
 9 | regardless of which field triggered the value change.
10 | 
11 | Imagine the following userflow:
12 | 
13 | - User updates confirm password field.
14 | - User updates the non-confirm password field.
15 | 
16 | In this example, the form will still have errors present,
17 | as the "confirm password" field validation has not been re-ran to mark as accepted.
18 | 
19 | To solve this, we need to make sure that the "confirm password" validation is re-run when the password field is updated.
20 | To do this, you can add a `onChangeListenTo` property to the `confirm_password` field.
21 | 
22 | ```tsx
23 | function App() {
24 |   const form = useForm({
25 |     defaultValues: {
26 |       password: '',
27 |       confirm_password: '',
28 |     },
29 |     // ...
30 |   })
31 | 
32 |   return (
33 |     <div>
34 |       <form.Field name="password">
35 |         {(field) => (
36 |           <label>
37 |             <div>Password</div>
38 |             <input
39 |               value={field.state.value}
40 |               onChange={(e) => field.handleChange(e.target.value)}
41 |             />
42 |           </label>
43 |         )}
44 |       </form.Field>
45 |       <form.Field
46 |         name="confirm_password"
47 |         validators={{
48 |           onChangeListenTo: ['password'],
49 |           onChange: ({ value, fieldApi }) => {
50 |             if (value !== fieldApi.form.getFieldValue('password')) {
51 |               return 'Passwords do not match'
52 |             }
53 |             return undefined
54 |           },
55 |         }}
56 |       >
57 |         {(field) => (
58 |           <div>
59 |             <label>
60 |               <div>Confirm Password</div>
61 |               <input
62 |                 value={field.state.value}
63 |                 onChange={(e) => field.handleChange(e.target.value)}
64 |               />
65 |             </label>
66 |             {field.state.meta.errors.map((err) => (
67 |               <div key={err}>{err}</div>
68 |             ))}
69 |           </div>
70 |         )}
71 |       </form.Field>
72 |     </div>
73 |   )
74 | }
75 | ```
76 | 
77 | This similarly works with `onBlurListenTo` property, which will re-run the validation when the field is blurred.
78 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/listeners.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: listeners
  3 | title: Side effects for event triggers
  4 | ---
  5 | 
  6 | For situations where you want to "affect" or "react" to triggers, there's the listener API. For example, if you, as the developer, want to reset a form field as a result of another field changing, you would use the listener API.
  7 | 
  8 | Imagine the following user flow:
  9 | 
 10 | - User selects a country from a drop-down.
 11 | - User then selects a province from another drop-down.
 12 | - User changes the selected country to a different one.
 13 | 
 14 | In this example, when the user changes the country, the selected province needs to be reset as it's no longer valid. With the listener API, we can subscribe to the onChange event and dispatch a reset to the field "province" when the listener is fired.
 15 | 
 16 | Events that can be "listened" to are:
 17 | 
 18 | - `onChange`
 19 | - `onBlur`
 20 | - `onMount`
 21 | - `onSubmit`
 22 | 
 23 | ```tsx
 24 | function App() {
 25 |   const form = useForm({
 26 |     defaultValues: {
 27 |       country: '',
 28 |       province: '',
 29 |     },
 30 |     // ...
 31 |   })
 32 | 
 33 |   return (
 34 |     <div>
 35 |       <form.Field
 36 |         name="country"
 37 |         listeners={{
 38 |           onChange: ({ value }) => {
 39 |             console.log(`Country changed to: ${value}, resetting province`)
 40 |             form.setFieldValue('province', '')
 41 |           },
 42 |         }}
 43 |       >
 44 |         {(field) => (
 45 |           <label>
 46 |             <div>Country</div>
 47 |             <input
 48 |               value={field.state.value}
 49 |               onChange={(e) => field.handleChange(e.target.value)}
 50 |             />
 51 |           </label>
 52 |         )}
 53 |       </form.Field>
 54 | 
 55 |       <form.Field name="province">
 56 |         {(field) => (
 57 |           <label>
 58 |             <div>Province</div>
 59 |             <input
 60 |               value={field.state.value}
 61 |               onChange={(e) => field.handleChange(e.target.value)}
 62 |             />
 63 |           </label>
 64 |         )}
 65 |       </form.Field>
 66 |     </div>
 67 |   )
 68 | }
 69 | ```
 70 | 
 71 | ### Built-in Debouncing
 72 | 
 73 | If you are making an API request inside a listener, you may want to debounce the calls as it can lead to performance issues.
 74 | We enable an easy method for debouncing your listeners by adding a `onChangeDebounceMs` or `onBlurDebounceMs`.
 75 | 
 76 | ```tsx
 77 | <form.Field
 78 |   name="country"
 79 |   listeners={{
 80 |     onChangeDebounceMs: 500, // 500ms debounce
 81 |     onChange: ({ value }) => {
 82 |       console.log(`Country changed to: ${value} without a change within 500ms, resetting province`)
 83 |       form.setFieldValue('province', '')
 84 |     },
 85 |   }}
 86 | >
 87 |   {(field) => (
 88 |     /* ... */
 89 |   )}
 90 | </form.Field>
 91 | ```
 92 | 
 93 | ### Form listeners
 94 | 
 95 | At a higher level, listeners are also available at the form level, allowing you access to the `onMount` and `onSubmit` events, and having `onChange` and `onBlur` propagated to all the form's children. Form-level listeners can also be debounced in the same way as previously discussed.
 96 | 
 97 | `onMount` and `onSubmit` listeners have to following props:
 98 | 
 99 | - `formApi`
100 | 
101 | `onChange` and `onBlur` listeners have access to:
102 | 
103 | - `fieldApi`
104 | - `formApi`
105 | 
106 | ```tsx
107 | const form = useForm({
108 |   listeners: {
109 |     onMount: ({ formApi }) => {
110 |       // custom logging service
111 |       loggingService('mount', formApi.state.values)
112 |     },
113 | 
114 |     onChange: ({ formApi, fieldApi }) => {
115 |       // autosave logic
116 |       if (formApi.state.isValid) {
117 |         formApi.handleSubmit()
118 |       }
119 | 
120 |       // fieldApi represents the field that triggered the event.
121 |       console.log(fieldApi.name, fieldApi.state.value)
122 |     },
123 |     onChangeDebounceMs: 500,
124 |   },
125 | })
126 | ```
127 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/react-native.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: react-native
 3 | title: Usage with React Native
 4 | ---
 5 | 
 6 | TanStack Form is headless and it should support React Native out-of-the-box without needing any additional configuration.
 7 | 
 8 | Here is an example:
 9 | 
10 | ```tsx
11 | <form.Field
12 |   name="age"
13 |   validators={{
14 |     onChange: (val) =>
15 |       val < 13 ? 'You must be 13 to make an account' : undefined,
16 |   }}
17 | >
18 |   {(field) => (
19 |     <>
20 |       <Text>Age:</Text>
21 |       <TextInput value={field.state.value} onChangeText={field.handleChange} />
22 |       {!field.state.meta.isValid && (
23 |         <Text>{field.state.meta.errors.join(', ')}</Text>
24 |       )}
25 |     </>
26 |   )}
27 | </form.Field>
28 | ```
29 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/reactivity.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: reactivity
 3 | title: Reactivity
 4 | ---
 5 | 
 6 | Tanstack Form doesn't cause re-renders when interacting with the form. So you might find yourself trying to use a form or field state value without success.
 7 | 
 8 | If you would like to access reactive values, you will need to subscribe to them using one of two methods: `useStore` or the `form.Subscribe` component.
 9 | 
10 | Some uses for these subscriptions are rendering up-to-date field values, determining what to render based on a condition, or using field values inside the logic of your component.
11 | 
12 | > For situations where you want to "react" to triggers, check out the [listener](../listeners.md) API.
13 | 
14 | ## useStore
15 | 
16 | The `useStore` hook is perfect when you need to access form values within the logic of your component. `useStore` takes two parameters. First, the form store. Second a selector to fine tune the piece of the form you wish to subscribe to.
17 | 
18 | ```tsx
19 | const firstName = useStore(form.store, (state) => state.values.firstName)
20 | const errors = useStore(form.store, (state) => state.errorMap)
21 | ```
22 | 
23 | You can access any piece of the form state in the selector.
24 | 
25 | > Note, that `useStore` will cause a whole component re-render whenever the value subscribed to changes.
26 | 
27 | While it IS possible to omit the selector, resist the urge as omitting it would result in many unnecessary re-renders whenever any of the form state changes.
28 | 
29 | ## form.Subscribe
30 | 
31 | The `form.Subscribe` component is best suited when you need to react to something within the UI of your component. For example, showing or hiding ui based on the value of a form field.
32 | 
33 | ```tsx
34 | <form.Subscribe
35 |   selector={(state) => state.values.firstName}
36 |   children={(firstName) => (
37 |     <form.Field>
38 |       {(field) => (
39 |         <input
40 |           name="lastName"
41 |           value={field.state.lastName}
42 |           onChange={field.handleChange}
43 |         />
44 |       )}
45 |     </form.Field>
46 |   )}
47 | />
48 | ```
49 | 
50 | > The `form.Subscribe` component doesn't trigger component-level re-renders. Anytime the value subscribed to changes, only the `form.Subscribe` component re-renders.
51 | 
52 | The choice between whether to use `useStore` or `form.Subscribe` mainly boils down to that if it's rendered in the ui, reach for `form.Subscribe` for its optimizations perks, and if you need the reactivity within the logic, then `useStore` is the choice to make.
53 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/ssr.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: ssr
  3 | title: React Meta-Framework Usage
  4 | ---
  5 | 
  6 | TanStack Form is compatible with React out of the box, supporting `SSR` and being framework-agnostic. However, specific configurations are necessary, according to your chosen framework.
  7 | 
  8 | Today we support the following meta-frameworks:
  9 | 
 10 | - [TanStack Start](https://tanstack.com/start/)
 11 | - [Next.js](https://nextjs.org/)
 12 | - [Remix](https://remix.run)
 13 | 
 14 | ## Using TanStack Form in TanStack Start
 15 | 
 16 | This section focuses on integrating TanStack Form with TanStack Start.
 17 | 
 18 | ### TanStack Start Prerequisites
 19 | 
 20 | - Start a new `TanStack Start` project, following the steps in the [TanStack Start Quickstart Guide](https://tanstack.com/router/latest/docs/framework/react/guide/tanstack-start)
 21 | - Install `@tanstack/react-form`
 22 | 
 23 | ### Start integration
 24 | 
 25 | Let's start by creating a `formOption` that we'll use to share the form's shape across the client and server.
 26 | 
 27 | ```typescript
 28 | // app/routes/index.tsx, but can be extracted to any other path
 29 | import { formOptions } from '@tanstack/react-form'
 30 | 
 31 | // You can pass other form options here
 32 | export const formOpts = formOptions({
 33 |   defaultValues: {
 34 |     firstName: '',
 35 |     age: 0,
 36 |   },
 37 | })
 38 | ```
 39 | 
 40 | Next, we can create [a Start Server Action](https://tanstack.com/start/latest/docs/framework/react/server-functions) that will handle the form submission on the server.
 41 | 
 42 | ```typescript
 43 | // app/routes/index.tsx, but can be extracted to any other path
 44 | import {
 45 |   createServerValidate,
 46 |   ServerValidateError,
 47 | } from '@tanstack/react-form/start'
 48 | 
 49 | const serverValidate = createServerValidate({
 50 |   ...formOpts,
 51 |   onServerValidate: ({ value }) => {
 52 |     if (value.age < 12) {
 53 |       return 'Server validation: You must be at least 12 to sign up'
 54 |     }
 55 |   },
 56 | })
 57 | 
 58 | export const handleForm = createServerFn({
 59 |   method: 'POST',
 60 | })
 61 |   .validator((data: unknown) => {
 62 |     if (!(data instanceof FormData)) {
 63 |       throw new Error('Invalid form data')
 64 |     }
 65 |     return data
 66 |   })
 67 |   .handler(async (ctx) => {
 68 |     try {
 69 |       const validatedData = await serverValidate(ctx.data)
 70 |       console.log('validatedData', validatedData)
 71 |       // Persist the form data to the database
 72 |       // await sql`
 73 |       //   INSERT INTO users (name, email, password)
 74 |       //   VALUES (${validatedData.name}, ${validatedData.email}, ${validatedData.password})
 75 |       // `
 76 |     } catch (e) {
 77 |       if (e instanceof ServerValidateError) {
 78 |         // Log form errors or do any other logic here
 79 |         return e.response
 80 |       }
 81 | 
 82 |       // Some other error occurred when parsing the form
 83 |       console.error(e)
 84 |       setResponseStatus(500)
 85 |       return 'There was an internal error'
 86 |     }
 87 | 
 88 |     return 'Form has validated successfully'
 89 |   })
 90 | ```
 91 | 
 92 | Then we need to establish a way to grab the form data from `serverValidate`'s `response` using another server action:
 93 | 
 94 | ```typescript
 95 | // app/routes/index.tsx, but can be extracted to any other path
 96 | import { getFormData } from '@tanstack/react-form/start'
 97 | 
 98 | export const getFormDataFromServer = createServerFn({ method: 'GET' }).handler(
 99 |   async () => {
100 |     return getFormData()
101 |   },
102 | )
103 | ```
104 | 
105 | Finally, we'll use `getFormDataFromServer` in our loader to get the state from our server into our client and `handleForm` in our client-side form component.
106 | 
107 | ```tsx
108 | // app/routes/index.tsx
109 | import { createFileRoute } from '@tanstack/react-router'
110 | import {
111 |   mergeForm,
112 |   useForm,
113 |   useStore,
114 |   useTransform,
115 | } from '@tanstack/react-form'
116 | 
117 | export const Route = createFileRoute('/')({
118 |   component: Home,
119 |   loader: async () => ({
120 |     state: await getFormDataFromServer(),
121 |   }),
122 | })
123 | 
124 | function Home() {
125 |   const { state } = Route.useLoaderData()
126 |   const form = useForm({
127 |     ...formOpts,
128 |     transform: useTransform((baseForm) => mergeForm(baseForm, state), [state]),
129 |   })
130 | 
131 |   const formErrors = useStore(form.store, (formState) => formState.errors)
132 | 
133 |   return (
134 |     <form action={handleForm.url} method="post" encType={'multipart/form-data'}>
135 |       {formErrors.map((error) => (
136 |         <p key={error as string}>{error}</p>
137 |       ))}
138 | 
139 |       <form.Field
140 |         name="age"
141 |         validators={{
142 |           onChange: ({ value }) =>
143 |             value < 8 ? 'Client validation: You must be at least 8' : undefined,
144 |         }}
145 |       >
146 |         {(field) => {
147 |           return (
148 |             <div>
149 |               <input
150 |                 name="age"
151 |                 type="number"
152 |                 value={field.state.value}
153 |                 onChange={(e) => field.handleChange(e.target.valueAsNumber)}
154 |               />
155 |               {field.state.meta.errors.map((error) => (
156 |                 <p key={error as string}>{error}</p>
157 |               ))}
158 |             </div>
159 |           )
160 |         }}
161 |       </form.Field>
162 |       <form.Subscribe
163 |         selector={(formState) => [formState.canSubmit, formState.isSubmitting]}
164 |       >
165 |         {([canSubmit, isSubmitting]) => (
166 |           <button type="submit" disabled={!canSubmit}>
167 |             {isSubmitting ? '...' : 'Submit'}
168 |           </button>
169 |         )}
170 |       </form.Subscribe>
171 |     </form>
172 |   )
173 | }
174 | ```
175 | 
176 | ## Using TanStack Form in a Next.js App Router
177 | 
178 | > Before reading this section, it's suggested you understand how React Server Components and React Server Actions work. [Check out this blog series for more information](https://playfulprogramming.com/collections/react-beyond-the-render)
179 | 
180 | This section focuses on integrating TanStack Form with `Next.js`, particularly using the `App Router` and `Server Actions`.
181 | 
182 | ### Next.js Prerequisites
183 | 
184 | - Start a new `Next.js` project, following the steps in the [Next.js Documentation](https://nextjs.org/docs/getting-started/installation). Ensure you select `yes` for `Would you like to use App Router?` during the setup to access all new features provided by Next.js.
185 | - Install `@tanstack/react-form`
186 | - Install any [form validator](/form/latest/docs/framework/react/guides/validation#validation-through-schema-libraries) of your choice. [Optional]
187 | 
188 | ## App Router integration
189 | 
190 | Let's start by creating a `formOption` that we'll use to share the form's shape across the client and server.
191 | 
192 | ```typescript
193 | // shared-code.ts
194 | // Notice the import path is different from the client
195 | import { formOptions } from '@tanstack/react-form/nextjs'
196 | 
197 | // You can pass other form options here
198 | export const formOpts = formOptions({
199 |   defaultValues: {
200 |     firstName: '',
201 |     age: 0,
202 |   },
203 | })
204 | ```
205 | 
206 | Next, we can create [a React Server Action](https://playfulprogramming.com/posts/what-are-react-server-components) that will handle the form submission on the server.
207 | 
208 | ```typescript
209 | // action.ts
210 | 'use server'
211 | 
212 | // Notice the import path is different from the client
213 | import {
214 |   ServerValidateError,
215 |   createServerValidate,
216 | } from '@tanstack/react-form/nextjs'
217 | import { formOpts } from './shared-code'
218 | 
219 | // Create the server action that will infer the types of the form from `formOpts`
220 | const serverValidate = createServerValidate({
221 |   ...formOpts,
222 |   onServerValidate: ({ value }) => {
223 |     if (value.age < 12) {
224 |       return 'Server validation: You must be at least 12 to sign up'
225 |     }
226 |   },
227 | })
228 | 
229 | export default async function someAction(prev: unknown, formData: FormData) {
230 |   try {
231 |     const validatedData = await serverValidate(formData)
232 |     console.log('validatedData', validatedData)
233 |     // Persist the form data to the database
234 |     // await sql`
235 |     //   INSERT INTO users (name, email, password)
236 |     //   VALUES (${validatedData.name}, ${validatedData.email}, ${validatedData.password})
237 |     // `
238 |   } catch (e) {
239 |     if (e instanceof ServerValidateError) {
240 |       return e.formState
241 |     }
242 | 
243 |     // Some other error occurred while validating your form
244 |     throw e
245 |   }
246 | 
247 |   // Your form has successfully validated!
248 | }
249 | ```
250 | 
251 | Finally, we'll use `someAction` in our client-side form component.
252 | 
253 | ```tsx
254 | // client-component.tsx
255 | 'use client'
256 | 
257 | import { useActionState } from 'react'
258 | import { initialFormState } from '@tanstack/react-form/nextjs'
259 | // Notice the import is from `react-form`, not `react-form/nextjs`
260 | import {
261 |   mergeForm,
262 |   useForm,
263 |   useStore,
264 |   useTransform,
265 | } from '@tanstack/react-form'
266 | import someAction from './action'
267 | import { formOpts } from './shared-code'
268 | 
269 | export const ClientComp = () => {
270 |   const [state, action] = useActionState(someAction, initialFormState)
271 | 
272 |   const form = useForm({
273 |     ...formOpts,
274 |     transform: useTransform((baseForm) => mergeForm(baseForm, state!), [state]),
275 |   })
276 | 
277 |   const formErrors = useStore(form.store, (formState) => formState.errors)
278 | 
279 |   return (
280 |     <form action={action as never} onSubmit={() => form.handleSubmit()}>
281 |       {formErrors.map((error) => (
282 |         <p key={error as string}>{error}</p>
283 |       ))}
284 | 
285 |       <form.Field
286 |         name="age"
287 |         validators={{
288 |           onChange: ({ value }) =>
289 |             value < 8 ? 'Client validation: You must be at least 8' : undefined,
290 |         }}
291 |       >
292 |         {(field) => {
293 |           return (
294 |             <div>
295 |               <input
296 |                 name="age"
297 |                 type="number"
298 |                 value={field.state.value}
299 |                 onChange={(e) => field.handleChange(e.target.valueAsNumber)}
300 |               />
301 |               {field.state.meta.errors.map((error) => (
302 |                 <p key={error as string}>{error}</p>
303 |               ))}
304 |             </div>
305 |           )
306 |         }}
307 |       </form.Field>
308 |       <form.Subscribe
309 |         selector={(formState) => [formState.canSubmit, formState.isSubmitting]}
310 |       >
311 |         {([canSubmit, isSubmitting]) => (
312 |           <button type="submit" disabled={!canSubmit}>
313 |             {isSubmitting ? '...' : 'Submit'}
314 |           </button>
315 |         )}
316 |       </form.Subscribe>
317 |     </form>
318 |   )
319 | }
320 | ```
321 | 
322 | Here, we're using [React's `useActionState` hook](https://playfulprogramming.com/posts/what-is-use-action-state-and-form-status) and TanStack Form's `useTransform` hook to merge state returned from the server action with the form state.
323 | 
324 | > If you get the following error in your Next.js application:
325 | >
326 | > ```typescript
327 | > x You're importing a component that needs `useState`. This React hook only works in a client component. To fix, mark the file (or its parent) with the `"use client"` directive.
328 | > ```
329 | >
330 | > This is because you're not importing server-side code from `@tanstack/react-form/nextjs`. Ensure you're importing the correct module based on the environment.
331 | >
332 | > [This is a limitation of Next.js](https://github.com/phryneas/rehackt). Other meta-frameworks will likely not have this same problem.
333 | 
334 | ## Using TanStack Form in Remix
335 | 
336 | > Before reading this section, it's suggested you understand how Remix actions work. [Check out Remix's docs for more information](https://remix.run/docs/en/main/discussion/data-flow#route-action)
337 | 
338 | ### Remix Prerequisites
339 | 
340 | - Start a new `Remix` project, following the steps in the [Remix Documentation](https://remix.run/docs/en/main/start/quickstart).
341 | - Install `@tanstack/react-form`
342 | - Install any [form validator](/form/latest/docs/framework/react/guides/validation#validation-through-schema-libraries) of your choice. [Optional]
343 | 
344 | ## Remix integration
345 | 
346 | Let's start by creating a `formOption` that we'll use to share the form's shape across the client and server.
347 | 
348 | ```typescript
349 | // routes/_index/route.tsx
350 | import { formOptions } from '@tanstack/react-form/remix'
351 | 
352 | // You can pass other form options here
353 | export const formOpts = formOptions({
354 |   defaultValues: {
355 |     firstName: '',
356 |     age: 0,
357 |   },
358 | })
359 | ```
360 | 
361 | Next, we can create [an action](https://remix.run/docs/en/main/discussion/data-flow#route-action) that will handle the form submission on the server.
362 | 
363 | ```tsx
364 | // routes/_index/route.tsx
365 | 
366 | import {
367 |   ServerValidateError,
368 |   createServerValidate,
369 |   formOptions,
370 | } from '@tanstack/react-form/remix'
371 | 
372 | import type { ActionFunctionArgs } from '@remix-run/node'
373 | 
374 | // export const formOpts = formOptions({
375 | 
376 | // Create the server action that will infer the types of the form from `formOpts`
377 | const serverValidate = createServerValidate({
378 |   ...formOpts,
379 |   onServerValidate: ({ value }) => {
380 |     if (value.age < 12) {
381 |       return 'Server validation: You must be at least 12 to sign up'
382 |     }
383 |   },
384 | })
385 | 
386 | export async function action({ request }: ActionFunctionArgs) {
387 |   const formData = await request.formData()
388 |   try {
389 |     const validatedData = await serverValidate(formData)
390 |     console.log('validatedData', validatedData)
391 |     // Persist the form data to the database
392 |     // await sql`
393 |     //   INSERT INTO users (name, email, password)
394 |     //   VALUES (${validatedData.name}, ${validatedData.email}, ${validatedData.password})
395 |     // `
396 |   } catch (e) {
397 |     if (e instanceof ServerValidateError) {
398 |       return e.formState
399 |     }
400 | 
401 |     // Some other error occurred while validating your form
402 |     throw e
403 |   }
404 | 
405 |   // Your form has successfully validated!
406 | }
407 | ```
408 | 
409 | Finally, the `action` will be called when the form submits.
410 | 
411 | ```tsx
412 | // routes/_index/route.tsx
413 | import { Form, useActionData } from '@remix-run/react'
414 | 
415 | import {
416 |   mergeForm,
417 |   useForm,
418 |   useStore,
419 |   useTransform,
420 | } from '@tanstack/react-form'
421 | import {
422 |   ServerValidateError,
423 |   createServerValidate,
424 |   formOptions,
425 |   initialFormState,
426 | } from '@tanstack/react-form/remix'
427 | 
428 | import type { ActionFunctionArgs } from '@remix-run/node'
429 | 
430 | // export const formOpts = formOptions({
431 | 
432 | // const serverValidate = createServerValidate({
433 | 
434 | // export async function action({request}: ActionFunctionArgs) {
435 | 
436 | export default function Index() {
437 |   const actionData = useActionData<typeof action>()
438 | 
439 |   const form = useForm({
440 |     ...formOpts,
441 |     transform: useTransform(
442 |       (baseForm) => mergeForm(baseForm, actionData ?? initialFormState),
443 |       [actionData],
444 |     ),
445 |   })
446 | 
447 |   const formErrors = useStore(form.store, (formState) => formState.errors)
448 | 
449 |   return (
450 |     <Form method="post" onSubmit={() => form.handleSubmit()}>
451 |       {formErrors.map((error) => (
452 |         <p key={error as string}>{error}</p>
453 |       ))}
454 | 
455 |       <form.Field
456 |         name="age"
457 |         validators={{
458 |           onChange: ({ value }) =>
459 |             value < 8 ? 'Client validation: You must be at least 8' : undefined,
460 |         }}
461 |       >
462 |         {(field) => {
463 |           return (
464 |             <div>
465 |               <input
466 |                 name="age"
467 |                 type="number"
468 |                 value={field.state.value}
469 |                 onChange={(e) => field.handleChange(e.target.valueAsNumber)}
470 |               />
471 |               {field.state.meta.errors.map((error) => (
472 |                 <p key={error as string}>{error}</p>
473 |               ))}
474 |             </div>
475 |           )
476 |         }}
477 |       </form.Field>
478 |       <form.Subscribe
479 |         selector={(formState) => [formState.canSubmit, formState.isSubmitting]}
480 |       >
481 |         {([canSubmit, isSubmitting]) => (
482 |           <button type="submit" disabled={!canSubmit}>
483 |             {isSubmitting ? '...' : 'Submit'}
484 |           </button>
485 |         )}
486 |       </form.Subscribe>
487 |     </Form>
488 |   )
489 | }
490 | ```
491 | 
492 | Here, we're using [Remix's `useActionData` hook](https://remix.run/docs/en/main/hooks/use-action-data) and TanStack Form's `useTransform` hook to merge state returned from the server action with the form state.
493 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/submission-handling.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: submission-handling
 3 | title: Submission handling
 4 | ---
 5 | 
 6 | ## Passing additional data to submission handling
 7 | 
 8 | You may have multiple types of submission behaviour, for example, going back to another page or staying on the form.
 9 | You can accomplish this by specifying the `onSubmitMeta` property. This meta data will be passed to the `onSubmit` function.
10 | 
11 | > Note: if `form.handleSubmit()` is called without metadata, it will use the provided default.
12 | 
13 | ```tsx
14 | import { useForm } from '@tanstack/react-form'
15 | 
16 | type FormMeta = {
17 |   submitAction: 'continue' | 'backToMenu' | null
18 | }
19 | 
20 | // Metadata is not required to call form.handleSubmit().
21 | // Specify what values to use as default if no meta is passed
22 | const defaultMeta: FormMeta = {
23 |   submitAction: null,
24 | }
25 | 
26 | function App() {
27 |   const form = useForm({
28 |     defaultValues: {
29 |       data: '',
30 |     },
31 |     // Define what meta values to expect on submission
32 |     onSubmitMeta: defaultMeta,
33 |     onSubmit: async ({ value, meta }) => {
34 |       // Do something with the values passed via handleSubmit
35 |       console.log(`Selected action - ${meta.submitAction}`, value)
36 |     },
37 |   })
38 | 
39 |   return (
40 |     <form
41 |       onSubmit={(e) => {
42 |         e.preventDefault()
43 |         e.stopPropagation()
44 |       }}
45 |     >
46 |       {/* ... */}
47 |       <button
48 |         type="submit"
49 |         // Overwrites the default specified in onSubmitMeta
50 |         onClick={() => form.handleSubmit({ submitAction: 'continue' })}
51 |       >
52 |         Submit and continue
53 |       </button>
54 |       <button
55 |         type="submit"
56 |         onClick={() => form.handleSubmit({ submitAction: 'backToMenu' })}
57 |       >
58 |         Submit and back to menu
59 |       </button>
60 |     </form>
61 |   )
62 | }
63 | ```
64 | 
65 | ## Transforming data with Standard Schemas
66 | 
67 | While Tanstack Form provides [Standard Schema support](../validation.md) for validation, it does not preserve the Schema's output data.
68 | 
69 | The value passed to the `onSubmit` function will always be the input data. To receive the output data of a Standard Schema, parse it in the `onSubmit` function:
70 | 
71 | ```tsx
72 | const schema = z.object({
73 |   age: z.string().transform((age) => Number(age)),
74 | })
75 | 
76 | // Tanstack Form uses the input type of Standard Schemas
77 | const defaultValues: z.input<typeof schema> = {
78 |   age: '13',
79 | }
80 | 
81 | const form = useForm({
82 |   defaultValues,
83 |   validators: {
84 |     onChange: schema,
85 |   },
86 |   onSubmit: ({ value }) => {
87 |     const inputAge: string = value.age
88 |     // Pass it through the schema to get the transformed value
89 |     const result = schema.parse(value)
90 |     const outputAge: number = result.age
91 |   },
92 | })
93 | ```
94 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/ui-libraries.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: ui-libraries
  3 | title: UI Libraries
  4 | ---
  5 | 
  6 | ## Usage of TanStack Form with UI Libraries
  7 | 
  8 | TanStack Form is a headless library, offering you complete flexibility to style it as you see fit. It's compatible with a wide range of UI libraries, including `Tailwind`, `Material UI`, `Mantine`, or even plain CSS.
  9 | 
 10 | This guide focuses on `Material UI` and `Mantine`, but the concepts are applicable to any UI library of your choice.
 11 | 
 12 | ### Prerequisites
 13 | 
 14 | Before integrating TanStack Form with a UI library, ensure the necessary dependencies are installed in your project:
 15 | 
 16 | - For `Material UI`, follow the installation instructions on their [official site](https://mui.com/material-ui/getting-started/).
 17 | - For `Mantine`, refer to their [documentation](https://mantine.dev/).
 18 | 
 19 | Note: While you can mix and match libraries, it's generally advisable to stick with one to maintain consistency and minimize bloat.
 20 | 
 21 | ### Example with Mantine
 22 | 
 23 | Here's an example demonstrating the integration of TanStack Form with Mantine components:
 24 | 
 25 | ```tsx
 26 | import { TextInput, Checkbox } from '@mantine/core'
 27 | import { useForm } from '@tanstack/react-form'
 28 | 
 29 | export default function App() {
 30 |   const { Field, handleSubmit, state } = useForm({
 31 |     defaultValues: {
 32 |       firstName: '',
 33 |       lastName: '',
 34 |       isChecked: false,
 35 |     },
 36 |     onSubmit: async ({ value }) => {
 37 |       // Handle form submission
 38 |       console.log(value)
 39 |     },
 40 |   })
 41 | 
 42 |   return (
 43 |     <>
 44 |       <form
 45 |         onSubmit={(e) => {
 46 |           e.preventDefault()
 47 |           handleSubmit()
 48 |         }}
 49 |       >
 50 |         <Field
 51 |           name="firstName"
 52 |           children={({ state, handleChange, handleBlur }) => (
 53 |             <TextInput
 54 |               defaultValue={state.value}
 55 |               onChange={(e) => handleChange(e.target.value)}
 56 |               onBlur={handleBlur}
 57 |               placeholder="Enter your name"
 58 |             />
 59 |           )}
 60 |         />
 61 |         <Field
 62 |           name="isChecked"
 63 |           children={({ state, handleChange, handleBlur }) => (
 64 |             <Checkbox
 65 |               onChange={(e) => handleChange(e.target.checked)}
 66 |               onBlur={handleBlur}
 67 |               checked={state.value}
 68 |             />
 69 |           )}
 70 |         />
 71 |       </form>
 72 |       <div>
 73 |         <pre>{JSON.stringify(state.values, null, 2)}</pre>
 74 |       </div>
 75 |     </>
 76 |   )
 77 | }
 78 | ```
 79 | 
 80 | - Initially, we utilize the `useForm` hook from TanStack and destructure the necessary properties. This step is optional; alternatively, you could use `const form = useForm()` if preferred. TypeScript's type inference ensures a smooth experience regardless of the approach.
 81 | - The `Field` component, derived from `useForm`, accepts several properties, such as `validators`. For this demonstration, we focus on two primary properties: `name` and `children`.
 82 |   - The `name` property identifies each `Field`, for instance, `firstName` in our example.
 83 |   - The `children` property leverages the concept of render props, allowing us to integrate components without unnecessary abstractions.
 84 | - TanStack's design relies heavily on render props, providing access to `children` within the `Field` component. This approach is entirely type-safe. When integrating with Mantine components, such as `TextInput`, we selectively destructure properties like `state.value`, `handleChange`, and `handleBlur`. This selective approach is due to the slight differences in types between `TextInput` and the `field` we get in the children.
 85 | - By following these steps, you can seamlessly integrate Mantine components with TanStack Form.
 86 | - This methodology is equally applicable to other components, such as `Checkbox`, ensuring consistent integration across different UI elements.
 87 | 
 88 | ### Usage with Material UI
 89 | 
 90 | The process for integrating Material UI components is similar. Here's an example using TextField and Checkbox from Material UI:
 91 | 
 92 | ```tsx
 93 |         <Field
 94 |             name="lastName"
 95 |             children={({ state, handleChange, handleBlur }) => {
 96 |               return (
 97 |                 <TextField
 98 |                   id="filled-basic"
 99 |                   label="Filled"
100 |                   variant="filled"
101 |                   defaultValue={state.value}
102 |                   onChange={(e) => handleChange(e.target.value)}
103 |                   onBlur={handleBlur}
104 |                   placeholder="Enter your last name"
105 |                 />
106 |               );
107 |             }}
108 |           />
109 | 
110 |            <Field
111 |             name="isMuiCheckBox"
112 |             children={({ state, handleChange, handleBlur }) => {
113 |               return (
114 |                 <MuiCheckbox
115 |                   onChange={(e) => handleChange(e.target.checked)}
116 |                   onBlur={handleBlur}
117 |                   checked={state.value}
118 |                 />
119 |               );
120 |             }}
121 |           />
122 | 
123 | ```
124 | 
125 | - The integration approach is the same as with Mantine.
126 | - The primary difference lies in the specific Material UI component properties and styling options.
127 | 


--------------------------------------------------------------------------------
/docs/framework/react/guides/validation.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: form-validation
  3 | title: Form and Field Validation
  4 | ---
  5 | 
  6 | At the core of TanStack Form's functionalities is the concept of validation. TanStack Form makes validation highly customizable:
  7 | 
  8 | - You can control when to perform the validation (on change, on input, on blur, on submit...)
  9 | - Validation rules can be defined at the field level or at the form level
 10 | - Validation can be synchronous or asynchronous (for example, as a result of an API call)
 11 | 
 12 | ## When is validation performed?
 13 | 
 14 | It's up to you! The `<Field />` component accepts some callbacks as props such as `onChange` or `onBlur`. Those callbacks are passed the current value of the field, as well as the fieldAPI object, so that you can perform the validation. If you find a validation error, simply return the error message as string and it will be available in `field.state.meta.errors`.
 15 | 
 16 | Here is an example:
 17 | 
 18 | ```tsx
 19 | <form.Field
 20 |   name="age"
 21 |   validators={{
 22 |     onChange: ({ value }) =>
 23 |       value < 13 ? 'You must be 13 to make an account' : undefined,
 24 |   }}
 25 | >
 26 |   {(field) => (
 27 |     <>
 28 |       <label htmlFor={field.name}>Age:</label>
 29 |       <input
 30 |         id={field.name}
 31 |         name={field.name}
 32 |         value={field.state.value}
 33 |         type="number"
 34 |         onChange={(e) => field.handleChange(e.target.valueAsNumber)}
 35 |       />
 36 |       {!field.state.meta.isValid && (
 37 |         <em role="alert">{field.state.meta.errors.join(', ')}</em>
 38 |       )}
 39 |     </>
 40 |   )}
 41 | </form.Field>
 42 | ```
 43 | 
 44 | In the example above, the validation is done at each keystroke (`onChange`). If, instead, we wanted the validation to be done when the field is blurred, we would change the code above like so:
 45 | 
 46 | ```tsx
 47 | <form.Field
 48 |   name="age"
 49 |   validators={{
 50 |     onBlur: ({ value }) =>
 51 |       value < 13 ? 'You must be 13 to make an account' : undefined,
 52 |   }}
 53 | >
 54 |   {(field) => (
 55 |     <>
 56 |       <label htmlFor={field.name}>Age:</label>
 57 |       <input
 58 |         id={field.name}
 59 |         name={field.name}
 60 |         value={field.state.value}
 61 |         type="number"
 62 |         // Listen to the onBlur event on the field
 63 |         onBlur={field.handleBlur}
 64 |         // We always need to implement onChange, so that TanStack Form receives the changes
 65 |         onChange={(e) => field.handleChange(e.target.valueAsNumber)}
 66 |       />
 67 |       {!field.state.meta.isValid && (
 68 |         <em role="alert">{field.state.meta.errors.join(', ')}</em>
 69 |       )}
 70 |     </>
 71 |   )}
 72 | </form.Field>
 73 | ```
 74 | 
 75 | So you can control when the validation is done by implementing the desired callback. You can even perform different pieces of validation at different times:
 76 | 
 77 | ```tsx
 78 | <form.Field
 79 |   name="age"
 80 |   validators={{
 81 |     onChange: ({ value }) =>
 82 |       value < 13 ? 'You must be 13 to make an account' : undefined,
 83 |     onBlur: ({ value }) => (value < 0 ? 'Invalid value' : undefined),
 84 |   }}
 85 | >
 86 |   {(field) => (
 87 |     <>
 88 |       <label htmlFor={field.name}>Age:</label>
 89 |       <input
 90 |         id={field.name}
 91 |         name={field.name}
 92 |         value={field.state.value}
 93 |         type="number"
 94 |         // Listen to the onBlur event on the field
 95 |         onBlur={field.handleBlur}
 96 |         // We always need to implement onChange, so that TanStack Form receives the changes
 97 |         onChange={(e) => field.handleChange(e.target.valueAsNumber)}
 98 |       />
 99 |       {!field.state.meta.isValid && (
100 |         <em role="alert">{field.state.meta.errors.join(', ')}</em>
101 |       )}
102 |     </>
103 |   )}
104 | </form.Field>
105 | ```
106 | 
107 | In the example above, we are validating different things on the same field at different times (at each keystroke and when blurring the field). Since `field.state.meta.errors` is an array, all the relevant errors at a given time are displayed. You can also use `field.state.meta.errorMap` to get errors based on _when_ the validation was done (onChange, onBlur etc...). More info about displaying errors below.
108 | 
109 | ## Displaying Errors
110 | 
111 | Once you have your validation in place, you can map the errors from an array to be displayed in your UI:
112 | 
113 | ```tsx
114 | <form.Field
115 |   name="age"
116 |   validators={{
117 |     onChange: ({ value }) =>
118 |       value < 13 ? 'You must be 13 to make an account' : undefined,
119 |   }}
120 | >
121 |   {(field) => {
122 |     return (
123 |       <>
124 |         {/* ... */}
125 |         {!field.state.meta.isValid && (
126 |           <em>{field.state.meta.errors.join(',')}</em>
127 |         )}
128 |       </>
129 |     )
130 |   }}
131 | </form.Field>
132 | ```
133 | 
134 | Or use the `errorMap` property to access the specific error you're looking for:
135 | 
136 | ```tsx
137 | <form.Field
138 |   name="age"
139 |   validators={{
140 |     onChange: ({ value }) =>
141 |       value < 13 ? 'You must be 13 to make an account' : undefined,
142 |   }}
143 | >
144 |   {(field) => (
145 |     <>
146 |       {/* ... */}
147 |       {field.state.meta.errorMap['onChange'] ? (
148 |         <em>{field.state.meta.errorMap['onChange']}</em>
149 |       ) : null}
150 |     </>
151 |   )}
152 | </form.Field>
153 | ```
154 | 
155 | It's worth mentioning that our `errors` array and the `errorMap` matches the types returned by the validators. This means that:
156 | 
157 | ```tsx
158 | <form.Field
159 |   name="age"
160 |   validators={{
161 |     onChange: ({ value }) => (value < 13 ? { isOldEnough: false } : undefined),
162 |   }}
163 | >
164 |   {(field) => (
165 |     <>
166 |       {/* ... */}
167 |       {/* errorMap.onChange is type `{isOldEnough: false} | undefined` */}
168 |       {/* meta.errors is type `Array<{isOldEnough: false} | undefined>` */}
169 |       {!field.state.meta.errorMap['onChange']?.isOldEnough ? (
170 |         <em>The user is not old enough</em>
171 |       ) : null}
172 |     </>
173 |   )}
174 | </form.Field>
175 | ```
176 | 
177 | ## Validation at field level vs at form level
178 | 
179 | As shown above, each `<Field>` accepts its own validation rules via the `onChange`, `onBlur` etc... callbacks. It is also possible to define validation rules at the form level (as opposed to field by field) by passing similar callbacks to the `useForm()` hook.
180 | 
181 | Example:
182 | 
183 | ```tsx
184 | export default function App() {
185 |   const form = useForm({
186 |     defaultValues: {
187 |       age: 0,
188 |     },
189 |     onSubmit: async ({ value }) => {
190 |       console.log(value)
191 |     },
192 |     validators: {
193 |       // Add validators to the form the same way you would add them to a field
194 |       onChange({ value }) {
195 |         if (value.age < 13) {
196 |           return 'Must be 13 or older to sign'
197 |         }
198 |         return undefined
199 |       },
200 |     },
201 |   })
202 | 
203 |   // Subscribe to the form's error map so that updates to it will render
204 |   // alternately, you can use `form.Subscribe`
205 |   const formErrorMap = useStore(form.store, (state) => state.errorMap)
206 | 
207 |   return (
208 |     <div>
209 |       {/* ... */}
210 |       {formErrorMap.onChange ? (
211 |         <div>
212 |           <em>There was an error on the form: {formErrorMap.onChange}</em>
213 |         </div>
214 |       ) : null}
215 |       {/* ... */}
216 |     </div>
217 |   )
218 | }
219 | ```
220 | 
221 | ### Setting field-level errors from the form's validators
222 | 
223 | You can set errors on the fields from the form's validators. One common use case for this is validating all the fields on submit by calling a single API endpoint in the form's `onSubmitAsync` validator.
224 | 
225 | ```tsx
226 | export default function App() {
227 |   const form = useForm({
228 |     defaultValues: {
229 |       age: 0,
230 |       socials: [],
231 |       details: {
232 |         email: '',
233 |       },
234 |     },
235 |     validators: {
236 |       onSubmitAsync: async ({ value }) => {
237 |         // Validate the value on the server
238 |         const hasErrors = await verifyDataOnServer(value)
239 |         if (hasErrors) {
240 |           return {
241 |             form: 'Invalid data', // The `form` key is optional
242 |             fields: {
243 |               age: 'Must be 13 or older to sign',
244 |               // Set errors on nested fields with the field's name
245 |               'socials[0].url': 'The provided URL does not exist',
246 |               'details.email': 'An email is required',
247 |             },
248 |           }
249 |         }
250 | 
251 |         return null
252 |       },
253 |     },
254 |   })
255 | 
256 |   return (
257 |     <div>
258 |       <form
259 |         onSubmit={(e) => {
260 |           e.preventDefault()
261 |           e.stopPropagation()
262 |           void form.handleSubmit()
263 |         }}
264 |       >
265 |         <form.Field name="age">
266 |           {(field) => (
267 |             <>
268 |               <label htmlFor={field.name}>Age:</label>
269 |               <input
270 |                 id={field.name}
271 |                 name={field.name}
272 |                 value={field.state.value}
273 |                 type="number"
274 |                 onChange={(e) => field.handleChange(e.target.valueAsNumber)}
275 |               />
276 |               {!field.state.meta.isValid && (
277 |                 <em role="alert">{field.state.meta.errors.join(', ')}</em>
278 |               )}
279 |             </>
280 |           )}
281 |         </form.Field>
282 |         <form.Subscribe
283 |           selector={(state) => [state.errorMap]}
284 |           children={([errorMap]) =>
285 |             errorMap.onSubmit ? (
286 |               <div>
287 |                 <em>There was an error on the form: {errorMap.onSubmit}</em>
288 |               </div>
289 |             ) : null
290 |           }
291 |         />
292 |         {/*...*/}
293 |       </form>
294 |     </div>
295 |   )
296 | }
297 | ```
298 | 
299 | > Something worth mentioning is that if you have a form validation function that returns an error, that error may be overwritten by the field-specific validation.
300 | >
301 | > This means that:
302 | >
303 | > ```jsx
304 | > const form = useForm({
305 | >   defaultValues: {
306 | >     age: 0,
307 | >   },
308 | >   validators: {
309 | >     onChange: ({ value }) => {
310 | >       return {
311 | >         fields: {
312 | >           age: value.age < 12 ? 'Too young!' : undefined,
313 | >         },
314 | >       }
315 | >     },
316 | >   },
317 | > })
318 | >
319 | > // ...
320 | >
321 | > return (
322 | >   <form.Field
323 | >     name="age"
324 | >     validators={{
325 | >       onChange: ({ value }) => (value % 2 === 0 ? 'Must be odd!' : undefined),
326 | >     }}
327 | >     children={() => <>{/* ... */}</>}
328 | >   />
329 | > )
330 | > ```
331 | >
332 | > Will only show `'Must be odd!` even if the 'Too young!' error is returned by the form-level validation.
333 | 
334 | ## Asynchronous Functional Validation
335 | 
336 | While we suspect most validations will be synchronous, there are many instances where a network call or some other async operation would be useful to validate against.
337 | 
338 | To do this, we have dedicated `onChangeAsync`, `onBlurAsync`, and other methods that can be used to validate against:
339 | 
340 | ```tsx
341 | <form.Field
342 |   name="age"
343 |   validators={{
344 |     onChangeAsync: async ({ value }) => {
345 |       await new Promise((resolve) => setTimeout(resolve, 1000))
346 |       return value < 13 ? 'You must be 13 to make an account' : undefined
347 |     },
348 |   }}
349 | >
350 |   {(field) => (
351 |     <>
352 |       <label htmlFor={field.name}>Age:</label>
353 |       <input
354 |         id={field.name}
355 |         name={field.name}
356 |         value={field.state.value}
357 |         type="number"
358 |         onChange={(e) => field.handleChange(e.target.valueAsNumber)}
359 |       />
360 |       {!field.state.meta.isValid && (
361 |         <em role="alert">{field.state.meta.errors.join(', ')}</em>
362 |       )}
363 |     </>
364 |   )}
365 | </form.Field>
366 | ```
367 | 
368 | Synchronous and Asynchronous validations can coexist. For example, it is possible to define both `onBlur` and `onBlurAsync` on the same field:
369 | 
370 | ```tsx
371 | <form.Field
372 |   name="age"
373 |   validators={{
374 |     onBlur: ({ value }) => (value < 13 ? 'You must be at least 13' : undefined),
375 |     onBlurAsync: async ({ value }) => {
376 |       const currentAge = await fetchCurrentAgeOnProfile()
377 |       return value < currentAge ? 'You can only increase the age' : undefined
378 |     },
379 |   }}
380 | >
381 |   {(field) => (
382 |     <>
383 |       <label htmlFor={field.name}>Age:</label>
384 |       <input
385 |         id={field.name}
386 |         name={field.name}
387 |         value={field.state.value}
388 |         type="number"
389 |         onBlur={field.handleBlur}
390 |         onChange={(e) => field.handleChange(e.target.valueAsNumber)}
391 |       />
392 |       {!field.state.meta.isValid && (
393 |         <em role="alert">{field.state.meta.errors.join(', ')}</em>
394 |       )}
395 |     </>
396 |   )}
397 | </form.Field>
398 | ```
399 | 
400 | The synchronous validation method (`onBlur`) is run first and the asynchronous method (`onBlurAsync`) is only run if the synchronous one (`onBlur`) succeeds. To change this behaviour, set the `asyncAlways` option to `true`, and the async method will be run regardless of the result of the sync method.
401 | 
402 | ### Built-in Debouncing
403 | 
404 | While async calls are the way to go when validating against the database, running a network request on every keystroke is a good way to DDOS your database.
405 | 
406 | Instead, we enable an easy method for debouncing your `async` calls by adding a single property:
407 | 
408 | ```tsx
409 | <form.Field
410 |   name="age"
411 |   asyncDebounceMs={500}
412 |   validators={{
413 |     onChangeAsync: async ({ value }) => {
414 |       // ...
415 |     },
416 |   }}
417 |   children={(field) => {
418 |     return <>{/* ... */}</>
419 |   }}
420 | />
421 | ```
422 | 
423 | This will debounce every async call with a 500ms delay. You can even override this property on a per-validation property:
424 | 
425 | ```tsx
426 | <form.Field
427 |   name="age"
428 |   asyncDebounceMs={500}
429 |   validators={{
430 |     onChangeAsyncDebounceMs: 1500,
431 |     onChangeAsync: async ({ value }) => {
432 |       // ...
433 |     },
434 |     onBlurAsync: async ({ value }) => {
435 |       // ...
436 |     },
437 |   }}
438 |   children={(field) => {
439 |     return <>{/* ... */}</>
440 |   }}
441 | />
442 | ```
443 | 
444 | This will run `onChangeAsync` every 1500ms while `onBlurAsync` will run every 500ms.
445 | 
446 | ## Validation through Schema Libraries
447 | 
448 | While functions provide more flexibility and customization over your validation, they can be a bit verbose. To help solve this, there are libraries that provide schema-based validation to make shorthand and type-strict validation substantially easier. You can also define a single schema for your entire form and pass it to the form level, errors will be automatically propagated to the fields.
449 | 
450 | ### Standard Schema Libraries
451 | 
452 | TanStack Form natively supports all libraries following the [Standard Schema specification](https://github.com/standard-schema/standard-schema), most notably:
453 | 
454 | - [Zod](https://zod.dev/)
455 | - [Valibot](https://valibot.dev/)
456 | - [ArkType](https://arktype.io/)
457 | - [Effect/Schema](https://effect.website/docs/schema/standard-schema/)
458 | 
459 | _Note:_ make sure to use the latest version of the schema libraries as older versions might not support Standard Schema yet.
460 | 
461 | > Validation will not provide you with transformed values. See [submission handling](../submission-handling.md) for more information.
462 | 
463 | To use schemas from these libraries you can pass them to the `validators` props as you would do with a custom function:
464 | 
465 | ```tsx
466 | const userSchema = z.object({
467 |   age: z.number().gte(13, 'You must be 13 to make an account'),
468 | })
469 | 
470 | function App() {
471 |   const form = useForm({
472 |     defaultValues: {
473 |       age: 0,
474 |     },
475 |     validators: {
476 |       onChange: userSchema,
477 |     },
478 |   })
479 |   return (
480 |     <div>
481 |       <form.Field
482 |         name="age"
483 |         children={(field) => {
484 |           return <>{/* ... */}</>
485 |         }}
486 |       />
487 |     </div>
488 |   )
489 | }
490 | ```
491 | 
492 | Async validations on form and field level are supported as well:
493 | 
494 | ```tsx
495 | <form.Field
496 |   name="age"
497 |   validators={{
498 |     onChange: z.number().gte(13, 'You must be 13 to make an account'),
499 |     onChangeAsyncDebounceMs: 500,
500 |     onChangeAsync: z.number().refine(
501 |       async (value) => {
502 |         const currentAge = await fetchCurrentAgeOnProfile()
503 |         return value >= currentAge
504 |       },
505 |       {
506 |         message: 'You can only increase the age',
507 |       },
508 |     ),
509 |   }}
510 |   children={(field) => {
511 |     return <>{/* ... */}</>
512 |   }}
513 | />
514 | ```
515 | 
516 | If you need even more control over your Standard Schema validation, you can combine a Standard Schema with a callback function like so:
517 | 
518 | ```tsx
519 | <form.Field
520 |   name="age"
521 |   asyncDebounceMs={500}
522 |   validators={{
523 |     onChangeAsync: async ({ value, fieldApi }) => {
524 |       const errors = fieldApi.parseValueWithSchema(
525 |         z.number().gte(13, 'You must be 13 to make an account'),
526 |       )
527 |       if (errors) return errors
528 |       // continue with your validation
529 |     },
530 |   }}
531 |   children={(field) => {
532 |     return <>{/* ... */}</>
533 |   }}
534 | />
535 | ```
536 | 
537 | ## Preventing invalid forms from being submitted
538 | 
539 | The `onChange`, `onBlur` etc... callbacks are also run when the form is submitted and the submission is blocked if the form is invalid.
540 | 
541 | The form state object has a `canSubmit` flag that is false when any field is invalid and the form has been touched (`canSubmit` is true until the form has been touched, even if some fields are "technically" invalid based on their `onChange`/`onBlur` props).
542 | 
543 | You can subscribe to it via `form.Subscribe` and use the value in order to, for example, disable the submit button when the form is invalid (in practice, disabled buttons are not accessible, use `aria-disabled` instead).
544 | 
545 | ```tsx
546 | const form = useForm(/* ... */)
547 | 
548 | return (
549 |   /* ... */
550 | 
551 |   // Dynamic submit button
552 |   <form.Subscribe
553 |     selector={(state) => [state.canSubmit, state.isSubmitting]}
554 |     children={([canSubmit, isSubmitting]) => (
555 |       <button type="submit" disabled={!canSubmit}>
556 |         {isSubmitting ? '...' : 'Submit'}
557 |       </button>
558 |     )}
559 |   />
560 | )
561 | ```
562 | 


--------------------------------------------------------------------------------
/docs/framework/react/quick-start.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: quick-start
  3 | title: Quick Start
  4 | ---
  5 | 
  6 | TanStack Form is unlike most form libraries you've used before. It's designed for large-scale production usage, with a focus on type safety, performance and composition for an unmatched developer experience.
  7 | 
  8 | As a result, we've developed [a philosophy around the library's usage](/form/latest/docs/philosophy) that values scalability and long-term developer experience over short and sharable code snippets.
  9 | 
 10 | Here's an example of a form following many of our best practices, which will allow you to rapidly develop even high-complexity forms after a short onboarding experience:
 11 | 
 12 | ```tsx
 13 | import React from 'react'
 14 | import ReactDOM from 'react-dom/client'
 15 | import { createFormHook, createFormHookContexts } from '@tanstack/react-form'
 16 | // Form components that pre-bind events from the form hook; check our "Form Composition" guide for more
 17 | import { TextField, NumberField, SubmitButton } from '~our-app/ui-library'
 18 | // We also support Valibot, ArkType, and any other standard schema library
 19 | import { z } from 'zod'
 20 | 
 21 | const { fieldContext, formContext } = createFormHookContexts()
 22 | 
 23 | // Allow us to bind components to the form to keep type safety but reduce production boilerplate
 24 | // Define this once to have a generator of consistent form instances throughout your app
 25 | const { useAppForm } = createFormHook({
 26 |   fieldComponents: {
 27 |     TextField,
 28 |     NumberField,
 29 |   },
 30 |   formComponents: {
 31 |     SubmitButton,
 32 |   },
 33 |   fieldContext,
 34 |   formContext,
 35 | })
 36 | 
 37 | const PeoplePage = () => {
 38 |   const form = useAppForm({
 39 |     defaultValues: {
 40 |       username: '',
 41 |       age: 0,
 42 |     },
 43 |     validators: {
 44 |       // Pass a schema or function to validate
 45 |       onChange: z.object({
 46 |         username: z.string(),
 47 |         age: z.number().min(13),
 48 |       }),
 49 |     },
 50 |     onSubmit: ({ value }) => {
 51 |       // Do something with form data
 52 |       alert(JSON.stringify(value, null, 2))
 53 |     },
 54 |   })
 55 | 
 56 |   return (
 57 |     <form
 58 |       onSubmit={(e) => {
 59 |         e.preventDefault()
 60 |         form.handleSubmit()
 61 |       }}
 62 |     >
 63 |       <h1>Personal Information</h1>
 64 |       {/* Components are bound to `form` and `field` to ensure extreme type safety */}
 65 |       {/* Use `form.AppField` to render a component bound to a single field */}
 66 |       <form.AppField
 67 |         name="username"
 68 |         children={(field) => <field.TextField label="Full Name" />}
 69 |       />
 70 |       {/* The "name" property will throw a TypeScript error if typo'd  */}
 71 |       <form.AppField
 72 |         name="age"
 73 |         children={(field) => <field.NumberField label="Age" />}
 74 |       />
 75 |       {/* Components in `form.AppForm` have access to the form context */}
 76 |       <form.AppForm>
 77 |         <form.SubmitButton />
 78 |       </form.AppForm>
 79 |     </form>
 80 |   )
 81 | }
 82 | 
 83 | const rootElement = document.getElementById('root')!
 84 | ReactDOM.createRoot(rootElement).render(<PeoplePage />)
 85 | ```
 86 | 
 87 | While we generally suggest using `createFormHook` for reduced boilerplate in the long-run, we also support one-off components and other behaviors using `useForm` and `form.Field`:
 88 | 
 89 | ```tsx
 90 | import React from 'react'
 91 | import ReactDOM from 'react-dom/client'
 92 | import { useForm } from '@tanstack/react-form'
 93 | 
 94 | const PeoplePage = () => {
 95 |   const form = useForm({
 96 |     defaultValues: {
 97 |       username: '',
 98 |       age: 0,
 99 |     },
100 |     onSubmit: ({ value }) => {
101 |       // Do something with form data
102 |       alert(JSON.stringify(value, null, 2))
103 |     },
104 |   })
105 | 
106 |   return (
107 |     <form.Field
108 |       name="age"
109 |       validators={{
110 |         // We can choose between form-wide and field-specific validators
111 |         onChange: ({ value }) =>
112 |           value > 13 ? undefined : 'Must be 13 or older',
113 |       }}
114 |       children={(field) => (
115 |         <>
116 |           <input
117 |             name={field.name}
118 |             value={field.state.value}
119 |             onBlur={field.handleBlur}
120 |             type="number"
121 |             onChange={(e) => field.handleChange(e.target.valueAsNumber)}
122 |           />
123 |           {!field.state.meta.isValid && (
124 |             <em>{field.state.meta.errors.join(',')}</em>
125 |           )}
126 |         </>
127 |       )}
128 |     />
129 |   )
130 | }
131 | 
132 | const rootElement = document.getElementById('root')!
133 | ReactDOM.createRoot(rootElement).render(<PeoplePage />)
134 | ```
135 | 
136 | All properties from `useForm` can be used in `useAppForm` and all properties from `form.Field` can be used in `form.AppField`.
137 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/functions/createformhook.md:
--------------------------------------------------------------------------------
  1 | ---
  2 | id: createFormHook
  3 | title: createFormHook
  4 | ---
  5 | 
  6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
  7 | 
  8 | # Function: createFormHook()
  9 | 
 10 | ```ts
 11 | function createFormHook<TComponents, TFormComponents>(__namedParameters): object
 12 | ```
 13 | 
 14 | Defined in: [packages/react-form/src/createFormHook.tsx:223](https://github.com/TanStack/form/blob/main/packages/react-form/src/createFormHook.tsx#L223)
 15 | 
 16 | ## Type Parameters
 17 | 
 18 | • **TComponents** *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>
 19 | 
 20 | • **TFormComponents** *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>
 21 | 
 22 | ## Parameters
 23 | 
 24 | ### \_\_namedParameters
 25 | 
 26 | `CreateFormHookProps`\<`TComponents`, `TFormComponents`\>
 27 | 
 28 | ## Returns
 29 | 
 30 | `object`
 31 | 
 32 | ### useAppForm()
 33 | 
 34 | ```ts
 35 | useAppForm: <TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta>(props) => AppFieldExtendedReactFormApi<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta, TComponents, TFormComponents>;
 36 | ```
 37 | 
 38 | #### Type Parameters
 39 | 
 40 | • **TFormData**
 41 | 
 42 | • **TOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
 43 | 
 44 | • **TOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
 45 | 
 46 | • **TOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
 47 | 
 48 | • **TOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
 49 | 
 50 | • **TOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
 51 | 
 52 | • **TOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
 53 | 
 54 | • **TOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
 55 | 
 56 | • **TOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
 57 | 
 58 | • **TSubmitMeta**
 59 | 
 60 | #### Parameters
 61 | 
 62 | ##### props
 63 | 
 64 | `FormOptions`\<`TFormData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TOnServer`, `TSubmitMeta`\>
 65 | 
 66 | #### Returns
 67 | 
 68 | `AppFieldExtendedReactFormApi`\<`TFormData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TOnServer`, `TSubmitMeta`, `TComponents`, `TFormComponents`\>
 69 | 
 70 | ### withForm()
 71 | 
 72 | ```ts
 73 | withForm: <TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta, TRenderProps>(__namedParameters) => (props) => Element;
 74 | ```
 75 | 
 76 | #### Type Parameters
 77 | 
 78 | • **TFormData**
 79 | 
 80 | • **TOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
 81 | 
 82 | • **TOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
 83 | 
 84 | • **TOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
 85 | 
 86 | • **TOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
 87 | 
 88 | • **TOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
 89 | 
 90 | • **TOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
 91 | 
 92 | • **TOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
 93 | 
 94 | • **TOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
 95 | 
 96 | • **TSubmitMeta**
 97 | 
 98 | • **TRenderProps** *extends* `Record`\<`string`, `unknown`\> = \{\}
 99 | 
100 | #### Parameters
101 | 
102 | ##### \_\_namedParameters
103 | 
104 | [`WithFormProps`](../../interfaces/withformprops.md)\<`TFormData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TOnServer`, `TSubmitMeta`, `TComponents`, `TFormComponents`, `TRenderProps`\>
105 | 
106 | #### Returns
107 | 
108 | `Function`
109 | 
110 | ##### Parameters
111 | 
112 | ###### props
113 | 
114 | `PropsWithChildren`\<`NoInfer`\<`UnwrapOrAny`\<`TRenderProps`\>\> & `object`\>
115 | 
116 | ##### Returns
117 | 
118 | `Element`
119 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/functions/createformhookcontexts.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: createFormHookContexts
 3 | title: createFormHookContexts
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Function: createFormHookContexts()
 9 | 
10 | ```ts
11 | function createFormHookContexts(): object
12 | ```
13 | 
14 | Defined in: [packages/react-form/src/createFormHook.tsx:53](https://github.com/TanStack/form/blob/main/packages/react-form/src/createFormHook.tsx#L53)
15 | 
16 | ## Returns
17 | 
18 | `object`
19 | 
20 | ### fieldContext
21 | 
22 | ```ts
23 | fieldContext: Context<AnyFieldApi>;
24 | ```
25 | 
26 | ### formContext
27 | 
28 | ```ts
29 | formContext: Context<AnyFormApi>;
30 | ```
31 | 
32 | ### useFieldContext()
33 | 
34 | ```ts
35 | useFieldContext: <TData>() => FieldApi<any, string, TData, any, any, any, any, any, any, any, any, any, any, any, any, any, any, any, any>;
36 | ```
37 | 
38 | #### Type Parameters
39 | 
40 | • **TData**
41 | 
42 | #### Returns
43 | 
44 | `FieldApi`\<`any`, `string`, `TData`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`\>
45 | 
46 | ### useFormContext()
47 | 
48 | ```ts
49 | useFormContext: () => ReactFormExtendedApi<Record<string, never>, any, any, any, any, any, any, any, any, any>;
50 | ```
51 | 
52 | #### Returns
53 | 
54 | [`ReactFormExtendedApi`](../../type-aliases/reactformextendedapi.md)\<`Record`\<`string`, `never`\>, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`\>
55 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/functions/field.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: Field
 3 | title: Field
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Function: Field()
 9 | 
10 | ```ts
11 | function Field<TParentData, TName, TData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta>(__namedParameters): ReactNode
12 | ```
13 | 
14 | Defined in: [packages/react-form/src/useField.tsx:428](https://github.com/TanStack/form/blob/main/packages/react-form/src/useField.tsx#L428)
15 | 
16 | A function component that takes field options and a render function as children and returns a React component.
17 | 
18 | The `Field` component uses the `useField` hook internally to manage the field instance.
19 | 
20 | ## Type Parameters
21 | 
22 | • **TParentData**
23 | 
24 | • **TName** *extends* `string`
25 | 
26 | • **TData**
27 | 
28 | • **TOnMount** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
29 | 
30 | • **TOnChange** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
31 | 
32 | • **TOnChangeAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
33 | 
34 | • **TOnBlur** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
35 | 
36 | • **TOnBlurAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
37 | 
38 | • **TOnSubmit** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
39 | 
40 | • **TOnSubmitAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
41 | 
42 | • **TFormOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
43 | 
44 | • **TFormOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
45 | 
46 | • **TFormOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
47 | 
48 | • **TFormOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
49 | 
50 | • **TFormOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
51 | 
52 | • **TFormOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
53 | 
54 | • **TFormOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
55 | 
56 | • **TFormOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
57 | 
58 | • **TPatentSubmitMeta**
59 | 
60 | ## Parameters
61 | 
62 | ### \_\_namedParameters
63 | 
64 | `FieldComponentProps`\<`TParentData`, `TName`, `TData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TFormOnMount`, `TFormOnChange`, `TFormOnChangeAsync`, `TFormOnBlur`, `TFormOnBlurAsync`, `TFormOnSubmit`, `TFormOnSubmitAsync`, `TFormOnServer`, `TPatentSubmitMeta`\>
65 | 
66 | ## Returns
67 | 
68 | `ReactNode`
69 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/functions/usefield.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: useField
 3 | title: useField
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Function: useField()
 9 | 
10 | ```ts
11 | function useField<TParentData, TName, TData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta>(opts): FieldApi<TParentData, TName, TData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta> & ReactFieldApi<TParentData, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta>
12 | ```
13 | 
14 | Defined in: [packages/react-form/src/useField.tsx:118](https://github.com/TanStack/form/blob/main/packages/react-form/src/useField.tsx#L118)
15 | 
16 | A hook for managing a field in a form.
17 | 
18 | ## Type Parameters
19 | 
20 | • **TParentData**
21 | 
22 | • **TName** *extends* `string`
23 | 
24 | • **TData**
25 | 
26 | • **TOnMount** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
27 | 
28 | • **TOnChange** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
29 | 
30 | • **TOnChangeAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
31 | 
32 | • **TOnBlur** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
33 | 
34 | • **TOnBlurAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
35 | 
36 | • **TOnSubmit** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
37 | 
38 | • **TOnSubmitAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
39 | 
40 | • **TFormOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
41 | 
42 | • **TFormOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
43 | 
44 | • **TFormOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
45 | 
46 | • **TFormOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
47 | 
48 | • **TFormOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
49 | 
50 | • **TFormOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
51 | 
52 | • **TFormOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
53 | 
54 | • **TFormOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
55 | 
56 | • **TPatentSubmitMeta**
57 | 
58 | ## Parameters
59 | 
60 | ### opts
61 | 
62 | `UseFieldOptions`\<`TParentData`, `TName`, `TData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TFormOnMount`, `TFormOnChange`, `TFormOnChangeAsync`, `TFormOnBlur`, `TFormOnBlurAsync`, `TFormOnSubmit`, `TFormOnSubmitAsync`, `TFormOnServer`, `TPatentSubmitMeta`\>
63 | 
64 | An object with field options.
65 | 
66 | ## Returns
67 | 
68 | `FieldApi`\<`TParentData`, `TName`, `TData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TFormOnMount`, `TFormOnChange`, `TFormOnChangeAsync`, `TFormOnBlur`, `TFormOnBlurAsync`, `TFormOnSubmit`, `TFormOnSubmitAsync`, `TFormOnServer`, `TPatentSubmitMeta`\> & `ReactFieldApi`\<`TParentData`, `TFormOnMount`, `TFormOnChange`, `TFormOnChangeAsync`, `TFormOnBlur`, `TFormOnBlurAsync`, `TFormOnSubmit`, `TFormOnSubmitAsync`, `TFormOnServer`, `TPatentSubmitMeta`\>
69 | 
70 | The `FieldApi` instance for the specified field.
71 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/functions/useform.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: useForm
 3 | title: useForm
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Function: useForm()
 9 | 
10 | ```ts
11 | function useForm<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta>(opts?): ReactFormExtendedApi<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta>
12 | ```
13 | 
14 | Defined in: [packages/react-form/src/useForm.tsx:142](https://github.com/TanStack/form/blob/main/packages/react-form/src/useForm.tsx#L142)
15 | 
16 | A custom React Hook that returns an extended instance of the `FormApi` class.
17 | 
18 | This API encapsulates all the necessary functionalities related to the form. It allows you to manage form state, handle submissions, and interact with form fields
19 | 
20 | ## Type Parameters
21 | 
22 | • **TFormData**
23 | 
24 | • **TOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
25 | 
26 | • **TOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
27 | 
28 | • **TOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
29 | 
30 | • **TOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
31 | 
32 | • **TOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
33 | 
34 | • **TOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
35 | 
36 | • **TOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
37 | 
38 | • **TOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
39 | 
40 | • **TSubmitMeta**
41 | 
42 | ## Parameters
43 | 
44 | ### opts?
45 | 
46 | `FormOptions`\<`TFormData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TOnServer`, `TSubmitMeta`\>
47 | 
48 | ## Returns
49 | 
50 | [`ReactFormExtendedApi`](../../type-aliases/reactformextendedapi.md)\<`TFormData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TOnServer`, `TSubmitMeta`\>
51 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/functions/usestore.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: useStore
 3 | title: useStore
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Function: useStore()
 9 | 
10 | ## Call Signature
11 | 
12 | ```ts
13 | function useStore<TState, TSelected>(store, selector?): TSelected
14 | ```
15 | 
16 | Defined in: node\_modules/.pnpm/@tanstack+react-store@0.7.1\_react-dom@19.1.0\_react@19.1.0\_\_react@19.1.0/node\_modules/@tanstack/react-store/dist/esm/index.d.ts:7
17 | 
18 | ### Type Parameters
19 | 
20 | • **TState**
21 | 
22 | • **TSelected** = `NoInfer`\<`TState`\>
23 | 
24 | ### Parameters
25 | 
26 | #### store
27 | 
28 | `Store`\<`TState`, `any`\>
29 | 
30 | #### selector?
31 | 
32 | (`state`) => `TSelected`
33 | 
34 | ### Returns
35 | 
36 | `TSelected`
37 | 
38 | ## Call Signature
39 | 
40 | ```ts
41 | function useStore<TState, TSelected>(store, selector?): TSelected
42 | ```
43 | 
44 | Defined in: node\_modules/.pnpm/@tanstack+react-store@0.7.1\_react-dom@19.1.0\_react@19.1.0\_\_react@19.1.0/node\_modules/@tanstack/react-store/dist/esm/index.d.ts:8
45 | 
46 | ### Type Parameters
47 | 
48 | • **TState**
49 | 
50 | • **TSelected** = `NoInfer`\<`TState`\>
51 | 
52 | ### Parameters
53 | 
54 | #### store
55 | 
56 | `Derived`\<`TState`, `any`\>
57 | 
58 | #### selector?
59 | 
60 | (`state`) => `TSelected`
61 | 
62 | ### Returns
63 | 
64 | `TSelected`
65 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/functions/usetransform.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: useTransform
 3 | title: useTransform
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Function: useTransform()
 9 | 
10 | ```ts
11 | function useTransform(fn, deps): FormTransform<any, any, any, any, any, any, any, any, any, any>
12 | ```
13 | 
14 | Defined in: [packages/react-form/src/useTransform.ts:9](https://github.com/TanStack/form/blob/main/packages/react-form/src/useTransform.ts#L9)
15 | 
16 | ## Parameters
17 | 
18 | ### fn
19 | 
20 | (`formBase`) => `AnyFormApi`
21 | 
22 | ### deps
23 | 
24 | `unknown`[]
25 | 
26 | ## Returns
27 | 
28 | `FormTransform`\<`any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`, `any`\>
29 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/index.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: "@tanstack/react-form"
 3 | title: "@tanstack/react-form"
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # @tanstack/react-form
 9 | 
10 | ## Interfaces
11 | 
12 | - [ReactFormApi](../interfaces/reactformapi.md)
13 | - [WithFormProps](../interfaces/withformprops.md)
14 | 
15 | ## Type Aliases
16 | 
17 | - [FieldComponent](../type-aliases/fieldcomponent.md)
18 | - [ReactFormExtendedApi](../type-aliases/reactformextendedapi.md)
19 | - [UseField](../type-aliases/usefield.md)
20 | 
21 | ## Functions
22 | 
23 | - [createFormHook](../functions/createformhook.md)
24 | - [createFormHookContexts](../functions/createformhookcontexts.md)
25 | - [Field](../functions/field.md)
26 | - [useField](../functions/usefield.md)
27 | - [useForm](../functions/useform.md)
28 | - [useStore](../functions/usestore.md)
29 | - [useTransform](../functions/usetransform.md)
30 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/interfaces/reactformapi.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: ReactFormApi
 3 | title: ReactFormApi
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Interface: ReactFormApi\<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta\>
 9 | 
10 | Defined in: [packages/react-form/src/useForm.tsx:21](https://github.com/TanStack/form/blob/main/packages/react-form/src/useForm.tsx#L21)
11 | 
12 | Fields that are added onto the `FormAPI` from `@tanstack/form-core` and returned from `useForm`
13 | 
14 | ## Type Parameters
15 | 
16 | • **TFormData**
17 | 
18 | • **TOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
19 | 
20 | • **TOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
21 | 
22 | • **TOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
23 | 
24 | • **TOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
25 | 
26 | • **TOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
27 | 
28 | • **TOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
29 | 
30 | • **TOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
31 | 
32 | • **TOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
33 | 
34 | • **TSubmitMeta**
35 | 
36 | ## Properties
37 | 
38 | ### Field
39 | 
40 | ```ts
41 | Field: FieldComponent<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta>;
42 | ```
43 | 
44 | Defined in: [packages/react-form/src/useForm.tsx:36](https://github.com/TanStack/form/blob/main/packages/react-form/src/useForm.tsx#L36)
45 | 
46 | A React component to render form fields. With this, you can render and manage individual form fields.
47 | 
48 | ***
49 | 
50 | ### Subscribe()
51 | 
52 | ```ts
53 | Subscribe: <TSelected>(props) => ReactNode;
54 | ```
55 | 
56 | Defined in: [packages/react-form/src/useForm.tsx:51](https://github.com/TanStack/form/blob/main/packages/react-form/src/useForm.tsx#L51)
57 | 
58 | A `Subscribe` function that allows you to listen and react to changes in the form's state. It's especially useful when you need to execute side effects or render specific components in response to state updates.
59 | 
60 | #### Type Parameters
61 | 
62 | • **TSelected** = `FormState`\<`TFormData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TOnServer`\>
63 | 
64 | #### Parameters
65 | 
66 | ##### props
67 | 
68 | ###### children
69 | 
70 | `ReactNode` \| (`state`) => `ReactNode`
71 | 
72 | ###### selector?
73 | 
74 | (`state`) => `TSelected`
75 | 
76 | #### Returns
77 | 
78 | `ReactNode`
79 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/interfaces/withformprops.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: WithFormProps
 3 | title: WithFormProps
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Interface: WithFormProps\<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta, TFieldComponents, TFormComponents, TRenderProps\>
 9 | 
10 | Defined in: [packages/react-form/src/createFormHook.tsx:173](https://github.com/TanStack/form/blob/main/packages/react-form/src/createFormHook.tsx#L173)
11 | 
12 | ## Extends
13 | 
14 | - `FormOptions`\<`TFormData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TOnServer`, `TSubmitMeta`\>
15 | 
16 | ## Type Parameters
17 | 
18 | • **TFormData**
19 | 
20 | • **TOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
21 | 
22 | • **TOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
23 | 
24 | • **TOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
25 | 
26 | • **TOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
27 | 
28 | • **TOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
29 | 
30 | • **TOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
31 | 
32 | • **TOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
33 | 
34 | • **TOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
35 | 
36 | • **TSubmitMeta**
37 | 
38 | • **TFieldComponents** *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>
39 | 
40 | • **TFormComponents** *extends* `Record`\<`string`, `ComponentType`\<`any`\>\>
41 | 
42 | • **TRenderProps** *extends* `Record`\<`string`, `unknown`\> = `Record`\<`string`, `never`\>
43 | 
44 | ## Properties
45 | 
46 | ### props?
47 | 
48 | ```ts
49 | optional props: TRenderProps;
50 | ```
51 | 
52 | Defined in: [packages/react-form/src/createFormHook.tsx:200](https://github.com/TanStack/form/blob/main/packages/react-form/src/createFormHook.tsx#L200)
53 | 
54 | ***
55 | 
56 | ### render()
57 | 
58 | ```ts
59 | render: (props) => Element;
60 | ```
61 | 
62 | Defined in: [packages/react-form/src/createFormHook.tsx:201](https://github.com/TanStack/form/blob/main/packages/react-form/src/createFormHook.tsx#L201)
63 | 
64 | #### Parameters
65 | 
66 | ##### props
67 | 
68 | `PropsWithChildren`\<`NoInfer`\<`TRenderProps`\> & `object`\>
69 | 
70 | #### Returns
71 | 
72 | `Element`
73 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/type-aliases/fieldcomponent.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: FieldComponent
 3 | title: FieldComponent
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Type Alias: FieldComponent()\<TParentData, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta, ExtendedApi\>
 9 | 
10 | ```ts
11 | type FieldComponent<TParentData, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta, ExtendedApi> = <TName, TData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync>({
12 |   children,
13 |   ...fieldOptions
14 | }) => ReactNode;
15 | ```
16 | 
17 | Defined in: [packages/react-form/src/useField.tsx:363](https://github.com/TanStack/form/blob/main/packages/react-form/src/useField.tsx#L363)
18 | 
19 | A type alias representing a field component for a specific form data type.
20 | 
21 | ## Type Parameters
22 | 
23 | • **TParentData**
24 | 
25 | • **TFormOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
26 | 
27 | • **TFormOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
28 | 
29 | • **TFormOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
30 | 
31 | • **TFormOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
32 | 
33 | • **TFormOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
34 | 
35 | • **TFormOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
36 | 
37 | • **TFormOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
38 | 
39 | • **TFormOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
40 | 
41 | • **TPatentSubmitMeta**
42 | 
43 | • **ExtendedApi** = \{\}
44 | 
45 | ## Type Parameters
46 | 
47 | • **TName** *extends* `DeepKeys`\<`TParentData`\>
48 | 
49 | • **TData** *extends* `DeepValue`\<`TParentData`, `TName`\>
50 | 
51 | • **TOnMount** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
52 | 
53 | • **TOnChange** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
54 | 
55 | • **TOnChangeAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
56 | 
57 | • **TOnBlur** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
58 | 
59 | • **TOnBlurAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
60 | 
61 | • **TOnSubmit** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
62 | 
63 | • **TOnSubmitAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
64 | 
65 | ## Parameters
66 | 
67 | ### \{
68 |   children,
69 |   ...fieldOptions
70 | \}
71 | 
72 | `FieldComponentBoundProps`\<`TParentData`, `TName`, `TData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TFormOnMount`, `TFormOnChange`, `TFormOnChangeAsync`, `TFormOnBlur`, `TFormOnBlurAsync`, `TFormOnSubmit`, `TFormOnSubmitAsync`, `TFormOnServer`, `TPatentSubmitMeta`, `ExtendedApi`\>
73 | 
74 | ## Returns
75 | 
76 | `ReactNode`
77 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/type-aliases/reactformextendedapi.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: ReactFormExtendedApi
 3 | title: ReactFormExtendedApi
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Type Alias: ReactFormExtendedApi\<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta\>
 9 | 
10 | ```ts
11 | type ReactFormExtendedApi<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta> = FormApi<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta> & ReactFormApi<TFormData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TOnServer, TSubmitMeta>;
12 | ```
13 | 
14 | Defined in: [packages/react-form/src/useForm.tsx:88](https://github.com/TanStack/form/blob/main/packages/react-form/src/useForm.tsx#L88)
15 | 
16 | An extended version of the `FormApi` class that includes React-specific functionalities from `ReactFormApi`
17 | 
18 | ## Type Parameters
19 | 
20 | • **TFormData**
21 | 
22 | • **TOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
23 | 
24 | • **TOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
25 | 
26 | • **TOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
27 | 
28 | • **TOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
29 | 
30 | • **TOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
31 | 
32 | • **TOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TFormData`\>
33 | 
34 | • **TOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
35 | 
36 | • **TOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TFormData`\>
37 | 
38 | • **TSubmitMeta**
39 | 


--------------------------------------------------------------------------------
/docs/framework/react/reference/type-aliases/usefield.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | id: UseField
 3 | title: UseField
 4 | ---
 5 | 
 6 | <!-- DO NOT EDIT: this page is autogenerated from the type comments -->
 7 | 
 8 | # Type Alias: UseField()\<TParentData, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta\>
 9 | 
10 | ```ts
11 | type UseField<TParentData, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta> = <TName, TData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync>(opts) => FieldApi<TParentData, TName, TData, TOnMount, TOnChange, TOnChangeAsync, TOnBlur, TOnBlurAsync, TOnSubmit, TOnSubmitAsync, TFormOnMount, TFormOnChange, TFormOnChangeAsync, TFormOnBlur, TFormOnBlurAsync, TFormOnSubmit, TFormOnSubmitAsync, TFormOnServer, TPatentSubmitMeta>;
12 | ```
13 | 
14 | Defined in: [packages/react-form/src/useField.tsx:50](https://github.com/TanStack/form/blob/main/packages/react-form/src/useField.tsx#L50)
15 | 
16 | A type representing a hook for using a field in a form with the given form data type.
17 | 
18 | A function that takes an optional object with a `name` property and field options, and returns a `FieldApi` instance for the specified field.
19 | 
20 | ## Type Parameters
21 | 
22 | • **TParentData**
23 | 
24 | • **TFormOnMount** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
25 | 
26 | • **TFormOnChange** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
27 | 
28 | • **TFormOnChangeAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
29 | 
30 | • **TFormOnBlur** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
31 | 
32 | • **TFormOnBlurAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
33 | 
34 | • **TFormOnSubmit** *extends* `undefined` \| `FormValidateOrFn`\<`TParentData`\>
35 | 
36 | • **TFormOnSubmitAsync** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
37 | 
38 | • **TFormOnServer** *extends* `undefined` \| `FormAsyncValidateOrFn`\<`TParentData`\>
39 | 
40 | • **TPatentSubmitMeta**
41 | 
42 | ## Type Parameters
43 | 
44 | • **TName** *extends* `DeepKeys`\<`TParentData`\>
45 | 
46 | • **TData** *extends* `DeepValue`\<`TParentData`, `TName`\>
47 | 
48 | • **TOnMount** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
49 | 
50 | • **TOnChange** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
51 | 
52 | • **TOnChangeAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
53 | 
54 | • **TOnBlur** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
55 | 
56 | • **TOnBlurAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
57 | 
58 | • **TOnSubmit** *extends* `undefined` \| `FieldValidateOrFn`\<`TParentData`, `TName`, `TData`\>
59 | 
60 | • **TOnSubmitAsync** *extends* `undefined` \| `FieldAsyncValidateOrFn`\<`TParentData`, `TName`, `TData`\>
61 | 
62 | ## Parameters
63 | 
64 | ### opts
65 | 
66 | `UseFieldOptionsBound`\<`TParentData`, `TName`, `TData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`\>
67 | 
68 | ## Returns
69 | 
70 | `FieldApi`\<`TParentData`, `TName`, `TData`, `TOnMount`, `TOnChange`, `TOnChangeAsync`, `TOnBlur`, `TOnBlurAsync`, `TOnSubmit`, `TOnSubmitAsync`, `TFormOnMount`, `TFormOnChange`, `TFormOnChangeAsync`, `TFormOnBlur`, `TFormOnBlurAsync`, `TFormOnSubmit`, `TFormOnSubmitAsync`, `TFormOnServer`, `TPatentSubmitMeta`\>
71 | 


--------------------------------------------------------------------------------