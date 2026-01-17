import os
import textwrap


structure = {
    "basic": [
        {"name": "variable", "desc": "变量、常量、基本类型与包装类", "samples": ["VariableDemo.java", "DataTypeDemo.java"]},
        {"name": "operator", "desc": "算术/赋值/关系/逻辑/位运算与优先级", "samples": ["ArithmeticOperatorDemo.java", "LogicalOperatorDemo.java", "BitwiseOperatorDemo.java"]},
        {"name": "control-flow", "desc": "分支与循环（if/else、switch、for/while/do-while、break/continue）", "samples": ["IfElseDemo.java", "SwitchDemo.java", "ForLoopDemo.java", "WhileLoopDemo.java"]},
        {"name": "array", "desc": "一维/多维数组与 Arrays 工具类", "samples": ["ArrayTraversalDemo.java", "MultiDimArrayDemo.java", "ArraysUtilDemo.java"]},
        {"name": "string", "desc": "String / StringBuilder / StringBuffer 的创建、拼接与性能", "samples": ["StringBasicsDemo.java", "StringBuilderDemo.java", "StringBufferDemo.java"]},
    ],
    "oop": [
        {"name": "encapsulation", "desc": "封装与访问控制，getter/setter 约定", "samples": ["EncapsulationDemo.java"]},
        {"name": "inheritance", "desc": "继承、super、方法重写", "samples": ["InheritanceDemo.java", "OverrideDemo.java"]},
        {"name": "polymorphism", "desc": "多态、向上/向下转型、动态绑定", "samples": ["PolymorphismDemo.java", "UpcastingDowncastingDemo.java"]},
        {"name": "abstract", "desc": "抽象类与接口的差异和适用场景", "samples": ["AbstractClassDemo.java", "InterfaceDefaultMethodDemo.java"]},
        {"name": "inner-class", "desc": "成员/静态/局部/匿名内部类", "samples": ["MemberInnerClassDemo.java", "StaticInnerClassDemo.java", "AnonymousInnerClassDemo.java"]},
        {"name": "enum", "desc": "枚举定义、常用模式与策略式用法", "samples": ["EnumBasicDemo.java", "EnumStrategyDemo.java"]},
    ],
    "core-features": [
        {"name": "reflection", "desc": "反射：类型信息、构造/方法/字段访问，以及简易 IOC 示例", "samples": ["ReflectCreateObject.java", "ReflectAccessField.java", "ReflectInvokeMethod.java", "ReflectFrameworkDemo.java"]},
        {"name": "annotation", "desc": "内置/自定义注解、元注解与注解解析", "samples": ["CustomAnnotationDemo.java", "RuntimeAnnotationProcessorDemo.java"]},
        {"name": "generic", "desc": "泛型类/方法、通配符与类型擦除", "samples": ["GenericClassDemo.java", "GenericMethodDemo.java", "WildcardDemo.java"]},
        {"name": "exception", "desc": "受检/非受检异常、自定义异常、try-with-resources", "samples": ["CheckedExceptionDemo.java", "CustomExceptionDemo.java", "TryWithResourcesDemo.java"]},
        {"name": "date-time", "desc": "Date/Calendar 与 java.time（LocalDateTime/Duration/Formatter）", "samples": ["DateApiLegacyDemo.java", "LocalDateTimeDemo.java", "DateTimeFormatterDemo.java"]},
        {"name": "wrapper", "desc": "包装类、自动装箱/拆箱与缓存", "samples": ["BoxingUnboxingDemo.java", "WrapperCachingDemo.java"]},
    ],
    "collection": [
        {"name": "list", "desc": "ArrayList/LinkedList/Vector，对比特性与遍历", "samples": ["ArrayListDemo.java", "LinkedListDemo.java", "VectorDemo.java"]},
        {"name": "set", "desc": "HashSet/TreeSet/LinkedHashSet，去重与有序性", "samples": ["HashSetDemo.java", "TreeSetDemo.java", "LinkedHashSetDemo.java"]},
        {"name": "map", "desc": "HashMap/TreeMap/LinkedHashMap/ConcurrentHashMap，遍历与负载因子", "samples": ["HashMapDemo.java", "TreeMapDemo.java", "LinkedHashMapDemo.java", "ConcurrentHashMapDemo.java"]},
        {"name": "queue", "desc": "Queue/Deque/ArrayDeque/PriorityQueue，阻塞队列预留", "samples": ["QueueBasicDemo.java", "ArrayDequeDemo.java", "PriorityQueueDemo.java"]},
        {"name": "util", "desc": "Collections / Arrays 工具方法", "samples": ["CollectionsUtilityDemo.java", "ArraysUtilityDemo.java"]},
    ],
    "io": [
        {"name": "io-basic", "desc": "传统 IO：InputStream/Reader/Writer/File 操作", "samples": ["FileReadWriteDemo.java", "BufferedStreamDemo.java"]},
        {"name": "nio", "desc": "NIO：Buffer/Channel/Selector", "samples": ["NioBufferDemo.java", "NioChannelDemo.java"]},
        {"name": "nio2", "desc": "NIO.2：Path/Paths/Files 常用操作", "samples": ["PathAndFilesDemo.java", "FileVisitorDemo.java"]},
    ],
    "concurrent": [
        {"name": "thread-basic", "desc": "线程创建、启动、生命周期与中断", "samples": ["ThreadCreationDemo.java", "ThreadLifecycleDemo.java"]},
        {"name": "sync", "desc": "synchronized、Lock、volatile，可见性与原子性", "samples": ["SynchronizedDemo.java", "LockDemo.java", "VolatileDemo.java"]},
        {"name": "thread-pool", "desc": "ExecutorService / ThreadPoolExecutor 参数与拒绝策略", "samples": ["ExecutorServiceDemo.java", "ThreadPoolExecutorDemo.java"]},
        {"name": "atomic", "desc": "原子类：AtomicInteger/AtomicReference/LongAdder", "samples": ["AtomicIntegerDemo.java", "LongAdderDemo.java"]},
        {"name": "concurrent-collection", "desc": "并发集合：ConcurrentHashMap/CopyOnWriteArrayList", "samples": ["ConcurrentHashMapDemo.java", "CopyOnWriteArrayListDemo.java"]},
        {"name": "completable-future", "desc": "CompletableFuture 链式与组合操作", "samples": ["CompletableFutureBasicsDemo.java", "CompletableFutureComposeDemo.java"]},
    ],
    "jdk-new-features": [
        {"name": "jdk8", "desc": "Lambda、Stream、Optional、函数式接口", "samples": ["LambdaBasicsDemo.java", "StreamBasicsDemo.java", "OptionalDemo.java", "FunctionalInterfaceDemo.java"]},
        {"name": "jdk11", "desc": "var 局部类型推断、新 HttpClient", "samples": ["VarInferenceDemo.java", "HttpClientDemo.java"]},
        {"name": "jdk17", "desc": "密封类、switch 表达式增强", "samples": ["SealedClassDemo.java", "SwitchExpressionDemo.java"]},
    ],
    "functional-and-stream": [
        {"name": "lambda", "desc": "lambda 语法与闭包语义", "samples": ["LambdaSyntaxDemo.java"]},
        {"name": "functional-interface", "desc": "核心函数式接口：Function/Supplier/Consumer/Predicate", "samples": ["FunctionalInterfacesDemo.java"]},
        {"name": "stream-basic", "desc": "流的创建/中间/终端操作", "samples": ["StreamCreationDemo.java", "StreamTerminalDemo.java"]},
        {"name": "stream-advanced", "desc": "并行流、自定义 Collector、性能对比", "samples": ["ParallelStreamDemo.java", "CustomCollectorDemo.java"]},
    ],
    "design-pattern": [
        {"name": "creational", "desc": "单例/工厂/建造者/原型等创建型模式", "samples": ["SingletonDemo.java", "FactoryMethodDemo.java", "BuilderPatternDemo.java", "PrototypePatternDemo.java"]},
        {"name": "structural", "desc": "代理/装饰/适配/组合/外观等结构型模式", "samples": ["ProxyPatternDemo.java", "DecoratorPatternDemo.java", "AdapterPatternDemo.java", "CompositePatternDemo.java", "FacadePatternDemo.java"]},
        {"name": "behavioral", "desc": "观察者/策略/模板方法/责任链等行为型模式", "samples": ["ObserverPatternDemo.java", "StrategyPatternDemo.java", "TemplateMethodDemo.java", "ChainOfResponsibilityDemo.java"]},
    ],
    "framework-basis": [
        {"name": "spring-core", "desc": "Spring IOC/DI、Bean 生命周期与简单配置示例", "samples": ["SpringIoCConcepts.md"]},
        {"name": "mybatis", "desc": "MyBatis 映射器、动态 SQL、插件机制", "samples": ["MyBatisMapperDemo.java", "MyBatisPluginDemo.java"]},
        {"name": "dynamic-proxy", "desc": "JDK 动态代理、CGLIB 与拦截器链", "samples": ["JdkDynamicProxyDemo.java", "CglibProxyDemo.java"]},
    ],
    "util": [
        {"name": "commons-lang3", "desc": "Apache Commons Lang3：StringUtils/ObjectUtils 等", "samples": ["CommonsStringUtilsDemo.java", "CommonsObjectUtilsDemo.java"]},
        {"name": "guava", "desc": "Guava：集合工具、缓存、不可变集合", "samples": ["GuavaCollectionsDemo.java", "GuavaCacheDemo.java"]},
        {"name": "jackson", "desc": "Jackson：JSON 序列化/反序列化与注解", "samples": ["JacksonSerializationDemo.java", "JacksonAnnotationDemo.java"]},
    ],
    "interview": [
        {"name": "basic", "desc": "基础高频题：字符串拼接、数组去重等", "samples": ["StringConcatenateQuestion.java", "ArrayDedupQuestion.java"]},
        {"name": "oop", "desc": "OOP 高频题：多态、抽象类 vs 接口", "samples": ["PolymorphismQuestion.java", "AbstractVsInterfaceQuestion.java"]},
        {"name": "collection", "desc": "集合高频题：HashMap 原理、ArrayList 扩容", "samples": ["HashMapResizeQuestion.java", "ArrayListGrowthQuestion.java"]},
        {"name": "concurrent", "desc": "并发高频题：死锁、线程池参数、volatile 原理", "samples": ["DeadlockQuestion.java", "ThreadPoolTuningQuestion.java", "VolatilePrincipleQuestion.java"]},
    ],
}

