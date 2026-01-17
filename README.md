# Java 代码样例百科

本仓库以 Maven 多模块形式整理 Java 各类知识点示例，按「主题 → 子主题」分层，便于查找与扩展。每个子模块包含 README 说明与最小可运行示例（后续补充代码）。

## 快速开始
- 构建全部：`mvn test`
- 构建单个子模块：`mvn -pl basic/variable -am test`
- 在子模块里直接构建：进入子模块目录后执行 `mvn test`

## 模块索引（一级）
- shared：公共工具、基类与测试基件
- basic：基础语法
- oop：面向对象
- core-features：语言进阶特性
- collection：集合框架
- io：IO/NIO/NIO.2
- concurrent：并发编程
- jdk-new-features：JDK 新特性（按版本）
- functional-and-stream：函数式与 Stream
- design-pattern：设计模式
- framework-basis：框架底层原理
- util：常用工具库
- interview：面试高频题

## 约定
- 包名建议：`com.example.<一级模块>.<子模块>`
- README 模板：目标/要点/运行方式/计划示例/扩展阅读
- 公共依赖：统一在根 `pom.xml` 中管理；子模块如需共享工具，依赖 `shared`
- 示例尽量小而全：可直接运行的 main 或 JUnit 5 测试
