# functional-and-stream

定位：函数式编程与 Stream 流处理

子模块概览：
- lambda：lambda 语法与闭包语义
- functional-interface：核心函数式接口：Function/Supplier/Consumer/Predicate
- stream-basic：流的创建/中间/终端操作
- stream-advanced：并行流、自定义 Collector、性能对比

运行：
- 构建当前父模块及子模块：`mvn -pl functional-and-stream -am test`
- 在子模块内执行：`mvn test`
