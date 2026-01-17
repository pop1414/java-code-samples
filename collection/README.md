# collection

定位：集合框架的核心类型与工具

子模块概览：
- list：ArrayList/LinkedList/Vector，对比特性与遍历
- set：HashSet/TreeSet/LinkedHashSet，去重与有序性
- map：HashMap/TreeMap/LinkedHashMap/ConcurrentHashMap，遍历与负载因子
- queue：Queue/Deque/ArrayDeque/PriorityQueue，阻塞队列预留
- util：Collections / Arrays 工具方法

运行：
- 构建当前父模块及子模块：`mvn -pl collection -am test`
- 在子模块内执行：`mvn test`
