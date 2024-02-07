# 路由管理项目

## 简介

路由管理项目是一个用于简化和管理 Flask 或类似框架中 URL 路由的 Python 库。它允许开发者通过 YAML 配置文件以声明性方式定义路由结构，从而使路由管理变得更加简单、直观。

## 特性

- **声明性路由配置**：使用 YAML 文件声明路由，简化配置过程。
- **支持多级路由**：轻松定义和管理多级路由结构。已成功测试至十级路由深度。
- **动态路由参数**：支持在路由中使用动态参数。
- **易于集成**：可轻松集成到 Flask 或类似的 Python web 框架中。

## 快速开始

1. **创建 YAML 路由配置文件**：在您的项目中创建一个 `routes.yaml` 文件，并定义您的路由结构。

    ```yaml
    # routes.yaml 示例
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

2. **在您的项目中使用路由管理项目**：

    ```python
    from 路由管理项目 import Route

    # 初始化并加载路由配置
    route = Route('path/to/your/routes.yaml')

    # 获取路由路径
    print(route.get_route_path('auth.login'))  # 输出: /auth/login
    ```

## 贡献

我们欢迎所有形式的贡献，包括但不限于新功能、代码审查、文档和问题报告。如果您有兴趣贡献，请查看 `CONTRIBUTING.md` 了解更多信息。

## 许可证

本项目采用 BSD 许可证。有关更多信息，请查看 `LICENSE` 文件。

## 致谢

感谢所有为这个项目做出贡献的开发者和贡献者。
