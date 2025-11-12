tool_list = [
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
    "description": "Fetch a paginated list of users from ReqRes API (requires token).",
    "args_schema": {"page": "int"},
    "api_url": "https://reqres.in/api/users?page={page}",
    "optional_headers": {"Authorization": "Bearer <token>"},
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
    "api_url": "https://dummyjson.com/products/search?q={query}&limit={limit}&skip={skip}",
    "optional_headers": {"Content-Type": "application/json", "User-Agent": "DynamicToolAgent/1.0"},
    "method": "GET"
  }
]
