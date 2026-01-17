# framework-basis

定位：框架底层原理与常用机制

子模块概览：
- spring-core：Spring IOC/DI、Bean 生命周期与简单配置示例
- mybatis：MyBatis 映射器、动态 SQL、插件机制
- dynamic-proxy：JDK 动态代理、CGLIB 与拦截器链

运行：
- 构建当前父模块及子模块：`mvn -pl framework-basis -am test`
- 在子模块内执行：`mvn test`
