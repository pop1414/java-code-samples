# concurrent

定位：并发编程与线程模型

子模块概览：
- thread-basic：线程创建、启动、生命周期与中断
- sync：synchronized、Lock、volatile，可见性与原子性
- thread-pool：ExecutorService / ThreadPoolExecutor 参数与拒绝策略
- atomic：原子类：AtomicInteger/AtomicReference/LongAdder
- concurrent-collection：并发集合：ConcurrentHashMap/CopyOnWriteArrayList
- completable-future：CompletableFuture 链式与组合操作

运行：
- 构建当前父模块及子模块：`mvn -pl concurrent -am test`
- 在子模块内执行：`mvn test`
