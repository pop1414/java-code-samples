package com.spike;

import java.io.InputStream;
import java.util.List;

import com.spike.entity.User;
import com.spike.mapper.UserMapper;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class MyBatisMain {
    public static void main(String[] args) {
        // 1. 定义MyBatis配置文件路径（以classpath为根目录）
        String resource = "mybatis-config.xml";
        InputStream inputStream = null;
        SqlSession sqlSession = null;

        try {
            // ===================== 第一步：加载配置，构建SqlSessionFactory
            // Resources是MyBatis的工具类，加载类路径下的配置文件（替代JDBC的Class.forName加载驱动）
            inputStream = Resources.getResourceAsStream(resource);
            // SqlSessionFactoryBuilder：构建器模式，解析配置文件生成SqlSessionFactory（全局唯一）
            SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);

            // ===================== 第二步：获取SqlSession（对应JDBC的Connection）
            // openSession(true)：自动提交事务（默认false，需要手动commit）
            // SqlSession是MyBatis的核心会话，封装了JDBC的Connection，线程不安全，用完必须关闭
            sqlSession = sqlSessionFactory.openSession(true);

            // ===================== 第三步：获取Mapper代理对象（核心：动态代理)
            // getMapper：MyBatis通过JDK动态代理生成UserMapper的实现类（无需自己写实现）
            // 代理类会拦截接口方法，找到对应的Mapper.xml中的SQL
            UserMapper userMapper = sqlSession.getMapper(UserMapper.class);

            // ===================== 第四步：执行SQL操作（替代JDBC的Statement.execute）
            // 操作1：根据ID查询用户
            User user = userMapper.findById(48L);
            System.out.println("根据ID查询用户：" + user);

            // 操作2：查询所有用户
            List<User> userList = userMapper.findAll();
            System.out.println("查询所有用户：");
            userList.forEach(System.out::println);

            // 操作3：新增用户
            User newUser = new User("new_user", "123456", "new_user@example.com");
            int rows = userMapper.insertUser(newUser);
            System.out.printf("新增用户影响行数：%d，生成的主键ID：%d%n", rows, newUser.getId());

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // ===================== 第五步：关闭资源（必须！） =====================
            if (sqlSession != null) {
                sqlSession.close();
            }
            if (inputStream != null) {
                try {
                    inputStream.close();
                } catch (Exception ignore) {
                    // ignore
                }
            }
        }
    }
}
