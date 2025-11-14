tool_list = [
  # ---------- GET TOOLS ----------
  {
    "tool_name": "product_fetch_tool_dummyjson",
    "description": "Fetch a single product by ID from DummyJSON API.",
    "args_schema": {"product_id": "int"},
    "api_url": "https://dummyjson.com/products/{product_id}",
    "optional_headers": {},
    "method": "GET"
  },
  {
    "tool_name": "product_fetch_tool_fakestore",
    "description": "Fetch a single product by ID from FakeStore API.",
    "args_schema": {"product_id": "int"},
    "api_url": "https://fakestoreapi.com/products/{product_id}",
    "optional_headers": {},
    "method": "GET"
  },
  {
    "tool_name": "post_fetch_tool_jsonplaceholder",
    "description": "Fetch a single post by ID from JSONPlaceholder API.",
    "args_schema": {"post_id": "int"},
    "api_url": "https://jsonplaceholder.typicode.com/posts/{post_id}",
    "optional_headers": {},
    "method": "GET"
  },
  {
    "tool_name": "public_api_list_tool",
    "description": "Fetch a list of all public APIs from Public APIs List.",
    "args_schema": {},
    "api_url": "https://api.publicapis.org/entries",
    "optional_headers": {},
    "method": "GET"
  },
  {
    "tool_name": "cat_fact_tool",
    "description": "Fetch a random cat fact from Cat Facts API.",
    "args_schema": {},
    "api_url": "https://catfact.ninja/fact",
    "optional_headers": {},
    "method": "GET"
  },
  {
    "tool_name": "user_list_tool_reqres",
    "description": "Fetch a paginated list of users from ReqRes API using x-api-key.",
    "args_schema": {"page": "int"},
    "api_url": "https://reqres.in/api/users?page={page}",
    "optional_headers": {"x-api-key": "reqres-free-v1"},
    "method": "GET"
},
  {
    "tool_name": "user_fetch_tool_gorest",
    "description": "Fetch a list of users from GoREST API (requires Bearer token).",
    "args_schema": {},
    "api_url": "https://gorest.co.in/public/v2/users",
    "optional_headers": {"Authorization": "Bearer <your_token>"},
    "method": "GET"
  },
  {
    "tool_name": "github_user_info_tool",
    "description": "Fetch authenticated user info from GitHub API.",
    "args_schema": {},
    "api_url": "https://api.github.com/user",
    "optional_headers": {"Authorization": "token <github_token>"},
    "method": "GET"
  },
  {
    "tool_name": "spotify_user_profile_tool",
    "description": "Fetch current user's profile from Spotify API.",
    "args_schema": {},
    "api_url": "https://api.spotify.com/v1/me",
    "optional_headers": {"Authorization": "Bearer <access_token>"},
    "method": "GET"
  },
  {
    "tool_name": "weather_fetch_tool_openweathermap",
    "description": "Fetch weather data by city name from OpenWeatherMap API.",
    "args_schema": {"city": "str"},
    "api_url": "https://api.openweathermap.org/data/2.5/weather?q={city}&appid=<API_KEY>",
    "optional_headers": {"X-API-Key": "<API_KEY>"},
    "method": "GET"
  },
  {
    "tool_name": "product_search_tool_dummyjson",
    "description": "Search products by name with pagination using DummyJSON API.",
    "args_schema": {"query": "str", "limit": "int", "skip": "int"},
    "api_url": "https://dummyjson.com/products/search",
    "optional_headers": {"Content-Type": "application/json", "User-Agent": "DynamicToolAgent/1.0"},
    "method": "GET"
  },

  # ---------- POST TOOLS ----------
  {
    "tool_name": "create_user_tool_reqres",
    "description": "Create a new user using ReqRes API.",
    "args_schema": {"name": "str", "job": "str"},
    "api_url": "https://reqres.in/api/users",
    "optional_headers": {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "x-api-key": "reqres-free-v1"
    },
    "method": "POST"
  },

  {
    "tool_name": "create_post_tool_jsonplaceholder",
    "description": "Create a new post using JSONPlaceholder.",
    "args_schema": {"title": "str", "body": "str", "userId": "int"},
    "api_url": "https://jsonplaceholder.typicode.com/posts",
    "optional_headers": {"Content-Type": "application/json"},
    "method": "POST"
  },
  {
    "tool_name": "add_product_tool_dummyjson",
    "description": "Add a new product to DummyJSON API.",
    "args_schema": {"title": "str", "price": "int", "category": "str"},
    "api_url": "https://dummyjson.com/products/add",
    "optional_headers": {"Content-Type": "application/json"},
    "method": "POST"
  },
  {
    "tool_name": "create_comment_tool_jsonplaceholder",
    "description": "Add a comment to a post using JSONPlaceholder.",
    "args_schema": {"postId": "int", "name": "str", "email": "str", "body": "str"},
    "api_url": "https://jsonplaceholder.typicode.com/comments",
    "optional_headers": {"Content-Type": "application/json"},
    "method": "POST"
  },

  # ---------- PUT TOOLS ----------
  {
    "tool_name": "update_user_tool_reqres",
    "description": "Update user details using ReqRes API.",
    "args_schema": {"user_id": "int", "name": "str", "job": "str"},
    "api_url": "https://reqres.in/api/users/{user_id}",
    "optional_headers": {
      "Content-Type": "application/json",
      "x-api-key": "reqres-free-v1"
    },
    "method": "PUT"
  },
  {
    "tool_name": "update_post_tool_jsonplaceholder",
    "description": "Update an existing post using JSONPlaceholder.",
    "args_schema": {"post_id": "int", "title": "str", "body": "str", "userId": "int"},
    "api_url": "https://jsonplaceholder.typicode.com/posts/{post_id}",
    "optional_headers": {"Content-Type": "application/json"},
    "method": "PUT"
  },
  {
    "tool_name": "update_product_tool_dummyjson",
    "description": "Update product details by ID in DummyJSON API.",
    "args_schema": {"product_id": "int", "title": "str", "price": "int"},
    "api_url": "https://dummyjson.com/products/{product_id}",
    "optional_headers": {"Content-Type": "application/json"},
    "method": "PUT"
  },

  # ---------- DELETE TOOLS ----------
   {
    "tool_name": "delete_user_tool_reqres",
    "description": "Delete a user by ID using ReqRes API.",
    "args_schema": {"user_id": "int"},
    "api_url": "https://reqres.in/api/users/{user_id}",
    "optional_headers": {"x-api-key": "reqres-free-v1"},
    "method": "DELETE"
  },
  {
    "tool_name": "delete_post_tool_jsonplaceholder",
    "description": "Delete a post by ID using JSONPlaceholder.",
    "args_schema": {"post_id": "int"},
    "api_url": "https://jsonplaceholder.typicode.com/posts/{post_id}",
    "optional_headers": {},
    "method": "DELETE"
  },
  {
    "tool_name": "delete_product_tool_dummyjson",
    "description": "Delete a product by ID using DummyJSON API.",
    "args_schema": {"product_id": "int"},
    "api_url": "https://dummyjson.com/products/{product_id}",
    "optional_headers": {},
    "method": "DELETE"
  }
]

