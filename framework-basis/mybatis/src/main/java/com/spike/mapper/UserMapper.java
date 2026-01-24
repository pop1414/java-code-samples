package com.spike.mapper;

import java.util.List;

import com.spike.entity.User;

public interface UserMapper {
    /**
     * 根据ID查询用户（对应JDBC的SELECT语句）
     */
    User findById(Long id);

    /**
     * 查询所有用户（对应JDBC的SELECT *）
     */
    List<User> findAll();

    /**
     * 插入新用户（核心方法）
     * 
     * @param user 待插入的用户对象（无需id、时间字段）
     * @return 影响的行数（1=成功，0=失败）
     */
    int insertUser(User user);
}
