# Route Management Project

## Introduction

The Route Management Project is a Python library designed to simplify and manage URL routing in Flask or similar frameworks. It allows developers to define their routing structure declaratively through a YAML configuration file, making route management simpler and more intuitive.
[中文版本](readme.zh.md)

## Features

- **Declarative Routing Configuration**: Declare routes using a YAML file to simplify the configuration process.
- **Support for Multi-level Routing**: Easily define and manage multi-level routing structures, with successful tests conducted up to a routing depth of ten levels.
- **Dynamic Route Parameters**: Support for using dynamic parameters within routes.
- **Easy Integration**: Can be easily integrated into Flask or similar Python web frameworks.

## Quick Start

1. **Create a YAML Routing Configuration File**: Create a `routes.yaml` file in your project and define your routing structure.

    ```yaml
    # Example routes.yaml
    root:
      path: "/"

    auth:
      path: "auth"
      children:
        login:
          path: "login"
        logout:
          path: "logout"
    ```

2. **Use the Route Management Project in Your Project**:

    ```python
    from route_management_project import Route

    # Initialize and load the routing configuration
    route = Route('path/to/your/routes.yaml')

    # Get the route path
    print(route.get_route_path('auth.login'))  # Output: /auth/login
    ```

## Contributing

We welcome all forms of contribution, including but not limited to new features, code reviews, documentation, and bug reports. If you are interested in contributing, please see `CONTRIBUTING.md` for more information.

## License

This project is licensed under the BSD License. For more information, please see the `LICENSE` file.

## Acknowledgements

Thanks to all the developers and contributors who have contributed to this project.