module_descriptions = {
    "basic": "Java 入门基础语法与常用操作",
    "oop": "面向对象核心概念与实践",
    "core-features": "Java 进阶特性与语言机制",
    "collection": "集合框架的核心类型与工具",
    "io": "IO/NIO/NIO.2 的文件与网络基础",
    "concurrent": "并发编程与线程模型",
    "jdk-new-features": "JDK 各版本的新特性示例",
    "functional-and-stream": "函数式编程与 Stream 流处理",
    "design-pattern": "经典设计模式示例与讲解",
    "framework-basis": "框架底层原理与常用机制",
    "util": "常用第三方工具库示例",
    "interview": "面试高频题目与解题思路",
}

project_version_ref = "${project.version}"


def write_file(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(textwrap.dedent(content).lstrip("\n"))


# shared module
os.makedirs("shared", exist_ok=True)
shared_pom = f"""
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>com.example</groupId>
    <artifactId>java-code-samples</artifactId>
    <version>1.0.0-SNAPSHOT</version>
  </parent>
  <artifactId>shared</artifactId>
  <packaging>jar</packaging>
  <name>shared</name>
  <description>公共工具与基类，供各子模块复用</description>
</project>
"""
write_file("shared/pom.xml", shared_pom)
shared_readme = """
# shared

定位：公共工具、常用基类、测试基件（后续可放日志封装、随机数据生成、测试基类等）。

运行示例：`mvn -pl shared -am test`
"""
write_file("shared/README.md", shared_readme)
for subdir in ("shared/src/main/java", "shared/src/test/java"):
    os.makedirs(subdir, exist_ok=True)
    write_file(f"{subdir}/.gitkeep", "")


for module_name, submodules in structure.items():
    os.makedirs(module_name, exist_ok=True)
    module_tags = "\n".join(f"    <module>{s['name']}</module>" for s in submodules)
    module_desc = module_descriptions[module_name]
    module_pom = f"""
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>com.example</groupId>
    <artifactId>java-code-samples</artifactId>
    <version>1.0.0-SNAPSHOT</version>
  </parent>
  <artifactId>{module_name}</artifactId>
  <packaging>pom</packaging>
  <name>{module_name}</name>
  <description>{module_desc}</description>
  <modules>
{module_tags}
  </modules>
</project>
"""
    write_file(f"{module_name}/pom.xml", module_pom)

    bullet = "\n".join(f"- {s['name']}：{s['desc']}" for s in submodules)
    module_readme = f"""
# {module_name}

定位：{module_desc}

子模块概览：
{bullet}

运行：
- 构建当前父模块及子模块：`mvn -pl {module_name} -am test`
- 在子模块内执行：`mvn test`
"""
    write_file(f"{module_name}/README.md", module_readme)

    for sub in submodules:
        sub_name = sub["name"]
        sub_desc = sub["desc"]
        samples = sub["samples"]
        path = os.path.join(module_name, sub_name)
        os.makedirs(path, exist_ok=True)
        for subdir in ("src/main/java", "src/test/java"):
            full = os.path.join(path, subdir)
            os.makedirs(full, exist_ok=True)
            write_file(os.path.join(full, ".gitkeep"), "")

        sample_lines = "\n".join(f"- {s}" for s in samples) if samples else "- TODO: 补充示例"

        sub_pom = f"""
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <parent>
    <groupId>com.example</groupId>
    <artifactId>{module_name}</artifactId>
    <version>1.0.0-SNAPSHOT</version>
  </parent>
  <artifactId>{sub_name}</artifactId>
  <packaging>jar</packaging>
  <name>{module_name} - {sub_name}</name>
  <description>{sub_desc}</description>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId>
      <artifactId>shared</artifactId>
      <version>{project_version_ref}</version>
    </dependency>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
"""
        write_file(os.path.join(path, "pom.xml"), sub_pom)

        sub_readme = f"""
# {module_name}/{sub_name}

定位：{sub_desc}

计划示例：
{sample_lines}

运行：
- 构建当前子模块：`mvn -pl {module_name}/{sub_name} -am test`
- 在本目录下直接执行：`mvn test`
"""
        write_file(os.path.join(path, "README.md"), sub_readme)
