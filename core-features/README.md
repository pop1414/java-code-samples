# core-features

定位：Java 进阶特性与语言机制

子模块概览：
- reflection：反射：类型信息、构造/方法/字段访问，以及简易 IOC 示例
- annotation：内置/自定义注解、元注解与注解解析
- generic：泛型类/方法、通配符与类型擦除
- exception：受检/非受检异常、自定义异常、try-with-resources
- date-time：Date/Calendar 与 java.time（LocalDateTime/Duration/Formatter）
- wrapper：包装类、自动装箱/拆箱与缓存

运行：
- 构建当前父模块及子模块：`mvn -pl core-features -am test`
- 在子模块内执行：`mvn test`
